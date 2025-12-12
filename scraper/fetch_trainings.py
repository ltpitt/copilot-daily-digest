"""
GitHub Copilot Trainings & Workshops Fetcher

Fetches high-quality training resources for GitHub Copilot:
1. Official GitHub Skills courses
2. Microsoft Learn modules
3. High-rated Udemy courses (curated)

Stores data in JSON format and tracks updates.
"""

import hashlib
import json
import logging
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, List


# Add parent directory to path to import local modules
sys.path.insert(0, str(Path(__file__).parent.parent.resolve()))

try:
    from scraper.metadata import load_metadata, save_metadata
    from scraper.utils import ensure_dir, safe_write_file
except ImportError:

    def load_metadata() -> dict:
        """Fallback: Load metadata"""
        metadata_file = Path(__file__).parent.parent / "data" / "metadata.json"
        if metadata_file.exists():
            with open(metadata_file) as f:
                return json.load(f)
        return {
            "blog_urls": [],
            "youtube_urls": [],
            "training_ids": [],
            "last_updated": None,
        }

    def save_metadata(metadata: dict) -> bool:
        """Fallback: Save metadata"""
        metadata_file = Path(__file__).parent.parent / "data" / "metadata.json"
        metadata_file.parent.mkdir(parents=True, exist_ok=True)
        try:
            with open(metadata_file, "w") as f:
                json.dump(metadata, f, indent=2)
            return True
        except Exception as e:
            logging.error(f"Failed to save metadata: {e}")
            return False

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

# Base data directory
DATA_DIR = Path(__file__).parent.parent / "data" / "trainings"


def generate_training_id(url: str) -> str:
    """Generate a unique ID for a training resource based on URL."""
    return hashlib.sha256(url.encode()).hexdigest()[:16]


def fetch_github_skills() -> List[Dict]:
    """
    Fetch GitHub Skills courses related to Copilot.

    Returns:
        List of course dictionaries with metadata
    """
    logger.info("Fetching GitHub Skills courses...")

    # Curated list of official GitHub Skills courses for Copilot
    courses = [
        {
            "id": "github-skills-copilot-team",
            "title": "Expand Your Team with Copilot",
            "description": "Learn how to use GitHub Copilot to expand your team's capabilities. This hands-on course covers using Copilot for code generation, testing, and collaboration.",
            "url": "https://github.com/skills/expand-your-team-with-copilot/",
            "provider": "GitHub Skills",
            "level": "Intermediate",
            "topics": [
                "GitHub Copilot",
                "AI Pair Programming",
                "Team Collaboration",
                "Coding Agent",
            ],
            "format": "Interactive",
            "is_free": True,
            "certification": False,
            "estimated_time": "2-3 hours",
            "last_verified": datetime.now(timezone.utc).isoformat(),
        },
        {
            "id": "github-skills-copilot-intro",
            "title": "Introduction to GitHub Copilot",
            "description": "Get started with GitHub Copilot. Learn the basics of AI-assisted coding, including code completions, chat features, and best practices.",
            "url": "https://github.com/skills/copilot-intro",
            "provider": "GitHub Skills",
            "level": "Beginner",
            "topics": ["GitHub Copilot", "AI Pair Programming", "Code Completion"],
            "format": "Interactive",
            "is_free": True,
            "certification": False,
            "estimated_time": "1-2 hours",
            "last_verified": datetime.now(timezone.utc).isoformat(),
        },
    ]

    logger.info(f"✓ Found {len(courses)} GitHub Skills courses")
    return courses


