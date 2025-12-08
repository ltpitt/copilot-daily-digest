# Task 1.3: Add Shared Utilities

**Phase**: 1 - Foundation & Infrastructure  
**Priority**: MEDIUM  
**Estimated Effort**: 2-3 hours  
**Assigned Agent**: GitHub Copilot Coding Agent

## Context
Multiple scrapers will need common functionality: HTTP requests with retries, file I/O, error handling, logging, and date formatting. Creating shared utilities prevents code duplication and ensures consistency.

## Objective
Create `scraper/utils.py` with reusable utility functions for all scrapers.

## Tasks

### 1. HTTP utilities
```python
def fetch_url(url: str, retries: int = 3, timeout: int = 30) -> str:
    """Fetch URL with exponential backoff retry logic"""
    pass

def fetch_json(url: str, retries: int = 3) -> dict:
    """Fetch and parse JSON from URL"""
    pass

def is_url_accessible(url: str) -> bool:
    """Check if URL is accessible (HEAD request)"""
    pass
```

### 2. File I/O utilities
```python
def safe_write_file(path: str, content: str) -> bool:
    """Write file with atomic operation (temp file + rename)"""
    pass

def safe_read_file(path: str, default: str = "") -> str:
    """Read file with error handling, return default if missing"""
    pass

def ensure_directory(path: str) -> None:
    """Create directory and parents if they don't exist"""
    pass

def get_file_age_hours(path: str) -> float:
    """Get file age in hours, return inf if missing"""
    pass
```

### 3. Date/time utilities
```python
def now_iso() -> str:
    """Get current UTC timestamp in ISO 8601 format"""
    pass

def parse_iso(timestamp: str) -> datetime:
    """Parse ISO 8601 timestamp to datetime"""
    pass

def format_human_date(timestamp: str) -> str:
    """Format ISO timestamp to human-readable (e.g., 'Dec 8, 2025')"""
    pass

def days_since(timestamp: str) -> int:
    """Calculate days elapsed since given timestamp"""
    pass
```

### 4. Content utilities
```python
def sanitize_filename(name: str) -> str:
    """Convert string to safe filename (remove special chars)"""
    pass

def truncate_text(text: str, max_length: int = 200) -> str:
    """Truncate text with ellipsis"""
    pass

def extract_domain(url: str) -> str:
    """Extract domain from URL"""
    pass

def slugify(text: str) -> str:
    """Convert text to URL-friendly slug"""
    pass
```

### 5. Error handling utilities
```python
class ScraperError(Exception):
    """Base exception for scraper errors"""
    pass

class NetworkError(ScraperError):
    """Network-related errors"""
    pass

class ParsingError(ScraperError):
    """Content parsing errors"""
    pass

def handle_scraper_error(func):
    """Decorator for consistent error handling and logging"""
    pass
```

### 6. Logging setup
```python
def setup_logger(name: str, level: str = "INFO") -> Logger:
    """Configure logger with consistent formatting"""
    pass
```

### 7. Add comprehensive tests
Create `tests/test_utils.py` with unit tests for all utilities.

## Implementation Details

### HTTP Requests
- Use `requests` library
- Implement exponential backoff: 1s, 2s, 4s delays
- Log all HTTP errors with URL and status code
- Set user agent: `copilot-daily-digest/1.0`
- Handle timeouts gracefully

### File Operations
- Use atomic writes (write to temp, then rename)
- Create parent directories automatically
- Handle permission errors
- Use UTF-8 encoding for all text files

### Error Handling
- All errors should be logged with context
- Use custom exception hierarchy
- Decorator should catch, log, and re-raise
- Include traceback in logs for debugging

## Acceptance Criteria
- [ ] `scraper/utils.py` created with all utility functions
- [ ] All functions have type hints and docstrings
- [ ] HTTP functions include retry logic with exponential backoff
- [ ] File operations are atomic and safe
- [ ] Date utilities handle timezones correctly (UTC)
- [ ] Error handling is consistent across all utilities
- [ ] Logging configured with appropriate formatting
- [ ] Unit tests cover all functions
- [ ] No external dependencies beyond `requests`, `loguru`
- [ ] Functions are pure/stateless where possible

## Dependencies
None - can be developed in parallel with other Phase 1 tasks.

## Testing
```python
# Test HTTP retry logic
assert fetch_url("https://httpstat.us/500") retries correctly

# Test file operations
safe_write_file("/tmp/test.txt", "content")
assert safe_read_file("/tmp/test.txt") == "content"

# Test date utilities
now = now_iso()
assert parse_iso(now) is valid datetime
assert days_since(now) == 0

# Test content utilities
assert sanitize_filename("hello/world?.txt") == "hello_world.txt"
assert slugify("Hello World!") == "hello-world"
```

## Notes
- Keep utilities focused and single-purpose
- Avoid dependencies on other scraper modules
- Make functions easy to test (pure functions preferred)
- Document all parameters and return types
