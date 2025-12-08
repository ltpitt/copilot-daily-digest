"""
YouTube Video Scraper (RSS-First with API Fallback)

Fetches videos from GitHub's YouTube channel using RSS feeds as the primary method,
with optional YouTube Data API v3 enrichment for additional metadata.

RSS Feed provides:
- Last 15 videos from channel
- No quota limits
- Basic metadata (title, description, published date, thumbnail)

YouTube Data API v3 provides (optional enrichment):
- Duration, view count, like count
- Detailed statistics
- Search capabilities for older videos
"""

import argparse
import feedparser
import json
import os
import sys
import yaml
from datetime import datetime, timezone, timedelta
from pathlib import Path
from typing import List, Dict, Optional
import re

# Add parent directory to path to import local modules
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from scraper.metadata import add_video_id, load_metadata
from scraper.utils import (
    safe_write_file,
    ensure_directory,
    parse_iso,
    days_since,
    sanitize_filename,
    now_iso
)

# Use standard logging with format similar to utils.py style
import logging
logging.basicConfig(
    level=logging.INFO,
    format='[%(levelname)s] %(message)s'
)
logger = logging.getLogger(__name__)

# Try to import YouTube API client (optional)
try:
    from googleapiclient.discovery import build
    from googleapiclient.errors import HttpError
    YOUTUBE_API_AVAILABLE = True
except ImportError:
    YOUTUBE_API_AVAILABLE = False
    logger.debug("YouTube API client not available (optional)")


# ============================================================================
# Configuration
# ============================================================================

CONFIG_FILE = Path(__file__).parent.parent / "config" / "youtube.yml"
DATA_DIR = Path(__file__).parent.parent / "data" / "videos"


def load_config() -> dict:
    """
    Load configuration from config/youtube.yml.
    
    Returns:
        dict: Configuration dictionary with channels, filters, and output settings
    """
    try:
        with open(CONFIG_FILE, 'r', encoding='utf-8') as f:
            config = yaml.safe_load(f)
        logger.debug(f"Loaded config from {CONFIG_FILE}")
        return config
    except FileNotFoundError:
        logger.error(f"Config file not found: {CONFIG_FILE}")
        raise
    except yaml.YAMLError as e:
        logger.error(f"Failed to parse YAML config: {e}")
        raise


# ============================================================================
# RSS Feed Functions
# ============================================================================

def fetch_videos_rss(channel_id: str) -> List[dict]:
    """
    Fetch videos from YouTube channel using RSS feed.
    
    RSS feed returns the last 15 videos from the channel.
    No API key required, no quota limits.
    
    Args:
        channel_id: YouTube channel ID
        
    Returns:
        List of video dictionaries with basic metadata
    """
    rss_url = f"https://www.youtube.com/feeds/videos.xml?channel_id={channel_id}"
    
    logger.info(f"Fetching videos from RSS: {rss_url}")
    
    try:
        feed = feedparser.parse(rss_url)
        
        if feed.bozo:
            logger.warning(f"Feed parsing warning: {feed.get('bozo_exception', 'Unknown')}")
        
        if not feed.entries:
            logger.warning("No entries found in RSS feed")
            return []
        
        logger.info(f"Found {len(feed.entries)} videos in RSS feed")
        
        videos = []
        for entry in feed.entries:
            try:
                video = parse_video_entry(entry, source="rss")
                if video:
                    videos.append(video)
            except Exception as e:
                logger.error(f"Failed to parse video entry: {e}")
                continue
        
        return videos
    
    except Exception as e:
        logger.error(f"Failed to fetch RSS feed: {e}")
        return []


