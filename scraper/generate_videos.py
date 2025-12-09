"""
Video Content Page Generator

Generates content/videos.md from video JSON files in data/videos/.
Organizes videos by category, highlights recent content, and creates
a browseable catalog with statistics.
"""

import json
import logging
import os
import re
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Dict, List, Optional


# Add parent directory to path to import local modules
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from scraper.utils import ensure_directory, format_human_date, parse_iso, safe_write_file


logging.basicConfig(level=logging.INFO, format="[%(levelname)s] %(message)s")
logger = logging.getLogger(__name__)


# ============================================================================
# Configuration
# ============================================================================

DATA_DIR = Path(__file__).parent.parent / "data" / "videos"
OUTPUT_FILE = Path(__file__).parent.parent / "content" / "videos.md"

# Category keywords for video classification
CATEGORIES = {
    "Getting Started": [
        "getting started",
        "intro",
        "introduction",
        "basics",
        "beginner",
        "first steps",
    ],
    "Features": ["feature", "new feature", "announcement", "release", "introducing"],
    "Tutorials": ["tutorial", "how to", "guide", "walkthrough", "demo", "learn"],
    "Updates": ["update", "changelog", "what's new", "improvements", "version"],
    "Extensions": ["extension", "plugin", "integrate", "integration", "api", "vscode", "jetbrains"],
    "Agents": ["agent", "coding agent", "workspace agent", "autonomous", "multi-file", "agentic"],
    "Other": [],  # Catch-all
}


# ============================================================================
# Core Functions
# ============================================================================


def load_all_videos() -> List[dict]:
    """
    Load all video metadata from data/videos/ directory.

    Reads all JSON files matching pattern: YYYY-MM-DD_{video_id}.json

    Returns:
        List of video dictionaries with metadata
    """
    videos = []

    if not DATA_DIR.exists():
        logger.warning(f"Videos directory not found: {DATA_DIR}")
        return videos

    # Find all JSON files
    json_files = list(DATA_DIR.glob("*.json"))

    if not json_files:
        logger.warning(f"No video JSON files found in {DATA_DIR}")
        return videos

    logger.info(f"Found {len(json_files)} video files")

    for json_file in json_files:
        try:
            with open(json_file, encoding="utf-8") as f:
                video = json.load(f)

            # Validate required fields
            if not video.get("video_id"):
                logger.warning(f"Skipping {json_file.name}: missing video_id")
                continue

            videos.append(video)

        except json.JSONDecodeError as e:
            logger.error(f"Failed to parse JSON in {json_file.name}: {e}")
            continue
        except Exception as e:
            logger.error(f"Error loading {json_file.name}: {e}")
            continue

    logger.info(f"Successfully loaded {len(videos)} videos")
    return videos


def categorize_videos(videos: List[dict]) -> Dict[str, List[dict]]:
    """
    Categorize videos by topic based on title/description keywords.

    Each video is assigned to the first matching category based on keyword matches.
    Videos that don't match any category go to "Other".

    Args:
        videos: List of video dictionaries

    Returns:
        Dictionary mapping category names to lists of videos
    """
    categorized = {category: [] for category in CATEGORIES}

    for video in videos:
        # Combine title and description for keyword matching
        title = video.get("title", "").lower()
        description = video.get("description", "").lower()
        text = f"{title} {description}"

        # Find first matching category
        assigned = False
        for category, keywords in CATEGORIES.items():
            if category == "Other":
                continue  # Skip catch-all for now

            # Check if any keyword matches
            if any(keyword.lower() in text for keyword in keywords):
                categorized[category].append(video)
                assigned = True
                break

        # If no category matched, assign to "Other"
        if not assigned:
            categorized["Other"].append(video)

    # Log category distribution
    for category, videos_list in categorized.items():
        if videos_list:
            logger.info(f"Category '{category}': {len(videos_list)} videos")

    return categorized


def get_recent_videos(videos: List[dict], days: int = 7) -> List[dict]:
    """
    Get videos published in the last N days.

    Args:
        videos: List of video dictionaries
        days: Number of days to look back (default: 7)

    Returns:
        List of recent videos, sorted by date (newest first)
    """
    cutoff_date = datetime.now(timezone.utc) - timedelta(days=days)
    recent = []

    for video in videos:
        try:
            published = video.get("published")
            if not published:
                continue

            video_date = parse_iso(published)
            if video_date >= cutoff_date:
                recent.append(video)
        except Exception as e:
            logger.warning(
                f"Failed to parse date for video {video.get('video_id', 'unknown')}: {e}"
            )
            continue

    # Sort by published date, newest first
    recent.sort(key=lambda v: v.get("published", ""), reverse=True)

    logger.info(f"Found {len(recent)} videos from last {days} days")
    return recent


