# Metadata Tracking System

This module provides a robust metadata tracking system for the Copilot Daily Digest project. It tracks content changes, prevents duplicates, and maintains version history.

## Features

- **Content Hashing**: SHA256-based change detection
- **Duplicate Prevention**: Track video IDs and blog URLs to prevent duplicates
- **Version History**: Maintain history of documentation changes
- **Timestamp Management**: ISO 8601 UTC timestamps for all operations
- **Error Handling**: Automatic recovery from corrupted metadata files
- **Type Safety**: Full type hints and comprehensive docstrings

## Installation

No additional dependencies required - uses Python standard library only.

## Usage

### Basic Usage

```python
from scraper.metadata import (
    load_metadata,
    is_content_changed,
    update_content_hash,
    add_video_id,
    add_blog_url,
    get_changes_summary
)

# Load metadata
metadata = load_metadata()

# Check if content changed
content = fetch_doc("https://docs.github.com/copilot/overview")
if is_content_changed("docs/copilot-overview.md", content):
    print("Content has changed!")
    save_doc(content)
    update_content_hash("docs/copilot-overview.md", content)

# Track video IDs
if add_video_id("dQw4w9WgXcQ"):
    print("New video detected!")
else:
    print("Duplicate video skipped")

# Track blog URLs
if add_blog_url("https://github.blog/2025-12-01-copilot-updates/"):
    print("New blog post detected!")
else:
    print("Duplicate blog post skipped")

# Get summary
summary = get_changes_summary()
print(f"Total docs: {summary['total_docs']}")
print(f"Total videos: {summary['total_videos']}")
print(f"Total blog posts: {summary['total_blog_posts']}")
```

### Integration with Scraper

See `example_integration.py` for a complete example of integrating metadata tracking with the scraper workflow.

## API Reference

### Core Functions

#### `load_metadata() -> dict`
Load metadata from `data/metadata.json`. Creates a new file with defaults if it doesn't exist. Automatically handles corrupted files by backing them up and creating a fresh copy.

#### `save_metadata(metadata: dict) -> None`
Save metadata to `data/metadata.json`. Automatically updates the `last_updated` timestamp.

#### `calculate_hash(content: str) -> str`
Calculate SHA256 hash of content. Returns a 64-character hexadecimal string.

#### `is_content_changed(file_path: str, content: str) -> bool`
Check if content has changed since the last scrape. Returns `True` if content is new or changed, `False` otherwise.

#### `add_video_id(video_id: str) -> bool`
Add a video ID to metadata. Returns `True` if the video ID is new, `False` if it's a duplicate.

#### `add_blog_url(url: str) -> bool`
Add a blog URL to metadata. Returns `True` if the URL is new, `False` if it's a duplicate.

#### `update_content_hash(file_path: str, content: str) -> None`
Update the hash for a given file path. Also updates `doc_versions` to track change history.

#### `get_changes_summary() -> dict`
Get a summary of changes since the last update. Returns a dictionary with statistics about tracked content.

### Timestamp Utilities

#### `get_current_timestamp() -> str`
Get the current timestamp in ISO 8601 UTC format (e.g., `"2025-12-08T10:00:00Z"`).

#### `parse_timestamp(timestamp_str: str) -> datetime`
Parse an ISO 8601 timestamp string to a datetime object.

#### `is_newer_than(timestamp_str: str, days: int = 7) -> bool`
Check if a timestamp is newer than a given number of days.

### Utility Functions

#### `reset_metadata() -> None`
Reset metadata to default state. Backs up the existing metadata before resetting.

## Metadata Schema

The `data/metadata.json` file follows this structure:

```json
{
  "version": "1.0.0",
  "last_updated": "2025-12-08T10:00:00Z",
  "content_hashes": {
    "docs/copilot-overview.md": "abc123...",
    "blog/2025-12-01-new-features.json": "def456..."
  },
  "video_ids": [
    "dQw4w9WgXcQ",
    "jNQXAC9IVRw"
  ],
  "blog_urls": [
    "https://github.blog/2025-12-01-copilot-updates/",
    "https://github.blog/2025-12-05-new-features/"
  ],
  "doc_versions": {
    "copilot-overview": {
      "current_hash": "abc123...",
      "previous_hash": "xyz789...",
      "last_changed": "2025-12-01T15:30:00Z"
    }
  },
  "stats": {
    "total_docs": 5,
    "total_blog_posts": 12,
    "total_videos": 8,
    "last_successful_scrape": "2025-12-08T10:00:00Z"
  }
}
```

## Error Handling

The metadata system includes robust error handling:

- **Missing File**: Automatically creates `data/metadata.json` with default values
- **Corrupted JSON**: Backs up the corrupted file to `data/metadata.backup.json` and creates a fresh copy
- **Missing Keys**: Automatically adds missing keys from the default schema
- **Invalid Data**: Validates structure and resets if necessary

## Testing

Run the metadata system test:

```bash
python scraper/metadata.py
```

This will run a series of tests to verify:
- Hash calculation consistency
- Duplicate detection
- Change detection
- Metadata persistence
- Summary generation
- Timestamp utilities

## Best Practices

1. **Always load metadata before scraping**: Call `load_metadata()` at the start of your scraper
2. **Check for changes before saving**: Use `is_content_changed()` to avoid unnecessary writes
3. **Update hashes after saving**: Call `update_content_hash()` after successfully saving content
4. **Use absolute paths consistently**: Store file paths relative to project root
5. **Handle errors gracefully**: The system will automatically recover from common errors
6. **Backup before major operations**: The system automatically backs up when resetting or recovering

## License

Part of the Copilot Daily Digest project.