def parse_video_entry(entry, source: str = "rss") -> Optional[dict]:
    """
    Parse video entry into structured format.
    
    Args:
        entry: feedparser entry object (for RSS) or API response (for API)
        source: Data source ("rss" or "api")
        
    Returns:
        Dictionary with video metadata:
        {
            "video_id": str,
            "title": str,
            "url": str,
            "thumbnail": str,
            "published": str (ISO 8601),
            "channel_name": str,
            "channel_id": str,
            "description": str,
            "duration": str (optional, from API),
            "view_count": int (optional, from API),
            "source": "rss" or "api"
        }
    """
    try:
        if source == "rss":
            # Parse RSS feed entry
            video_id = entry.get('yt_videoid', '')
            
            # Fallback: extract video ID from link if yt_videoid not available
            if not video_id and 'link' in entry:
                link = entry.get('link', '')
                # Extract from URL like https://www.youtube.com/watch?v=VIDEO_ID
                match = re.search(r'[?&]v=([^&]+)', link)
                if match:
                    video_id = match.group(1)
            
            if not video_id:
                logger.warning("Entry missing video ID, skipping")
                return None
            
            title = entry.get('title', '').strip()
            url = entry.get('link', f"https://www.youtube.com/watch?v={video_id}")
            
            # Extract published date
            published_parsed = entry.get('published_parsed') or entry.get('updated_parsed')
            if published_parsed and len(published_parsed) >= 6:
                published = datetime(*published_parsed[:6], tzinfo=timezone.utc).isoformat()
            else:
                published = entry.get('published', entry.get('updated', now_iso()))
            
            # Extract description/summary
            description = entry.get('summary', '').strip()
            
            # Extract thumbnail URL
            thumbnail = ''
            if 'media_thumbnail' in entry and entry.media_thumbnail:
                thumbnail = entry.media_thumbnail[0].get('url', '')
            
            # Extract channel info
            channel_name = entry.get('author', 'Unknown')
            channel_id = entry.get('yt_channelid', '')
            
            return {
                'video_id': video_id,
                'title': title,
                'url': url,
                'thumbnail': thumbnail,
                'published': published,
                'channel_name': channel_name,
                'channel_id': channel_id,
                'description': description,
                'source': source
            }
        
        elif source == "api":
            # Parse API response
            snippet = entry.get('snippet', {})
            content_details = entry.get('contentDetails', {})
            statistics = entry.get('statistics', {})
            
            video_id = entry.get('id', '')
            if isinstance(video_id, dict):
                video_id = video_id.get('videoId', '')
            
            if not video_id:
                logger.warning("API entry missing video ID, skipping")
                return None
            
            # Extract published date (handle timezone)
            published_at = snippet.get('publishedAt', '')
            # YouTube API always returns ISO 8601 with Z or timezone offset
            # No need to modify it
            
            return {
                'video_id': video_id,
                'title': snippet.get('title', '').strip(),
                'url': f"https://www.youtube.com/watch?v={video_id}",
                'thumbnail': snippet.get('thumbnails', {}).get('high', {}).get('url', ''),
                'published': published_at or now_iso(),
                'channel_name': snippet.get('channelTitle', 'Unknown'),
                'channel_id': snippet.get('channelId', ''),
                'description': snippet.get('description', '').strip(),
                'duration': content_details.get('duration', ''),
                'view_count': int(statistics.get('viewCount', 0)) if 'viewCount' in statistics else None,
                'source': source
            }
        
        else:
            logger.error(f"Unknown source: {source}")
            return None
    
    except Exception as e:
        logger.error(f"Error parsing video entry: {e}")
        return None


# ============================================================================
# YouTube Data API v3 Functions (Optional)
# ============================================================================

