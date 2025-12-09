"""
Metadata management utilities for tracking content changes and preventing duplicates.

This module provides functions to:
- Track content hashes for change detection
- Store scrape timestamps
- Prevent duplicate videos and blog posts
- Maintain version history for documentation
"""

import difflib
import hashlib
import json
import os
from datetime import datetime, timezone
from pathlib import Path


METADATA_FILE = "data/metadata.json"
METADATA_BACKUP = "data/metadata.backup.json"

DEFAULT_METADATA = {
    "version": "1.0.0",
    "last_updated": None,
    "content_hashes": {},
    "video_ids": [],
    "blog_urls": [],
    "doc_versions": {},
    "stats": {
        "total_docs": 0,
        "total_blog_posts": 0,
        "total_videos": 0,
        "last_successful_scrape": None,
    },
}


def load_metadata() -> dict:
    """
    Load metadata from data/metadata.json.

    Creates a new metadata file with defaults if it doesn't exist.
    If the file is corrupted, backs it up and creates a new one.

    Returns:
        dict: The metadata dictionary
    """
    metadata_path = Path(METADATA_FILE)

    # Ensure data directory exists
    metadata_path.parent.mkdir(parents=True, exist_ok=True)

    if not metadata_path.exists():
        # Create new metadata file with defaults
        metadata = DEFAULT_METADATA.copy()
        save_metadata(metadata)
        return metadata

    try:
        with open(metadata_path, encoding="utf-8") as f:
            metadata = json.load(f)

        # Validate structure
        if not isinstance(metadata, dict):
            raise ValueError("Metadata is not a dictionary")

        # Ensure all required keys exist
        for key in DEFAULT_METADATA:
            if key not in metadata:
                metadata[key] = DEFAULT_METADATA[key]

        return metadata

    except (json.JSONDecodeError, ValueError) as e:
        # Backup corrupted file and create new one
        print(f"Warning: Corrupted metadata.json: {e}")
        if metadata_path.exists():
            backup_path = Path(METADATA_BACKUP)
            metadata_path.rename(backup_path)
            print(f"Backed up corrupted metadata to {METADATA_BACKUP}")

        metadata = DEFAULT_METADATA.copy()
        save_metadata(metadata)
        return metadata


def save_metadata(metadata: dict) -> None:
    """
    Save metadata to data/metadata.json.

    Updates the last_updated timestamp automatically.

    Args:
        metadata: The metadata dictionary to save
    """
    metadata_path = Path(METADATA_FILE)

    # Ensure data directory exists
    metadata_path.parent.mkdir(parents=True, exist_ok=True)

    # Update last_updated timestamp
    metadata["last_updated"] = get_current_timestamp()

    # Write to file with pretty formatting
    with open(metadata_path, "w", encoding="utf-8") as f:
        json.dump(metadata, f, indent=2, ensure_ascii=False)


def calculate_hash(content: str) -> str:
    """
    Calculate SHA256 hash of content.

    Args:
        content: The content to hash

    Returns:
        str: Hex digest of the hash
    """
    return hashlib.sha256(content.encode("utf-8")).hexdigest()


def generate_content_diff(old_content: str, new_content: str) -> dict:
    """
    Generate a human-readable diff summary between two content versions.

    Args:
        old_content: Previous version of the content
        new_content: Current version of the content

    Returns:
        dict: Contains summary, added lines, and removed lines
    """
    old_lines = old_content.splitlines(keepends=True)
    new_lines = new_content.splitlines(keepends=True)

    # Generate unified diff
    diff = list(difflib.unified_diff(old_lines, new_lines, lineterm=""))

    # Extract meaningful changes (skip diff headers)
    added = []
    removed = []
    
    for line in diff[2:]:  # Skip the first 2 header lines
        if line.startswith("+") and not line.startswith("+++"):
            added.append(line[1:].strip())
        elif line.startswith("-") and not line.startswith("---"):
            removed.append(line[1:].strip())

    # Create summary
    summary = f"+{len(added)} lines, -{len(removed)} lines"
    
    return {
        "summary": summary,
        "added": len(added),
        "removed": len(removed),
        "added_preview": added[:5] if added else [],  # First 5 added lines
        "removed_preview": removed[:5] if removed else [],  # First 5 removed lines
    }


