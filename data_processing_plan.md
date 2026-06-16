#!/usr/bin/env python3
"""
GitHub Ecosystem Data Pipeline

Orchestrates fetching, transforming, validating, and reporting on
GitHub repository and activity data for ecosystem analysis.

Usage:
    python pipeline.py

Environment Variables:
    GITHUB_TOKEN (optional) – GitHub personal access token for higher rate limits.
    REQUEST_TIMEOUT (optional) – HTTP request timeout in seconds (default: 15.0).
    MAX_RETRIES (optional) – number of retry attempts per request (default: 5).
    LOG_LEVEL (optional) – logging level (default: INFO).
    OUTPUT_DIR (optional) – directory for generated reports (default: reports).
"""

import asyncio
import json
import logging
import os
import sys
import time
from contextlib import asynccontextmanager
from dataclasses import dataclass, field, asdict
from datetime import datetime, timezone
from functools import lru_cache
from pathlib import Path
from typing import (
    Any,
    AsyncContextManager,
    AsyncGenerator,
    Dict,
    List,
    Mapping,
    Optional,
    Sequence,
    Set,
    Tuple,
    Union,
    cast,
)

import aiohttp
import backoff
import httpx
import tenacity
from pydantic import BaseModel, Field, ValidationError, field_validator, model_validator

# ---------------------------------------------------------------------------
# Configuration & Logging
# ---------------------------------------------------------------------------

_LOG_LEVEL: str = os.environ.get("LOG_LEVEL", "INFO").upper()
logging.basicConfig(
    level=getattr(logging, _LOG_LEVEL, logging.INFO),
    format="%(asctime)s [%(levelname)s] %(name)s - %(message)s",
    handlers=[
        logging.StreamHandler(sys.stdout),
        logging.FileHandler(
            Path(os.environ.get("LOG_DIR", "logs")) / "pipeline.log", mode="a"
        ),
    ],
)
logger: logging.Logger = logging.getLogger("ecosystem_pipeline")

# Ensure log directory exists
Path(os.environ.get("LOG_DIR", "logs")).mkdir(parents=True, exist_ok=True)

# Environment-driven configuration
GITHUB_TOKEN: Optional[str] = os.environ.get("GITHUB_TOKEN")
BASE_URL: str = "https://api.github.com"
REQUEST_TIMEOUT: float = float(os.environ.get("REQUEST_TIMEOUT", "15.0"))
MAX_RETRIES: int = int(os.environ.get("MAX_RETRIES", "5"))
OUTPUT_DIR: Path = Path(os.environ.get("OUTPUT_DIR", "reports"))
REPO_LIST_FILE: Optional[str] = os.environ.get("REPO_LIST_FILE")

# ---------------------------------------------------------------------------
# Data Models (Pydantic for validation)
# ---------------------------------------------------------------------------


class GitHubRepo(BaseModel):
    """Normalized repository data from GitHub API."""

    name: str
    full_name: str
    description: Optional[str] = None
    url: str
    stars: int = Field(ge=0, default=0)
    forks: int = Field(ge=0, default=0)
    open_issues_count: int = Field(ge=0, default=0)
    language: Optional[str] = None
    topics: List[str] = Field(default_factory=list)
    last_updated: Optional[str] = None

    @field_validator("full_name")
    @classmethod
    def validate_full_name(cls, v: str) -> str:
        """Validate that full_name follows 'owner/repo' format."""
        if not v or "/" not in v:
            raise ValueError("full_name must be in 'owner/repo' format")
        parts = v.split("/", 1)
        if not parts[0] or not parts[1]:
            raise ValueError("owner and repo parts must not be empty")
        return v

    @field_validator("url")
    @classmethod
    def validate_url(cls, v: str) -> str:
        """Ensure url is a valid HTTPS URL."""
        if v and not v.startswith("https://"):
            raise ValueError("URL must be HTTPS")
        return v

    @field_validator("topics", mode="before")
    @classmethod
    def validate_topics(cls, v: Any) -> List[str]:
        """Ensure topics is a list of non-empty strings."""
        if not isinstance(v, list):
            raise ValueError("topics must be a list")
        for topic in v:
            if not isinstance(topic, str) or not topic.strip():
                raise ValueError("Each topic must be a non-empty string")
        return [t.strip() for t in v]


