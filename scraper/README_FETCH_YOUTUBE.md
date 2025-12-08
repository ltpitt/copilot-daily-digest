# YouTube Video Scraper

Fetches videos from GitHub's YouTube channel using RSS feeds as the primary method, with optional YouTube Data API v3 enrichment for additional metadata.

## Features

- **RSS-First Approach**: Uses YouTube RSS feeds (no API key required, no quota limits)
- **API Fallback**: Optional enrichment with YouTube Data API v3 for duration, view counts, etc.
- **Keyword Filtering**: Filters videos by Copilot-related keywords
- **Age Filtering**: Only fetch recent videos (configurable, default 90 days)
- **Duplicate Prevention**: Uses metadata system to prevent re-processing videos
- **Multi-Channel Support**: Can fetch from multiple channels
- **Error Handling**: Graceful degradation on network/API failures

## Usage

### Basic Usage (RSS Only, Default 30-day Filter)

No API key required. Fetches all videos from the last 30 days:

```bash
python scraper/fetch_youtube.py
```

### Dry-Run Mode

Preview what would be saved without actually writing files:

```bash
python scraper/fetch_youtube.py --dry-run
```

### Custom Age Filter

Fetch videos from a specific time period:

```bash
# Last 7 days
python scraper/fetch_youtube.py --max-age-days 7

# Last 60 days
python scraper/fetch_youtube.py --max-age-days 60
```

### Keyword Filtering

Enable keyword filtering to only get Copilot-related content:

```bash
python scraper/fetch_youtube.py --require-keywords
```

Or disable it explicitly (if enabled in config):

```bash
python scraper/fetch_youtube.py --no-require-keywords
```

### Combined Options

Combine multiple flags:

```bash
# Dry-run with custom age and keyword filtering
python scraper/fetch_youtube.py --max-age-days 14 --require-keywords --dry-run
```

### With API Enrichment

Set your YouTube API key for additional metadata (duration, views):

```bash
export YOUTUBE_API_KEY="your-api-key-here"
python scraper/fetch_youtube.py
```

## Command-Line Arguments

| Argument | Description |
|----------|-------------|
| `--max-age-days N` | Override config's max_age_days (default: 30) |
| `--require-keywords` | Enable keyword filtering (overrides config) |
| `--no-require-keywords` | Disable keyword filtering (overrides config) |
| `--dry-run` | Show what would be saved without writing files |
| `-h, --help` | Show help message with examples |

## Configuration

Edit `config/youtube.yml` to configure:

```yaml
channels:
  - id: "UC7c3Kb6jYCRj4JOHHZTxKsQ"  # @GitHub
    name: "GitHub"
    enabled: true

filters:
  keywords:
    - "copilot"
    - "ai"
    - "agent"
    # ... more keywords
  
  max_age_days: 30  # Only fetch videos from last 30 days
  
  require_keywords: false  # Set to true to require keyword matches

api:
  enabled: false  # Set to true to enable API enrichment
```

### Filter Configuration

- **max_age_days**: Number of days to look back for videos (default: 30)
- **require_keywords**: When `false` (default), returns ALL videos from the time period. When `true`, only returns videos matching the configured keywords.
- **keywords**: List of keywords to search for when `require_keywords: true`

### Default Behavior

By default, the scraper:
- Fetches all videos from the last **30 days**
- Does **NOT** require keyword matches (returns all videos)
- Uses RSS feeds (no API key needed)
- Saves to `data/videos/` as `YYYY-MM-DD_{video_id}.json`

## Output

Videos are saved to `data/videos/` with filename format: `YYYY-MM-DD_{video_id}.json`

Example output structure:
```json
{
  "video_id": "abc123",
  "title": "GitHub Copilot Tutorial",
  "url": "https://www.youtube.com/watch?v=abc123",
  "thumbnail": "https://...",
  "published": "2025-12-08T10:00:00Z",
  "channel_name": "GitHub",
  "channel_id": "UC7c3Kb6jYCRj4JOHHZTxKsQ",
  "description": "Learn about GitHub Copilot...",
  "source": "rss",
  "scraped_at": "2025-12-08T15:30:00Z"
}
```

With API enrichment, additional fields are included:
- `duration`: Video duration in ISO 8601 format (e.g., "PT10M30S")
- `view_count`: Number of views

## Functions

### Core Functions

- `fetch_videos_rss(channel_id: str)` - Fetch videos from RSS feed
- `fetch_videos_api(channel_id: str, max_results: int)` - Fetch videos via API
- `parse_video_entry(entry, source: str)` - Parse RSS/API entry to video dict
- `filter_copilot_videos(videos: list)` - Filter by keywords
- `filter_by_age(videos: list, max_days: int)` - Filter by age
- `enrich_with_api_data(videos: list)` - Add API metadata
- `save_videos(videos: list)` - Save videos to JSON files
- `load_config()` - Load configuration from YAML
- `main()` - Main entry point

## Dependencies

