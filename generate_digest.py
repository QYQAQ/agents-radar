#!/usr/bin/env python3
"""
Agenda: Aggregate per-repo CSV files into a single digest CSV and produce summary statistics.

This script expects a directory containing CSV files, one per repository, each with at least the
following columns: id, type (issue/pr), title, state, created_at, updated_at, url (optional).
It generates:
  - A consolidated digest CSV with all records and a 'repo' column.
  - A summary JSON file with total issues, PRs, project count, and top N most active repos.

Usage:
    python generate_digest.py --input_dir ./per_repo_csvs --output_dir ./digest --date 2026-05-30

Dependencies: pandas (>=1.3), optional openpyxl for Excel output (not used here).
"""

from __future__ import annotations

import argparse
import json
import logging
import sys
from collections.abc import Sequence
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional

import pandas as pd

# -----------------------------------------------------------------------------
# Logging configuration
# -----------------------------------------------------------------------------
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    handlers=[logging.StreamHandler(sys.stdout)],
)
logger = logging.getLogger(__name__)

# -----------------------------------------------------------------------------
# Constants
# -----------------------------------------------------------------------------
REQUIRED_COLUMNS: frozenset = frozenset({"id", "type", "title", "state", "created_at", "updated_at"})
OPTIONAL_COLUMNS: frozenset = frozenset({"url", "labels", "assignee"})
DEFAULT_TOP_REPOS: int = 5
EXPECTED_CSV_ENCODING: str = "utf-8-sig"
VALID_TYPES: frozenset = frozenset({"issue", "pr", "pull_request"})
DATE_INPUT_FORMAT: str = "%Y-%m-%d"
OUTPUT_DATE_FORMAT: str = "%Y-%m-%d %H:%M UTC"
CSV_SUFFIX: str = ".csv"

# -----------------------------------------------------------------------------
# Custom Exceptions
# -----------------------------------------------------------------------------
class DigestError(Exception):
    """Base exception for digest generation errors."""


class DataValidationError(DigestError):
    """Raised when data validation fails."""


class ConfigurationError(DigestError):
    """Raised when configuration (e.g., arguments) is invalid."""


# -----------------------------------------------------------------------------
# Helpers
# -----------------------------------------------------------------------------
def _validate_date_str(date_str: str) -> None:
    """Validate that a string conforms to ISO date format (YYYY-MM-DD).

    Parameters
    ----------
    date_str : str
        Date string to validate.

    Raises
    ------
    ValueError
        If the string does not match the expected format.
    """
    try:
        datetime.strptime(date_str, DATE_INPUT_FORMAT)
    except ValueError as exc:
        raise ValueError(f"Date '{date_str}' does not match format YYYY-MM-DD.") from exc


def _write_csv(df: pd.DataFrame, output_path: Path) -> None:
    """Write a DataFrame to a CSV file with consistent encoding.

    Parameters
    ----------
    df : pd.DataFrame
        DataFrame to write.
    output_path : Path
        Destination file path.

    Raises
    ------
    DigestError
        If the file cannot be written due to permissions or disk issues.
    """
    try:
        df.to_csv(output_path, index=False, encoding=EXPECTED_CSV_ENCODING)
        logger.info("Written CSV to %s (rows=%d)", output_path, len(df))
    except PermissionError:
        logger.error("Permission denied writing to %s", output_path)
        raise DigestError(f"Permission denied: {output_path}") from None
    except OSError as exc:
        logger.exception("Failed to write CSV to %s", output_path)
        raise DigestError(f"Failed to write CSV: {exc}") from exc


def _write_json(data: Dict[str, Any], output_path: Path) -> None:
    """Write a dictionary to a JSON file with indentation.

    Parameters
    ----------
    data : Dict[str, Any]
        Data to serialize.
    output_path : Path
        Destination file path.

    Raises
    ------
    DigestError
        If the file cannot be written.
    """
    try:
        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        logger.info("Written JSON to %s", output_path)
    except (OSError, PermissionError) as exc:
        logger.error("Failed to write JSON to %s: %s", output_path, exc)
        raise DigestError(f"Failed to write JSON: {exc}") from exc


