#!/usr/bin/env python3
"""
validate_data.py

Validates transformed CSV files (issues, PRs, releases, digest) against defined rules:
- Required columns presence
- Non-null values for key fields
- Unique IDs where applicable
- Date format and logical integrity (start <= end)
- Cross-file consistency (optional)

Outputs a validation report (JSON) and error summary to stdout.
"""

from __future__ import annotations

import argparse
import json
import logging
import os
import sys
from dataclasses import dataclass, field, asdict
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List, Optional, Set, Tuple, Union

import pandas as pd

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

# Expected date range for all date fields
DATE_RANGE: Tuple[str, str] = ("2025-01-01", "2027-12-31")

# Allowed date formats (order matters for performance)
# We use a vectorized approach where possible, fallback to trial-and-error for edge cases
DATE_FORMATS: Tuple[str, ...] = (
    "%Y-%m-%dT%H:%M:%SZ",
    "%Y-%m-%dT%H:%M:%S.%fZ",
    "%Y-%m-%d %H:%M:%S",
    "%Y-%m-%d",
)

# Logical date pair rules (start, end)
DATE_PAIR_RULES: List[Tuple[str, str]] = [
    ("created_at", "updated_at"),
    ("created_at", "closed_at"),
    ("created_at", "merged_at"),
]

# Mapping of file stem to expected file name for consistency
FILE_NAME_MAP: Dict[str, str] = {
    "issues": "issues.csv",
    "pull_requests": "pull_requests.csv",
    "releases": "releases.csv",
    "digest": "digest.csv",
}

# Maximum errors to collect per validation category (to avoid huge output)
MAX_ERRORS_PER_CATEGORY: int = 1000

# Allowed base directory for security (path traversal prevention)
ALLOWED_BASE_DIR: Optional[str] = os.environ.get("VALIDATION_BASE_DIR")

# ---------------------------------------------------------------------------
# Rule definitions per file type
# ---------------------------------------------------------------------------

FILE_RULES: Dict[str, Dict[str, Any]] = {
    "issues": {
        "required_columns": ["id", "repo", "title", "state", "created_at", "updated_at"],
        "unique_columns": ["id"],
        "non_null_columns": ["id", "repo", "created_at"],
        "date_columns": ["created_at", "updated_at", "closed_at"],
        "date_range": DATE_RANGE,
    },
    "pull_requests": {
        "required_columns": ["id", "repo", "title", "state", "created_at", "updated_at"],
        "unique_columns": ["id"],
        "non_null_columns": ["id", "repo", "created_at"],
        "date_columns": ["created_at", "updated_at", "merged_at", "closed_at"],
        "date_range": DATE_RANGE,
    },
    "releases": {
        "required_columns": ["id", "repo", "tag_name", "created_at", "published_at"],
        "unique_columns": ["id"],
        "non_null_columns": ["id", "repo", "tag_name", "published_at"],
        "date_columns": ["created_at", "published_at"],
        "date_range": DATE_RANGE,
    },
    "digest": {
        "required_columns": ["repo", "issue_count", "pr_count", "release_count", "generated_at"],
        "unique_columns": ["repo"],
        "non_null_columns": ["repo", "generated_at"],
        "date_columns": ["generated_at"],
        "date_range": ("2025-01-01", "2027-12-31"),
    },
}

# ---------------------------------------------------------------------------
# Logging configuration
# ---------------------------------------------------------------------------

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
logger = logging.getLogger("validate_data")


# ---------------------------------------------------------------------------
# Custom exceptions
# ---------------------------------------------------------------------------


class ValidationError(Exception):
    """Base exception for validation errors."""


class FileAccessError(ValidationError):
    """Error accessing or reading a file."""


class ParseError(ValidationError):
    """Error parsing file content."""


class SecurityError(ValidationError):
    """Security policy violation (e.g., path traversal)."""


# ---------------------------------------------------------------------------
# Data classes for validation results
# ---------------------------------------------------------------------------


@dataclass(frozen=True)
class ValidationErrorItem:
    """A single validation error with file, row (0-based), column, and message."""

    file: str
    row: int
    column: str
    message: str

    def to_dict(self) -> Dict[str, Any]:
        """Convert to JSON-serializable dictionary."""
        return asdict(self)


