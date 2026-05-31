#!/usr/bin/env python3
"""
fetch_github_data.py - Fetches issues, PRs, and releases from GitHub for all 13 repositories.

Uses pagination, respects rate limits, and stores raw JSON in a cache directory.
Designed for the first stage of the OpenClaw Ecosystem data pipeline.

Usage:
    export GITHUB_TOKEN=your_token
    python fetch_github_data.py [--cache-dir PATH] [--max-pages N] [--log-level LEVEL]

Environment Variables:
    GITHUB_TOKEN (required): GitHub personal access token for authentication.
"""

from __future__ import annotations

import argparse
import json
import logging
import os
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, Generator, List, Optional, Tuple, Union

import requests
from requests.adapters import HTTPAdapter
from requests.exceptions import (
    ConnectionError,
    HTTPError,
    SSLError,
    Timeout,
    TooManyRedirects,
)
from urllib3.util.retry import Retry

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

# All 13 repositories. Format: (owner, repo)
REPOSITORIES: List[Tuple[str, str]] = [
    ("openclaw", "openclaw"),
    ("HKUDS", "nanobot"),
    ("nousresearch", "hermes-agent"),
    ("sipeed", "picoclaw"),
    ("qwibitai", "nanoclaw"),
    ("nullclaw", "nullclaw"),
    ("nearai", "ironclaw"),
    ("netease-youdao", "LobsterAI"),
    ("TinyAGI", "tinyagi"),
    ("moltis-org", "moltis"),
    ("agentscope-ai", "CoPaw"),
    ("qhkm", "zeptoclaw"),
    ("zeroclaw-labs", "zeroclaw"),
]

# GitHub REST API base URL
API_BASE = "https://api.github.com"

# Per-page size (max 100)
PER_PAGE = 100

# Default cache directory (relative to script location)
DEFAULT_CACHE_DIR = Path(__file__).resolve().parent.parent / "cache" / "raw"

# Request timeout (seconds)
TIMEOUT = 30

# Max retries on 5xx or connection errors
MAX_RETRIES = 3

# Backoff factor for retries
BACKOFF_FACTOR = 0.5

# Supported log levels
LOG_LEVELS: List[str] = ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]

# API endpoints (relative to repo)
ENDPOINTS: Dict[str, str] = {
    "issues": "/issues",
    "pulls": "/pulls",
    "releases": "/releases",
}

# ---------------------------------------------------------------------------
# Custom Exceptions
# ---------------------------------------------------------------------------


class GitHubAPIError(Exception):
    """Base exception for GitHub API errors."""


class RateLimitExceeded(GitHubAPIError):
    """Raised when primary rate limit is exhausted and no reset time available."""


class AuthenticationError(GitHubAPIError):
    """Raised when authentication fails (e.g., invalid token)."""


class ResourceNotFound(GitHubAPIError):
    """Raised when requested resource is not found."""


class InvalidArgumentError(GitHubAPIError):
    """Raised for invalid command-line arguments or configuration."""


# ---------------------------------------------------------------------------
# Logging
# ---------------------------------------------------------------------------


def setup_logging(level: str = "INFO") -> None:
    """Configure logging with a specific level.

    Args:
        level: Logging level string (must be one of 'DEBUG', 'INFO', 'WARNING',
               'ERROR', 'CRITICAL').

    Raises:
        ValueError: If the level is not a valid logging level.
    """
    normalized_level = level.upper()
    if normalized_level not in LOG_LEVELS:
        raise ValueError(
            f"Invalid log level: {level}. Must be one of {LOG_LEVELS}"
        )
    logging.basicConfig(
        level=normalized_level,
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
        datefmt="%Y-%m-%dT%H:%M:%S",
    )
    # Suppress overly verbose library logs
    logging.getLogger("urllib3").setLevel(logging.WARNING)
    logging.getLogger("requests").setLevel(logging.WARNING)


logger = logging.getLogger("fetch_github_data")


# ---------------------------------------------------------------------------
# Rate limiting helpers
# ---------------------------------------------------------------------------


def _sleep_until_reset(reset_timestamp: int) -> None:
    """Sleep until the rate limit window resets.

    Args:
        reset_timestamp: Unix timestamp when the rate limit resets.
    """
    now = int(time.time())
    sleep_duration = max(reset_timestamp - now, 0) + 1
    reset_iso = datetime.fromtimestamp(reset_timestamp, tz=timezone.utc).isoformat()
    logger.warning(
        "Primary rate limit exhausted. Sleeping %d seconds (until %s)...",
        sleep_duration,
        reset_iso,
    )
    time.sleep(sleep_duration)