def is_content_changed(file_path: str, content: str) -> bool:
    """
    Check if content has changed since last scrape.

    Args:
        file_path: The relative file path used as the key
        content: The current content to check

    Returns:
        bool: True if content has changed or is new, False otherwise
    """
    metadata = load_metadata()
    current_hash = calculate_hash(content)

    if file_path not in metadata["content_hashes"]:
        # New content
        return True

    previous_hash = metadata["content_hashes"][file_path]
    return current_hash != previous_hash


def add_video_id(video_id: str) -> bool:
    """
    Add video ID to metadata.

    Args:
        video_id: The YouTube video ID to add

    Returns:
        bool: True if video ID is new (not a duplicate), False if it already exists
    """
    metadata = load_metadata()

    if video_id in metadata["video_ids"]:
        # Duplicate
        return False

    # New video ID
    metadata["video_ids"].append(video_id)
    metadata["stats"]["total_videos"] = len(metadata["video_ids"])
    save_metadata(metadata)
    return True


def add_blog_url(url: str) -> bool:
    """
    Add blog URL to metadata.

    Args:
        url: The blog post URL to add

    Returns:
        bool: True if URL is new (not a duplicate), False if it already exists
    """
    metadata = load_metadata()

    if url in metadata["blog_urls"]:
        # Duplicate
        return False

    # New blog URL
    metadata["blog_urls"].append(url)
    metadata["stats"]["total_blog_posts"] = len(metadata["blog_urls"])
    save_metadata(metadata)
    return True


def update_content_hash(file_path: str, content: str, previous_content: str = None) -> None:
    """
    Update hash for given file path and track content changes.

    Also updates doc_versions to track the history of changes with diffs.

    Args:
        file_path: The relative file path used as the key
        content: The content to hash and store
        previous_content: Optional previous content for generating diffs
    """
    metadata = load_metadata()
    new_hash = calculate_hash(content)

    # Get previous hash if it exists
    previous_hash = metadata["content_hashes"].get(file_path)

    # Update content hash
    metadata["content_hashes"][file_path] = new_hash

    # Update doc_versions if this is a documentation file
    if file_path.startswith("docs/"):
        doc_name = os.path.splitext(os.path.basename(file_path))[0]

        if doc_name not in metadata["doc_versions"]:
            metadata["doc_versions"][doc_name] = {"history": []}

        # Check if content actually changed
        content_changed = previous_hash != new_hash

        # Prepare version entry
        version_entry = {
            "hash": new_hash,
            "timestamp": get_current_timestamp(),
            "changed": content_changed,
        }

        # Generate diff if content changed and we have previous content
        if content_changed and previous_content:
            diff = generate_content_diff(previous_content, content)
            version_entry["diff_summary"] = diff["summary"]
            version_entry["added_lines"] = diff["added"]
            version_entry["removed_lines"] = diff["removed"]
            version_entry["has_diff"] = True
        else:
            version_entry["has_diff"] = False

        # Update current version info
        metadata["doc_versions"][doc_name]["current_hash"] = new_hash
        metadata["doc_versions"][doc_name]["previous_hash"] = previous_hash
        metadata["doc_versions"][doc_name]["last_changed"] = get_current_timestamp()

        # Append to history (keep last 10 versions)
        if "history" not in metadata["doc_versions"][doc_name]:
            metadata["doc_versions"][doc_name]["history"] = []
        
        metadata["doc_versions"][doc_name]["history"].append(version_entry)
        
        # Keep only last 10 versions to avoid metadata bloat
        if len(metadata["doc_versions"][doc_name]["history"]) > 10:
            metadata["doc_versions"][doc_name]["history"] = metadata["doc_versions"][doc_name]["history"][-10:]

    # Update stats
    metadata["stats"]["total_docs"] = len(
        [k for k in metadata["content_hashes"].keys() if k.startswith("docs/")]
    )
    metadata["stats"]["last_successful_scrape"] = get_current_timestamp()

    save_metadata(metadata)