def format_duration(duration: str) -> str:
    """
    Format ISO 8601 duration (PT1H2M3S) to human-readable format.

    Args:
        duration: ISO 8601 duration string (e.g., 'PT12M34S')

    Returns:
        Human-readable duration (e.g., '12:34')
    """
    if not duration:
        return "N/A"

    try:
        # Parse PT format (e.g., PT1H2M3S)
        match = re.match(r"PT(?:(\d+)H)?(?:(\d+)M)?(?:(\d+)S)?", duration)
        if not match:
            return duration

        hours, minutes, seconds = match.groups()
        hours = int(hours) if hours else 0
        minutes = int(minutes) if minutes else 0
        seconds = int(seconds) if seconds else 0

        if hours > 0:
            return f"{hours}:{minutes:02d}:{seconds:02d}"
        return f"{minutes}:{seconds:02d}"
    except Exception:
        return duration


def format_view_count(count: Optional[int]) -> str:
    """
    Format view count with K/M suffix.

    Args:
        count: View count as integer

    Returns:
        Formatted string (e.g., '1.2K views', '3.4M views')
    """
    if count is None:
        return "N/A"

    if count >= 1_000_000:
        return f"{count / 1_000_000:.1f}M views"
    if count >= 1_000:
        return f"{count / 1_000:.1f}K views"
    return f"{count} views"


def format_video_entry(video: dict) -> str:
    """
    Format video as markdown entry with thumbnail and metadata.

    Creates a consistent video card format with:
    - Title (linked to YouTube)
    - Clickable thumbnail
    - Metadata line (date, duration, channel)
    - Description snippet
    - Watch link

    Args:
        video: Video dictionary with metadata

    Returns:
        Markdown-formatted video entry
    """
    video_id = video.get("video_id", "")
    title = video.get("title", "Untitled Video")
    url = video.get("url", f"https://www.youtube.com/watch?v={video_id}")
    thumbnail = video.get("thumbnail", "")

    # If no thumbnail, construct default
    if not thumbnail and video_id:
        thumbnail = f"https://i.ytimg.com/vi/{video_id}/mqdefault.jpg"

    # Format published date
    published = video.get("published", "")
    try:
        date_str = format_human_date(published) if published else "Unknown date"
    except Exception:
        date_str = "Unknown date"

    # Format duration
    duration = video.get("duration", "")
    duration_str = format_duration(duration)

    # Channel name
    channel_name = video.get("channel_name", "GitHub")

    # View count (if available)
    view_count = video.get("view_count")
    views_str = format_view_count(view_count)

    # Description (truncated)
    description = video.get("description", "").strip()
    if description:
        # Truncate to ~200 chars
        if len(description) > 200:
            description = description[:197] + "..."
        # Remove newlines
        description = " ".join(description.split())
    else:
        description = "No description available."

    # Build markdown entry
    entry = f"### [{title}]({url})\n\n"

    # Add thumbnail if available
    if thumbnail:
        entry += f"[![{title}]({thumbnail})]({url})\n\n"

    # Metadata line
    metadata_parts = [f"**Published**: {date_str}"]
    if duration_str != "N/A":
        metadata_parts.append(f"**Duration**: {duration_str}")
    if views_str != "N/A":
        metadata_parts.append(f"**Views**: {views_str}")
    metadata_parts.append(f"**Channel**: {channel_name}")

    entry += " | ".join(metadata_parts) + "\n\n"

    # Description
    entry += f"{description}\n\n"

    # Watch link
    entry += f"[Watch on YouTube →]({url})\n\n"
    entry += "---\n\n"

    return entry