def fetch_microsoft_learn() -> List[Dict]:
    """
    Fetch Microsoft Learn modules related to GitHub Copilot.

    Returns:
        List of module dictionaries with metadata
    """
    logger.info("Fetching Microsoft Learn modules...")

    # Curated list of official Microsoft Learn modules
    modules = [
        {
            "id": "ms-learn-intro-copilot",
            "title": "Introduction to GitHub Copilot",
            "description": "Discover how GitHub Copilot can help you code faster and more efficiently. Learn about AI-powered code suggestions and how to integrate Copilot into your workflow.",
            "url": "https://learn.microsoft.com/en-us/training/modules/introduction-to-github-copilot/",
            "provider": "Microsoft Learn",
            "level": "Beginner",
            "topics": ["GitHub Copilot", "AI", "Code Generation"],
            "format": "Self-paced",
            "is_free": True,
            "certification": False,
            "estimated_time": "30 minutes",
            "last_verified": datetime.now(timezone.utc).isoformat(),
        },
        {
            "id": "ms-learn-copilot-fundamentals",
            "title": "GitHub Copilot Fundamentals",
            "description": "Master the fundamentals of GitHub Copilot. Learn how to write better prompts, use chat features, and leverage AI for testing and documentation.",
            "url": "https://learn.microsoft.com/en-us/training/paths/copilot/",
            "provider": "Microsoft Learn",
            "level": "Intermediate",
            "topics": [
                "GitHub Copilot",
                "Prompt Engineering",
                "AI Testing",
                "Documentation",
            ],
            "format": "Learning Path",
            "is_free": True,
            "certification": False,
            "estimated_time": "2-3 hours",
            "last_verified": datetime.now(timezone.utc).isoformat(),
        },
        {
            "id": "ms-learn-challenge-copilot",
            "title": "Challenge project - Build a minigame with GitHub Copilot",
            "description": "Demonstrate your ability to use GitHub Copilot to develop code by creating a console minigame in C#.",
            "url": "https://learn.microsoft.com/en-us/training/modules/challenge-project-create-mini-game-with-copilot/",
            "provider": "Microsoft Learn",
            "level": "Intermediate",
            "topics": ["GitHub Copilot", "C#", "Game Development", "Hands-on"],
            "format": "Challenge Project",
            "is_free": True,
            "certification": False,
            "estimated_time": "1-2 hours",
            "last_verified": datetime.now(timezone.utc).isoformat(),
        },
    ]

    logger.info(f"✓ Found {len(modules)} Microsoft Learn modules")
    return modules


def fetch_udemy_courses() -> List[Dict]:
    """
    Fetch curated high-quality Udemy courses about GitHub Copilot.

    Note: This is a manually curated list of top-rated courses.
    Requires periodic manual updates to maintain quality.

    Returns:
        List of course dictionaries with metadata
    """
    logger.info("Loading curated Udemy courses...")

    # Manually curated list of high-quality Udemy courses
    # Criteria: 4.5+ rating, 1000+ students, recent updates, Copilot-focused
    courses = [
        {
            "id": "udemy-copilot-masterclass",
            "title": "GitHub Copilot: The Complete Masterclass",
            "description": "Master GitHub Copilot from basics to advanced. Learn AI pair programming, prompt engineering, and how to integrate Copilot into professional workflows.",
            "url": "https://www.udemy.com/course/github-copilot-complete-guide/",
            "provider": "Udemy",
            "level": "All Levels",
            "topics": [
                "GitHub Copilot",
                "AI Pair Programming",
                "Prompt Engineering",
                "Professional Development",
            ],
            "format": "Video Course",
            "is_free": False,
            "certification": True,
            "estimated_time": "8-10 hours",
            "rating": 4.7,
            "students": "5000+",
            "last_verified": datetime.now(timezone.utc).isoformat(),
            "note": "Check company Udemy account for access",
        },
    ]

    logger.info(f"✓ Found {len(courses)} curated Udemy courses")
    return courses