def handle_rate_limits(response: requests.Response) -> None:
    """Check GitHub rate limit headers and sleep if necessary.

    Args:
        response: The response from a GitHub API call.

    Raises:
        RateLimitExceeded: If rate limit exhausted and no reset time available.
        HTTPError: If secondary rate limit detected (HTTP 403/429) and Retry-After
                   header present.
    """
    remaining: Optional[str] = response.headers.get("X-RateLimit-Remaining")
    reset_time: Optional[str] = response.headers.get("X-RateLimit-Reset")

    if remaining is not None and reset_time is not None:
        remaining_int = int(remaining)
        if remaining_int == 0:
            reset_timestamp = int(reset_time)
            _sleep_until_reset(reset_timestamp)
            return

    # Secondary rate limit (HTTP 403 or 429)
    if response.status_code in (403, 429):
        retry_after: Optional[str] = response.headers.get("Retry-After")
        if retry_after:
            sleep_duration = int(retry_after)
            logger.warning(
                "Secondary rate limit hit (HTTP %d). Sleeping %d seconds.",
                response.status_code,
                sleep_duration,
            )
            time.sleep(sleep_duration)
            # After sleeping, raise HTTPError to trigger retry in caller
            raise HTTPError(
                f"Secondary rate limit (HTTP {response.status_code}) – slept {sleep_duration}s",
                response=response,
            )


# ---------------------------------------------------------------------------
# Retry session factory
# ---------------------------------------------------------------------------


def create_retry_session() -> requests.Session:
    """Create a requests session with retry and backoff for transient failures.

    Retries on 5xx status codes (except 501, 505) and connection errors.
    Rate limit handling is done separately via `handle_rate_limits`.

    Returns:
        Configured requests.Session object.
    """
    session = requests.Session()
    retry_strategy = Retry(
        total=MAX_RETRIES,
        backoff_factor=BACKOFF_FACTOR,
        status_forcelist=[500, 502, 503, 504],
        allowed_methods=["GET"],
        raise_on_status=False,  # We handle status codes manually
    )
    adapter = HTTPAdapter(max_retries=retry_strategy)
    session.mount("https://", adapter)
    session.mount("http://", adapter)
    return session


# ---------------------------------------------------------------------------
# Authentication
# ---------------------------------------------------------------------------


def get_auth_headers() -> Dict[str, str]:
    """Retrieve GitHub token from environment and return authorization headers.

    Returns:
        Dictionary with Authorization header.

    Raises:
        AuthenticationError: If GITHUB_TOKEN is not set or empty.
    """
    token = os.environ.get("GITHUB_TOKEN")
    if not token or not token.strip():
        raise AuthenticationError(
            "GITHUB_TOKEN environment variable is not set or empty. "
            "Please export a valid GitHub personal access token."
        )
    return {"Authorization": f"token {token.strip()}"}


# ---------------------------------------------------------------------------
# Pagination helpers
# ---------------------------------------------------------------------------


def extract_next_url(response: requests.Response) -> Optional[str]:
    """Extract the next page URL from the Link header.

    Args:
        response: Response object from a GitHub API call.

    Returns:
        URL string or None if there is no next page.
    """
    link_header = response.headers.get("Link")
    if not link_header:
        return None

    for part in link_header.split(","):
        section = part.strip()
        if section.endswith('rel="next"'):
            # Extract URL from <...>
            start = section.find("<")
            end = section.find(">")
            if start != -1 and end != -1:
                return section[start + 1 : end]
    return None