def fetch_videos_api(channel_id: str, max_results: int = 50) -> List[dict]:
    """
    Fetch videos using YouTube Data API v3 (fallback/enrichment).
    
    Requires YOUTUBE_API_KEY environment variable.
    Uses quota: search().list costs 100 units, videos().list costs 1 unit per video.
    
    Args:
        channel_id: YouTube channel ID
        max_results: Maximum number of results to fetch (default: 50)
        
    Returns:
        List of video dictionaries with enhanced metadata
    """
    if not YOUTUBE_API_AVAILABLE:
        logger.warning("YouTube API client not available. Install google-api-python-client.")
        return []
    
    api_key = os.getenv('YOUTUBE_API_KEY')
    if not api_key:
        logger.info("YOUTUBE_API_KEY not set, skipping API enrichment")
        return []
    
    try:
        youtube = build('youtube', 'v3', developerKey=api_key)
        
        logger.info(f"Fetching videos from YouTube API for channel {channel_id}")
        
        # Search for videos from this channel
        search_response = youtube.search().list(
            channelId=channel_id,
            part='id,snippet',
            type='video',
            order='date',
            maxResults=min(max_results, 50)  # API max is 50 per request
        ).execute()
        
        video_ids = [item['id']['videoId'] for item in search_response.get('items', [])]
        
        if not video_ids:
            logger.warning("No videos found via API")
            return []
        
        logger.info(f"Found {len(video_ids)} video IDs, fetching details...")
        
        # Fetch detailed video information
        videos_response = youtube.videos().list(
            id=','.join(video_ids),
            part='snippet,contentDetails,statistics'
        ).execute()
        
        videos = []
        for item in videos_response.get('items', []):
            try:
                video = parse_video_entry(item, source="api")
                if video:
                    videos.append(video)
            except Exception as e:
                logger.error(f"Failed to parse API video entry: {e}")
                continue
        
        logger.info(f"Successfully fetched {len(videos)} videos from API")
        return videos
    
    except HttpError as e:
        if e.resp.status == 403:
            logger.error("YouTube API quota exceeded or invalid API key")
        else:
            logger.error(f"YouTube API error: {e}")
        return []
    
    except Exception as e:
        logger.error(f"Failed to fetch videos from API: {e}")
        return []


def enrich_with_api_data(videos: List[dict]) -> List[dict]:
    """
    Optionally enrich RSS data with API data (duration, views).
    
    Takes videos fetched from RSS and adds duration/view count from API.
    
    Args:
        videos: List of video dictionaries from RSS
        
    Returns:
        List of enriched video dictionaries
    """
    if not YOUTUBE_API_AVAILABLE:
        logger.debug("YouTube API not available for enrichment")
        return videos
    
    api_key = os.getenv('YOUTUBE_API_KEY')
    if not api_key:
        logger.debug("YOUTUBE_API_KEY not set, skipping enrichment")
        return videos
    
    if not videos:
        return videos
    
    try:
        youtube = build('youtube', 'v3', developerKey=api_key)
        
        # Get video IDs from videos
        video_ids = [v['video_id'] for v in videos if 'video_id' in v]
        
        if not video_ids:
            return videos
        
        logger.info(f"Enriching {len(video_ids)} videos with API data...")
        
        # Fetch video details in batches (API accepts up to 50 IDs)
        batch_size = 50
        enriched_data = {}
        
        for i in range(0, len(video_ids), batch_size):
            batch = video_ids[i:i + batch_size]
            
            videos_response = youtube.videos().list(
                id=','.join(batch),
                part='contentDetails,statistics'
            ).execute()
            
            for item in videos_response.get('items', []):
                video_id = item['id']
                content_details = item.get('contentDetails', {})
                statistics = item.get('statistics', {})
                
                enriched_data[video_id] = {
                    'duration': content_details.get('duration', ''),
                    'view_count': int(statistics.get('viewCount', 0)) if 'viewCount' in statistics else None
                }
        
        # Apply enrichment to videos
        enriched_videos = []
        for video in videos:
            video_id = video.get('video_id')
            if video_id in enriched_data:
                video.update(enriched_data[video_id])
            enriched_videos.append(video)
        
        logger.info(f"Successfully enriched {len(enriched_data)} videos")
        return enriched_videos
    
    except HttpError as e:
        if e.resp.status == 403:
            logger.warning("YouTube API quota exceeded, skipping enrichment")
        else:
            logger.warning(f"YouTube API error during enrichment: {e}")
        return videos
    
    except Exception as e:
        logger.warning(f"Failed to enrich videos: {e}")
        return videos