class RepositoryActivity(BaseModel):
    """Activity metrics per repository."""

    repo_name: str
    issues_updated_last_24h: int = Field(default=0, ge=0)
    prs_updated_last_24h: int = Field(default=0, ge=0)
    total_issues: int = Field(default=0, ge=0)
    total_prs: int = Field(default=0, ge=0)
    recent_commits: int = Field(default=0, ge=0)

    @field_validator("repo_name")
    @classmethod
    def validate_repo_name(cls, v: str) -> str:
        """Validate repository name format."""
        if not v or "/" not in v:
            raise ValueError("repo_name must be in 'owner/repo' format")
        return v


class EcosystemReport(BaseModel):
    """Final aggregated report for the ecosystem."""

    generated_at: str = Field(
        default_factory=lambda: datetime.now(timezone.utc).isoformat()
    )
    total_repos: int = 0
    total_stars: int = 0
    total_forks: int = 0
    total_issues: int = 0
    total_prs: int = 0
    repos: List[GitHubRepo] = Field(default_factory=list)
    activity: Dict[str, RepositoryActivity] = Field(default_factory=dict)

    @model_validator(mode="after")
    def recompute_totals(self) -> "EcosystemReport":
        """Recompute totals from repos and activity data."""
        self.total_repos = len(self.repos)
        self.total_stars = sum(r.stars for r in self.repos)
        self.total_forks = sum(r.forks for r in self.repos)
        self.total_issues = sum(a.total_issues for a in self.activity.values())
        self.total_prs = sum(a.total_prs for a in self.activity.values())
        return self


# ---------------------------------------------------------------------------
# Custom Exceptions
# ---------------------------------------------------------------------------


class PipelineError(Exception):
    """Base pipeline exception."""
    pass


class FetchError(PipelineError):
    """Raised when data retrieval fails after retries."""
    pass


class TransformError(PipelineError):
    """Raised on data transformation failures."""
    pass


class ValidationPipelineError(PipelineError):
    """Raised on data validation failures."""
    pass


class ConfigError(PipelineError):
    """Raised on configuration errors."""
    pass


# ---------------------------------------------------------------------------
# Utility Functions
# ---------------------------------------------------------------------------


def load_repo_list(file_path: Optional[str] = None) -> List[str]:
    """
    Load list of repository full names from a file or environment variable.

    If file_path is provided, it reads one repo per line (ignoring comments and blank lines).
    If not provided, it falls back to the REPO_LIST_FILE environment variable.
    If neither is set, raises ConfigError.

    Args:
        file_path: Optional path to a text file containing repo names.

    Returns:
        List of repository full names (e.g., ["owner/repo1", "owner/repo2"]).

    Raises:
        ConfigError: If no repo list source is configured or file not found.
    """
    source = file_path or REPO_LIST_FILE
    if not source:
        raise ConfigError(
            "No repository list provided: set REPO_LIST_FILE environment variable "
            "or pass file_path to load_repo_list()."
        )

    path = Path(source)
    if not path.exists():
        raise ConfigError(f"Repository list file not found: {path}")

    repos: List[str] = []
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith("#"):
                # Basic validation
                if "/" in line and not line.startswith("/") and not line.endswith("/"):
                    repos.append(line)
                else:
                    logger.warning("Skipping invalid repo line: %s", line)
    if not repos:
        raise ConfigError("No valid repositories found in the list file.")
    return repos


# ---------------------------------------------------------------------------
# Data Fetching (Step 1)
# ---------------------------------------------------------------------------


async def fetch_github_data(
    repo_full_names: Sequence[str],
    *,
    token: Optional[str] = GITHUB_TOKEN,
    session: Optional[aiohttp.ClientSession] = None,
) -> Dict[str, Dict[str, Any]]:
    """
    Fetch raw repository data from GitHub API concurrently.

    Args:
        repo_full_names: List of 'owner/repo' strings.
        token: GitHub personal access token (optional, increases rate limit).
        session: Shared aiohttp session (created if not provided).

    Returns:
        Dictionary mapping repo full_name to raw API response dict.

    Raises:
        FetchError: If all attempts fail for all repositories.
    """
    headers: Dict[str, str] = {"Accept": "application/vnd.github.v3+json"}
    if token:
        headers["Authorization"] = f"Bearer {token}"

    if session is None:
        async with aiohttp.ClientSession() as s:
            return await _fetch_all(repo_full_names, s, headers)
    else:
        return await _fetch_all(repo_full_names, session, headers)


