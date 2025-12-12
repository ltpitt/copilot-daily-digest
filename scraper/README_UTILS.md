# Scraper Utilities

Shared utility functions for all scrapers in the copilot-daily-digest project.

## Overview

The `scraper/utils.py` module provides common functionality for HTTP requests, file I/O, date/time handling, content processing, error handling, and logging. These utilities ensure consistency across all scrapers and prevent code duplication.

## Quick Start

```python
from scraper.utils import (
    fetch_url, safe_write_file, now_iso, 
    sanitize_filename, handle_scraper_error, setup_logger
)

# Fetch URL with automatic retries
content = fetch_url("https://example.com", retries=3)

# Save with atomic write
safe_write_file("output.txt", content)

# Get current UTC timestamp
timestamp = now_iso()  # "2025-12-08T15:30:00Z"
```

## Features

### 🌐 HTTP Utilities

- **Retry Logic**: Automatic retries with exponential backoff (1s, 2s, 4s)
- **Timeout Handling**: Configurable timeouts for all requests
- **User Agent**: Automatically sets `copilot-daily-digest/1.0`
- **Error Logging**: Logs all HTTP errors with context

```python
from scraper.utils import fetch_url, fetch_json, is_url_accessible

# Fetch HTML content
html = fetch_url("https://github.blog", retries=3, timeout=30)

# Fetch and parse JSON
data = fetch_json("https://api.github.com/repos/github/docs")

# Check URL accessibility
if is_url_accessible("https://example.com"):
    print("URL is accessible")
```

### 📁 File I/O Utilities

- **Atomic Writes**: Uses temp file + rename pattern
- **Safe Operations**: Handles errors gracefully
- **Auto Directory Creation**: Creates parent directories automatically
- **UTF-8 Encoding**: Consistent encoding for all text files

```python
from scraper.utils import safe_write_file, safe_read_file, ensure_directory, get_file_age_hours

# Atomic write (creates parent directories)
safe_write_file("data/output/file.txt", "content")

# Safe read with default value
content = safe_read_file("data/input/file.txt", default="")

# Ensure directory exists
ensure_directory("data/output")

# Check file age
age = get_file_age_hours("data/cache.json")
if age > 24:
    print("Cache expired")
```

### 📅 Date/Time Utilities

- **UTC Timestamps**: All timestamps in UTC timezone
- **ISO 8601 Format**: Standard format for all dates
- **Timezone Handling**: Proper timezone conversions
- **Human-Readable Dates**: Format dates for display

```python
from scraper.utils import now_iso, parse_iso, format_human_date, days_since

# Current UTC timestamp
timestamp = now_iso()  # "2025-12-08T15:30:00Z"

# Parse ISO timestamp
dt = parse_iso("2025-12-08T15:30:00Z")

# Format for humans
human = format_human_date("2025-12-08T15:30:00Z")  # "Dec 8, 2025"

# Calculate days elapsed
days = days_since("2025-01-01T00:00:00Z")
```

### 🔧 Content Utilities

- **Filename Sanitization**: Remove special characters
- **Text Truncation**: Truncate with ellipsis
- **Domain Extraction**: Parse URLs for domains
- **Slugification**: Create URL-friendly slugs

```python
from scraper.utils import sanitize_filename, truncate_text, extract_domain, slugify

# Sanitize filename
safe = sanitize_filename("my file?.txt")  # "my_file.txt"

# Truncate text
short = truncate_text("A" * 300, max_length=200)  # 200 chars + "..."

# Extract domain
domain = extract_domain("https://github.com/user/repo")  # "github.com"

# Create slug
slug = slugify("Hello World!")  # "hello-world"
```

### 🚨 Error Handling

- **Custom Exceptions**: ScraperError, NetworkError, ParsingError
- **Decorator**: Automatic error logging with traceback
- **Consistent Handling**: Standardized error patterns

```python
from scraper.utils import ScraperError, NetworkError, handle_scraper_error

# Use custom exceptions
if not content:
    raise ScraperError("No content found")

# Decorator for automatic error handling
@handle_scraper_error
def my_scraper():
    # Errors are automatically logged
    return fetch_url("https://example.com")
```

### 📝 Logging Setup

- **Consistent Formatting**: Standardized log format
- **File Logging**: Errors logged to `logs/scraper_errors.log`
- **Rotation**: 10 MB file rotation
- **Retention**: 30 days retention

```python
from scraper.utils import setup_logger

# Initialize logger
logger = setup_logger("my_scraper", level="INFO")

# Use logger
logger.info("Starting scraper")
logger.error("An error occurred")
```

## Testing

Comprehensive test suite with 57 tests covering all functionality:

```bash
# Run tests
python tests/test_utils.py

# Or with pytest
python -m pytest tests/test_utils.py
```

Test coverage:
- ✅ HTTP utilities (retry logic, error handling)
- ✅ File I/O (atomic writes, safe reads)
- ✅ Date/time (timezone handling, formatting)
- ✅ Content processing (sanitization, truncation)
- ✅ Error handling (exceptions, decorator)
- ✅ Logging setup (configuration, formatting)
- ✅ Integration tests (complete workflows)

## Examples

See the individual scraper files for complete examples of:
- HTTP requests with retry logic
- File operations and caching
- Date/time handling
- Content processing
- Error handling patterns
- Logging setup
- Complete scraping workflows

## Dependencies

- `requests>=2.31.0` - HTTP requests
- `loguru>=0.7.0` - Logging

Both are already included in `requirements.txt`.

## Best Practices

### HTTP Requests

```python
# ✅ Good: Use fetch_url for automatic retries
content = fetch_url(url, retries=3, timeout=30)

# ❌ Avoid: Direct requests without retry logic
response = requests.get(url)  # No retries
```

### File Operations

```python
# ✅ Good: Use safe_write_file for atomic writes
safe_write_file(path, content)

# ❌ Avoid: Direct file writes (not atomic)
with open(path, 'w') as f:
    f.write(content)
```

### Date Handling

```python
# ✅ Good: Use now_iso() for UTC timestamps
timestamp = now_iso()

# ❌ Avoid: Local time without timezone
timestamp = datetime.now().isoformat()  # No timezone
```

### Error Handling

```python
# ✅ Good: Use custom exceptions
raise NetworkError("Failed to connect")

# ❌ Avoid: Generic exceptions without context
raise Exception("Error")
```

## Security

All utilities have been validated for security:
- ✅ No known vulnerabilities in dependencies
- ✅ CodeQL analysis passed (0 alerts)
- ✅ Safe file operations (no path traversal)
- ✅ Timeout limits on all HTTP requests
- ✅ No hardcoded secrets

## Contributing

When adding new utilities:
1. Add type hints and docstrings
2. Write comprehensive unit tests
3. Follow existing patterns and conventions
4. Keep functions pure/stateless when possible
5. Document in this README

## License

Part of the copilot-daily-digest project.
