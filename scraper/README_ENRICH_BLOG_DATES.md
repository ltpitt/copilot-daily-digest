# Blog Date Enrichment Script

## Purpose

Enriches blog post metadata with publish dates by:
1. Extracting dates from changelog URLs (format: `/changelog/YYYY-MM-DD-`)
2. Fetching dates from RSS feeds for blog posts without dates in URLs
3. Storing enriched metadata in `data/blog/url_dates.json`

## When to Run

Run this script whenever:
- New blog URLs are added to `data/metadata.json`
- You need to regenerate content and ensure dates are available
- The `data/blog/url_dates.json` file is missing or outdated

## Requirements

```bash
pip install feedparser certifi requests
```

## Usage

```bash
cd /path/to/copilot-daily-digest
python3 scraper/enrich_blog_dates.py
```

## Output

Creates/updates `data/blog/url_dates.json` with structure:

```json
{
  "generated_at": "2025-12-16T08:12:50.445510Z",
  "total_urls": 30,
  "url_dates": {
    "https://github.blog/ai-and-ml/github-copilot/title/": "2025-12-04",
    "https://github.blog/changelog/2025-12-08-title": "2025-12-08"
  }
}
```

## How It Works

### 1. Date Extraction from URLs

For changelog URLs with dates embedded:
```
https://github.blog/changelog/2025-12-08-model-picker
                              ^^^^^^^^^^
                              Extracted date
```

Regex pattern: `/changelog/(\d{4}-\d{2}-\d{2})-`

### 2. RSS Feed Fetching

For blog posts without dates in URLs:
```
https://github.blog/ai-and-ml/github-copilot/how-to-use-spaces/
```

The script:
1. Fetches GitHub Blog RSS feed (`https://github.blog/tag/github-copilot/feed/`)
2. Searches for matching entry by URL
3. Extracts `published_parsed` field from feed entry
4. Converts to ISO date format (YYYY-MM-DD)

### 3. Data Storage

Maps URLs to ISO dates in JSON format for fast lookup during content generation.

## Error Handling

- **No date in URL and not found in RSS**: Logs warning, skips URL
- **RSS feed unavailable**: Tries both blog and changelog feeds
- **Invalid date format**: Logs error, skips URL

## Integration

This file is used by:
- `content-generator` agent (reads url_dates.json for WHATS-NEW.md)
- `publisher` agent (reads url_dates.json for date extraction)
- Content generation workflows (ensures complete dates)

## Validation

After running, verify output:
```bash
python3 -c "import json; data=json.load(open('data/blog/url_dates.json')); print(f'{data[\"total_urls\"]} URLs mapped')"
```

Expected output: `30 URLs mapped` (or similar count)

## Maintenance

- **Automatic**: Can be added to CI/CD pipeline to run before content generation
- **Manual**: Run when you notice incomplete dates in WHATS-NEW.md
- **Frequency**: Run whenever blog URLs are updated in metadata.json

## Related Files

- `scraper/fetch_blog.py` - Fetches blog posts and stores URLs in metadata.json
- `scripts/validate_whats_new.py` - Validates that dates are complete and ordered
- `.github/agents/content-generator.agent.md` - Uses url_dates.json for content generation
- `.github/agents/publisher.agent.md` - Uses url_dates.json for content synthesis
