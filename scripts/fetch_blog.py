"""
GitHub Blog RSS Feed Scraper

Fetches GitHub Blog posts and Changelog entries about Copilot using RSS feeds.
Stores raw data and prevents duplicates using metadata tracking.
"""

import json
import logging
import os
import re
import sys
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional

import certifi
import feedparser
import requests


# Add parent directory to path to import local modules
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

try:
    from scraper.metadata import add_blog_url, load_metadata
    from scraper.utils import ensure_dir, safe_write_file
except ImportError:
    # Fallback implementations if modules don't exist yet
    def add_blog_url(url: str) -> bool:
        """Fallback: Add URL to metadata"""
        metadata_file = Path(__file__).parent.parent / "data" / "metadata.json"
        metadata_file.parent.mkdir(parents=True, exist_ok=True)

        if metadata_file.exists():
            with open(metadata_file) as f:
                metadata = json.load(f)
        else:
            metadata = {"blog_urls": [], "youtube_urls": [], "last_updated": None}

        if url in metadata.get("blog_urls", []):
            return False

        metadata.setdefault("blog_urls", []).append(url)
        metadata["last_updated"] = datetime.utcnow().isoformat()

        with open(metadata_file, "w") as f:
            json.dump(metadata, f, indent=2)

        return True

    def load_metadata() -> dict:
        """Fallback: Load metadata"""
        metadata_file = Path(__file__).parent.parent / "data" / "metadata.json"
        if metadata_file.exists():
            with open(metadata_file) as f:
                return json.load(f)
        return {"blog_urls": [], "youtube_urls": [], "last_updated": None}

    def safe_write_file(filepath: Path, content: str) -> bool:
        """Fallback: Safely write file"""
        try:
            filepath.parent.mkdir(parents=True, exist_ok=True)
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(content)
            return True
        except Exception as e:
            logging.error(f"Failed to write file {filepath}: {e}")
            return False

    def ensure_dir(path: Path) -> bool:
        """Fallback: Ensure directory exists"""
        try:
            path.mkdir(parents=True, exist_ok=True)
            return True
        except Exception as e:
            logging.error(f"Failed to create directory {path}: {e}")
            return False


# Configure logging
logging.basicConfig(level=logging.INFO, format="[%(levelname)s] %(message)s")
logger = logging.getLogger(__name__)

# RSS Feed URLs
GITHUB_BLOG_FEED = "https://github.blog/tag/github-copilot/feed/"
GITHUB_CHANGELOG_FEED = "https://github.blog/changelog/feed/"

# Keywords for filtering Copilot-related content
COPILOT_KEYWORDS = ["copilot", "ai", "agent", "coding agent", "workspace agent", "extensions"]

# Base data directory
DATA_DIR = Path(__file__).parent.parent / "data" / "blog"


def fetch_github_blog() -> List[Dict]:
    """
    Fetch GitHub Blog posts about Copilot via RSS.

    Returns:
        List of parsed blog entries
    """
    logger.info("Fetching GitHub Blog RSS feed...")

    try:
        # Use requests to fetch with proper SSL verification
        response = requests.get(GITHUB_BLOG_FEED, timeout=30, verify=certifi.where())
        response.raise_for_status()

        # Parse the fetched content with feedparser
        feed = feedparser.parse(response.content)

        if feed.bozo:
            logger.warning(f"Feed parsing warning: {feed.get('bozo_exception', 'Unknown')}")

        if not feed.entries:
            logger.warning("No entries found in GitHub Blog feed")
            return []

        logger.info(f"Found {len(feed.entries)} entries in GitHub Blog feed")

        entries = []
        for entry in feed.entries:
            try:
                parsed = parse_blog_entry(entry, source="github-blog")
                if parsed:
                    entries.append(parsed)
            except Exception as e:
                logger.error(f"Failed to parse blog entry: {e}")
                continue

        return entries

    except Exception as e:
        logger.error(f"Failed to fetch GitHub Blog RSS feed: {e}")
        return []


