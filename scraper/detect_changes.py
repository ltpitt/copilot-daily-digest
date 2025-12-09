"""
Change Detection System for Copilot Daily Digest

This module detects changes in documentation files, blog posts, and videos
by comparing current content with previously tracked metadata.
"""

import hashlib
import json
from datetime import datetime, timedelta
from pathlib import Path
from typing import Any, Dict


def load_metadata() -> Dict[str, Any]:
    """
    Load metadata from data/metadata.json

    Returns:
        Dict containing metadata, or empty structure if file doesn't exist
    """
    metadata_path = Path(__file__).parent.parent / "data" / "metadata.json"

    if not metadata_path.exists():
        return {
            "last_updated": None,
            "sources": {
                "github_docs": {"files": {}},
                "github_blog": {"entries": {}, "blog_urls": []},
                "youtube": {"videos": {}, "video_ids": []},
            },
        }

    try:
        with open(metadata_path, encoding="utf-8") as f:
            return json.load(f)
    except Exception as e:
        print(f"[ERROR] Failed to load metadata: {e}")
        return {
            "last_updated": None,
            "sources": {
                "github_docs": {"files": {}},
                "github_blog": {"entries": {}, "blog_urls": []},
                "youtube": {"videos": {}, "video_ids": []},
            },
        }


def calculate_hash(content: str) -> str:
    """
    Calculate SHA-256 hash of content

    Args:
        content: String content to hash

    Returns:
        First 12 characters of hex digest
    """
    return hashlib.sha256(content.encode("utf-8")).hexdigest()[:12]


def safe_read_file(filepath: Path) -> str:
    """
    Safely read file content

    Args:
        filepath: Path to file

    Returns:
        File content as string, or empty string on error
    """
    try:
        with open(filepath, encoding="utf-8") as f:
            return f.read()
    except Exception as e:
        print(f"[ERROR] Failed to read {filepath}: {e}")
        return ""


def detect_doc_changes() -> Dict[str, Any]:
    """
    Detect changes in documentation files using doc_versions metadata.

    Returns:
        Dict with keys: changed, new, unchanged, deleted
        Changed docs include diff information (timestamp, lines added/removed)
    """
    metadata = load_metadata()
    docs_dir = Path(__file__).parent.parent / "data" / "docs"

    doc_versions = metadata.get("doc_versions", {})
    content_hashes = metadata.get("content_hashes", {})

    changed = []
    new = []
    unchanged = []
    deleted = []

    # Check for new and changed files
    if docs_dir.exists():
        for doc_file in docs_dir.glob("*.md"):
            if doc_file.name == "scrape-summary.md":
                continue  # Skip summary file
                
            filename = doc_file.name
            doc_name = doc_file.stem
            content = safe_read_file(doc_file)
            current_hash = calculate_hash(content)

            hash_key = f"docs/{filename}"
            
            if hash_key in content_hashes:
                # File was tracked before
                old_hash = content_hashes[hash_key]
                if old_hash != current_hash:
                    # Get diff info from doc_versions
                    change_info = {"filename": filename}
                    if doc_name in doc_versions and "history" in doc_versions[doc_name]:
                        history = doc_versions[doc_name]["history"]
                        if history:
                            latest = history[-1]
                            change_info["timestamp"] = latest.get("timestamp")
                            change_info["diff_summary"] = latest.get("diff_summary", "")
                            change_info["added_lines"] = latest.get("added_lines", 0)
                            change_info["removed_lines"] = latest.get("removed_lines", 0)
                    changed.append(change_info)
                else:
                    unchanged.append(filename)
            else:
                # New file
                new.append(filename)

    # Check for deleted files
    current_files = set([f.name for f in docs_dir.glob("*.md") if f.name != "scrape-summary.md"]) if docs_dir.exists() else set()
    tracked_filenames = set([k.replace("docs/", "") for k in content_hashes.keys() if k.startswith("docs/")])
    deleted = list(tracked_filenames - current_files)

    return {"changed": changed, "new": new, "unchanged": unchanged, "deleted": deleted}