```
feedparser>=6.0.10
pyyaml>=6.0.1
google-api-python-client>=2.100.0  # Optional, only for API enrichment
```

## Integration

The scraper integrates with:
- **Metadata System** (`scraper/metadata.py`) - For duplicate tracking
- **Utilities** (`scraper/utils.py`) - For file I/O, date parsing, etc.
- **Configuration** (`config/youtube.yml`) - For settings

## Error Handling

The scraper handles errors gracefully:
- Network errors (feed unavailable) → Logs error, continues
- Parsing errors (malformed RSS) → Skips entry, continues
- API quota exceeded → Falls back to RSS-only mode
- Individual video failures → Logs error, continues with other videos

## API Quota Management

YouTube Data API v3 has a daily quota of 10,000 units (free tier):
- `search().list`: 100 units per request
- `videos().list`: 1 unit per request

The scraper is efficient:
- Uses RSS as primary method (0 quota)
- Only uses API for enrichment when enabled
- Batches API requests (up to 50 videos per request)

## Example Output

```
[INFO] Starting YouTube video scraper...
[INFO] Loading config from config/youtube.yml
[INFO] Found 1 enabled channel(s)
[INFO] Processing channel: GitHub (UC7c3Kb6jYCRj4JOHHZTxKsQ)
[INFO] Fetching videos from RSS: https://...
[INFO] Found 15 videos in RSS feed
[INFO] Successfully fetched 15 videos from GitHub (RSS)
[INFO] Total videos fetched: 15
[INFO] Filtered by age (90 days): 12 videos from 15 total
[INFO] Filtered to 7 Copilot-related videos from 12 total
[INFO] Checking for duplicates...
[INFO] Saved: 2025-12-06_abc123.json
[INFO] 3 duplicates skipped
[INFO] Scraping complete: 4 new videos saved
[INFO] Saved to data/videos
[INFO] Updated metadata.json

New videos:
  - "GitHub Copilot Workspace Demo" (Dec 6, 2025)
  - "Building with Copilot Agents" (Dec 3, 2025)
```

## Testing

### Local Testing

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Test with dry-run mode:**
   ```bash
   python scraper/fetch_youtube.py --dry-run
   ```
   
   Expected output:
   - Fetches RSS feed from GitHub channel
   - Shows N videos found from the last 30 days
   - Lists videos that would be saved
   - Does NOT write any files

3. **Test with custom age filter:**
   ```bash
   python scraper/fetch_youtube.py --max-age-days 7 --dry-run
   ```
   
   Expected: Only shows videos from the last 7 days

4. **Test with keyword filtering:**
   ```bash
   python scraper/fetch_youtube.py --require-keywords --dry-run
   ```
   
   Expected: Only shows videos matching configured keywords

5. **Run actual scrape:**
   ```bash
   python scraper/fetch_youtube.py
   ```
   
   Expected: Saves JSON files to `data/videos/`

### Verify Output

After running without `--dry-run`, check:

```bash
# List saved videos
ls -lh data/videos/*.json

# View a video's metadata
cat data/videos/2025-12-08_VIDEO_ID.json | python -m json.tool

# Check metadata tracking
cat data/metadata.json | python -m json.tool | grep -A 5 video_ids
```

### CI/CD Testing

In GitHub Actions, the scraper runs automatically:

```yaml
- name: Fetch YouTube Videos
  run: python scraper/fetch_youtube.py
  env:
    YOUTUBE_API_KEY: ${{ secrets.YOUTUBE_API_KEY }}  # Optional
```

To enable API enrichment in CI:
1. Add `YOUTUBE_API_KEY` secret in GitHub repository settings
2. Set `api.enabled: true` in `config/youtube.yml`

## Troubleshooting

**No videos found:**
- Check network connectivity
- Verify channel ID is correct in config (currently: `UC7c3Kb6jYCRj4JOHHZTxKsQ` for @GitHub)
- Check if channel has videos in the configured time period
- If `require_keywords: true`, verify keywords aren't too restrictive
- Try with `--dry-run` to see debug output

**All videos filtered out:**
- Check `max_age_days` setting - increase if needed
- If using `--require-keywords`, try without it
- Verify the channel has uploaded videos recently

**API errors:**
- Verify `YOUTUBE_API_KEY` is set correctly
- Check API key permissions in Google Cloud Console
- Verify YouTube Data API v3 is enabled
- Check quota hasn't been exceeded (10,000 units/day free tier)

**Duplicate videos:**
- Videos are tracked by `video_id` in `data/metadata.json`
- Delete entry from `video_ids` array to re-process
- Or reset metadata: `rm data/metadata.json` (will re-process all videos)

**Network errors in sandboxed environments:**
- The scraper may fail in environments without internet access
- Use `--dry-run` mode for testing code changes without network calls
- For actual execution, ensure network access to youtube.com

## See Also

- [Metadata System Documentation](./README_METADATA.md)
- [Utilities Documentation](./README_UTILS.md)
- [Blog Scraper Documentation](./README_FETCH_BLOG.md)