def paginate(
    session: requests.Session,
    url: str,
    headers: Dict[str, str],
    max_pages: Optional[int] = None,
) -> Generator[Dict[str, Any], None, None]:
    """Yield items from a paginated GitHub API endpoint.

    Respects rate limits and retries on transient errors.

    Args:
        session: Requests session with retry adapter.
        url: Initial API URL to start pagination.
        headers: Request headers (including Authorization).
        max_pages: Maximum number of pages to fetch (None = all).

    Yields:
        Each item (dict) from consecutive pages.

    Raises:
        GitHubAPIError: On persistent API failures.
        AuthenticationError: On 401 responses.
        RateLimitExceeded: If primary rate limit exhausted and no reset in headers.
    """
    page_count = 0
    current_url: Optional[str] = url

    while current_url is not None:
        if max_pages is not None and page_count >= max_pages:
            logger.info("Reached max_pages limit (%d), stopping pagination.", max_pages)
            break

        try:
            response = session.get(
                current_url,
                headers=headers,
                timeout=TIMEOUT,
            )
        except (ConnectionError, Timeout, SSLError, TooManyRedirects) as exc:
            logger.error("Network error fetching %s: %s", current_url, exc)
            raise GitHubAPIError(
                f"Failed to fetch {current_url}: {exc}"
            ) from exc

        # Check for authentication failure
        if response.status_code == 401:
            raise AuthenticationError(
                "GitHub authentication failed (HTTP 401). Check your GITHUB_TOKEN."
            )

        if response.status_code == 404:
            raise ResourceNotFound(f"Resource not found: {current_url}")

        # Handle rate limits (may sleep or raise HTTPError for secondary)
        handle_rate_limits(response)

        # Check for other HTTP errors
        try:
            response.raise_for_status()
        except HTTPError as exc:
            logger.error(
                "HTTP error %s for %s: %s",
                response.status_code,
                current_url,
                response.text[:500],
            )
            raise GitHubAPIError(
                f"GitHub API returned {response.status_code} for {current_url}"
            ) from exc

        # Parse JSON and yield items
        try:
            data = response.json()
        except json.JSONDecodeError as exc:
            logger.error("Invalid JSON from %s: %s", current_url, exc)
            raise GitHubAPIError(f"Non-JSON response from {current_url}") from exc

        if not isinstance(data, list):
            logger.warning("Unexpected response format (non-list) at %s", current_url)
            continue

        yield from data
        page_count += 1

        # Determine next URL
        current_url = extract_next_url(response)

        # Optional small delay to be friendly
        time.sleep(0.1)


# ---------------------------------------------------------------------------
# Fetching
# ---------------------------------------------------------------------------


def fetch_endpoint(
    owner: str,
    repo: str,
    endpoint: str,
    session: requests.Session,
    headers: Dict[str, str],
    max_pages: Optional[int] = None,
) -> List[Dict[str, Any]]:
    """Fetch all items from a specific GitHub API endpoint for a repository.

    Args:
        owner: Repository owner (user or organization).
        repo: Repository name.
        endpoint: API endpoint path (e.g., '/issues').
        session: Requests session with retry.
        headers: Request headers.
        max_pages: Maximum number of pages to fetch (None = all).

    Returns:
        List of JSON items (dicts) from the endpoint.

    Raises:
        GitHubAPIError: On persistent failures.
        AuthenticationError: On 401.
    """
    url = f"{API_BASE}/repos/{owner}/{repo}{endpoint}"
    params: Dict[str, Union[int, str]] = {
        "per_page": PER_PAGE,
        "state": "all",
    }

    # Add extra parameters for specific endpoints to reduce noise
    if endpoint == "/pulls":
        params["state"] = "all"  # includes open, closed, merged

    first_page_url = requests.Request("GET", url, params=params).prepare().url
    logger.debug("Fetching from %s", first_page_url)

    items: List[Dict[str, Any]] = []
    try:
        for item in paginate(session, first_page_url, headers, max_pages):
            items.append(item)
    except GitHubAPIError:
        logger.exception("Failed to fetch %s/%s%s", owner, repo, endpoint)
        raise

    logger.info(
        "Fetched %d items from %s/%s%s",
        len(items),
        owner,
        repo,
        endpoint,
    )
    return items


# ---------------------------------------------------------------------------
# Data persistence
# ---------------------------------------------------------------------------


def save_data(
    cache_dir: Path,
    owner: str,
    repo: str,
    endpoint: str,
    data: List[Dict[str, Any]],
) -> None:
    """Save fetched data as JSON to the cache directory.

    Creates subdirectories as needed.

    Args:
        cache_dir: Base cache directory.
        owner: Repository owner.
        repo: Repository name.
        endpoint: API endpoint (used to build filename).
        data: List of JSON-serializable items.

    Raises:
        InvalidArgumentError: If data is not a list.
        OSError: If directory creation or file writing fails.
    """
    if not isinstance(data, list):
        raise InvalidArgumentError("Data must be a list of dicts.")

    # Build path: cache_dir/owner/repo/endpoint.json (strip leading slash)
    endpoint_clean = endpoint.lstrip("/")
    target_dir = cache_dir / owner / repo
    target_dir.mkdir(parents=True, exist_ok=True)

    timestamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    filename = f"{endpoint_clean}_{timestamp}.json"
    filepath = target_dir / filename

    try:
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        logger.info("Saved %d items to %s", len(data), filepath)
    except OSError as exc:
        logger.error("Failed to write %s: %s", filepath, exc)
        raise