def detect_blog_changes() -> Dict[str, Any]:
    """
    Detect new blog posts (comparing URLs in metadata)

    Returns:
        Dict with new_posts list and count
    """
    metadata = load_metadata()
    blog_dir = Path(__file__).parent.parent / "data" / "blog"

    tracked_entries = metadata.get("sources", {}).get("github_blog", {}).get("entries", {})
    tracked_urls = [entry.get("url", "") for entry in tracked_entries.values()]

    new_posts = []

    # Read all blog post files
    if blog_dir.exists():
        for blog_file in blog_dir.glob("*.json"):
            try:
                with open(blog_file, encoding="utf-8") as f:
                    posts = json.load(f)

                # Handle both list and dict structures
                if isinstance(posts, list):
                    post_list = posts
                elif isinstance(posts, dict) and "posts" in posts:
                    post_list = posts["posts"]
                else:
                    post_list = [posts]

                for post in post_list:
                    url = post.get("url", post.get("link", ""))
                    if url and url not in tracked_urls:
                        new_posts.append(
                            {
                                "title": post.get("title", ""),
                                "url": url,
                                "date": post.get("published", post.get("date", "")),
                                "summary": post.get("summary", post.get("description", ""))[:200],
                            }
                        )
            except Exception as e:
                print(f"[ERROR] Failed to read blog file {blog_file}: {e}")

    # Sort by date (newest first)
    new_posts.sort(key=lambda x: x.get("date", ""), reverse=True)

    return {"new_posts": new_posts, "count": len(new_posts)}


def detect_video_changes() -> Dict[str, Any]:
    """
    Detect new videos (comparing video IDs in metadata)

    Returns:
        Dict with new_videos list and count
    """
    metadata = load_metadata()
    videos_dir = Path(__file__).parent.parent / "data" / "videos"

    tracked_videos = metadata.get("sources", {}).get("youtube", {}).get("videos", {})
    tracked_video_ids = set(tracked_videos.keys())

    new_videos = []

    # Read all video files
    if videos_dir.exists():
        for video_file in videos_dir.glob("*.json"):
            try:
                with open(video_file, encoding="utf-8") as f:
                    videos = json.load(f)

                # Handle both list and dict structures
                if isinstance(videos, list):
                    video_list = videos
                elif isinstance(videos, dict) and "videos" in videos:
                    video_list = videos["videos"]
                else:
                    video_list = [videos]

                for video in video_list:
                    video_id = video.get("video_id", video.get("id", ""))
                    if video_id and video_id not in tracked_video_ids:
                        new_videos.append(
                            {
                                "title": video.get("title", ""),
                                "video_id": video_id,
                                "date": video.get("published", video.get("date", "")),
                                "thumbnail": video.get("thumbnail", ""),
                            }
                        )
            except Exception as e:
                print(f"[ERROR] Failed to read video file {video_file}: {e}")

    # Sort by date (newest first)
    new_videos.sort(key=lambda x: x.get("date", ""), reverse=True)

    return {"new_videos": new_videos, "count": len(new_videos)}


def generate_change_summary() -> Dict[str, Any]:
    """
    Generate comprehensive change summary

    Returns:
        Dict with has_changes flag, summary text, details, and timestamp
    """
    docs = detect_doc_changes()
    blog = detect_blog_changes()
    videos = detect_video_changes()

    # Calculate total changes
    total_docs_changes = len(docs["changed"]) + len(docs["new"]) + len(docs["deleted"])
    total_changes = total_docs_changes + blog["count"] + videos["count"]
    has_changes = total_changes > 0

    # Generate summary text
    summary_lines = [f"Changes detected on {datetime.utcnow().strftime('%B %d, %Y')}:", ""]

    if total_docs_changes > 0:
        summary_lines.append(f"📄 Documentation: {total_docs_changes} changes")
        for item in docs["changed"]:
            filename = item["filename"] if isinstance(item, dict) else item
            if isinstance(item, dict) and item.get("diff_summary"):
                summary_lines.append(f"  - {filename}: Updated ({item['diff_summary']})")
            else:
                summary_lines.append(f"  - {filename}: Updated content")
        for filename in docs["new"]:
            summary_lines.append(f"  - {filename}: New file added")
        for filename in docs["deleted"]:
            summary_lines.append(f"  - {filename}: File deleted")
        summary_lines.append("")

    if blog["count"] > 0:
        summary_lines.append(
            f"📝 Blog Posts: {blog['count']} new article{'s' if blog['count'] != 1 else ''}"
        )
        for post in blog["new_posts"][:5]:  # Show first 5
            date_str = post.get("date", "")[:10] if post.get("date") else "Unknown date"
            summary_lines.append(f'  - "{post["title"]}" ({date_str})')
        summary_lines.append("")

    if videos["count"] > 0:
        summary_lines.append(
            f"🎥 Videos: {videos['count']} new video{'s' if videos['count'] != 1 else ''}"
        )
        for video in videos["new_videos"][:5]:  # Show first 5
            date_str = video.get("date", "")[:10] if video.get("date") else "Unknown date"
            summary_lines.append(f'  - "{video["title"]}" ({date_str})')
        summary_lines.append("")

    if has_changes:
        summary_lines.append(f"Total: {total_changes} changes detected")
    else:
        summary_lines = ["No changes detected since last update."]

    summary_text = "\n".join(summary_lines)

    return {
        "has_changes": has_changes,
        "summary": summary_text,
        "details": {"docs": docs, "blog": blog, "videos": videos},
        "timestamp": datetime.utcnow().isoformat() + "Z",
    }


