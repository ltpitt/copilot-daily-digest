"""
Enrich blog post metadata with publish dates.

This script:
1. Extracts dates from changelog URLs (format: /changelog/YYYY-MM-DD-)
2. Fetches dates from RSS feeds for blog posts without dates in URLs
3. Stores enriched metadata in data/blog/ directory
"""

import json
import logging
import re
import sys
from datetime import datetime
from pathlib import Path
from typing import Dict, Optional

import certifi
import feedparser
import requests


# Configure logging
logging.basicConfig(level=logging.INFO, format="[%(levelname)s] %(message)s")
logger = logging.getLogger(__name__)

# Base paths
REPO_ROOT = Path(__file__).parent.parent
DATA_DIR = REPO_ROOT / "data"
BLOG_DIR = DATA_DIR / "blog"
METADATA_FILE = DATA_DIR / "metadata.json"

# RSS Feed URLs
GITHUB_BLOG_FEED = "https://github.blog/tag/github-copilot/feed/"
GITHUB_CHANGELOG_FEED = "https://github.blog/changelog/feed/"


def extract_date_from_changelog_url(url: str) -> Optional[str]:
    """
    Extract date from changelog URL.

    Args:
        url: URL like https://github.blog/changelog/2025-12-08-some-title

    Returns:
        ISO date string (YYYY-MM-DD) or None
    """
    match = re.search(r"/changelog/(\d{4}-\d{2}-\d{2})-", url)
    if match:
        return match.group(1)
    return None


def fetch_post_date_from_rss(url: str) -> Optional[str]:
    """
    Fetch publish date for a blog post from RSS feed.

    Args:
        url: Blog post URL

    Returns:
        ISO date string (YYYY-MM-DD) or None
    """
    logger.info(f"Fetching date from RSS for: {url}")

    # Try both feeds
    for feed_url in [GITHUB_BLOG_FEED, GITHUB_CHANGELOG_FEED]:
        try:
            response = requests.get(feed_url, timeout=30, verify=certifi.where())
            response.raise_for_status()
            feed = feedparser.parse(response.content)

            for entry in feed.entries:
                entry_url = entry.get("link", "").strip()
                if entry_url == url or entry_url.rstrip("/") == url.rstrip("/"):
                    # Found the entry, extract date
                    published_parsed = entry.get("published_parsed") or entry.get("updated_parsed")
                    if published_parsed:
                        date = datetime(*published_parsed[:6])
                        return date.strftime("%Y-%m-%d")

        except Exception as e:
            logger.debug(f"Error fetching from {feed_url}: {e}")
            continue

    logger.warning(f"Could not find date for {url}")
    return None


def enrich_metadata() -> Dict[str, str]:
    """
    Enrich blog URLs with publish dates.

    Returns:
        Dictionary mapping URL -> ISO date string (YYYY-MM-DD)
    """
    # Load metadata
    if not METADATA_FILE.exists():
        logger.error(f"Metadata file not found: {METADATA_FILE}")
        return {}

    with open(METADATA_FILE) as f:
        metadata = json.load(f)

    blog_urls = metadata.get("blog_urls", [])
    logger.info(f"Processing {len(blog_urls)} blog URLs")

    url_to_date = {}

    for url in blog_urls:
        # Try extracting from URL first (for changelog entries)
        date = extract_date_from_changelog_url(url)

        if date:
            logger.info(f"Extracted date from URL: {date} -> {url}")
        else:
            # Fetch from RSS feed
            date = fetch_post_date_from_rss(url)
            if date:
                logger.info(f"Fetched date from RSS: {date} -> {url}")

        if date:
            url_to_date[url] = date
        else:
            logger.warning(f"No date found for: {url}")

    return url_to_date


def save_enriched_metadata(url_to_date: Dict[str, str]):
    """
    Save enriched metadata to blog directory.

    Args:
        url_to_date: Dictionary mapping URL -> ISO date string
    """
    BLOG_DIR.mkdir(parents=True, exist_ok=True)

    # Create enriched metadata file
    enriched_file = BLOG_DIR / "url_dates.json"

    enriched_data = {
        "generated_at": datetime.utcnow().isoformat() + "Z",
        "url_dates": url_to_date,
        "total_urls": len(url_to_date),
    }

    with open(enriched_file, "w") as f:
        json.dump(enriched_data, f, indent=2, sort_keys=True)

    logger.info(f"Saved enriched metadata to {enriched_file}")
    logger.info(f"Total URLs with dates: {len(url_to_date)}")


def main():
    """Main entry point."""
    logger.info("Starting blog date enrichment...")

    # Enrich metadata
    url_to_date = enrich_metadata()

    if not url_to_date:
        logger.error("No dates extracted, aborting")
        sys.exit(1)

    # Save enriched metadata
    save_enriched_metadata(url_to_date)

    logger.info("Blog date enrichment completed successfully")


if __name__ == "__main__":
    main()
