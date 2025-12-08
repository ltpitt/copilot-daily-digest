# Task 1.2: Implement Metadata Tracking System

**Phase**: 1 - Foundation & Infrastructure  
**Priority**: HIGH  
**Estimated Effort**: 2-3 hours  
**Assigned Agent**: `change-detector`

## Context
We need a robust system to track content changes, prevent duplicates, and maintain history. This enables the change detection system to identify what's new.

## Objective
Create a metadata tracking system that stores:
- Content hashes for change detection
- Scrape timestamps
- Video IDs and blog URLs to prevent duplicates
- Version history for documentation

## Tasks

### 1. Define metadata schema
Create `data/metadata.json` with this structure:
```json
{
  "version": "1.0.0",
  "last_updated": "2025-12-08T10:00:00Z",
  "content_hashes": {
    "docs/copilot-overview.md": "abc123...",
    "docs/copilot-chat.md": "def456...",
    "blog/2025-12-01-new-features.json": "ghi789..."
  },
  "video_ids": [
    "dQw4w9WgXcQ",
    "jNQXAC9IVRw"
  ],
  "blog_urls": [
    "https://github.blog/2025-12-01-copilot-agent-updates/",
    "https://github.blog/changelog/2025-11-30-copilot-extensions/"
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

### 2. Create metadata management utilities
Create `scraper/metadata.py` with these functions:

```python
def load_metadata() -> dict:
    """Load metadata from data/metadata.json"""
    pass

def save_metadata(metadata: dict) -> None:
    """Save metadata to data/metadata.json"""
    pass

def calculate_hash(content: str) -> str:
    """Calculate SHA256 hash of content"""
    pass

def is_content_changed(file_path: str, content: str) -> bool:
    """Check if content has changed since last scrape"""
    pass

def add_video_id(video_id: str) -> bool:
    """Add video ID, return True if new (not duplicate)"""
    pass

def add_blog_url(url: str) -> bool:
    """Add blog URL, return True if new (not duplicate)"""
    pass

def update_content_hash(file_path: str, content: str) -> None:
    """Update hash for given file path"""
    pass

def get_changes_summary() -> dict:
    """Get summary of changes since last update"""
    pass
```

### 3. Add robust error handling
- Handle missing metadata.json (create with defaults)
- Handle corrupted JSON (backup and recreate)
- Add validation for metadata structure
- Log all metadata operations

### 4. Add timestamp utilities
- Use ISO 8601 format for all timestamps
- Add timezone support (UTC)
- Create helpers for date comparisons

### 5. Integrate with existing scraper
Update `scraper/fetch_docs.py` to:
- Load metadata before scraping
- Calculate hashes for all fetched content
- Compare with previous hashes
- Update metadata after successful scrape
- Log changes detected

## Acceptance Criteria
- [ ] `scraper/metadata.py` created with all utility functions
- [ ] `data/metadata.json` follows defined schema
- [ ] Content hashing works correctly (SHA256)
- [ ] Duplicate detection works for videos and blog posts
- [ ] Change detection identifies modified content
- [ ] Timestamps are in ISO 8601 UTC format
- [ ] Error handling covers edge cases (missing file, corrupt JSON)
- [ ] Existing scraper integrated with metadata system
- [ ] All functions have docstrings and type hints
- [ ] Metadata is properly versioned

## Dependencies
- Requires Task 1.1 (directory structure) to be completed

## Testing
1. Run scraper twice with unchanged content - no changes detected
2. Modify a doc file - change is detected
3. Add a duplicate video ID - correctly rejected
4. Corrupt metadata.json - automatically recovered
5. Check hash calculation consistency

## Example Usage
```python
from scraper.metadata import load_metadata, is_content_changed, update_content_hash

metadata = load_metadata()
content = fetch_doc("https://docs.github.com/copilot/overview")

if is_content_changed("docs/copilot-overview.md", content):
    print("Content has changed!")
    save_doc(content)
    update_content_hash("docs/copilot-overview.md", content)
```

## Notes
- Use standard library `hashlib` for hashing (SHA256)
- Use `json` module with `indent=2` for readable output
- Consider adding backup/restore functionality for metadata