@dataclass
class ValidationResult:
    """Aggregated validation result for one file or the whole run."""

    file_type: str
    total_rows: int
    passed_rows: int
    errors: List[ValidationErrorItem] = field(default_factory=list)
    file_path: str = ""

    def failed_rows(self) -> int:
        """Return number of rows with at least one error (ignores header-only errors)."""
        return len({e.row for e in self.errors if e.row >= 0})

    def add_error(self, row: int, column: str, message: str) -> None:
        """Add a validation error, respecting MAX_ERRORS_PER_CATEGORY."""
        # Limit per column per file? For simplicity we limit total errors per file type.
        if len(self.errors) >= MAX_ERRORS_PER_CATEGORY:
            logger.warning("Reached error limit for %s, suppressing further errors.", self.file_type)
            return
        self.errors.append(ValidationErrorItem(
            file=self.file_path, row=row, column=column, message=message
        ))

    def to_dict(self) -> Dict[str, Any]:
        """Convert to JSON-serializable dictionary for reports."""
        return {
            "file": self.file_path,
            "file_type": self.file_type,
            "total_rows": self.total_rows,
            "passed_rows": self.passed_rows,
            "failed_rows": self.failed_rows(),
            "error_count": len(self.errors),
            "errors": [e.to_dict() for e in self.errors],
        }


# ---------------------------------------------------------------------------
# Date parsing utilities
# ---------------------------------------------------------------------------


def parse_date(val: Any) -> Optional[datetime]:
    """
    Parse a single date string into a datetime object.

    Uses a set of predefined formats; returns None if no format matches.

    Args:
        val: Input value (expected string).

    Returns:
        Parsed datetime if successful, None otherwise.
    """
    if not isinstance(val, str) or not val.strip():
        return None
    stripped = val.strip()
    for fmt in DATE_FORMATS:
        try:
            return datetime.strptime(stripped, fmt)
        except ValueError:
            continue
    return None


def parse_date_column_series(series: pd.Series) -> Tuple[pd.Series, List[int]]:
    """
    Parse a pandas Series of date strings using the fastest available method.

    First attempts vectorized parsing with pd.to_datetime (multiple formats),
    then falls back to manual parsing for remaining rows.

    Args:
        series: Pandas Series of string values.

    Returns:
        Tuple of (parsed datetime Series, list of row indices that failed to parse).
    """
    # Try vectorized parsing first (handles most cases)
    parsed = pd.to_datetime(series, format="mixed", errors="coerce", utc=True)

    # Identify failed rows (NaT)
    failed_mask = parsed.isna() & series.notna() & (series.astype(str).str.strip() != "")
    failed_indices = series[failed_mask].index.tolist()

    # If there are failures, try manual parsing for those rows only
    if failed_indices:
        for idx in failed_indices:
            val = series.iloc[idx]
            dt = parse_date(val)
            if dt is not None:
                parsed.iloc[idx] = dt
        # Recompute failed indices after manual attempt
        failed_mask = parsed.isna() & series.notna() & (series.astype(str).str.strip() != "")
        failed_indices = series[failed_mask].index.tolist()

    return parsed, failed_indices


# ---------------------------------------------------------------------------
# Security & input validation
# ---------------------------------------------------------------------------


def validate_file_path(file_path: Path) -> Path:
    """
    Validate and resolve a file path for security.

    Ensures the file exists, is a regular file, has a .csv extension,
    and is within an allowed base directory (if configured).

    Args:
        file_path: Input file path.

    Returns:
        Resolved absolute path.

    Raises:
        SecurityError: If path traversal detected or file outside allowed directory.
        FileAccessError: If file does not exist or is not a regular file.
    """
    resolved = file_path.resolve()
    if not resolved.is_file():
        raise FileAccessError(f"File does not exist or is not a regular file: {resolved}")
    if resolved.suffix.lower() != ".csv":
        raise FileAccessError(f"File must have .csv extension: {resolved}")

    if ALLOWED_BASE_DIR is not None:
        allowed = Path(ALLOWED_BASE_DIR).resolve()
        if not resolved.parent.samefile(allowed):
            # Check if resolved is inside allowed directory
            try:
                resolved.relative_to(allowed)
            except ValueError:
                raise SecurityError(f"File {resolved} is outside allowed base directory {allowed}")

    return resolved