# ---------------------------------------------------------------------------
# Argument parsing
# ---------------------------------------------------------------------------


def parse_arguments(argv: Optional[List[str]] = None) -> argparse.Namespace:
    """Parse command-line arguments.

    Args:
        argv: Command-line argument list (defaults to sys.argv[1:]).

    Returns:
        Parsed namespace with attributes: cache_dir, max_pages, log_level.

    Raises:
        InvalidArgumentError: If cache_dir does not exist and cannot be created.
    """
    parser = argparse.ArgumentParser(
        description="Fetch issues, PRs, and releases from 13 GitHub repositories.",
    )
    parser.add_argument(
        "--cache-dir",
        type=str,
        default=str(DEFAULT_CACHE_DIR),
        help="Directory to store raw JSON cache (default: ../cache/raw relative to script)",
    )
    parser.add_argument(
        "--max-pages",
        type=int,
        default=None,
        help="Maximum pages per endpoint (default: all)",
    )
    parser.add_argument(
        "--log-level",
        type=str,
        default="INFO",
        choices=LOG_LEVELS,
        help="Set logging level (default: INFO)",
    )

    args = parser.parse_args(argv)

    # Validate cache_dir
    cache_path = Path(args.cache_dir).resolve()
    if not cache_path.exists():
        try:
            cache_path.mkdir(parents=True, exist_ok=True)
            logger.info("Created cache directory: %s", cache_path)
        except OSError as exc:
            raise InvalidArgumentError(
                f"Cannot create cache directory {cache_path}: {exc}"
            ) from exc
    args.cache_dir = cache_path

    # Validate max_pages if provided
    if args.max_pages is not None and args.max_pages < 1:
        raise InvalidArgumentError("max_pages must be >= 1 or None.")

    return args


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------


def main() -> int:
    """Main entry point: fetch data from all repositories and endpoints.

    Returns:
        Exit code: 0 on success, 1 on error.
    """
    try:
        args = parse_arguments()
        setup_logging(args.log_level)
        logger.info("Starting data fetch for %d repositories.", len(REPOSITORIES))

        headers = get_auth_headers()
        session = create_retry_session()

        total_fetched = 0
        errors: List[str] = []

        for owner, repo in REPOSITORIES:
            logger.info("Processing %s/%s", owner, repo)
            for endpoint_name, endpoint_path in ENDPOINTS.items():
                try:
                    data = fetch_endpoint(
                        owner=owner,
                        repo=repo,
                        endpoint=endpoint_path,
                        session=session,
                        headers=headers,
                        max_pages=args.max_pages,
                    )
                    save_data(
                        cache_dir=args.cache_dir,
                        owner=owner,
                        repo=repo,
                        endpoint=endpoint_path,
                        data=data,
                    )
                    total_fetched += len(data)
                except (GitHubAPIError, ResourceNotFound, OSError) as exc:
                    error_msg = f"{owner}/{repo}/{endpoint_name}: {exc}"
                    logger.error("Skipping %s due to error: %s", error_msg, exc)
                    errors.append(error_msg)
                    # Continue with next endpoint/repo
                    continue

        logger.info(
            "Completed. Total items fetched: %d. Errors: %d/%d endpoints.",
            total_fetched,
            len(errors),
            len(REPOSITORIES) * len(ENDPOINTS),
        )

        if errors:
            logger.warning("Errors encountered:")
            for err in errors:
                logger.warning("  - %s", err)
            return 1  # Non-zero exit if errors

        return 0

    except (AuthenticationError, InvalidArgumentError) as exc:
        logger.critical("Critical error: %s", exc)
        return 1
    except Exception:
        logger.exception("Unexpected fatal error")
        return 1
    finally:
        logging.shutdown()


if __name__ == "__main__":
    sys.exit(main())