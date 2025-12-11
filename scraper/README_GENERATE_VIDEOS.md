# Video Content Page Generator

## Overview

The `generate_videos.py` script generates a comprehensive video library page (`content/videos.md`) from video metadata stored in the `data/videos/` directory.

## Features

- **Automatic Categorization**: Organizes videos by topic based on keywords
- **Recent Content Highlighting**: "What's New This Week" section for videos from last 7 days
- **No Duplication**: Recent videos marked with 🆕 badge in categories instead of being shown twice
- **Streamlined Metadata**: Full metadata in "What's New", minimal metadata in categories
- **Featured Videos**: Optional section for manually curated high-value content
- **Rich Metadata Display**: Shows thumbnails, duration, view counts, publish dates
- **Category Navigation**: Browse videos by topic with clear organization
- **Actionable Descriptions**: "When to watch" guidance for each category
- **Statistics Callout**: Compact stats box at the top of the page

## Categories

Videos are automatically categorized based on keywords in titles and descriptions:

1. **Getting Started** - Introductory content for beginners
2. **Features & Updates** - New feature announcements, releases, and updates (combined category)
3. **Tutorials** - Step-by-step guides and walkthroughs
4. **Agents** - Content about coding agents and automation
5. **Extensions** - Integration and extension guides
6. **Other** - Uncategorized content

## Featured Videos

You can manually curate high-value evergreen content by adding video IDs to the `FEATURED_VIDEO_IDS` list in the script:

```python
FEATURED_VIDEO_IDS = [
    "dI4H5ZyYOx0",  # Assign Linear issues to Copilot coding agent
    "LwqUp4Dc1mQ",  # Extending AI Agents: GitHub MCP Server demo
]
```

Featured videos will appear in a dedicated section after "What's New This Week" and before category sections. If no videos are featured (empty list), the section is automatically hidden.

## Usage

### Basic Usage

```bash
python scraper/generate_videos.py
```

### From Repository Root

```bash
cd /path/to/copilot-daily-digest
python scraper/generate_videos.py
```

### Expected Output

The script will:
1. Load all video JSON files from `data/videos/`
2. Categorize videos by keywords
3. Identify recent videos (last 7 days)
4. Check for featured videos (if any)
5. Generate `content/videos.md` with:
   - Header with statistics callout box
   - Quick Navigation (table of contents)
   - What's New This Week section (full metadata)
   - Featured Videos section (if configured)
   - Browse by Topic overview with "When to watch" guidance
   - Category sections with videos (minimal metadata, 🆕 badge for recent)
   - More Resources footer

## Input Format

Videos are stored as JSON files: `data/videos/YYYY-MM-DD_{video_id}.json`

### Required Fields

- `video_id`: Unique YouTube video identifier
- `title`: Video title
- `url`: YouTube URL
- `published`: ISO 8601 timestamp (e.g., "2025-12-06T10:00:00Z")

### Optional Fields

- `thumbnail`: Thumbnail URL (auto-generated if missing)
- `description`: Video description
- `duration`: ISO 8601 duration (e.g., "PT12M34S")
- `view_count`: Number of views (integer)
- `channel_name`: Channel name
- `channel_id`: Channel identifier

### Example Video JSON

```json
{
  "video_id": "dQw4w9WgXcQ",
  "title": "Getting Started with GitHub Copilot",
  "url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
  "thumbnail": "https://i.ytimg.com/vi/dQw4w9WgXcQ/mqdefault.jpg",
  "published": "2025-12-06T10:00:00Z",
  "channel_name": "GitHub",
  "description": "Learn how to get started with GitHub Copilot...",
  "duration": "PT12M34S",
  "view_count": 15420
}
```

## Output Format

The generated `content/videos.md` includes:

### Header Section
- Title and last updated timestamp
- Statistics callout box showing:
  - Total videos
  - New this week
  - Category breakdown
- Quick Navigation (table of contents)

### What's New This Week
- Videos from last 7 days
- Sorted by date (newest first)
- Full video cards with thumbnails and complete metadata
- Published date, duration, views, channel

### Featured Videos (Optional)
- Manually curated high-value content
- Only appears if `FEATURED_VIDEO_IDS` is populated
- Same format as "What's New" section

### Browse by Topic
- Overview of all categories
- Category descriptions with "When to watch" guidance
- Video counts per category