def get_whats_new(days: int = 7) -> Dict[str, Any]:
    """
    Get everything new in the last N days

    Args:
        days: Number of days to look back (default: 7)

    Returns:
        Dict with period, total_changes, and lists of new items
    """
    cutoff_date = datetime.utcnow() - timedelta(days=days)
    cutoff_str = cutoff_date.isoformat()

    docs = detect_doc_changes()
    blog = detect_blog_changes()
    videos = detect_video_changes()

    # Filter by date
    new_docs = docs["new"] + docs["changed"]  # Recent changes

    # Filter blog posts by date
    recent_blog_posts = [post for post in blog["new_posts"] if post.get("date", "") >= cutoff_str]

    # Filter videos by date
    recent_videos = [video for video in videos["new_videos"] if video.get("date", "") >= cutoff_str]

    total = len(new_docs) + len(recent_blog_posts) + len(recent_videos)

    return {
        "period": f"Last {days} days" if days > 1 else "Last 24 hours",
        "total_changes": total,
        "new_docs": new_docs,
        "new_blog_posts": recent_blog_posts,
        "new_videos": recent_videos,
    }


def save_change_summary(summary: Dict[str, Any]) -> None:
    """
    Save change summary to data/changes-summary.json

    Args:
        summary: Change summary dict from generate_change_summary()
    """
    output_path = Path(__file__).parent.parent / "data" / "changes-summary.json"

    # Ensure data directory exists
    output_path.parent.mkdir(parents=True, exist_ok=True)

    # Add metadata
    output_data = {
        "generated_at": datetime.utcnow().isoformat() + "Z",
        "has_changes": summary["has_changes"],
        "total_changes": (
            len(summary["details"]["docs"]["changed"])
            + len(summary["details"]["docs"]["new"])
            + len(summary["details"]["docs"]["deleted"])
            + summary["details"]["blog"]["count"]
            + summary["details"]["videos"]["count"]
        ),
        "docs": summary["details"]["docs"],
        "blog": {
            "new_count": summary["details"]["blog"]["count"],
            "new_posts": summary["details"]["blog"]["new_posts"],
        },
        "videos": {
            "new_count": summary["details"]["videos"]["count"],
            "new_videos": summary["details"]["videos"]["new_videos"],
        },
        "summary_text": summary["summary"],
        "whats_new_7_days": get_whats_new(7),
    }

    try:
        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(output_data, f, indent=2, ensure_ascii=False)
        print(f"[INFO] Change summary saved to {output_path}")
    except Exception as e:
        print(f"[ERROR] Failed to save change summary: {e}")


def main():
    """Main entry point - detect all changes and print summary"""
    print("[INFO] Detecting changes...")
    print("[INFO] Checking documentation files...")
    print("[INFO] Checking blog posts...")
    print("[INFO] Checking videos...")
    print()

    summary = generate_change_summary()

    if summary["has_changes"]:
        print("✅ Changes detected!")
        print()
        print(summary["summary"])
    else:
        print("ℹ️  No changes detected since last update.")

    # Save to file
    save_change_summary(summary)
    print("\nSaved to data/changes-summary.json")


if __name__ == "__main__":
    main()
