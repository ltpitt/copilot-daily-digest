"""
Shared utility functions for all scrapers.

This module provides common functionality for:
- HTTP requests with retry logic
- File I/O operations
- Date/time utilities
- Content processing
- Error handling
- Logging setup
"""

import hashlib
import json
import os
import re
import time
from datetime import datetime, timezone, timedelta
from pathlib import Path
from typing import Optional, Any, Callable
from urllib.parse import urlparse
import requests
from loguru import logger


# ============================================================================
# Custom Exceptions
# ============================================================================

class ScraperError(Exception):
    """Base exception for scraper errors"""
    pass


class NetworkError(ScraperError):
    """Network-related errors"""
    pass


class ParsingError(ScraperError):
    """Content parsing errors"""
    pass


# ============================================================================
# HTTP Utilities
# ============================================================================

def fetch_url(url: str, retries: int = 3, timeout: int = 30) -> str:
    """
    Fetch URL with exponential backoff retry logic.
    
    Args:
        url: URL to fetch
        retries: Number of retry attempts (default: 3)
        timeout: Request timeout in seconds (default: 30)
        
    Returns:
        str: Response content as text
        
    Raises:
        NetworkError: If all retry attempts fail
    """
    headers = {
        'User-Agent': 'copilot-daily-digest/1.0'
    }
    
    last_error = None
    for attempt in range(retries):
        try:
            logger.debug(f"Fetching {url} (attempt {attempt + 1}/{retries})")
            response = requests.get(url, headers=headers, timeout=timeout)
            response.raise_for_status()
            logger.debug(f"Successfully fetched {url}")
            return response.text
        except requests.exceptions.Timeout as e:
            last_error = e
            logger.warning(f"Timeout fetching {url} (attempt {attempt + 1}/{retries})")
        except requests.exceptions.HTTPError as e:
            last_error = e
            logger.warning(f"HTTP error {response.status_code} for {url} (attempt {attempt + 1}/{retries})")
        except requests.exceptions.RequestException as e:
            last_error = e
            logger.warning(f"Request error for {url} (attempt {attempt + 1}/{retries}): {str(e)}")
        
        # Exponential backoff: 1s, 2s, 4s
        if attempt < retries - 1:
            delay = 2 ** attempt
            logger.debug(f"Waiting {delay}s before retry...")
            time.sleep(delay)
    
    # All retries failed
    error_msg = f"Failed to fetch {url} after {retries} attempts: {str(last_error)}"
    logger.error(error_msg)
    raise NetworkError(error_msg)


def fetch_json(url: str, retries: int = 3) -> dict:
    """
    Fetch and parse JSON from URL.
    
    Args:
        url: URL to fetch
        retries: Number of retry attempts (default: 3)
        
    Returns:
        dict: Parsed JSON data
        
    Raises:
        NetworkError: If fetch fails
        ParsingError: If JSON parsing fails
    """
    try:
        content = fetch_url(url, retries=retries)
        return json.loads(content)
    except json.JSONDecodeError as e:
        error_msg = f"Failed to parse JSON from {url}: {str(e)}"
        logger.error(error_msg)
        raise ParsingError(error_msg)


def is_url_accessible(url: str) -> bool:
    """
    Check if URL is accessible (HEAD request).
    
    Args:
        url: URL to check
        
    Returns:
        bool: True if URL is accessible, False otherwise
    """
    headers = {
        'User-Agent': 'copilot-daily-digest/1.0'
    }
    
    try:
        response = requests.head(url, headers=headers, timeout=10, allow_redirects=True)
        is_accessible = response.status_code < 400
        logger.debug(f"URL {url} accessible: {is_accessible} (status: {response.status_code})")
        return is_accessible
    except requests.exceptions.RequestException as e:
        logger.debug(f"URL {url} not accessible: {str(e)}")
        return False


# ============================================================================
# File I/O Utilities
# ============================================================================

