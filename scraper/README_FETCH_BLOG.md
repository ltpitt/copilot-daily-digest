# GitHub Blog Scraper

RSS-based scraper for fetching GitHub Blog posts and Changelog entries about GitHub Copilot.

## Features

- ✅ Fetches content from GitHub Blog RSS feeds
- ✅ Filters for Copilot-related content using keywords
- ✅ Prevents duplicate processing using metadata tracking
- ✅ Saves structured JSON data to `data/blog/`
- ✅ Comprehensive error handling and logging
- ✅ Standalone executable script

## Installation

```bash
pip install -r requirements.txt
```

Required dependencies:
- `feedparser` - RSS/Atom feed parsing
- `python-dateutil` - Date parsing utilities

## Usage

Run the scraper:

```bash
python scraper/fetch_blog.py
```

Or as a module:

```bash
python -m scraper.fetch_blog
```

## RSS Feeds

The scraper uses the following official RSS feeds:

1. **GitHub Blog (Copilot tag)**: `https://github.blog/tag/github-copilot/feed/`
2. **GitHub Changelog**: `https://github.blog/changelog/feed/`

## Output Format

Blog posts are saved as JSON files in `data/blog/` with the format:

```
data/blog/YYYY-MM-DD-slug.json
```

Each JSON file contains:

```json
{
  "title": "Post title",
  "url": "https://github.blog/...",
  "published": "2025-12-01T10:00:00Z",
  "summary": "Brief summary...",
  "content": "Full content...",
  "tags": ["copilot", "ai"],
  "author": "Author Name",
  "source": "github-blog",
  "scraped_at": "2025-12-08T15:30:00Z"
}
```

## Filtering

The scraper filters content using these keywords:
- copilot
- ai
- agent
- coding agent
- workspace agent
- extensions

Filtering checks:
1. Post title (highest priority)
2. Post content/summary
3. Post tags

## Duplicate Prevention

URLs are tracked in `data/metadata.json` to prevent re-processing the same content. If a URL already exists in metadata, it will be skipped.

## Error Handling

The scraper handles:
- Network failures (RSS feed unavailable)
- Malformed RSS/XML
- Missing fields in entries
- File system errors
- Individual entry parsing failures (continues processing)

## Logging

All operations are logged with appropriate levels:

```
[INFO] Fetching GitHub Blog RSS feed...
[INFO] Found 25 entries in GitHub Blog feed
[INFO] Filtered to 8 Copilot-related posts from 25 total entries
[INFO] Saved: 2025-12-08-introducing-copilot-workspace.json
[INFO] 3 duplicates skipped
[INFO] Scraping complete: 5 new posts saved
```

## Module Structure

```python
from scraper.fetch_blog import (
    fetch_github_blog,      # Fetch blog RSS
    fetch_github_changelog, # Fetch changelog RSS
    parse_blog_entry,       # Parse single entry
    filter_copilot_content, # Filter by keywords
    save_blog_posts         # Save to disk
)
```

## Testing

```bash
# Run the scraper
python scraper/fetch_blog.py

# Verify JSON files created
ls -la data/blog/

# Run again to test duplicate detection
python scraper/fetch_blog.py

# Check metadata
cat data/metadata.json
```

## Dependencies

This module depends on:
- `scraper.metadata` - URL tracking and metadata management
- `scraper.utils` - File I/O utilities

Fallback implementations are included if these modules are unavailable.