def fetch_github_changelog() -> List[Dict]:
    """
    Fetch GitHub Changelog entries via RSS.

    Returns:
        List of parsed changelog entries
    """
    logger.info("Fetching GitHub Changelog RSS feed...")

    try:
        # Use requests to fetch with proper SSL verification
        response = requests.get(GITHUB_CHANGELOG_FEED, timeout=30, verify=certifi.where())
        response.raise_for_status()

        # Parse the fetched content with feedparser
        feed = feedparser.parse(response.content)

        if feed.bozo:
            logger.warning(f"Feed parsing warning: {feed.get('bozo_exception', 'Unknown')}")

        if not feed.entries:
            logger.warning("No entries found in GitHub Changelog feed")
            return []

        logger.info(f"Found {len(feed.entries)} entries in GitHub Changelog feed")

        entries = []
        for entry in feed.entries:
            try:
                parsed = parse_blog_entry(entry, source="github-changelog")
                if parsed:
                    entries.append(parsed)
            except Exception as e:
                logger.error(f"Failed to parse changelog entry: {e}")
                continue

        return entries

    except Exception as e:
        logger.error(f"Failed to fetch GitHub Changelog RSS feed: {e}")
        return []


def parse_blog_entry(entry, source: str = "github-blog") -> Optional[Dict]:
    """
    Parse RSS entry into structured format.

    Args:
        entry: feedparser entry object
        source: Source identifier (github-blog or github-changelog)

    Returns:
        Dictionary with structured blog post data:
        {
            "title": str,
            "url": str,
            "date": str (ISO 8601),
            "summary": str,
            "content": str,
            "tags": list[str],
            "author": str,
            "source": str,
            "scraped_at": str
        }
    """
    try:
        # Extract basic fields
        title = entry.get("title", "").strip()
        url = entry.get("link", "").strip()

        if not title or not url:
            logger.warning("Entry missing title or URL, skipping")
            return None

        # Parse published date
        published_parsed = entry.get("published_parsed") or entry.get("updated_parsed")
        if published_parsed:
            published = datetime(*published_parsed[:6]).isoformat() + "Z"
        else:
            published = entry.get("published", entry.get("updated", ""))

        # Extract summary and content
        summary = entry.get("summary", "").strip()
        content = entry.get("content", [{}])[0].get("value", "") if "content" in entry else summary

        # Extract tags
        tags = []
        if "tags" in entry:
            tags = [tag.get("term", "") for tag in entry.get("tags", []) if tag.get("term")]

        # Extract author
        author = entry.get("author", "Unknown")

        # Create structured data
        post_data = {
            "title": title,
            "url": url,
            "published": published,
            "summary": summary,
            "content": content,
            "tags": tags,
            "author": author,
            "source": source,
            "scraped_at": datetime.utcnow().isoformat() + "Z",
        }

        return post_data

    except Exception as e:
        logger.error(f"Error parsing entry: {e}")
        return None


def filter_copilot_content(entries: List[Dict]) -> List[Dict]:
    """
    Filter entries related to Copilot based on keywords.

    Args:
        entries: List of parsed blog entries

    Returns:
        Filtered list of Copilot-related entries
    """
    filtered = []

    for entry in entries:
        # Check title first (highest priority)
        title_lower = entry.get("title", "").lower()
        if any(keyword.lower() in title_lower for keyword in COPILOT_KEYWORDS):
            filtered.append(entry)
            continue

        # Check content and summary
        content_lower = entry.get("content", "").lower()
        summary_lower = entry.get("summary", "").lower()
        combined_text = f"{content_lower} {summary_lower}"

        if any(keyword.lower() in combined_text for keyword in COPILOT_KEYWORDS):
            filtered.append(entry)
            continue

        # Check tags
        tags_lower = [tag.lower() for tag in entry.get("tags", [])]
        if any(keyword.lower() in tag for keyword in COPILOT_KEYWORDS for tag in tags_lower):
            filtered.append(entry)
            continue

    logger.info(
        f"Filtered to {len(filtered)} Copilot-related posts from {len(entries)} total entries"
    )
    return filtered