def safe_write_file(path: str, content: str) -> bool:
    """
    Write file with atomic operation (temp file + rename).
    
    Args:
        path: File path to write to
        content: Content to write
        
    Returns:
        bool: True if successful, False otherwise
    """
    try:
        file_path = Path(path)
        ensure_directory(str(file_path.parent))
        
        # Write to temporary file first
        temp_path = file_path.with_suffix(file_path.suffix + '.tmp')
        with open(temp_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        # Atomic rename
        temp_path.replace(file_path)
        logger.debug(f"Successfully wrote file: {path}")
        return True
    except (IOError, OSError) as e:
        logger.error(f"Failed to write file {path}: {str(e)}")
        return False


def safe_read_file(path: str, default: str = "") -> str:
    """
    Read file with error handling, return default if missing.
    
    Args:
        path: File path to read from
        default: Default value if file doesn't exist or read fails
        
    Returns:
        str: File content or default value
    """
    try:
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()
        logger.debug(f"Successfully read file: {path}")
        return content
    except FileNotFoundError:
        logger.debug(f"File not found: {path}, returning default")
        return default
    except (IOError, OSError) as e:
        logger.warning(f"Failed to read file {path}: {str(e)}, returning default")
        return default


def ensure_directory(path: str) -> None:
    """
    Create directory and parents if they don't exist.
    
    Args:
        path: Directory path to create
    """
    try:
        Path(path).mkdir(parents=True, exist_ok=True)
        logger.debug(f"Ensured directory exists: {path}")
    except (IOError, OSError) as e:
        logger.error(f"Failed to create directory {path}: {str(e)}")
        raise


def get_file_age_hours(path: str) -> float:
    """
    Get file age in hours, return inf if missing.
    
    Args:
        path: File path to check
        
    Returns:
        float: Age in hours, or float('inf') if file doesn't exist
    """
    try:
        file_path = Path(path)
        if not file_path.exists():
            return float('inf')
        
        modified_time = file_path.stat().st_mtime
        current_time = time.time()
        age_seconds = current_time - modified_time
        age_hours = age_seconds / 3600
        logger.debug(f"File {path} age: {age_hours:.2f} hours")
        return age_hours
    except (IOError, OSError) as e:
        logger.warning(f"Failed to get file age for {path}: {str(e)}")
        return float('inf')


# ============================================================================
# Date/Time Utilities
# ============================================================================

def now_iso() -> str:
    """
    Get current UTC timestamp in ISO 8601 format.
    
    Returns:
        str: ISO 8601 timestamp (e.g., '2025-12-08T15:30:00Z')
    """
    timestamp = datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
    return timestamp


def parse_iso(timestamp: str) -> datetime:
    """
    Parse ISO 8601 timestamp to datetime.
    
    Args:
        timestamp: ISO 8601 timestamp string
        
    Returns:
        datetime: Parsed datetime object (UTC)
        
    Raises:
        ValueError: If timestamp format is invalid
    """
    try:
        # Handle both 'Z' suffix and timezone offset formats
        if timestamp.endswith('Z'):
            dt = datetime.strptime(timestamp, '%Y-%m-%dT%H:%M:%SZ')
            return dt.replace(tzinfo=timezone.utc)
        elif '+' in timestamp or timestamp.count('-') > 2:
            # Has timezone offset
            return datetime.fromisoformat(timestamp)
        else:
            # No timezone info, assume UTC
            dt = datetime.fromisoformat(timestamp)
            return dt.replace(tzinfo=timezone.utc)
    except ValueError as e:
        logger.error(f"Failed to parse timestamp '{timestamp}': {str(e)}")
        raise


def format_human_date(timestamp: str) -> str:
    """
    Format ISO timestamp to human-readable (e.g., 'Dec 8, 2025').
    
    Args:
        timestamp: ISO 8601 timestamp string
        
    Returns:
        str: Human-readable date (e.g., 'Dec 8, 2025')
    """
    try:
        dt = parse_iso(timestamp)
        return dt.strftime('%b %d, %Y')
    except ValueError:
        logger.warning(f"Failed to format timestamp '{timestamp}'")
        return timestamp


def days_since(timestamp: str) -> int:
    """
    Calculate days elapsed since given timestamp.
    
    Args:
        timestamp: ISO 8601 timestamp string
        
    Returns:
        int: Number of days elapsed
    """
    try:
        dt = parse_iso(timestamp)
        now = datetime.now(timezone.utc)
        delta = now - dt
        return delta.days
    except ValueError:
        logger.warning(f"Failed to calculate days since '{timestamp}'")
        return 0


# ============================================================================
# Content Utilities
# ============================================================================

def sanitize_filename(name: str) -> str:
    """
    Convert string to safe filename (remove special chars).
    
    Args:
        name: String to sanitize
        
    Returns:
        str: Safe filename (alphanumeric, underscores, hyphens, dots)
    """
    # Split into name and extension
    parts = name.rsplit('.', 1)
    base_name = parts[0]
    extension = f'.{parts[1]}' if len(parts) > 1 else ''
    
    # Replace spaces with underscores
    base_name = base_name.replace(' ', '_')
    # Remove or replace special characters
    base_name = re.sub(r'[^\w\-]', '_', base_name)
    # Remove consecutive underscores
    base_name = re.sub(r'_+', '_', base_name)
    # Remove leading/trailing underscores
    base_name = base_name.strip('_')
    
    return base_name + extension


def truncate_text(text: str, max_length: int = 200) -> str:
    """
    Truncate text with ellipsis.
    
    Args:
        text: Text to truncate
        max_length: Maximum length (default: 200)
        
    Returns:
        str: Truncated text with '...' if needed
    """
    if len(text) <= max_length:
        return text
    return text[:max_length - 3] + '...'


def extract_domain(url: str) -> str:
    """
    Extract domain from URL.
    
    Args:
        url: URL to parse
        
    Returns:
        str: Domain name (e.g., 'github.com')
    """
    try:
        parsed = urlparse(url)
        domain = parsed.netloc
        # Remove 'www.' prefix if present
        if domain.startswith('www.'):
            domain = domain[4:]
        return domain
    except Exception as e:
        logger.warning(f"Failed to extract domain from '{url}': {str(e)}")
        return ''


def slugify(text: str) -> str:
    """
    Convert text to URL-friendly slug.
    
    Args:
        text: Text to slugify
        
    Returns:
        str: URL-friendly slug (lowercase, hyphens, alphanumeric)
    """
    # Convert to lowercase
    text = text.lower()
    # Replace spaces with hyphens
    text = re.sub(r'\s+', '-', text)
    # Remove non-alphanumeric characters (except hyphens)
    text = re.sub(r'[^\w\-]', '', text)
    # Remove consecutive hyphens
    text = re.sub(r'-+', '-', text)
    # Remove leading/trailing hyphens
    text = text.strip('-')
    return text


# ============================================================================
# Error Handling Utilities
# ============================================================================

def handle_scraper_error(func: Callable) -> Callable:
    """
    Decorator for consistent error handling and logging.
    
    Catches ScraperError and its subclasses, logs them with context,
    and re-raises for caller to handle.
    
    Args:
        func: Function to wrap
        
    Returns:
        Callable: Wrapped function
    """
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ScraperError as e:
            logger.error(f"Scraper error in {func.__name__}: {str(e)}")
            logger.exception("Full traceback:")
            raise
        except Exception as e:
            logger.error(f"Unexpected error in {func.__name__}: {str(e)}")
            logger.exception("Full traceback:")
            raise ScraperError(f"Unexpected error in {func.__name__}: {str(e)}")
    
    wrapper.__name__ = func.__name__
    wrapper.__doc__ = func.__doc__
    return wrapper


# ============================================================================
# Logging Setup
# ============================================================================

def setup_logger(name: str, level: str = "INFO") -> Any:
    """
    Configure logger with consistent formatting.
    
    Args:
        name: Logger name
        level: Log level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
        
    Returns:
        Logger: Configured logger instance
    """
    from loguru import logger as log
    
    # Remove default handler
    log.remove()
    
    # Add custom handler with formatting
    log.add(
        lambda msg: print(msg, end=""),
        format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level: <8}</level> | <cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>",
        level=level
    )
    
    # Add file handler for errors
    log.add(
        "logs/scraper_errors.log",
        format="{time:YYYY-MM-DD HH:mm:ss} | {level: <8} | {name}:{function}:{line} - {message}",
        level="ERROR",
        rotation="10 MB",
        retention="30 days"
    )
    
    logger.info(f"Logger '{name}' configured with level {level}")
    return log