def _parse_arguments(argv: Optional[Sequence[str]] = None) -> argparse.Namespace:
    """Parse command-line arguments with validation.

    Parameters
    ----------
    argv : Sequence[str] or None
        Command-line arguments (default: sys.argv[1:]).

    Returns
    -------
    argparse.Namespace
        Parsed arguments.

    Raises
    ------
    ConfigurationError
        If required arguments are missing or invalid.
    """
    parser = argparse.ArgumentParser(
        description="Aggregate per-repo CSV files into a digest and produce summary statistics."
    )
    parser.add_argument(
        "--input_dir",
        type=Path,
        required=True,
        help="Directory containing per-repo CSV files.",
    )
    parser.add_argument(
        "--output_dir",
        type=Path,
        required=True,
        help="Directory for output digest CSV and summary JSON.",
    )
    parser.add_argument(
        "--date",
        type=str,
        required=True,
        help="Digest date in YYYY-MM-DD format.",
    )
    parser.add_argument(
        "--top_repos",
        type=int,
        default=DEFAULT_TOP_REPOS,
        help=f"Number of top repos to include in summary (default: {DEFAULT_TOP_REPOS}).",
    )

    # Use parse_known_args for partial error handling, but keep strict
    try:
        args = parser.parse_args(argv)
    except SystemExit as exc:
        raise ConfigurationError("Argument parsing failed.") from exc

    # Validate date
    try:
        _validate_date_str(args.date)
    except ValueError as exc:
        parser.error(str(exc))
        raise ConfigurationError(str(exc)) from exc

    # Validate input directory
    if not args.input_dir.is_dir():
        parser.error(f"Input directory does not exist or is not a directory: {args.input_dir}")
        raise ConfigurationError(f"Invalid input directory: {args.input_dir}")

    # Ensure top_repos is positive
    if args.top_repos <= 0:
        parser.error("top_repos must be a positive integer.")
        raise ConfigurationError("top_repos must be positive.")

    return args


# -----------------------------------------------------------------------------
# Data Validation
# -----------------------------------------------------------------------------
def validate_dataframe(df: pd.DataFrame, repo_name: str) -> pd.DataFrame:
    """Validate required columns and sanitise data for a single repo DataFrame.

    Parameters
    ----------
    df : pd.DataFrame
        Raw DataFrame loaded from CSV.
    repo_name : str
        Repository name (used for logging).

    Returns
    -------
    pd.DataFrame
        Cleaned DataFrame with coerced types and replaced invalid values.

    Raises
    ------
    DataValidationError
        If DataFrame is not of the expected type or is empty.
    """
    if not isinstance(df, pd.DataFrame):
        raise DataValidationError(f"Expected pd.DataFrame, got {type(df).__name__}")

    if df.empty:
        logger.warning("Repo '%s' DataFrame is empty.", repo_name)
        return df

    # Add missing required columns
    missing_cols = REQUIRED_COLUMNS - set(df.columns)
    if missing_cols:
        logger.warning("Repo '%s' missing columns: %s. Adding empty placeholders.", repo_name, missing_cols)
        for col in missing_cols:
            df[col] = ""

    # Normalise type column
    if "type" in df.columns:
        df["type"] = df["type"].astype(str).str.lower().str.strip()
        df["type"] = df["type"].replace({"pull_request": "pr"})
        invalid_mask = ~df["type"].isin({"issue", "pr"})
        if invalid_mask.any():
            invalid_vals = df.loc[invalid_mask, "type"].unique().tolist()
            logger.warning("Repo '%s' has invalid type values: %s. Setting to 'issue'.", repo_name, invalid_vals)
            df.loc[invalid_mask, "type"] = "issue"

    # Coerce id to string
    if "id" in df.columns:
        df["id"] = df["id"].astype(str)

    # Convert date columns to datetime if possible (silent on failure)
    for col in ["created_at", "updated_at"]:
        if col in df.columns:
            try:
                df[col] = pd.to_datetime(df[col], errors="coerce")
            except Exception:
                logger.warning("Could not convert '%s' to datetime for repo '%s'.", col, repo_name)

    return df


# -----------------------------------------------------------------------------
# Main Logic
# -----------------------------------------------------------------------------
def _load_and_validate_csvs(input_dir: Path) -> List[pd.DataFrame]:
    """Load all CSV files from input directory, validate, and return list of DataFrames.

    Parameters
    ----------
    input_dir : Path
        Directory containing per-repo CSV files.

    Returns
    -------
    List[pd.DataFrame]
        List of validated DataFrames, each with a 'repo' column added.

    Raises
    ------
    DataValidationError
        If no CSV files found or all files fail to load.
    """
    csv_files: List[Path] = sorted(input_dir.glob(f"*{CSV_SUFFIX}"))
    if not csv_files:
        raise DataValidationError(f"No CSV files found in {input_dir}")

    dataframes: List[pd.DataFrame] = []
    for csv_file in csv_files:
        repo_name: str = csv_file.stem  # filename without extension
        logger.debug("Processing CSV: %s", csv_file)
        try:
            df: pd.DataFrame = pd.read_csv(csv_file, encoding=EXPECTED_CSV_ENCODING, dtype_backend="numpy_nullable")
        except (pd.errors.EmptyDataError, pd.errors.ParserError, FileNotFoundError, PermissionError) as exc:
            logger.error("Failed to read CSV %s: %s", csv_file, exc)
            continue
        except Exception as exc:
            logger.exception("Unexpected error reading CSV %s", csv_file)
            continue

        if df.empty:
            logger.warning("Skipping empty CSV: %s", csv_file)
            continue

        try:
            df = validate_dataframe(df, repo_name)
        except DataValidationError as exc:
            logger.error("Validation failed for CSV %s: %s", csv_file, exc)
            continue

        # Add repo column
        df["repo"] = repo_name
        dataframes.append(df)

    if not dataframes:
        raise DataValidationError("No valid DataFrames could be loaded from CSV files.")

    return dataframes


