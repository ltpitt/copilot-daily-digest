# Task 2.2: Create YouTube Scraper (RSS-First with API Fallback)

**Phase**: 2 - YouTube Integration  
**Priority**: HIGH  
**Estimated Effort**: 3-4 hours  
**Assigned Agent**: `youtube-specialist`

## Context
YouTube provides both RSS feeds and a REST API. We should prefer RSS feeds (no quota limits, simpler) and use the API only when we need additional metadata like duration, view count, or detailed filtering.

## Objective
Create a YouTube scraper that fetches videos from the GitHub channel, filters by Copilot-related keywords, and stores metadata for content generation.

## Tasks

### 1. Create `scraper/fetch_youtube.py`
```python
import feedparser
from googleapiclient.discovery import build
from scraper.utils import fetch_url, safe_write_file, sanitize_filename
from scraper.metadata import add_video_id, load_metadata
import os
import yaml

def fetch_videos_rss(channel_id: str) -> list[dict]:
    """
    Fetch videos from YouTube channel using RSS feed (preferred)
    RSS URL: https://www.youtube.com/feeds/videos.xml?channel_id={channel_id}
    """
    pass

def fetch_videos_api(channel_id: str, max_results: int = 50) -> list[dict]:
    """
    Fetch videos using YouTube Data API v3 (fallback/enrichment)
    """
    pass

def parse_video_entry(entry, source: str = "rss") -> dict:
    """
    Parse video entry into structured format:
    {
        "video_id": str,
        "title": str,
        "url": str,
        "thumbnail": str,
        "published": str (ISO 8601),
        "channel_name": str,
        "channel_id": str,
        "description": str,
        "duration": str (if from API),
        "view_count": int (if from API),
        "source": "rss" or "api"
    }
    """
    pass

def filter_copilot_videos(videos: list[dict]) -> list[dict]:
    """
    Filter videos by Copilot-related keywords in title/description
    """
    pass

def enrich_with_api_data(videos: list[dict]) -> list[dict]:
    """
    Optionally enrich RSS data with API data (duration, views, etc.)
    Only if API key available and quota permits
    """
    pass

def save_videos(videos: list[dict]) -> int:
    """
    Save videos to data/videos/
    Filename format: YYYY-MM-DD_{video_id}.json
    Return count of new videos saved
    """
    pass

def load_config() -> dict:
    """Load configuration from config/youtube.yml"""
    pass

def main():
    """Main entry point for YouTube scraper"""
    pass
```

### 2. Implement RSS-first approach
```python
def fetch_videos_rss(channel_id: str) -> list[dict]:
    feed_url = f"https://www.youtube.com/feeds/videos.xml?channel_id={channel_id}"
    feed = feedparser.parse(feed_url)
    
    videos = []
    for entry in feed.entries:
        video = {
            "video_id": entry.yt_videoid,
            "title": entry.title,
            "url": entry.link,
            "thumbnail": entry.media_thumbnail[0]["url"],
            "published": entry.published,
            "channel_name": entry.author,
            "channel_id": channel_id,
            "description": entry.summary,
            "source": "rss"
        }
        videos.append(video)
    
    return videos
```

### 3. Implement API fallback (optional enrichment)
```python
def fetch_videos_api(channel_id: str, max_results: int = 50) -> list[dict]:
    api_key = os.getenv("YOUTUBE_API_KEY")
    if not api_key:
        return []
    
    youtube = build("youtube", "v3", developerKey=api_key)
    
    # Search for videos in channel
    search_response = youtube.search().list(
        part="id,snippet",
        channelId=channel_id,
        maxResults=max_results,
        order="date",
        type="video"
    ).execute()
    
    video_ids = [item["id"]["videoId"] for item in search_response["items"]]
    
    # Get video details (duration, views, etc.)
    videos_response = youtube.videos().list(
        part="snippet,contentDetails,statistics",
        id=",".join(video_ids)
    ).execute()
    
    # Parse and return videos
    return [parse_api_video(item) for item in videos_response["items"]]
```

