#!/usr/bin/env python3
"""
GitHub Next Projects Scraper

Fetches experimental projects from GitHub Next (https://githubnext.com/).
This source contains experimental and research projects that may or may not
become official GitHub features.

IMPORTANT: Content from this source should be marked as experimental/research
and not treated as official GitHub roadmap or documentation.
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
import requests
from bs4 import BeautifulSoup
from loguru import logger

# Add parent directory to path to import local modules
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

try:
    from scraper.metadata import add_github_next_url, load_metadata
    from scraper.utils import ensure_dir, safe_write_file
except ImportError:
    # Fallback implementations if modules don't exist yet
    def add_github_next_url(url: str) -> bool:
        """Fallback: Add URL to metadata"""
        metadata_file = Path(__file__).parent.parent / "data" / "metadata.json"
        metadata_file.parent.mkdir(parents=True, exist_ok=True)

        if metadata_file.exists():
            with open(metadata_file) as f:
                metadata = json.load(f)
        else:
            metadata = {
                "blog_urls": [],
                "youtube_urls": [],
                "github_next_urls": [],
                "last_updated": None,
            }

        if url in metadata.get("github_next_urls", []):
            return False

        metadata.setdefault("github_next_urls", []).append(url)
        metadata["last_updated"] = datetime.utcnow().isoformat()

        with open(metadata_file, "w") as f:
            json.dump(metadata, f, indent=2)

        return True

    def load_metadata():
        """Fallback: Load metadata"""
        metadata_file = Path(__file__).parent.parent / "data" / "metadata.json"
        if metadata_file.exists():
            with open(metadata_file) as f:
                return json.load(f)
        return {"github_next_urls": []}

    def ensure_dir(path: Path) -> None:
        """Ensure directory exists"""
        path.mkdir(parents=True, exist_ok=True)

    def safe_write_file(path: Path, content: str) -> None:
        """Write file safely"""
        path.write_text(content)


# GitHub Next base URL
GITHUB_NEXT_URL = "https://githubnext.com/"

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")


def fetch_github_next_projects() -> List[Dict]:
    """
    Fetch GitHub Next projects by scraping the main page.

    Returns:
        List of parsed project entries
    """
    logger.info("Fetching GitHub Next projects...")

    try:
        # Fetch the main page
        headers = {
            "User-Agent": "Mozilla/5.0 (compatible; GitHub-Copilot-Daily-Digest/1.0)"
        }
        response = requests.get(GITHUB_NEXT_URL, headers=headers, timeout=30, verify=certifi.where())
        response.raise_for_status()

        # Parse HTML
        soup = BeautifulSoup(response.text, "html.parser")

        projects = []

        # Look for project cards (based on the HTML structure observed)
        # GitHub Next uses anchor tags with href="/projects/..."
        project_links = soup.find_all("a", href=re.compile(r"^/projects/[^/]+/$"))

        logger.info(f"Found {len(project_links)} project links")

        for link in project_links:
            try:
                project = parse_project_card(link)
                if project:
                    projects.append(project)
            except Exception as e:
                logger.error(f"Failed to parse project: {e}")
                continue

        logger.info(f"Successfully parsed {len(projects)} projects")
        return projects

    except Exception as e:
        logger.error(f"Failed to fetch GitHub Next projects: {e}")
        return []


def parse_project_card(link_element) -> Optional[Dict]:
    """
    Parse a project card element into structured format.

    Args:
        link_element: BeautifulSoup element for project link

    Returns:
        Dictionary with structured project data:
        {
            "title": str,
            "url": str,
            "date": str (ISO 8601),
            "status": str,
            "description": str,
            "source": "github-next",
            "experimental": True,
            "scraped_at": str (ISO 8601)
        }
    """
    try:
        # Get URL
        url = link_element.get("href", "")
        if url.startswith("/"):
            url = GITHUB_NEXT_URL.rstrip("/") + url

        # Get title (h3 tag)
        title_elem = link_element.find("h3")
        title = title_elem.get_text(strip=True) if title_elem else ""

        # Get date
        date_elem = link_element.find("div", class_="text-gh-textLight")
        date_str = date_elem.get_text(strip=True) if date_elem else ""
        
        # Try to parse date to ISO 8601
        date_iso = None
        if date_str:
            try:
                # Parse dates like "January 11, 2023"
                parsed_date = datetime.strptime(date_str, "%B %d, %Y")
                date_iso = parsed_date.isoformat() + "Z"
            except ValueError:
                logger.warning(f"Could not parse date: {date_str}")
                date_iso = date_str

        # Get status (completed, WIP, napkin sketch, etc.)
        status_elem = link_element.find("div", class_=re.compile(r"inline-block.*uppercase"))
        status = status_elem.get_text(strip=True) if status_elem else "Unknown"

        # Get description
        desc_elem = link_element.find("div", class_=re.compile(r"font-light.*mt-5"))
        description = desc_elem.get_text(strip=True) if desc_elem else ""

        if not title or not url:
            logger.warning("Missing required fields (title or URL)")
            return None

        return {
            "title": title,
            "url": url,
            "date": date_iso or date_str,
            "status": status,
            "description": description,
            "source": "github-next",
            "experimental": True,  # ALWAYS mark as experimental
            "scraped_at": datetime.utcnow().isoformat() + "Z",
        }

    except Exception as e:
        logger.error(f"Error parsing project card: {e}")
        return None


def save_project(project: Dict, output_dir: Path) -> bool:
    """
    Save project to JSON file and track in metadata.

    Args:
        project: Project dictionary
        output_dir: Directory to save project data

    Returns:
        True if saved (new project), False if skipped (duplicate)
    """
    try:
        url = project["url"]

        # Check if URL already processed
        if not add_github_next_url(url):
            logger.debug(f"Skipping duplicate: {url}")
            return False

        # Generate filename from URL
        # e.g., /projects/copilot-radar/ -> copilot-radar.json
        url_slug = url.rstrip("/").split("/")[-1]
        filename = f"{url_slug}.json"
        filepath = output_dir / filename

        # Save full project data
        safe_write_file(filepath, json.dumps(project, indent=2))
        logger.info(f"Saved project: {filename}")

        return True

    except Exception as e:
        logger.error(f"Failed to save project: {e}")
        return False


def main():
    """Main function to fetch and save GitHub Next projects"""
    logger.info("Starting GitHub Next scraper...")

    # Set up output directory
    output_dir = Path(__file__).parent.parent / "data" / "github-next"
    ensure_dir(output_dir)

    # Fetch projects
    projects = fetch_github_next_projects()

    if not projects:
        logger.warning("No projects fetched")
        return

    # Save projects
    new_count = 0
    for project in projects:
        if save_project(project, output_dir):
            new_count += 1

    logger.info(f"Scraping complete: {new_count} new projects, {len(projects)} total")


if __name__ == "__main__":
    main()
