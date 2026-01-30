# YouTube Scraper Implementation Summary

## Overview

This document describes the implementation of the YouTube video scraper for the Copilot Daily Digest project. The scraper fetches videos from GitHub's YouTube channel using an RSS-first approach with optional API enrichment.

## Problem Statement

The original YouTube scraper had the following issues:
1. **Overly restrictive keyword filtering** - Required videos to match specific keywords (copilot, ai, agent) which filtered out most GitHub channel videos
2. **90-day age window** - Too broad, not focused on recent content
3. **No CLI flexibility** - No way to override config settings without editing files
4. **Missing dry-run mode** - Difficult to test without writing files

## Solution Implemented

### 1. Configuration Changes (`config/youtube.yml`)

```yaml
filters:
  max_age_days: 30  # Changed from 90
  require_keywords: false  # NEW: Disable keyword filtering by default
```

**Rationale**: The default behavior now returns ALL videos from the last 30 days, matching the requirement for "all the news in github channel in YouTube that are in the last 30 days."

### 2. Code Changes (`scripts/fetch_youtube.py`)

#### A. CLI Argument Parser

Added `parse_arguments()` function with the following flags:

| Flag | Type | Description |
|------|------|-------------|
| `--max-age-days N` | Integer | Override config's max_age_days |
| `--require-keywords` | Boolean | Enable keyword filtering |
| `--no-require-keywords` | Boolean | Disable keyword filtering |
| `--dry-run` | Boolean | Preview without writing files |

The `--require-keywords` and `--no-require-keywords` flags are mutually exclusive using `argparse.add_mutually_exclusive_group()`.

#### B. Main Function Updates

```python
def main():
    # Parse CLI arguments
    args = parse_arguments()
    
    # Override config with CLI arguments
    if args.max_age_days is not None:
        max_age_days = args.max_age_days
    else:
        max_age_days = filters.get('max_age_days', 30)
    
    # Determine keyword filtering behavior
    if args.require_keywords:
        require_keywords = True
    elif args.no_require_keywords:
        require_keywords = False
    else:
        require_keywords = filters.get('require_keywords', False)
    
    # Apply age filter
    all_videos = filter_by_age(all_videos, max_age_days)
    
    # Optionally apply keyword filter
    if require_keywords:
        all_videos = filter_copilot_videos(all_videos)
    
    # Save (or dry-run)
    new_count = save_videos(all_videos, dry_run=args.dry_run)
```

#### C. Dry-Run Mode

Modified `save_videos()` to support dry-run:

```python
def save_videos(videos: List[dict], dry_run: bool = False) -> int:
    if dry_run:
        logger.info(f"[DRY-RUN] Would save: {filename}")
        logger.info(f"  Title: {video.get('title', 'N/A')}")
        logger.info(f"  Published: {video.get('published', 'N/A')}")
        new_count += 1
    else:
        # Actually write file
        ...
```

#### D. Improved Logging

Added clear log messages at each filtering stage:
- "Using max_age_days from CLI: N" or "Using max_age_days from config: N"
- "Keyword filtering enabled/disabled"
- "Filtered by age (N days): X videos from Y total"
- "Skipping keyword filter, keeping all X videos"

### 3. Documentation Updates (`scripts/README_FETCH_YOUTUBE.md`)

Added comprehensive sections:
- **Usage Examples**: All CLI combinations with clear examples
- **Command-Line Arguments**: Table documenting all flags
- **Configuration**: Detailed explanation of `require_keywords` flag
- **Testing**: Step-by-step local testing instructions
- **Troubleshooting**: Common issues and solutions

## Default Behavior

With no arguments, `python scripts/fetch_youtube.py`:

1. Loads `config/youtube.yml`
2. Fetches RSS feed from GitHub channel (UC7c3Kb6jYCRj4JOHHZTxKsQ)
3. Parses 15 most recent videos from feed
4. Filters to videos from last **30 days**
5. Does **NOT** apply keyword filtering (includes all videos)
6. Saves new videos to `data/videos/` as `YYYY-MM-DD_{video_id}.json`
7. Updates `data/metadata.json` to track video IDs

