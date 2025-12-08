# Task 1.4: Add GitHub Blog Scraper (RSS-First)

**Phase**: 1 - Foundation & Infrastructure  
**Priority**: HIGH  
**Estimated Effort**: 3-4 hours  
**Assigned Agent**: `feed-fetcher`

## Context
GitHub publishes Copilot-related content in two places:
1. GitHub Blog: https://github.blog/tag/github-copilot/
2. Changelog: https://github.blog/changelog/

We should use RSS feeds as the primary method (preferred over web scraping).

## Objective
Create a scraper that fetches GitHub Blog and Changelog content using RSS feeds, stores raw data, and tracks URLs to prevent duplicates.

## Tasks

### 1. Research RSS feed URLs
Find official RSS feeds for:
- GitHub Blog Copilot tag
- GitHub Changelog (Copilot filtered)
- Alternative: GitHub Blog main feed + filter by tag

Expected feeds:
- `https://github.blog/tag/github-copilot/feed/`
- `https://github.blog/changelog/feed/` (then filter)

### 2. Create `scraper/fetch_blog.py`
```python
import feedparser
from scraper.utils import fetch_url, safe_write_file
from scraper.metadata import add_blog_url, load_metadata

def fetch_github_blog() -> list[dict]:
    """Fetch GitHub Blog posts about Copilot via RSS"""
    pass

def fetch_github_changelog() -> list[dict]:
    """Fetch GitHub Changelog entries via RSS"""
    pass

def parse_blog_entry(entry) -> dict:
    """
    Parse RSS entry into structured format:
    {
        "title": str,
        "url": str,
        "date": str (ISO 8601),
        "summary": str,
        "content": str,
        "tags": list[str],
        "author": str
    }
    """
    pass

def filter_copilot_content(entries: list) -> list:
    """Filter entries related to Copilot (keywords in title/content)"""
    pass

def save_blog_posts(posts: list[dict]) -> int:
    """
    Save blog posts to data/blog/
    Filename format: YYYY-MM-DD-slug.json
    Return count of new posts saved
    """
    pass

def main():
    """Main entry point for blog scraper"""
    pass
```

### 3. Implement RSS parsing with feedparser
- Use `feedparser` library (add to requirements.txt)
- Handle malformed feeds gracefully
- Extract: title, link, published date, summary, content
- Parse HTML content if needed (BeautifulSoup)

### 4. Implement duplicate prevention
- Check URL against `metadata.json` before saving
- Use `add_blog_url()` from metadata module
- Log skipped duplicates
- Return count of new posts

### 5. Implement content filtering
Keywords to look for (case-insensitive):
- "copilot"
- "ai"
- "agent"
- "coding agent"
- "workspace agent"
- "extensions"

Filter logic:
- Check title first (highest priority)
- Then check content/summary
- Include changelog entries with "copilot" tag

### 6. Store raw data
Save each post as `data/blog/YYYY-MM-DD-{slug}.json`:
```json
{
  "title": "Introducing GitHub Copilot Workspace",
  "url": "https://github.blog/2025-12-01-copilot-workspace/",
  "published": "2025-12-01T10:00:00Z",
  "summary": "Brief summary...",
  "content": "Full HTML or markdown content...",
  "tags": ["copilot", "ai", "workspace"],
  "author": "John Doe",
  "source": "github-blog",
  "scraped_at": "2025-12-08T15:30:00Z"
}
```

### 7. Add error handling
- Handle network errors (RSS feed unavailable)
- Handle parsing errors (malformed XML/RSS)
- Handle missing fields in RSS entries
- Log all errors with context
- Continue on individual entry failures

### 8. Add logging
- Log feed fetch attempts
- Log number of entries found
- Log number filtered out
- Log number of new posts saved
- Log duplicates skipped

## Acceptance Criteria
- [ ] `scraper/fetch_blog.py` created with all functions
- [ ] Uses RSS feeds (not web scraping) as primary method
- [ ] Successfully fetches GitHub Blog Copilot posts
- [ ] Successfully fetches GitHub Changelog entries
- [ ] Filters content by Copilot-related keywords
- [ ] Saves posts as JSON in `data/blog/`
- [ ] Prevents duplicate posts using metadata
- [ ] Handles network and parsing errors gracefully
- [ ] Logs all operations clearly
- [ ] Can be run standalone: `python scraper/fetch_blog.py`
- [ ] Returns count of new posts found

## Dependencies
- Requires Task 1.1 (directory structure)
- Requires Task 1.2 (metadata system)
- Recommended: Task 1.3 (utilities) for cleaner code

## Testing
1. Run scraper: `python scraper/fetch_blog.py`
2. Verify JSON files created in `data/blog/`
3. Run again - should skip duplicates
4. Check `metadata.json` - URLs should be tracked
5. Verify filtering - only Copilot-related content saved
6. Test with network error (disconnect wifi)
7. Verify graceful error handling

## Example Output
```
[INFO] Fetching GitHub Blog RSS feed...
[INFO] Found 25 entries in feed
[INFO] Filtered to 8 Copilot-related posts
[INFO] 5 new posts, 3 duplicates skipped
[INFO] Saved to data/blog/
[INFO] Updated metadata.json
```

## Notes
- Prefer RSS over web scraping (more reliable, less fragile)
- If RSS unavailable, document fallback to web scraping
- Use `feedparser` library: `pip install feedparser`
- Consider pagination if feeds are truncated
- GitHub Blog may have multiple feed formats (Atom, RSS2)