def _calculate_summary(digest_df: pd.DataFrame, top_repos: int) -> Dict[str, Any]:
    """Calculate summary statistics from the consolidated digest DataFrame.

    Parameters
    ----------
    digest_df : pd.DataFrame
        Consolidated DataFrame with columns: repo, type, state, etc.
    top_repos : int
        Number of top repos by total activity to include.

    Returns
    -------
    Dict[str, Any]
        Summary dictionary with keys: total_issues, total_prs, project_count,
        top_active_repos, generated_at, digest_date.
    """
    total_issues: int = int((digest_df["type"] == "issue").sum())
    total_prs: int = int((digest_df["type"] == "pr").sum())
    project_count: int = digest_df["repo"].nunique()
    repo_activity: pd.Series = digest_df["repo"].value_counts()
    top_active: List[Dict[str, Any]] = [
        {"repo": repo, "count": int(count)}
        for repo, count in repo_activity.head(top_repos).items()
    ]

    summary: Dict[str, Any] = {
        "total_issues": total_issues,
        "total_prs": total_prs,
        "project_count": project_count,
        "top_active_repos": top_active,
        "generated_at": datetime.now(timezone.utc).strftime(OUTPUT_DATE_FORMAT),
        "digest_date": args.date if "args" in dir() else "",  # noqa
    }
    return summary


def generate_digest(input_dir: Path, output_dir: Path, date_str: str, top_repos: int = DEFAULT_TOP_REPOS) -> None:
    """Main orchestrator: load CSVs, aggregate, write outputs.

    Parameters
    ----------
    input_dir : Path
        Directory containing per-repo CSV files.
    output_dir : Path
        Directory for output files.
    date_str : str
        Digest date in YYYY-MM-DD format.
    top_repos : int, optional
        Number of top active repos to include (default: 5).

    Raises
    ------
    DigestError
        If any step fails.
    """
    logger.info("Starting digest generation for %s from %s", date_str, input_dir)

    # Ensure output directory exists
    try:
        output_dir.mkdir(parents=True, exist_ok=True)
    except OSError as exc:
        raise DigestError(f"Cannot create output directory {output_dir}: {exc}") from exc

    # Load and validate CSVs
    try:
        dataframes: List[pd.DataFrame] = _load_and_validate_csvs(input_dir)
    except DataValidationError as exc:
        raise DigestError(f"Data loading failed: {exc}") from exc

    # Concatenate all DataFrames (performance: single concat)
    logger.info("Concatenating %d DataFrames...", len(dataframes))
    try:
        digest_df: pd.DataFrame = pd.concat(dataframes, ignore_index=True, sort=False)
    except Exception as exc:
        raise DigestError(f"Failed to concatenate DataFrames: {exc}") from exc

    if digest_df.empty:
        raise DigestError("Digest DataFrame is empty after concatenation.")

    # Write digest CSV
    digest_csv_path: Path = output_dir / f"digest_{date_str}.csv"
    _write_csv(digest_df, digest_csv_path)

    # Calculate and write summary JSON
    summary: Dict[str, Any] = _calculate_summary(digest_df, top_repos)
    summary_json_path: Path = output_dir / f"summary_{date_str}.json"
    _write_json(summary, summary_json_path)

    logger.info(
        "Digest generation complete: %d issues, %d PRs, %d projects.",
        summary["total_issues"],
        summary["total_prs"],
        summary["project_count"],
    )


# -----------------------------------------------------------------------------
# Entry Point
# -----------------------------------------------------------------------------
def main(argv: Optional[Sequence[str]] = None) -> int:
    """Command-line entry point.

    Parameters
    ----------
    argv : Sequence[str] or None
        Command-line arguments (default: sys.argv[1:]).

    Returns
    -------
    int
        Exit code: 0 on success, 1 on error.
    """
    try:
        args: argparse.Namespace = _parse_arguments(argv)
        # Store date for summary (workaround)
        global _digest_date  # noqa: keep for summary
        _digest_date = args.date

        generate_digest(
            input_dir=args.input_dir,
            output_dir=args.output_dir,
            date_str=args.date,
            top_repos=args.top_repos,
        )
        return 0
    except ConfigurationError as exc:
        logger.error("Configuration error: %s", exc)
        return 1
    except DigestError as exc:
        logger.error("Digest generation failed: %s", exc)
        return 1
    except Exception as exc:
        logger.exception("Unexpected fatal error: %s", exc)
        return 1


if __name__ == "__main__":
    sys.exit(main())