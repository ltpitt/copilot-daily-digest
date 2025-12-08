"""
Example usage of scraper utilities.

This script demonstrates how to use the shared utility functions
from scraper/utils.py in your scraper implementations.
"""

from scraper.utils import (
    # HTTP utilities
    fetch_url, fetch_json, is_url_accessible,
    # File I/O utilities
    safe_write_file, safe_read_file, ensure_directory, get_file_age_hours,
    # Date/time utilities
    now_iso, parse_iso, format_human_date, days_since,
    # Content utilities
    sanitize_filename, truncate_text, extract_domain, slugify,
    # Error handling
    ScraperError, NetworkError, ParsingError, handle_scraper_error,
    # Logging
    setup_logger
)


# Example 1: HTTP Requests with Retry Logic
# ==========================================

def fetch_github_blog():
    """Fetch GitHub blog with automatic retries"""
    try:
        # Automatically retries 3 times with exponential backoff
        content = fetch_url("https://github.blog/", retries=3, timeout=30)
        print(f"✓ Fetched {len(content)} bytes from GitHub blog")
        return content
    except NetworkError as e:
        print(f"✗ Failed to fetch: {e}")
        return None


def fetch_api_data():
    """Fetch and parse JSON API response"""
    try:
        # Automatically parses JSON
        data = fetch_json("https://api.github.com/repos/github/docs")
        print(f"✓ Repo stars: {data.get('stargazers_count')}")
        return data
    except (NetworkError, ParsingError) as e:
        print(f"✗ API error: {e}")
        return None


# Example 2: File Operations
# ===========================

def save_scraped_content(content: str, filename: str):
    """Save scraped content to file with atomic write"""
    # Ensure directory exists
    ensure_directory("data/scraped")
    
    # Sanitize filename to remove special characters
    safe_name = sanitize_filename(filename)
    filepath = f"data/scraped/{safe_name}"
    
    # Atomic write (temp file + rename)
    if safe_write_file(filepath, content):
        print(f"✓ Saved content to {filepath}")
        
        # Check file age
        age = get_file_age_hours(filepath)
        print(f"  File age: {age:.2f} hours")
    else:
        print(f"✗ Failed to save {filepath}")


def load_cached_content(filename: str, max_age_hours: int = 24) -> str:
    """Load content from cache if it's recent enough"""
    filepath = f"data/scraped/{filename}"
    
    # Check if cache exists and is fresh
    age = get_file_age_hours(filepath)
    if age < max_age_hours:
        content = safe_read_file(filepath)
        print(f"✓ Using cached content ({age:.2f} hours old)")
        return content
    else:
        print(f"✗ Cache expired or missing ({age:.2f} hours old)")
        return ""


# Example 3: Date/Time Handling
# ==============================

def log_scrape_metadata(source: str):
    """Log scraping metadata with timestamps"""
    timestamp = now_iso()
    human_date = format_human_date(timestamp)
    
    metadata = {
        "source": source,
        "timestamp": timestamp,
        "human_date": human_date,
        "scraped_at": timestamp
    }
    
    print(f"✓ Scraped {source} on {human_date}")
    return metadata


def check_last_scrape(last_timestamp: str):
    """Check how long since last scrape"""
    if not last_timestamp:
        print("✗ Never scraped before")
        return float('inf')
    
    days = days_since(last_timestamp)
    human_date = format_human_date(last_timestamp)
    
    print(f"✓ Last scraped {days} days ago ({human_date})")
    return days


# Example 4: Content Processing
# ==============================

def process_article(title: str, content: str, url: str):
    """Process scraped article"""
    # Create URL-friendly slug
    slug = slugify(title)
    
    # Extract domain for categorization
    domain = extract_domain(url)
    
    # Create preview text
    preview = truncate_text(content, max_length=200)
    
    print(f"✓ Processed article:")
    print(f"  Title: {title}")
    print(f"  Slug: {slug}")
    print(f"  Domain: {domain}")
    print(f"  Preview: {preview}")
    
    return {
        "title": title,
        "slug": slug,
        "domain": domain,
        "preview": preview,
        "content": content,
        "url": url
    }


# Example 5: Error Handling
# ==========================

@handle_scraper_error
def scrape_with_error_handling(url: str):
    """Scraper function with automatic error logging"""
    # Check if URL is accessible first
    if not is_url_accessible(url):
        raise NetworkError(f"URL not accessible: {url}")
    
    # Fetch content
    content = fetch_url(url)
    
    # Process content
    if not content:
        raise ScraperError("Empty content received")
    
    return content


# Example 6: Logging Setup
# =========================

def initialize_scraper(name: str):
    """Initialize scraper with logging"""
    # Set up logger with INFO level
    logger = setup_logger(name, level="INFO")
    
    print(f"✓ Logger '{name}' initialized")
    print(f"✓ Logs will be written to: logs/scraper_errors.log")
    
    return logger


# Example 7: Complete Scraping Workflow
# ======================================

def complete_scraping_example():
    """Complete example showing all utilities together"""
    print("\n" + "="*60)
    print("Complete Scraping Workflow Example")
    print("="*60 + "\n")
    
    # 1. Initialize
    logger = initialize_scraper("example_scraper")
    
    # 2. Check cache
    cached = load_cached_content("github_blog.html", max_age_hours=24)
    
    if not cached:
        # 3. Fetch fresh content
        print("\nFetching fresh content...")
        content = fetch_github_blog()
        
        if content:
            # 4. Save to file
            save_scraped_content(content, "github_blog.html")
    else:
        content = cached
    
    # 5. Process content
    if content:
        article = process_article(
            title="Example GitHub Blog Post",
            content=content[:500],  # First 500 chars
            url="https://github.blog/example-post"
        )
        
        # 6. Log metadata
        log_scrape_metadata("GitHub Blog")
    
    print("\n" + "="*60)
    print("✅ Workflow complete!")
    print("="*60 + "\n")


if __name__ == "__main__":
    # Run the complete example
    # Note: This requires network access
    print("This is an example file showing utility usage.")
    print("Individual functions are demonstrated above.")
    print("\nTo run the complete workflow (requires network):")
    print("  python scraper/example_usage.py")