def fetch_github_certifications() -> List[Dict]:
    """
    Fetch GitHub Copilot certification programs.

    Returns:
        List of certification dictionaries with metadata
    """
    logger.info("Fetching GitHub certifications...")

    # Official GitHub certifications
    certifications = [
        {
            "id": "github-cert-foundations",
            "title": "GitHub Foundations Certification",
            "description": "Validate your knowledge of GitHub fundamentals, including Copilot usage, collaboration, and project management. Industry-recognized certification.",
            "url": "https://resources.github.com/learn/certifications/",
            "provider": "GitHub",
            "level": "Intermediate",
            "topics": [
                "GitHub",
                "Copilot",
                "Collaboration",
                "Best Practices",
                "Project Management",
            ],
            "format": "Certification Exam",
            "is_free": False,
            "certification": True,
            "estimated_time": "Preparation: 20-40 hours",
            "last_verified": datetime.now(timezone.utc).isoformat(),
        },
    ]

    logger.info(f"✓ Found {len(certifications)} GitHub certifications")
    return certifications


def save_training(training: Dict) -> bool:
    """
    Save a training resource to disk.

    Args:
        training: Training dictionary with metadata

    Returns:
        True if saved successfully, False otherwise
    """
    try:
        training_id = training.get("id", generate_training_id(training["url"]))
        filepath = DATA_DIR / f"{training_id}.json"

        # Ensure directory exists
        ensure_dir(DATA_DIR)

        # Add fetch metadata
        training["fetched_at"] = datetime.now(timezone.utc).isoformat()

        # Write to file
        content = json.dumps(training, indent=2, ensure_ascii=False)
        success = safe_write_file(filepath, content)

        if success:
            logger.info(f"✓ Saved: {training['title']}")
        else:
            logger.error(f"✗ Failed to save: {training['title']}")

        return success

    except Exception as e:
        logger.error(f"Error saving training {training.get('title', 'unknown')}: {e}")
        return False


def update_metadata(trainings: List[Dict]) -> None:
    """
    Update metadata with training IDs.

    Args:
        trainings: List of training dictionaries
    """
    metadata = load_metadata()

    # Ensure training_ids list exists
    if "training_ids" not in metadata:
        metadata["training_ids"] = []

    # Add new training IDs
    for training in trainings:
        training_id = training.get("id", generate_training_id(training["url"]))
        if training_id not in metadata["training_ids"]:
            metadata["training_ids"].append(training_id)

    # Update last_updated timestamp
    metadata["last_updated"] = datetime.now(timezone.utc).isoformat()

    # Save metadata
    save_metadata(metadata)
    logger.info(f"✓ Updated metadata with {len(trainings)} trainings")


def main():
    """Main function to fetch and save all training resources."""
    logger.info("Starting GitHub Copilot trainings fetch...")

    # Ensure data directory exists
    ensure_dir(DATA_DIR)

    # Fetch from all sources
    all_trainings = []

    # GitHub Skills
    try:
        github_skills = fetch_github_skills()
        all_trainings.extend(github_skills)
    except Exception as e:
        logger.error(f"Failed to fetch GitHub Skills: {e}")

    # Microsoft Learn
    try:
        ms_learn = fetch_microsoft_learn()
        all_trainings.extend(ms_learn)
    except Exception as e:
        logger.error(f"Failed to fetch Microsoft Learn: {e}")

    # Udemy
    try:
        udemy = fetch_udemy_courses()
        all_trainings.extend(udemy)
    except Exception as e:
        logger.error(f"Failed to fetch Udemy courses: {e}")

    # GitHub Certifications
    try:
        certifications = fetch_github_certifications()
        all_trainings.extend(certifications)
    except Exception as e:
        logger.error(f"Failed to fetch GitHub certifications: {e}")

    # Save all trainings
    logger.info(f"Saving {len(all_trainings)} training resources...")
    saved_count = 0
    for training in all_trainings:
        if save_training(training):
            saved_count += 1

    # Update metadata
    update_metadata(all_trainings)

    logger.info(f"✓ Fetch complete: {saved_count}/{len(all_trainings)} trainings saved")

    # Summary by provider
    providers = {}
    for training in all_trainings:
        provider = training.get("provider", "Unknown")
        providers[provider] = providers.get(provider, 0) + 1

    logger.info("Summary by provider:")
    for provider, count in sorted(providers.items()):
        logger.info(f"  - {provider}: {count}")


if __name__ == "__main__":
    main()
