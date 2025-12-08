# Task 1.5: Implement Change Detection System

**Phase**: 1 - Foundation & Infrastructure  
**Priority**: HIGH  
**Estimated Effort**: 2-3 hours  
**Assigned Agent**: `change-detector`

## Context
We need to detect what's new or changed since the last scrape to power the "What's New" section and avoid unnecessary content regeneration when nothing has changed.

## Objective
Create a change detection system that compares current content with previous versions, generates diff summaries, and identifies what's new for users.

## Tasks

### 1. Create `scraper/detect_changes.py`
```python
from scraper.metadata import load_metadata, calculate_hash
from scraper.utils import safe_read_file
from typing import List, Dict

def detect_doc_changes() -> Dict[str, any]:
    """
    Detect changes in documentation files
    Returns: {
        "changed": ["file1.md", "file2.md"],
        "new": ["file3.md"],
        "unchanged": ["file4.md"],
        "deleted": ["file5.md"]
    }
    """
    pass

def detect_blog_changes() -> Dict[str, any]:
    """
    Detect new blog posts (comparing URLs in metadata)
    Returns: {
        "new_posts": [{"title": ..., "url": ..., "date": ...}],
        "count": 5
    }
    """
    pass

def detect_video_changes() -> Dict[str, any]:
    """
    Detect new videos (comparing video IDs in metadata)
    Returns: {
        "new_videos": [{"title": ..., "video_id": ..., "date": ...}],
        "count": 3
    }
    """
    pass

def generate_change_summary() -> Dict[str, any]:
    """
    Generate comprehensive change summary
    Returns: {
        "has_changes": bool,
        "summary": str,
        "details": {
            "docs": {...},
            "blog": {...},
            "videos": {...}
        },
        "timestamp": str
    }
    """
    pass

def get_whats_new(days: int = 7) -> Dict[str, any]:
    """
    Get everything new in the last N days
    Returns: {
        "period": "Last 7 days",
        "total_changes": 12,
        "new_docs": [...],
        "new_blog_posts": [...],
        "new_videos": [...]
    }
    """
    pass

def main():
    """Main entry point - detect all changes and print summary"""
    pass
```

### 2. Implement documentation change detection
- Compare current file hashes with `metadata.json`
- Identify: new files, changed files, deleted files
- Track version history in metadata
- Store previous hash for each doc

### 3. Implement blog post change detection
- Compare blog URLs in `data/blog/` with metadata
- Identify new posts by checking `blog_urls` list
- Sort by date (newest first)
- Return post details (title, URL, date, summary)

### 4. Implement video change detection
- Compare video IDs in `data/videos/` with metadata
- Identify new videos by checking `video_ids` list
- Sort by publish date (newest first)
- Return video details (title, ID, date, thumbnail)

### 5. Generate human-readable summaries
```python
# Example summary format:
"""
Changes detected on December 8, 2025:

📄 Documentation: 2 files changed
  - copilot-chat.md: Updated content
  - copilot-extensions.md: New file added

📝 Blog Posts: 3 new articles
  - "New Copilot Workspace Features" (Dec 5)
  - "Copilot Extensions Now GA" (Dec 3)
  - "Agent Mode Improvements" (Dec 1)

🎥 Videos: 1 new video
  - "Getting Started with Copilot Agents" (Dec 6)

Total: 6 changes detected
"""
```

### 6. Implement time-based filtering
- Filter changes by date range (last 7 days, 30 days, etc.)
- Use ISO 8601 timestamps from metadata
- Support "What's New This Week" functionality

### 7. Add detailed diff information (optional enhancement)
- For changed docs, calculate line-level diffs
- Highlight added/removed sections
- Provide change percentage
- Store diff in metadata for historical tracking

### 8. Save change summary to file
Save detection results to `data/changes-summary.json`:
```json
{
  "generated_at": "2025-12-08T15:30:00Z",
  "has_changes": true,
  "total_changes": 6,
  "docs": {
    "changed": ["copilot-chat.md"],
    "new": ["copilot-extensions.md"],
    "unchanged": ["copilot-overview.md", "..."],
    "deleted": []
  },
  "blog": {
    "new_count": 3,
    "new_posts": [...]
  },
  "videos": {
    "new_count": 1,
    "new_videos": [...]
  },
  "summary_text": "...",
  "whats_new_7_days": {...}
}
```

## Acceptance Criteria
- [ ] `scraper/detect_changes.py` created with all functions
- [ ] Detects changed/new/deleted documentation files
- [ ] Detects new blog posts (compares URLs)
- [ ] Detects new videos (compares video IDs)
- [ ] Generates human-readable change summary
- [ ] Supports time-based filtering (last N days)
- [ ] Saves change summary to `data/changes-summary.json`
- [ ] Returns `has_changes: false` when nothing changed
- [ ] All functions have type hints and docstrings
- [ ] Can be run standalone: `python scraper/detect_changes.py`
- [ ] Integrates with metadata system

## Dependencies
- Requires Task 1.2 (metadata system)
- Requires Task 1.1 (directory structure)
- Recommended: Task 1.3 (utilities)

## Testing
1. Initial scrape - all content is "new"
2. Second scrape with no changes - `has_changes: false`
3. Modify a doc file - detected as "changed"
4. Add a new blog post - detected as "new"
5. Test time filtering - only recent changes returned
6. Verify change summary is accurate and readable

## Example Output
```bash
$ python scraper/detect_changes.py

[INFO] Detecting changes...
[INFO] Checking documentation files...
[INFO] Checking blog posts...
[INFO] Checking videos...

✅ Changes detected!

📄 Documentation: 2 changes
  - copilot-chat.md: Content updated
  - copilot-extensions.md: New file

📝 Blog: 3 new posts
  - "Copilot Workspace Updates" (Dec 5, 2025)
  - "Extensions Now GA" (Dec 3, 2025)
  - "Agent Mode v2" (Dec 1, 2025)

🎥 Videos: 1 new video
  - "Getting Started with Agents" (Dec 6, 2025)

Total: 6 changes
Saved to data/changes-summary.json
```

## Notes
- This module is critical for the "What's New" feature
- Should be fast - avoid expensive operations
- Consider caching for repeated calls
- May be called by GitHub Actions to decide if PR is needed