async def _fetch_all(
    repo_full_names: Sequence[str],
    session: aiohttp.ClientSession,
    headers: Dict[str, str],
) -> Dict[str, Dict[str, Any]]:
    """
    Internal helper to run concurrent fetches with retries.

    Args:
        repo_full_names: List of repository full names.
        session: aiohttp ClientSession.
        headers: Request headers.

    Returns:
        Dict of full_name -> raw response data.
    """
    tasks = [
        _fetch_single_with_retry(full_name, session, headers)
        for full_name in repo_full_names
    ]
    results = await asyncio.gather(*tasks, return_exceptions=True)

    data_dict: Dict[str, Dict[str, Any]] = {}
    for full_name, result in zip(repo_full_names, results):
        if isinstance(result, Exception):
            logger.error("Failed to fetch %s: %s", full_name, result)
            continue
        data_dict[full_name] = result

    if not data_dict:
        raise FetchError("No repository data retrieved; all fetches failed.")
    return data_dict


@tenacity.retry(
    stop=tenacity.stop_after_attempt(MAX_RETRIES),
    wait=tenacity.wait_exponential(multiplier=1, min=1, max=60),
    before_sleep=tenacity.before_sleep_log(logger, logging.WARNING),
    retry=tenacity.retry_if_exception_type(
        (aiohttp.ClientError, asyncio.TimeoutError)
    ),
    reraise=True,
)
async def _fetch_single_with_retry(
    full_name: str,
    session: aiohttp.ClientSession,
    headers: Dict[str, str],
) -> Dict[str, Any]:
    """
    Fetch a single repository with exponential backoff and retry on transient errors.

    Args:
        full_name: Repository full name (owner/repo).
        session: aiohttp ClientSession.
        headers: Request headers.

    Returns:
        Parsed JSON response as dict.

    Raises:
        FetchError: If request fails after all retries.
    """
    url = f"{BASE_URL}/repos/{full_name}"
    try:
        async with session.get(
            url,
            headers=headers,
            timeout=aiohttp.ClientTimeout(total=REQUEST_TIMEOUT),
        ) as resp:
            if resp.status == 403:
                logger.warning("Rate limit hit (403) on %s; waiting 60s...", full_name)
                await asyncio.sleep(60)
                # Retry will handle if it fails again
                resp.raise_for_status()
            elif resp.status == 404:
                logger.warning("Repository %s not found (404), skipping.", full_name)
                # Return empty dict to indicate not found, but not raise exception
                return {"not_found": True, "full_name": full_name}
            elif resp.status >= 500:
                logger.error(
                    "Server error on %s (status %d).", full_name, resp.status
                )
                resp.raise_for_status()
            else:
                resp.raise_for_status()  # Raises on any other error status
            data: Dict[str, Any] = await resp.json()
            return data
    except aiohttp.ClientConnectorError as e:
        logger.error("Connection error for %s: %s", full_name, e)
        raise
    except asyncio.TimeoutError as e:
        logger.error("Timeout fetching %s: %s", full_name, e)
        raise
    except aiohttp.ClientResponseError as e:
        logger.error("HTTP error for %s: %s", full_name, e)
        raise


# ---------------------------------------------------------------------------
# Data Transformation (Step 2)
# ---------------------------------------------------------------------------


def transform_repo_data(
    raw_data: Dict[str, Dict[str, Any]],
) -> List[GitHubRepo]:
    """
    Transform raw API responses into validated GitHubRepo objects.

    Args:
        raw_data: Dictionary mapping repo full_name to raw API response dict.

    Returns:
        List of validated GitHubRepo instances.

    Raises:
        TransformError: If transformation fails due to invalid data.
    """
    repos: List[GitHubRepo] = []
    errors: List[str] = []
    for full_name, raw in raw_data.items():
        # Skip placeholder for not found
        if raw.get("not_found"):
            logger.warning("Skipping missing repository: %s", full_name)
            continue
        try:
            repo = GitHubRepo(
                name=raw.get("name", full_name.split("/")[-1]),
                full_name=full_name,
                description=raw.get("description"),
                url=raw.get("html_url", ""),
                stars=raw.get("stargazers_count", 0),
                forks=raw.get("forks_count", 0),
                open_issues_count=raw.get("open_issues_count", 0),
                language=raw.get("language"),
                topics=raw.get("topics", []),
                last_updated=raw.get("updated_at"),
            )
            repos.append(repo)
            logger.debug("Transformed repo: %s", full_name)
        except ValidationError as e:
            error_msg = f"Validation error for {full_name}: {e}"
            errors.append(error_msg)
            logger.error(error_msg)
        except Exception as e:
            error_msg = f"Unexpected error transforming {full_name}: {e}"
            errors.append(error_msg)
            logger.error(error_msg)

    if errors and not repos:
        raise TransformError(
            f"All transformations failed. Errors: {'; '.join(errors[:5])}"
        )

    return repos


