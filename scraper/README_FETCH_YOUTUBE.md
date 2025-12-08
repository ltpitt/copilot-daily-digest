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

### Basic Usage (RSS Only)

No API key required:

```bash
python scraper/fetch_youtube.py
```

### With API Enrichment

Set your YouTube API key:

```bash
export YOUTUBE_API_KEY="your-api-key-here"
python scraper/fetch_youtube.py
```

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
  
  max_age_days: 90  # Only fetch videos from last 90 days

api:
  enabled: false  # Set to true to enable API enrichment
```

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

The scraper has been tested with:
- Configuration loading ✓
- Keyword filtering ✓
- Age-based filtering ✓
- Video saving ✓
- Duplicate prevention ✓
- Metadata integration ✓
- CodeQL security analysis (0 alerts) ✓

## Troubleshooting

**No videos found:**
- Check network connectivity
- Verify channel ID is correct in config
- Check if channel has recent videos
- Verify keywords aren't too restrictive

**API errors:**
- Verify `YOUTUBE_API_KEY` is set correctly
- Check API key permissions in Google Cloud Console
- Verify YouTube Data API v3 is enabled
- Check quota hasn't been exceeded

**Duplicate videos:**
- Videos are tracked by `video_id` in `data/metadata.json`
- Delete entry from `video_ids` array to re-process

## See Also

- [Metadata System Documentation](./README_METADATA.md)
- [Utilities Documentation](./README_UTILS.md)
- [Blog Scraper Documentation](./README_FETCH_BLOG.md)