# ============================================================================
# Filtering Functions
# ============================================================================

def filter_copilot_videos(videos: List[dict]) -> List[dict]:
    """
    Filter videos by Copilot-related keywords in title/description.
    
    Args:
        videos: List of video dictionaries
        
    Returns:
        Filtered list of Copilot-related videos
    """
    config = load_config()
    keywords = config.get('filters', {}).get('keywords', ['copilot', 'ai', 'agent'])
    
    filtered = []
    
    for video in videos:
        # Combine title and description for searching
        text = f"{video.get('title', '')} {video.get('description', '')}".lower()
        
        # Check if any keyword is present
        if any(keyword.lower() in text for keyword in keywords):
            filtered.append(video)
    
    logger.info(f"Filtered to {len(filtered)} Copilot-related videos from {len(videos)} total")
    return filtered


def filter_by_age(videos: List[dict], max_days: int) -> List[dict]:
    """
    Filter out videos older than max_days.
    
    Args:
        videos: List of video dictionaries
        max_days: Maximum age in days
        
    Returns:
        Filtered list of recent videos
    """
    if max_days <= 0:
        return videos
    
    filtered = []
    cutoff_date = datetime.now(timezone.utc) - timedelta(days=max_days)
    
    for video in videos:
        try:
            published = video.get('published', '')
            if not published:
                continue
            
            video_date = parse_iso(published)
            if video_date >= cutoff_date:
                filtered.append(video)
        except Exception as e:
            logger.warning(f"Failed to parse date for video {video.get('video_id', 'unknown')}: {e}")
            # Include video if we can't parse date
            filtered.append(video)
    
    logger.info(f"Filtered by age ({max_days} days): {len(filtered)} videos from {len(videos)} total")
    return filtered


# ============================================================================
# Save Functions
# ============================================================================

def save_videos(videos: List[dict], dry_run: bool = False) -> int:
    """
    Save videos to data/videos/ as YYYY-MM-DD_{video_id}.json.
    
    Uses add_video_id() from metadata.py to prevent duplicates.
    
    Args:
        videos: List of video dictionaries to save
        dry_run: If True, only print what would be saved without writing files
        
    Returns:
        Count of new videos saved (or would be saved in dry-run mode)
    """
    # Ensure output directory exists
    if not dry_run:
        ensure_directory(str(DATA_DIR))
    
    new_count = 0
    duplicate_count = 0
    
    for video in videos:
        video_id = video.get('video_id')
        
        if not video_id:
            logger.warning("Video missing video_id, skipping")
            continue
        
        # Check if already processed (skip duplicate check in dry-run to show all potential saves)
        if not dry_run and not add_video_id(video_id):
            duplicate_count += 1
            logger.debug(f"Skipping duplicate video: {video_id}")
            continue
        
        # Extract date from published field
        try:
            published = video.get('published', '')
            if published:
                # Parse ISO date
                dt = parse_iso(published)
                date_part = dt.strftime('%Y-%m-%d')
            else:
                date_part = datetime.now(timezone.utc).strftime('%Y-%m-%d')
        except Exception as e:
            logger.warning(f"Failed to parse date for video {video_id}, using current date: {e}")
            date_part = datetime.now(timezone.utc).strftime('%Y-%m-%d')
        
        # Create filename
        filename = f"{date_part}_{video_id}.json"
        filepath = DATA_DIR / filename
        
        # Avoid filename collisions (shouldn't happen with video_id, but just in case)
        counter = 1
        while filepath.exists() and not dry_run:
            filename = f"{date_part}_{video_id}_{counter}.json"
            filepath = DATA_DIR / filename
            counter += 1
        
        # Add scraped timestamp
        video['scraped_at'] = now_iso()
        
        if dry_run:
            # In dry-run mode, just log what would be saved
            logger.info(f"[DRY-RUN] Would save: {filename}")
            logger.info(f"  Title: {video.get('title', 'N/A')}")
            logger.info(f"  Published: {video.get('published', 'N/A')}")
            new_count += 1
        else:
            # Write video data
            try:
                video_json = json.dumps(video, indent=2, ensure_ascii=False)
                if safe_write_file(str(filepath), video_json):
                    logger.info(f"Saved: {filename}")
                    new_count += 1
                else:
                    logger.error(f"Failed to save: {filename}")
            except Exception as e:
                logger.error(f"Error saving video {filename}: {e}")
                continue
    
    if not dry_run and duplicate_count > 0:
        logger.info(f"{duplicate_count} duplicates skipped")
    
    return new_count