# ---------------------------------------------------------------------------
# File reading with validation
# ---------------------------------------------------------------------------


def safe_read_csv(
    file_path: Path,
    dtype: str = "str",
    usecols: Optional[List[str]] = None,
    max_rows: Optional[int] = None,
) -> Optional[pd.DataFrame]:
    """
    Read a CSV file with proper error handling, type enforcement, and optional column selection.

    Args:
        file_path: Absolute path to the CSV file.
        dtype: Default dtype for columns (default "str").
        usecols: List of columns to load (None = all).
        max_rows: Maximum number of rows to read (None = all).

    Returns:
        DataFrame if successful, None if critical error.
    """
    try:
        kwargs: Dict[str, Any] = {
            "dtype": dtype,
            "keep_default_na": False,
            "low_memory": False,
        }
        if usecols is not None:
            kwargs["usecols"] = usecols
        if max_rows is not None:
            kwargs["nrows"] = max_rows

        df = pd.read_csv(file_path, **kwargs)
        # Replace empty strings with NaN for consistent null detection
        df.replace("", pd.NA, inplace=True)
        logger.info(
            "Loaded %d rows from %s (columns: %s)",
            len(df),
            file_path,
            list(df.columns) if not df.empty else [],
        )
        return df

    except FileNotFoundError as e:
        raise FileAccessError(f"File not found: {file_path}") from e
    except pd.errors.EmptyDataError as e:
        logger.warning("Empty file (no data rows): %s", file_path)
        return pd.DataFrame()
    except pd.errors.ParserError as e:
        raise ParseError(f"CSV parsing error in {file_path}: {e}") from e
    except PermissionError as e:
        raise FileAccessError(f"Permission denied reading {file_path}: {e}") from e
    except OSError as e:
        raise FileAccessError(f"OS error reading {file_path}: {e}") from e
    except Exception as e:
        logger.exception("Unexpected error reading %s", file_path)
        raise ParseError(f"Unexpected error reading {file_path}: {e}") from e


# ---------------------------------------------------------------------------
# Column-level validation helpers
# ---------------------------------------------------------------------------


def validate_required_columns(df: pd.DataFrame, rules: Dict[str, Any], result: ValidationResult) -> None:
    """
    Check that all required columns exist in the DataFrame.

    Args:
        df: DataFrame to validate.
        rules: Rule dict for the file type.
        result: ValidationResult to populate with errors.
    """
    required = rules.get("required_columns", [])
    missing = [col for col in required if col not in df.columns]
    if missing:
        for col in missing:
            result.add_error(-1, col, f"Required column '{col}' is missing from the file.")
        logger.error("Missing required columns in %s: %s", result.file_type, missing)


def validate_non_null_columns(df: pd.DataFrame, rules: Dict[str, Any], result: ValidationResult) -> None:
    """
    Check that specified columns have no null values.

    Args:
        df: DataFrame to validate.
        rules: Rule dict for the file type.
        result: ValidationResult to populate with errors.
    """
    non_null_cols = rules.get("non_null_columns", [])
    for col in non_null_cols:
        if col not in df.columns:
            continue
        null_mask = df[col].isna()
        if null_mask.any():
            for idx in null_mask[null_mask].index[:MAX_ERRORS_PER_CATEGORY]:
                result.add_error(idx, col, f"Non-null column '{col}' is null/empty at row {idx}.")
            total_nulls = null_mask.sum()
            if total_nulls > MAX_ERRORS_PER_CATEGORY:
                logger.warning(
                    "%s has %d null values in column '%s', reporting first %d",
                    result.file_type, total_nulls, col, MAX_ERRORS_PER_CATEGORY
                )