def create_slug(title: str) -> str:
    """
    Create a URL-friendly slug from a title.

    Args:
        title: Blog post title

    Returns:
        Slugified title
    """
    # Convert to lowercase
    slug = title.lower()

    # Replace spaces and special characters with hyphens
    slug = re.sub(r"[^\w\s-]", "", slug)
    slug = re.sub(r"[-\s]+", "-", slug)

    # Trim hyphens from ends
    slug = slug.strip("-")

    # Limit length
    slug = slug[:100]

    return slug


def save_blog_posts(posts: List[Dict]) -> int:
    """
    Save blog posts to data/blog/ directory.

    Filename format: YYYY-MM-DD-slug.json

    Args:
        posts: List of blog post dictionaries

    Returns:
        Count of new posts saved
    """
    # Ensure data directory exists
    ensure_dir(DATA_DIR)

    new_count = 0
    duplicate_count = 0

    for post in posts:
        url = post.get("url")

        # Check if already processed
        if not add_blog_url(url):
            duplicate_count += 1
            logger.debug(f"Skipping duplicate: {url}")
            continue

        # Extract date from published field
        try:
            published = post.get("published", "")
            if published:
                # Handle various date formats
                if "T" in published:
                    date_part = published.split("T")[0]
                else:
                    date_part = published[:10]
            else:
                date_part = datetime.utcnow().strftime("%Y-%m-%d")
        except Exception as e:
            logger.warning(f"Failed to parse date, using current date: {e}")
            date_part = datetime.utcnow().strftime("%Y-%m-%d")

        # Create filename
        slug = create_slug(post.get("title", "untitled"))
        filename = f"{date_part}-{slug}.json"
        filepath = DATA_DIR / filename

        # Avoid filename collisions
        counter = 1
        while filepath.exists():
            filename = f"{date_part}-{slug}-{counter}.json"
            filepath = DATA_DIR / filename
            counter += 1

        # Write post data
        try:
            post_json = json.dumps(post, indent=2, ensure_ascii=False)
            if safe_write_file(filepath, post_json):
                logger.info(f"Saved: {filename}")
                new_count += 1
            else:
                logger.error(f"Failed to save: {filename}")
        except Exception as e:
            logger.error(f"Error saving post {filename}: {e}")
            continue

    if duplicate_count > 0:
        logger.info(f"{duplicate_count} duplicates skipped")

    return new_count


def main():
    """
    Main entry point for blog scraper.
    """
    logger.info("Starting GitHub Blog scraper...")

    # Fetch blog posts
    blog_posts = fetch_github_blog()

    # Fetch changelog entries
    changelog_entries = fetch_github_changelog()

    # Combine all entries
    all_entries = blog_posts + changelog_entries

    if not all_entries:
        logger.warning("No entries fetched from any source")
        return 0

    logger.info(f"Total entries fetched: {len(all_entries)}")

    # Filter for Copilot-related content
    copilot_posts = filter_copilot_content(all_entries)

    if not copilot_posts:
        logger.warning("No Copilot-related posts found after filtering")
        return 0

    # Save posts
    new_count = save_blog_posts(copilot_posts)

    logger.info(f"Scraping complete: {new_count} new posts saved")
    logger.info(f"Saved to {DATA_DIR}")
    logger.info("Updated metadata.json")

    return new_count


if __name__ == "__main__":
    try:
        count = main()
        sys.exit(0 if count >= 0 else 1)
    except KeyboardInterrupt:
        logger.info("Interrupted by user")
        sys.exit(130)
    except Exception as e:
        logger.error(f"Unexpected error: {e}", exc_info=True)
        sys.exit(1)