def transform_activity_data(
    repos: List[GitHubRepo],
    issues_data: Optional[Dict[str, Dict[str, Any]]] = None,
    prs_data: Optional[Dict[str, Dict[str, Any]]] = None,
) -> Dict[str, RepositoryActivity]:
    """
    Transform raw activity data into RepositoryActivity objects.

    Args:
        repos: List of validated GitHubRepo objects.
        issues_data: Optional raw data for issues (repo -> issues list).
        prs_data: Optional raw data for pull requests (repo -> prs list).

    Returns:
        Dictionary mapping repo full_name to RepositoryActivity.

    Raises:
        TransformError: If processing fails critically.
    """
    activities: Dict[str, RepositoryActivity] = {}
    for repo in repos:
        try:
            # Placeholder: In production, fetch issues/PRs from separate endpoints
            # Here we simulate with open_issues_count
            activity = RepositoryActivity(
                repo_name=repo.full_name,
                total_issues=repo.open_issues_count,
                total_prs=repo.open_issues_count,  # Simplified, would be separate count
                issues_updated_last_24h=0,
                prs_updated_last_24h=0,
                recent_commits=0,
            )
            activities[repo.full_name] = activity
        except ValidationError as e:
            logger.error("Validation error creating activity for %s: %s", repo.full_name, e)
        except Exception as e:
            logger.error("Unexpected error creating activity for %s: %s", repo.full_name, e)

    return activities


# ---------------------------------------------------------------------------
# Data Validation (Step 3)
# ---------------------------------------------------------------------------


def validate_report(report: EcosystemReport) -> EcosystemReport:
    """
    Validate the aggregated report for consistency.

    Args:
        report: EcosystemReport to validate.

    Returns:
        The validated report (may be modified for consistency).

    Raises:
        ValidationPipelineError: If validation fails critically.
    """
    if report.total_repos != len(report.repos):
        logger.warning(
            "Report.total_repos (%d) does not match number of repos (%d). Correcting.",
            report.total_repos,
            len(report.repos),
        )
        report.total_repos = len(report.repos)

    if report.total_repos == 0:
        raise ValidationPipelineError("Report has zero repositories; cannot proceed.")

    # Check for duplicate repo names
    repo_names: Set[str] = {r.full_name for r in report.repos}
    if len(repo_names) != len(report.repos):
        raise ValidationPipelineError("Duplicate repository names found in report.")

    # Verify activity keys match repo names
    for activity_repo in report.activity:
        if activity_repo not in repo_names:
            raise ValidationPipelineError(
                f"Activity for unknown repo: {activity_repo}"
            )

    return report


# ---------------------------------------------------------------------------
# Reporting (Step 4)
# ---------------------------------------------------------------------------


def generate_report(
    repos: List[GitHubRepo], activity: Dict[str, RepositoryActivity]
) -> EcosystemReport:
    """
    Create the final EcosystemReport from processed data.

    Args:
        repos: List of validated GitHubRepo objects.
        activity: Dictionary of activity data.

    Returns:
        Complete EcosystemReport instance.
    """
    report = EcosystemReport(
        repos=repos,
        activity=activity,
    )
    # The model validator will recompute totals
    return report


def export_report(report: EcosystemReport, output_path: Path) -> None:
    """
    Export report to JSON file with pretty printing.

    Args:
        report: EcosystemReport to export.
        output_path: Path to write JSON file.

    Raises:
        OSError: If file writing fails.
    """
    try:
        output_path.parent.mkdir(parents=True, exist_ok=True)
        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(report.model_dump(), f, indent=2, ensure_ascii=False)
        logger.info("Report exported to %s", output_path)
    except OSError as e:
        logger.error("Failed to export report: %s", e)
        raise