## Testing

### Unit Tests

Created test script with mock data (`/tmp/test_youtube_scraper.py`):
- ✓ Age filtering (30-day, 10-day, 60-day filters)
- ✓ Keyword filtering (matches copilot, ai, agent)
- ✓ Video structure validation

### Integration Tests

```bash
# Test configuration loading
python -c "from scraper.fetch_youtube import load_config; ..."

# Test CLI help
python scripts/fetch_youtube.py --help

# Test mutually exclusive args
python scripts/fetch_youtube.py --require-keywords --no-require-keywords
# (Should error: "not allowed with argument")

# Test dry-run
python scripts/fetch_youtube.py --dry-run
```

### Security Scan

CodeQL security analysis: **0 alerts** ✓

## Usage Examples

### Basic Usage (Default: 30 days, no keyword filter)

```bash
python scripts/fetch_youtube.py
```

### Dry-Run Preview

```bash
python scripts/fetch_youtube.py --dry-run
```

### Custom Age Filter

```bash
# Last 7 days
python scripts/fetch_youtube.py --max-age-days 7

# Last 60 days  
python scripts/fetch_youtube.py --max-age-days 60
```

### With Keyword Filtering

```bash
python scripts/fetch_youtube.py --require-keywords
```

### Combined

```bash
python scripts/fetch_youtube.py --max-age-days 14 --require-keywords --dry-run
```

## Architecture

```
┌─────────────────┐
│  CLI Arguments  │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  load_config()  │◄─── config/youtube.yml
└────────┬────────┘
         │
         ▼
┌──────────────────┐
│ fetch_videos_rss │◄─── YouTube RSS Feed
└────────┬─────────┘      (last 15 videos)
         │
         ▼
┌──────────────────┐
│  filter_by_age   │
└────────┬─────────┘
         │
         ▼
┌────────────────────┐
│ filter_copilot_*   │ (optional, if require_keywords=true)
└────────┬───────────┘
         │
         ▼
┌──────────────────┐
│  save_videos()   │──► data/videos/*.json
└────────┬─────────┘
         │
         ▼
┌──────────────────┐
│ metadata.json    │ (track video IDs)
└──────────────────┘
```

## Files Modified

1. `config/youtube.yml` - Updated defaults (max_age_days: 30, require_keywords: false)
2. `scripts/fetch_youtube.py` - Added CLI args, dry-run, improved logic
3. `scripts/README_FETCH_YOUTUBE.md` - Comprehensive documentation

## Backward Compatibility

The changes are backward compatible:
- Running without arguments works as before (but now with 30-day default)
- Config file structure unchanged (just added optional `require_keywords` field)
- All existing functions maintain same signatures
- API enrichment still works when enabled with `YOUTUBE_API_KEY`

## Future Enhancements

Possible improvements for future PRs:
1. Support for multiple channels simultaneously
2. Output format options (JSON, CSV, Markdown)
3. Custom keyword lists via CLI
4. Video deduplication across multiple runs
5. Statistics reporting (videos per day, topics, etc.)

## Verification

To verify the implementation works:

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Test with dry-run
python scripts/fetch_youtube.py --dry-run

# Expected output:
# [INFO] Starting YouTube video scraper...
# [INFO] [DRY-RUN MODE] No files will be written
# [INFO] Using max_age_days from config: 30
# [INFO] Keyword filtering from config: disabled
# ...

# 3. Check configuration
python -c "import yaml; print(yaml.safe_load(open('config/youtube.yml'))['filters'])"

# Expected output:
# {'keywords': [...], 'max_age_days': 30, 'require_keywords': False, ...}
```

## Notes

- **Network access required**: The scraper fetches from `https://www.youtube.com/feeds/videos.xml`
- **No API key needed**: Default RSS-only mode requires no authentication
- **Quota-free**: RSS feeds have no rate limits or quota restrictions
- **Latest 15 videos**: RSS feed returns maximum 15 most recent videos per channel

## Author

Implementation by GitHub Copilot Coding Agent
Date: December 8, 2025
Issue: Implement YouTube scraper RSS-first approach with 30-day age filter