def validate_unique_columns(df: pd.DataFrame, rules: Dict[str, Any], result: ValidationResult) -> None:
    """
    Check that specified columns have unique values.

    Args:
        df: DataFrame to validate.
        rules: Rule dict for the file type.
        result: ValidationResult to populate with errors.
    """
    unique_cols = rules.get("unique_columns", [])
    for col in unique_cols:
        if col not in df.columns:
            continue
        duplicates = df[col].duplicated(keep=False)
        if duplicates.any():
            duplicate_indices = df[duplicates].index.tolist()
            for idx in duplicate_indices[:MAX_ERRORS_PER_CATEGORY]:
                val = df.at[idx, col]
                result.add_error(idx, col, f"Duplicate value '{val}' in unique column '{col}'.")
            if len(duplicate_indices) > MAX_ERRORS_PER_CATEGORY:
                logger.warning(
                    "%s has %d duplicate values in column '%s', reporting first %d",
                    result.file_type, len(duplicate_indices), col, MAX_ERRORS_PER_CATEGORY
                )


def validate_date_columns(df: pd.DataFrame, rules: Dict[str, Any], result: ValidationResult) -> None:
    """
    Validate date columns: parseable formats and within expected range.

    Uses vectorized parsing for performance.

    Args:
        df: DataFrame to validate.
        rules: Rule dict for the file type.
        result: ValidationResult to populate with errors.
    """
    date_cols = rules.get("date_columns", [])
    date_range = rules.get("date_range", DATE_RANGE)
    range_start = datetime.strptime(date_range[0], "%Y-%m-%d")
    range_end = datetime.strptime(date_range[1], "%Y-%m-%d")

    for col in date_cols:
        if col not in df.columns:
            continue
        series = df[col].astype(str)
        # Skip empty values (they are allowed unless non-null rule catches them)
        filled_mask = series.str.strip() != ""
        if not filled_mask.any():
            continue

        parsed, failed_indices = parse_date_column_series(series[filled_mask])

        # Report unparseable dates
        if failed_indices:
            for idx in failed_indices:
                result.add_error(idx, col, f"Date '{series.iloc[idx]}' could not be parsed in column '{col}'.")

        # Check date range (only for successfully parsed)
        valid_parsed = parsed.dropna()
        out_of_range = (valid_parsed < range_start) | (valid_parsed > range_end)
        if out_of_range.any():
            for idx in out_of_range[out_of_range].index[:MAX_ERRORS_PER_CATEGORY]:
                result.add_error(idx, col, f"Date '{series.iloc[idx]}' is outside expected range [{date_range[0]}, {date_range[1]}].")


def validate_date_pairs(df: pd.DataFrame, result: ValidationResult) -> None:
    """
    Validate logical date pairs (start <= end) where both columns exist and are parseable.

    Args:
        df: DataFrame to validate.
        result: ValidationResult to populate with errors.
    """
    for start_col, end_col in DATE_PAIR_RULES:
        if start_col not in df.columns or end_col not in df.columns:
            continue
        # Parse both columns using vectorized approach
        start_parsed, _ = parse_date_column_series(df[start_col].astype(str))
        end_parsed, _ = parse_date_column_series(df[end_col].astype(str))

        if start_parsed.isna().all() or end_parsed.isna().all():
            continue

        # Compare where both are non-na
        valid_mask = start_parsed.notna() & end_parsed.notna()
        invalid = (start_parsed > end_parsed) & valid_mask
        if invalid.any():
            for idx in invalid[invalid].index[:MAX_ERRORS_PER_CATEGORY]:
                result.add_error(
                    idx, f"{start_col}/{end_col}",
                    f"Date pair ({start_col}, {end_col}) violates start <= end: "
                    f"start='{df.at[idx, start_col]}', end='{df.at[idx, end_col]}'."
                )


# ---------------------------------------------------------------------------
# Cross-file consistency checks (optional)
# ---------------------------------------------------------------------------