def generate_videos_page(videos: List[dict]) -> str:
    """
    Generate complete videos.md content.

    Creates a comprehensive video catalog page with:
    - Header with statistics
    - What's New section (last 7 days)
    - Browse by Category section
    - Category sections with videos
    - Statistics footer

    Args:
        videos: List of all video dictionaries

    Returns:
        Complete markdown content for videos.md
    """
    # Generate timestamp
    now = datetime.now(timezone.utc)
    timestamp = now.strftime("%B %d, %Y at %H:%M UTC")

    # Calculate statistics
    total_count = len(videos)
    recent_videos = get_recent_videos(videos, days=7)
    recent_count = len(recent_videos)

    # Categorize videos
    categorized = categorize_videos(videos)

    # Sort videos by date within each category (newest first)
    for category in categorized:
        categorized[category].sort(key=lambda v: v.get("published", ""), reverse=True)

    # Start building the page
    content = "# 🎥 GitHub Copilot Video Library\n\n"
    content += f"> **Last Updated**: {timestamp}\n\n"
    content += f"**Total Videos**: {total_count} | "
    content += f"**New This Week**: {recent_count}\n\n"
    content += "---\n\n"

    # Table of Contents
    content += "## 📋 Table of Contents\n\n"
    content += "- [What's New This Week](#whats-new-this-week)\n"
    content += "- [Browse by Category](#browse-by-category)\n"
    for category in CATEGORIES:
        count = len(categorized[category])
        if count > 0:
            slug = category.lower().replace(" ", "-")
            content += f"  - [{category}](#-{slug}) ({count})\n"
    content += "- [Statistics](#statistics)\n\n"
    content += "---\n\n"

    # What's New This Week section
    content += "## 🆕 What's New This Week\n\n"

    if recent_videos:
        content += "*Videos published in the last 7 days*\n\n"
        for video in recent_videos:
            content += format_video_entry(video)
    else:
        content += "*No new videos this week. Check back soon!*\n\n"
        content += "---\n\n"

    # Browse by Category section
    content += "## 📂 Browse by Category\n\n"
    content += "Videos are organized by topic for easy navigation:\n\n"

    for category, keywords in CATEGORIES.items():
        count = len(categorized[category])
        slug = category.lower().replace(" ", "-")

        if count > 0:
            # Add emoji based on category
            emoji = {
                "Getting Started": "🎓",
                "Features": "✨",
                "Tutorials": "📚",
                "Updates": "🔄",
                "Extensions": "🔌",
                "Agents": "🤖",
                "Other": "📦",
            }.get(category, "📦")

            content += (
                f"- [{emoji} {category}](#-{slug}) - {count} video{'s' if count != 1 else ''}\n"
            )

    content += "\n---\n\n"

    # Category sections
    for category in CATEGORIES:
        videos_list = categorized[category]

        if not videos_list:
            continue

        # Category header with emoji
        emoji = {
            "Getting Started": "🎓",
            "Features": "✨",
            "Tutorials": "📚",
            "Updates": "🔄",
            "Extensions": "🔌",
            "Agents": "🤖",
            "Other": "📦",
        }.get(category, "📦")

        slug = category.lower().replace(" ", "-")
        content += f"## {emoji} {category}\n\n"

        # Category description
        descriptions = {
            "Getting Started": "New to GitHub Copilot? Start here with introductory content and beginner-friendly guides.",
            "Features": "Discover new features, product announcements, and capability releases.",
            "Tutorials": "Step-by-step guides and walkthroughs to help you master Copilot.",
            "Updates": "Stay current with the latest updates, improvements, and changelogs.",
            "Extensions": "Learn about extensions, integrations, and API capabilities.",
            "Agents": "Explore autonomous coding agents and advanced AI-powered workflows.",
            "Other": "Additional content and resources that don't fit into other categories.",
        }

        content += f"*{descriptions.get(category, '')}*\n\n"
        content += f"**{len(videos_list)} video{'s' if len(videos_list) != 1 else ''}**\n\n"

        # Videos in this category
        for video in videos_list:
            content += format_video_entry(video)

        content += "\n"

    # Statistics section
    content += "---\n\n"
    content += "## 📊 Statistics\n\n"
    content += f"- **Total Videos**: {total_count}\n"
    content += f"- **New This Week**: {recent_count}\n"

    # Category breakdown
    content += "- **By Category**:\n"
    for category in CATEGORIES:
        count = len(categorized[category])
        if count > 0:
            content += f"  - {category}: {count}\n"

    # Most recent video
    if videos:
        all_sorted = sorted(videos, key=lambda v: v.get("published", ""), reverse=True)
        most_recent = all_sorted[0]
        try:
            recent_date = format_human_date(most_recent.get("published", ""))
            content += f"- **Most Recent**: {most_recent.get('title', 'Unknown')} ({recent_date})\n"
        except Exception:
            pass

    content += "\n---\n\n"

    # Footer
    content += "## 🔗 Quick Links\n\n"
    content += "- [GitHub Copilot Documentation](https://docs.github.com/en/copilot)\n"
    content += "- [GitHub Blog](https://github.blog/tag/github-copilot/)\n"
    content += "- [GitHub YouTube Channel](https://www.youtube.com/github)\n"
    content += "- [Back to Digest Home](README.md)\n\n"
    content += "---\n\n"
    content += f"*Generated on {timestamp}*\n"

    return content


# ============================================================================
# Main Entry Point
# ============================================================================


def main():
    """
    Main entry point for video page generator.

    Loads all videos, categorizes them, and generates content/videos.md.
    """
    logger.info("Starting video page generation...")

    try:
        # Load all videos
        videos = load_all_videos()

        if not videos:
            logger.warning("No videos found, generating empty page")
            # Still generate a page, just with no content

        # Generate page content
        logger.info("Generating videos.md content...")
        content = generate_videos_page(videos)

        # Ensure output directory exists
        ensure_directory(str(OUTPUT_FILE.parent))

        # Write to file
        if safe_write_file(str(OUTPUT_FILE), content):
            logger.info(f"Successfully generated: {OUTPUT_FILE}")
            logger.info(f"Total videos: {len(videos)}")

            # Show recent videos
            recent = get_recent_videos(videos, days=7)
            if recent:
                logger.info(f"New this week: {len(recent)}")

            return 0
        logger.error(f"Failed to write output file: {OUTPUT_FILE}")
        return 1

    except Exception as e:
        logger.error(f"Error generating video page: {e}", exc_info=True)
        return 1


if __name__ == "__main__":
    try:
        sys.exit(main())
    except KeyboardInterrupt:
        logger.info("Interrupted by user")
        sys.exit(130)
    except Exception as e:
        logger.error(f"Unexpected error: {e}", exc_info=True)
        sys.exit(1)