### Category Sections
- One section per non-empty category
- Category description and "When to watch" guidance
- Videos sorted by date (newest first)
- Video cards with:
  - 🆕 badge if published in last 7 days
  - Clickable thumbnail
  - Title (linked to YouTube)
  - Minimal metadata: Published date + duration only
  - Description snippet
  - Watch link

### Footer
- More Resources links to documentation
- Generation timestamp

## Functions

### `load_all_videos() -> List[dict]`
Loads all video JSON files from `data/videos/` directory.

### `categorize_videos(videos: List[dict]) -> Dict[str, List[dict]]`
Categorizes videos by topic based on keywords in titles and descriptions.

### `get_recent_videos(videos: List[dict], days: int = 7) -> List[dict]`
Filters videos published in the last N days.

### `format_video_entry(video: dict, metadata_level: str = "full", is_recent: bool = False) -> str`
Formats a video as a markdown card with thumbnail and metadata.

Parameters:
- `video`: Video dictionary with metadata
- `metadata_level`: "full" (shows all metadata) or "minimal" (date + duration only)
- `is_recent`: If True, adds 🆕 badge to video title

### `format_duration(duration: str) -> str`
Converts ISO 8601 duration (e.g., "PT12M34S") to human-readable format (e.g., "12:34").

### `format_view_count(count: Optional[int]) -> str`
Formats view counts with K/M suffixes (e.g., "15.4K views").

### `generate_videos_page(videos: List[dict]) -> str`
Generates the complete markdown content for videos.md.

## Error Handling

The script handles various error conditions:
- Missing or empty `data/videos/` directory
- Invalid JSON files
- Missing required fields
- Invalid date formats
- Empty video library

In all cases, the script will generate a valid output file (even if empty) and log warnings/errors to the console.

## Dependencies

- Python 3.7+
- `scraper.utils` module (for date parsing and file I/O)
- Standard library: `json`, `os`, `sys`, `datetime`, `pathlib`, `typing`, `collections`, `logging`

## Exit Codes

- `0`: Success
- `1`: Error occurred
- `130`: Interrupted by user (Ctrl+C)

## Logging

The script logs its progress to stdout with levels:
- `INFO`: Normal operations
- `WARNING`: Non-critical issues
- `ERROR`: Critical errors

Example output:
```
[INFO] Starting video page generation...
[INFO] Found 4 video files
[INFO] Successfully loaded 4 videos
[INFO] Category 'Getting Started': 1 videos
[INFO] Category 'Features': 1 videos
[INFO] Found 2 videos from last 7 days
[INFO] Generating videos.md content...
[INFO] Successfully generated: content/videos.md
[INFO] Total videos: 4
[INFO] New this week: 2
```

## Integration

This script is designed to be part of the content generation pipeline:

1. `fetch_youtube.py` - Fetches videos from YouTube RSS/API
2. `generate_videos.py` - Generates videos.md from fetched data
3. Other generators create README.md, changelog.md, etc.

## Testing

To test with sample data:

```bash
# Create sample video
cat > data/videos/2025-12-06_test.json << EOF
{
  "video_id": "test123",
  "title": "Test Video",
  "url": "https://youtube.com/watch?v=test123",
  "published": "2025-12-06T10:00:00Z",
  "channel_name": "Test Channel"
}
EOF

# Run generator
python scraper/generate_videos.py

# Check output
cat content/videos.md
```

## Maintenance

### Updating Categories

The category keywords can be updated in the `CATEGORIES` dictionary at the top of the script. When adding new categories:

1. Add category name and keywords to `CATEGORIES` dict
2. Add category emoji to the emoji dicts in `generate_videos_page()`
3. Add category description and "When to watch" text to the descriptions dict

### Curating Featured Videos

To highlight evergreen high-value content:

1. Find the video ID from the YouTube URL (e.g., `dI4H5ZyYOx0` from `https://www.youtube.com/watch?v=dI4H5ZyYOx0`)
2. Add it to `FEATURED_VIDEO_IDS` list at the top of the script:
   ```python
   FEATURED_VIDEO_IDS = [
       "dI4H5ZyYOx0",  # Assign Linear issues to Copilot coding agent
   ]
   ```
3. Re-run the script to regenerate videos.md

The featured section will automatically appear if the list is not empty.

## Future Enhancements

Potential improvements:
- Search functionality
- Playlist support
- Speaker/presenter tags
- Date range filtering
- Export to other formats (JSON, CSV)
- Video language detection
- Transcript integration