### 4. Implement keyword filtering
Use keywords from `config/youtube.yml`:
```python
def filter_copilot_videos(videos: list[dict]) -> list[dict]:
    config = load_config()
    keywords = [k.lower() for k in config["filters"]["keywords"]]
    
    filtered = []
    for video in videos:
        text = f"{video['title']} {video['description']}".lower()
        if any(keyword in text for keyword in keywords):
            filtered.append(video)
    
    return filtered
```

### 5. Implement duplicate prevention
```python
def save_videos(videos: list[dict]) -> int:
    new_count = 0
    
    for video in videos:
        # Check if video already tracked
        if not add_video_id(video["video_id"]):
            continue  # Skip duplicate
        
        # Save video metadata
        date = video["published"][:10]  # YYYY-MM-DD
        filename = f"{date}_{video['video_id']}.json"
        filepath = f"data/videos/{filename}"
        
        safe_write_file(filepath, json.dumps(video, indent=2))
        new_count += 1
    
    return new_count
```

### 6. Add age filtering
Filter out old videos based on `max_age_days` in config:
```python
def filter_by_age(videos: list[dict], max_days: int) -> list[dict]:
    cutoff = datetime.now(timezone.utc) - timedelta(days=max_days)
    
    filtered = []
    for video in videos:
        published = datetime.fromisoformat(video["published"].replace("Z", "+00:00"))
        if published >= cutoff:
            filtered.append(video)
    
    return filtered
```

### 7. Add error handling and logging
- Handle network errors (feed unavailable)
- Handle parsing errors (malformed RSS/XML)
- Handle API quota exceeded gracefully
- Log all operations with context
- Continue on individual video failures

### 8. Create configuration loader
```python
def load_config() -> dict:
    config_path = "config/youtube.yml"
    with open(config_path) as f:
        return yaml.safe_load(f)
```

## Acceptance Criteria
- [ ] `scraper/fetch_youtube.py` created with all functions
- [ ] Uses RSS feeds as primary method (no quota limits)
- [ ] Successfully fetches videos from GitHub channel
- [ ] Filters videos by Copilot-related keywords
- [ ] Optionally enriches with API data (duration, views)
- [ ] Saves videos as JSON in `data/videos/`
- [ ] Prevents duplicate videos using metadata
- [ ] Filters by age (last 90 days by default)
- [ ] Handles errors gracefully (network, API quota)
- [ ] Logs all operations clearly
- [ ] Can be run standalone: `python scraper/fetch_youtube.py`
- [ ] Returns count of new videos found

## Dependencies
- Requires Task 2.1 (YouTube API setup) - but RSS works without API
- Requires Task 1.2 (metadata system)
- Requires Task 1.1 (directory structure)

## Testing
```bash
# Test RSS-only (no API key needed)
python scraper/fetch_youtube.py

# Test with API enrichment
export YOUTUBE_API_KEY="your-key"
python scraper/fetch_youtube.py

# Verify files created
ls -la data/videos/

# Run again - should skip duplicates
python scraper/fetch_youtube.py
```

## Example Output
```
[INFO] Loading config from config/youtube.yml
[INFO] Fetching videos from GitHub channel (RSS)
[INFO] Found 25 videos in RSS feed
[INFO] Filtered by age (90 days): 18 videos
[INFO] Filtered by keywords: 7 videos
[INFO] Checking for duplicates...
[INFO] 4 new videos, 3 duplicates skipped
[INFO] Saved to data/videos/
[INFO] Updated metadata.json

New videos:
  - "GitHub Copilot Workspace Demo" (Dec 6, 2025)
  - "Building with Copilot Agents" (Dec 3, 2025)
  - "Copilot Extensions Tutorial" (Dec 1, 2025)
  - "AI-Powered Development" (Nov 28, 2025)
```

## Notes
- RSS is preferred: no quota limits, simpler, faster
- API is optional: only for enrichment (duration, views, likes)
- Consider adding `--enrich` flag to optionally use API
- YouTube RSS returns last 15 videos by default
- For older videos, API search is needed