def get_changes_summary() -> dict:
    """
    Get summary of changes since last update.

    Returns:
        dict: Summary containing counts of new and changed content
    """
    metadata = load_metadata()

    summary = {
        "last_updated": metadata.get("last_updated"),
        "total_docs": metadata["stats"]["total_docs"],
        "total_blog_posts": metadata["stats"]["total_blog_posts"],
        "total_videos": metadata["stats"]["total_videos"],
        "last_successful_scrape": metadata["stats"]["last_successful_scrape"],
        "tracked_files": len(metadata["content_hashes"]),
        "doc_versions_tracked": len(metadata["doc_versions"]),
    }

    return summary


def get_current_timestamp() -> str:
    """
    Get current timestamp in ISO 8601 UTC format.

    Returns:
        str: Current timestamp (e.g., "2025-12-08T10:00:00Z")
    """
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def parse_timestamp(timestamp_str: str) -> datetime:
    """
    Parse ISO 8601 timestamp string to datetime object.

    Args:
        timestamp_str: ISO 8601 formatted timestamp string

    Returns:
        datetime: Parsed datetime object in UTC
    """
    # Handle both with and without 'Z' suffix
    if timestamp_str.endswith("Z"):
        timestamp_str = timestamp_str[:-1] + "+00:00"

    return datetime.fromisoformat(timestamp_str)


def is_newer_than(timestamp_str: str, days: int = 7) -> bool:
    """
    Check if a timestamp is newer than a given number of days.

    Args:
        timestamp_str: ISO 8601 formatted timestamp string
        days: Number of days to compare against (default: 7)

    Returns:
        bool: True if timestamp is within the last N days, False otherwise
    """
    if not timestamp_str:
        return False

    try:
        timestamp = parse_timestamp(timestamp_str)
        now = datetime.now(timezone.utc)
        delta = now - timestamp
        return delta.days < days
    except (ValueError, AttributeError):
        return False


def reset_metadata() -> None:
    """
    Reset metadata to default state.

    Backs up existing metadata before resetting.
    """
    metadata_path = Path(METADATA_FILE)

    if metadata_path.exists():
        # Backup existing metadata
        backup_path = Path(METADATA_BACKUP)
        with open(metadata_path, encoding="utf-8") as f:
            existing = f.read()
        with open(backup_path, "w", encoding="utf-8") as f:
            f.write(existing)
        print(f"Backed up metadata to {METADATA_BACKUP}")

    # Create fresh metadata
    metadata = DEFAULT_METADATA.copy()
    save_metadata(metadata)
    print("Metadata reset to defaults")


if __name__ == "__main__":
    # Example usage and testing
    print("Metadata System Test")
    print("=" * 50)

    # Load or create metadata
    metadata = load_metadata()
    print(f"Loaded metadata version: {metadata['version']}")

    # Test content hashing
    test_content = "This is test content for hashing"
    test_hash = calculate_hash(test_content)
    print(f"\nTest hash: {test_hash[:16]}...")

    # Test change detection
    changed = is_content_changed("test/file.txt", test_content)
    print(f"Content changed: {changed}")

    # Test video ID tracking
    is_new = add_video_id("test_video_123")
    print(f"\nVideo ID 'test_video_123' is new: {is_new}")
    is_new = add_video_id("test_video_123")
    print(f"Video ID 'test_video_123' is new (2nd time): {is_new}")

    # Test blog URL tracking
    is_new = add_blog_url("https://example.com/blog/test")
    print(f"\nBlog URL is new: {is_new}")
    is_new = add_blog_url("https://example.com/blog/test")
    print(f"Blog URL is new (2nd time): {is_new}")

    # Update content hash
    update_content_hash("test/file.txt", test_content)
    print("\nUpdated content hash for test/file.txt")

    # Get changes summary
    summary = get_changes_summary()
    print("\nChanges Summary:")
    for key, value in summary.items():
        print(f"  {key}: {value}")

    print("\n" + "=" * 50)
    print("Test complete. Check data/metadata.json for results.")
