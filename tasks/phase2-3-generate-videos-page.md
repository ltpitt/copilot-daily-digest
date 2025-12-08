# Task 2.3: Generate Video Content Page

**Phase**: 2 - YouTube Integration  
**Priority**: MEDIUM  
**Estimated Effort**: 2 hours  
**Assigned Agent**: `content-generator`

## Context
Now that we have video metadata stored in `data/videos/`, we need to generate a user-facing page (`content/videos.md`) that presents videos in an organized, newspaper-style format.

## Objective
Create a script that reads video data and generates a well-formatted `content/videos.md` with categorization, thumbnails, and "What's New" highlights.

## Tasks

### 1. Create `scraper/generate_videos.py`
```python
from pathlib import Path
import json
from datetime import datetime, timedelta
from typing import List, Dict

def load_all_videos() -> List[dict]:
    """Load all video metadata from data/videos/"""
    pass

def categorize_videos(videos: List[dict]) -> Dict[str, List[dict]]:
    """
    Categorize videos by topic based on title/description keywords
    Categories: Getting Started, Features, Tutorials, Updates, Extensions, Agents
    """
    pass

def get_recent_videos(videos: List[dict], days: int = 7) -> List[dict]:
    """Get videos published in the last N days"""
    pass

def format_video_entry(video: dict) -> str:
    """
    Format video as markdown entry with thumbnail and metadata
    Returns:
    ### [Video Title](https://youtube.com/watch?v=...)
    ![Thumbnail](thumbnail_url)
    
    **Published**: Dec 6, 2025 | **Duration**: 12:34 | **Channel**: GitHub
    
    Brief description...
    
    ---
    """
    pass

def generate_videos_page(videos: List[dict]) -> str:
    """Generate complete videos.md content"""
    pass

def main():
    """Main entry point"""
    pass
```

### 2. Implement video categorization
```python
CATEGORIES = {
    "Getting Started": ["getting started", "intro", "introduction", "basics", "beginner"],
    "Features": ["feature", "new feature", "announcement", "release"],
    "Tutorials": ["tutorial", "how to", "guide", "walkthrough", "demo"],
    "Updates": ["update", "changelog", "what's new", "improvements"],
    "Extensions": ["extension", "plugin", "integrate", "api"],
    "Agents": ["agent", "coding agent", "workspace agent", "autonomous"],
    "Other": []  # Catch-all
}

def categorize_video(video: dict) -> str:
    """Return category name for video based on keywords"""
    text = f"{video['title']} {video['description']}".lower()
    
    for category, keywords in CATEGORIES.items():
        if any(kw in text for kw in keywords):
            return category
    
    return "Other"
```

### 3. Create videos.md template structure
```markdown
# 🎥 GitHub Copilot Videos

> Curated video content from GitHub's official channel

**Last Updated**: December 8, 2025  
**Total Videos**: 42 | **New This Week**: 4

---

## 🆕 What's New This Week

[4 recent videos from last 7 days]

---

## 📚 Browse by Category

- [Getting Started](#getting-started) (8 videos)
- [Features](#features) (12 videos)
- [Tutorials](#tutorials) (15 videos)
- [Updates](#updates) (5 videos)
- [Extensions](#extensions) (6 videos)
- [Agents](#agents) (4 videos)

---

## Getting Started

[Videos in this category...]

---

## Features

[Videos in this category...]

[... more categories ...]

---

## 📊 Statistics

- Total Videos Tracked: 42
- Latest Video: "GitHub Copilot Workspace Demo" (Dec 6, 2025)
- Oldest Video: "Introducing GitHub Copilot" (Mar 15, 2024)
- Most Popular Category: Tutorials (15 videos)

---

*Videos are automatically updated daily. See something missing? [Open an issue](https://github.com/ltpitt/copilot-daily-digest/issues).*
```

### 4. Implement video entry formatting
```markdown
### [GitHub Copilot Workspace Demo](https://youtube.com/watch?v=dQw4w9WgXcQ)

[![Thumbnail](https://i.ytimg.com/vi/dQw4w9WgXcQ/mqdefault.jpg)](https://youtube.com/watch?v=dQw4w9WgXcQ)

**Published**: December 6, 2025 | **Duration**: 12:34 | **Channel**: GitHub

Learn how to use GitHub Copilot Workspace to build entire features with AI assistance. This demo shows real-world examples...

[Watch on YouTube →](https://youtube.com/watch?v=dQw4w9WgXcQ)

---
```

### 5. Add "What's New This Week" section
- Show videos from last 7 days at the top
- Sort by date (newest first)
- Highlight with emoji/badge
- Show count: "4 new videos this week"

### 6. Add statistics and metadata
- Total video count
- Count per category
- Latest video (with date)
- Oldest tracked video
- Last updated timestamp

### 7. Implement sorting
- Within each category: newest first
- "What's New" section: newest first
- Consider adding sort options (date, title, duration)

### 8. Save generated content
```python
def main():
    videos = load_all_videos()
    content = generate_videos_page(videos)
    
    output_path = "content/videos.md"
    with open(output_path, "w") as f:
        f.write(content)
    
    print(f"✅ Generated {output_path}")
    print(f"   Total videos: {len(videos)}")
    print(f"   Categories: {len(get_categories(videos))}")
```

## Acceptance Criteria
- [ ] `scraper/generate_videos.py` created with all functions
- [ ] Loads all videos from `data/videos/` directory
- [ ] Categorizes videos by topic intelligently
- [ ] Generates `content/videos.md` with proper formatting
- [ ] "What's New This Week" section highlights recent videos
- [ ] Each video entry includes: title, thumbnail, date, duration, description
- [ ] Videos sorted by date within categories (newest first)
- [ ] Statistics section shows totals and metadata
- [ ] Thumbnails are clickable and link to YouTube
- [ ] Markdown renders correctly on GitHub
- [ ] Can be run standalone: `python scraper/generate_videos.py`

## Dependencies
- Requires Task 2.2 (YouTube scraper) to have videos in `data/videos/`
- Requires Task 1.1 (directory structure)

## Testing
```bash
# Generate videos page
python scraper/generate_videos.py

# Verify output
cat content/videos.md

# Check on GitHub
git add content/videos.md
git commit -m "Update videos page"
git push
# View rendered page on GitHub
```

## Example Statistics Output
```
✅ Generated content/videos.md
   Total videos: 42
   New this week: 4
   Categories: 6
   Latest: "Copilot Workspace Demo" (Dec 6, 2025)
```

## Notes
- Keep formatting consistent with other content pages
- Ensure thumbnails work (HTTPS URLs)
- Consider adding video duration in MM:SS format
- YouTube embeds won't work in GitHub markdown (use links)
- Consider adding "Featured" section for important videos