def validate_cross_file_consistency(
    results: Dict[str, ValidationResult],
    dataframes: Dict[str, pd.DataFrame],
) -> List[ValidationErrorItem]:
    """
    Check that repositories mentioned in issues/PRs/releases exist in digest (if present).

    Args:
        results: Mapping of file type to ValidationResult.
        dataframes: Mapping of file type to DataFrame.

    Returns:
        List of cross-file validation errors.
    """
    cross_errors: List[ValidationErrorItem] = []
    if "digest" not in dataframes or "issues" not in dataframes:
        return cross_errors

    digest_repos = set(dataframes["digest"]["repo"].dropna().unique())
    issues_repos = set(dataframes["issues"]["repo"].dropna().unique())

    orphan_repos = issues_repos - digest_repos
    if orphan_repos:
        for repo in orphan_repos:
            cross_errors.append(ValidationErrorItem(
                file="cross-file",
                row=-1,
                column="repo",
                message=f"Repository '{repo}' appears in issues.csv but not in digest.csv."
            ))

    # Similarly for PRs and releases if present
    if "pull_requests" in dataframes:
        pr_repos = set(dataframes["pull_requests"]["repo"].dropna().unique())
        orphan_pr = pr_repos - digest_repos
        for repo in orphan_pr:
            cross_errors.append(ValidationErrorItem(
                file="cross-file",
                row=-1,
                column="repo",
                message=f"Repository '{repo}' appears in pull_requests.csv but not in digest.csv."
            ))

    if "releases" in dataframes:
        rel_repos = set(dataframes["releases"]["repo"].dropna().unique())
        orphan_rel = rel_repos - digest_repos
        for repo in orphan_rel:
            cross_errors.append(ValidationErrorItem(
                file="cross-file",
                row=-1,
                column="repo",
                message=f"Repository '{repo}' appears in releases.csv but not in digest.csv."
            ))

    return cross_errors


# ---------------------------------------------------------------------------
# Main validation orchestrator
# ---------------------------------------------------------------------------


def validate_single_file(
    file_path: Path,
    file_type: str,
    rules: Dict[str, Any],
) -> ValidationResult:
    """
    Validate a single CSV file against its defined rules.

    Args:
        file_path: Resolved path to the CSV file.
        file_type: Type of file (e.g., "issues", "pull_requests").
        rules: Rule dictionary for that file type.

    Returns:
        ValidationResult with all errors collected.
    """
    logger.info("Validating %s file: %s", file_type, file_path)
    df = safe_read_csv(file_path)
    if df is None:
        # Critical read failure – return result with error indicator
        result = ValidationResult(file_type=file_type, total_rows=0, passed_rows=0, file_path=str(file_path))
        result.add_error(-1, "__file__", f"Failed to read file: {file_path}")
        return result

    result = ValidationResult(file_type=file_type, total_rows=len(df), passed_rows=len(df), file_path=str(file_path))

    validate_required_columns(df, rules, result)
    validate_non_null_columns(df, rules, result)
    validate_unique_columns(df, rules, result)
    validate_date_columns(df, rules, result)
    validate_date_pairs(df, result)

    # Compute passed rows (rows with no errors)
    error_rows = {e.row for e in result.errors if e.row >= 0}
    result.passed_rows = len(df) - len(error_rows)

    return result


def validate_all_files(file_map: Dict[str, Path], cross_checks: bool = True) -> Dict[str, ValidationResult]:
    """
    Validate a mapping of file types to file paths.

    Args:
        file_map: Dictionary mapping file type to file path.
        cross_checks: Whether to perform cross-file consistency checks.

    Returns:
        Dictionary mapping file type to ValidationResult.
    """
    results: Dict[str, ValidationResult] = {}
    dataframes: Dict[str, pd.DataFrame] = {}

    for file_type, file_path in file_map.items():
        if file_type not in FILE_RULES:
            logger.warning("Unknown file type '%s', skipping validation.", file_type)
            continue
        rules = FILE_RULES[file_type]
        result = validate_single_file(file_path, file_type, rules)
        results[file_type] = result
        # If read was successful, store dataframe for cross-checks
        try:
            df = safe_read_csv(file_path)
            if df is not None:
                dataframes[file_type] = df
        except Exception as e:
            logger.warning("Could not read %s for cross-file checks: %s", file_type, e)

    # Cross-file consistency
    if cross_checks:
        cross_errors = validate_cross_file_consistency(results, dataframes)
        if cross_errors:
            # Add cross-file errors to an aggregated result or separate key
            if "cross_file" not in results:
                results["cross_file"] = ValidationResult(
                    file_type="cross_file", total_rows=0, passed_rows=0, file_path="cross_file"
                )
            for err in cross_errors:
                results["cross_file"].add_error(err.row, err.column, err.message)

    return results