# ============================================================================
# Main Entry Point
# ============================================================================

def parse_arguments():
    """
    Parse command-line arguments.
    
    Returns:
        argparse.Namespace: Parsed arguments
    """
    parser = argparse.ArgumentParser(
        description='Fetch videos from YouTube channels using RSS feeds',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Run with defaults (30 days, no keyword filter)
  python scraper/fetch_youtube.py
  
  # Dry-run to see what would be saved
  python scraper/fetch_youtube.py --dry-run
  
  # Fetch videos from last 7 days
  python scraper/fetch_youtube.py --max-age-days 7
  
  # Enable keyword filtering
  python scraper/fetch_youtube.py --require-keywords
  
  # Combine flags
  python scraper/fetch_youtube.py --max-age-days 14 --require-keywords --dry-run
        """
    )
    
    parser.add_argument(
        '--max-age-days',
        type=int,
        help='Maximum age of videos in days (overrides config)'
    )
    
    # Create mutually exclusive group for keyword filtering
    keyword_group = parser.add_mutually_exclusive_group()
    keyword_group.add_argument(
        '--require-keywords',
        action='store_true',
        help='Require keyword matches in title/description (overrides config)'
    )
    
    keyword_group.add_argument(
        '--no-require-keywords',
        action='store_true',
        help='Disable keyword filtering (overrides config)'
    )
    
    parser.add_argument(
        '--dry-run',
        action='store_true',
        help='Show what would be saved without actually saving files'
    )
    
    return parser.parse_args()


def main():
    """
    Main entry point for YouTube scraper.
    
    Fetches videos from enabled channels, filters by age and optionally by keywords,
    optionally enriches with API data, saves new videos, and reports statistics.
    """
    # Parse command-line arguments
    args = parse_arguments()
    
    logger.info("Starting YouTube video scraper...")
    logger.info(f"Loading config from {CONFIG_FILE}")
    
    if args.dry_run:
        logger.info("[DRY-RUN MODE] No files will be written")
    
    try:
        config = load_config()
    except Exception as e:
        logger.error(f"Failed to load config: {e}")
        return 1
    
    # Get enabled channels
    channels = config.get('channels', [])
    enabled_channels = [ch for ch in channels if ch.get('enabled', False)]
    
    if not enabled_channels:
        logger.warning("No enabled channels found in config")
        return 0
    
    logger.info(f"Found {len(enabled_channels)} enabled channel(s)")
    
    # Get filter settings
    filters = config.get('filters', {})
    
    # Override config with CLI arguments
    if args.max_age_days is not None:
        max_age_days = args.max_age_days
        logger.info(f"Using max_age_days from CLI: {max_age_days}")
    else:
        max_age_days = filters.get('max_age_days', 30)
        logger.info(f"Using max_age_days from config: {max_age_days}")
    
    # Determine if keyword filtering should be applied
    if args.require_keywords:
        require_keywords = True
        logger.info("Keyword filtering enabled (from CLI)")
    elif args.no_require_keywords:
        require_keywords = False
        logger.info("Keyword filtering disabled (from CLI)")
    else:
        require_keywords = filters.get('require_keywords', False)
        logger.info(f"Keyword filtering from config: {'enabled' if require_keywords else 'disabled'}")
    
    # Get API settings
    api_config = config.get('api', {})
    api_enabled = api_config.get('enabled', False)
    
    # Fetch videos from all enabled channels
    all_videos = []
    
    for channel in enabled_channels:
        channel_id = channel.get('id')
        channel_name = channel.get('name', 'Unknown')
        
        logger.info(f"Processing channel: {channel_name} ({channel_id})")
        
        # Fetch from RSS (primary method)
        videos = fetch_videos_rss(channel_id)
        
        if videos:
            all_videos.extend(videos)
            logger.info(f"Fetched {len(videos)} videos from {channel_name} (RSS)")
        else:
            logger.warning(f"No videos fetched from {channel_name} via RSS")
            
            # Fallback to API if enabled and RSS failed
            if api_enabled and YOUTUBE_API_AVAILABLE:
                logger.info(f"Trying API fallback for {channel_name}...")
                videos = fetch_videos_api(channel_id)
                if videos:
                    all_videos.extend(videos)
                    logger.info(f"Fetched {len(videos)} videos from {channel_name} (API)")
    
    if not all_videos:
        logger.warning("No videos fetched from any channel")
        return 0
    
    logger.info(f"Total videos fetched: {len(all_videos)}")
    
    # Filter by age
    all_videos = filter_by_age(all_videos, max_age_days)
    
    if not all_videos:
        logger.warning(f"No videos remaining after age filter ({max_age_days} days)")
        return 0
    
    # Optionally filter by keywords
    if require_keywords:
        all_videos = filter_copilot_videos(all_videos)
        if not all_videos:
            logger.warning("No videos remaining after keyword filtering")
            return 0
    else:
        logger.info(f"Skipping keyword filter, keeping all {len(all_videos)} videos")
    
    # Optional: Enrich with API data if enabled and videos came from RSS
    if api_enabled and any(v.get('source') == 'rss' for v in all_videos):
        logger.info("API enrichment enabled, adding duration and view counts...")
        all_videos = enrich_with_api_data(all_videos)
    
    # Check for duplicates
    logger.info("Checking for duplicates...")
    
    # Save videos (or show what would be saved in dry-run mode)
    new_count = save_videos(all_videos, dry_run=args.dry_run)
    
    # Report results
    if args.dry_run:
        logger.info(f"[DRY-RUN] Would save {new_count} new videos")
        logger.info(f"[DRY-RUN] Would save to {DATA_DIR}")
    else:
        logger.info(f"Scraping complete: {new_count} new videos saved")
        logger.info(f"Saved to {DATA_DIR}")
        logger.info("Updated metadata.json")
    
    # Print summary of new videos
    if new_count > 0:
        logger.info("\nVideos to be saved:" if args.dry_run else "\nNew videos:")
        
        # Sort videos by published date
        sorted_videos = sorted(
            all_videos,
            key=lambda x: x.get('published', ''),
            reverse=True
        )
        
        for video in sorted_videos[:10]:  # Show up to 10 most recent
            try:
                published = video.get('published', '')
                if published:
                    dt = parse_iso(published)
                    date_str = dt.strftime('%b %d, %Y')
                else:
                    date_str = 'Unknown date'
                
                logger.info(f'  - "{video.get("title", "Untitled")}" ({date_str})')
            except Exception as e:
                logger.warning(f"Failed to format video info: {e}")
    
    return 0


if __name__ == "__main__":
    try:
        exit_code = main()
        sys.exit(exit_code)
    except KeyboardInterrupt:
        logger.info("Interrupted by user")
        sys.exit(130)
    except Exception as e:
        logger.error(f"Unexpected error: {e}", exc_info=True)
        sys.exit(1)