def generate_markdown_summary(report: EcosystemReport) -> str:
    """
    Generate a human-readable Markdown summary of the ecosystem report.

    Args:
        report: EcosystemReport to summarize.

    Returns:
        String containing Markdown summary.
    """
    lines: List[str] = []
    lines.append("# Ecosystem Report")
    lines.append(f"**Generated:** {report.generated_at}")
    lines.append("")
    lines.append("## Overview")
    lines.append(f"- Total repositories: {report.total_repos}")
    lines.append(f"- Total stars: {report.total_stars}")
    lines.append(f"- Total forks: {report.total_forks}")
    lines.append(f"- Total issues: {report.total_issues}")
    lines.append(f"- Total PRs: {report.total_prs}")
    lines.append("")
    lines.append("## Repositories")
    for repo in sorted(report.repos, key=lambda x: x.stars, reverse=True):
        lines.append(f"- **[{repo.full_name}]({repo.url})** - ⭐ {repo.stars}")
    lines.append("")
    lines.append("## Activity")
    for repo_name, activity in sorted(report.activity.items()):
        lines.append(f"- {repo_name}: Issues: {activity.total_issues}, PRs: {activity.total_prs}")
    lines.append("")
    lines.append("---")
    lines.append("*Auto-generated by GitHub Ecosystem Pipeline*")
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Pipeline Orchestration
# ---------------------------------------------------------------------------


@asynccontextmanager
async def pipeline_context() -> AsyncGenerator[None, None]:
    """
    Context manager for pipeline setup and teardown.

    Creates necessary directories and cleans up resources.
    """
    logger.info("Pipeline starting...")
    try:
        yield
    finally:
        logger.info("Pipeline finished.")


async def run_pipeline(
    repo_list: Sequence[str],
    output_dir: Path = OUTPUT_DIR,
    token: Optional[str] = GITHUB_TOKEN,
) -> EcosystemReport:
    """
    Execute the full pipeline: fetch, transform, validate, report.

    Args:
        repo_list: List of repository full names.
        output_dir: Directory to write reports.
        token: GitHub token for authentication.

    Returns:
        Final validated EcosystemReport.

    Raises:
        PipelineError: If any stage fails critically.
    """
    async with pipeline_context():
        logger.info("Fetching data for %d repositories...", len(repo_list))
        raw_data: Dict[str, Dict[str, Any]] = await fetch_github_data(repo_list, token=token)

        logger.info("Transforming data...")
        repos: List[GitHubRepo] = transform_repo_data(raw_data)
        if not repos:
            raise TransformError("No repositories transformed successfully.")

        logger.info("Building activity data...")
        activity: Dict[str, RepositoryActivity] = transform_activity_data(repos)

        logger.info("Generating report...")
        report: EcosystemReport = generate_report(repos, activity)

        logger.info("Validating report...")
        report = validate_report(report)

        # Export both JSON and Markdown
        json_path = output_dir / f"ecosystem_report_{datetime.now(timezone.utc).strftime('%Y%m%d_%H%M%S')}.json"
        export_report(report, json_path)

        md_path = output_dir / f"ecosystem_summary_{datetime.now(timezone.utc).strftime('%Y%m%d_%H%M%S')}.md"
        markdown_summary = generate_markdown_summary(report)
        output_dir.mkdir(parents=True, exist_ok=True)
        with open(md_path, "w", encoding="utf-8") as f:
            f.write(markdown_summary)
        logger.info("Markdown summary written to %s", md_path)

        return report


# ---------------------------------------------------------------------------
# Main Entry Point
# ---------------------------------------------------------------------------


async def main() -> None:
    """
    Main entry point for the pipeline.

    Loads repo list, runs pipeline, handles exceptions.
    """
    try:
        repo_list: List[str] = load_repo_list()
        logger.info("Loaded %d repositories from file.", len(repo_list))
    except ConfigError as e:
        logger.error("Configuration error: %s", e)
        sys.exit(1)

    try:
        report: EcosystemReport = await run_pipeline(repo_list)
        logger.info("Pipeline completed successfully. Total repos: %d", report.total_repos)
    except (FetchError, TransformError, ValidationPipelineError) as e:
        logger.error("Pipeline failed: %s", e)
        sys.exit(2)
    except Exception as e:
        logger.exception("Unexpected pipeline error: %s", e)
        sys.exit(3)


if __name__ == "__main__":
    asyncio.run(main())