def generate_report(results: Dict[str, ValidationResult]) -> Dict[str, Any]:
    """
    Generate a comprehensive validation report as a dictionary.

    Args:
        results: Mapping of file type to ValidationResult.

    Returns:
        Report dictionary with file-wise results and overall summary.
    """
    report: Dict[str, Any] = {
        "summary": {
            "total_files_validated": 0,
            "total_rows": 0,
            "total_errors": 0,
            "passed": True,
        },
        "files": {},
    }

    overall_errors = 0
    for file_type, result in results.items():
        report["files"][file_type] = result.to_dict()
        report["summary"]["total_files_validated"] += 1
        report["summary"]["total_rows"] += result.total_rows
        overall_errors += len(result.errors)

    report["summary"]["total_errors"] = overall_errors
    report["summary"]["passed"] = overall_errors == 0
    return report


# ---------------------------------------------------------------------------
# CLI entry point
# ---------------------------------------------------------------------------


def parse_arguments(argv: Optional[List[str]] = None) -> argparse.Namespace:
    """
    Parse command-line arguments.

    Args:
        argv: List of argument strings (default: sys.argv[1:]).

    Returns:
        Parsed namespace.
    """
    parser = argparse.ArgumentParser(
        description="Validate transformed CSV files against defined rules.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument(
        "files",
        nargs="+",
        type=str,
        help="CSV files to validate (e.g., issues.csv pull_requests.csv). "
             "File names are matched to expected types via FILE_NAME_MAP.",
    )
    parser.add_argument(
        "--no-cross-checks",
        action="store_true",
        help="Disable cross-file consistency checks.",
    )
    parser.add_argument(
        "--output",
        type=str,
        help="Path to write JSON report (default: stdout).",
    )
    parser.add_argument(
        "--max-errors",
        type=int,
        default=MAX_ERRORS_PER_CATEGORY,
        help=f"Maximum errors per category (default: {MAX_ERRORS_PER_CATEGORY}).",
    )
    return parser.parse_args(argv)


def main(argv: Optional[List[str]] = None) -> int:
    """
    Main entry point for the validation script.

    Args:
        argv: Command-line arguments (default: sys.argv[1:]).

    Returns:
        Exit code (0 = success, 1 = validation failure, 2 = error).
    """
    args = parse_arguments(argv)

    # Update global MAX_ERRORS_PER_CATEGORY if provided
    global MAX_ERRORS_PER_CATEGORY
    MAX_ERRORS_PER_CATEGORY = args.max_errors

    # Build file map by matching basenames
    file_map: Dict[str, Path] = {}
    for fpath_str in args.files:
        file_path = Path(fpath_str)
        try:
            resolved = validate_file_path(file_path)
        except (FileAccessError, SecurityError) as e:
            logger.error("File validation failed: %s", e)
            continue

        basename = resolved.name
        matched = False
        for file_type, expected_name in FILE_NAME_MAP.items():
            if basename == expected_name:
                file_map[file_type] = resolved
                matched = True
                break
        if not matched:
            logger.warning("File '%s' does not match any expected name; treating as unknown.", basename)

    if not file_map:
        logger.error("No valid files provided. Exiting.")
        return 2

    # Run validation
    try:
        results = validate_all_files(file_map, cross_checks=not args.no_cross_checks)
    except Exception as e:
        logger.exception("Unexpected error during validation.")
        return 2

    # Generate report
    report = generate_report(results)

    # Output report
    report_json = json.dumps(report, indent=2, default=str)
    if args.output:
        output_path = Path(args.output)
        try:
            output_path.write_text(report_json, encoding="utf-8")
            logger.info("Report written to %s", output_path)
        except OSError as e:
            logger.error("Failed to write report to %s: %s", output_path, e)
            # Fallback to stdout
            print(report_json)
    else:
        print(report_json)

    # Log summary
    summary = report["summary"]
    logger.info("Validation complete: %d errors found across %d files.",
                summary["total_errors"], summary["total_files_validated"])

    return 0 if summary["passed"] else 1


if __name__ == "__main__":
    sys.exit(main())