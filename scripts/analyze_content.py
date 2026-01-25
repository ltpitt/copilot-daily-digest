#!/usr/bin/env python3
"""
Analyze scraped data to extract key information for content generation.
"""

import json
from datetime import datetime, timedelta
from pathlib import Path
from typing import Dict, List, Any

# Paths
DATA_DIR = Path(__file__).parent.parent / "data"
METADATA_FILE = DATA_DIR / "metadata.json"
CHANGES_FILE = DATA_DIR / "changes-summary.json"

def load_metadata() -> Dict[str, Any]:
    """Load metadata.json"""
    with open(METADATA_FILE) as f:
        return json.load(f)

def load_changes() -> Dict[str, Any]:
    """Load changes-summary.json"""
    with open(CHANGES_FILE) as f:
        return json.load(f)

def get_recent_blog_posts(days: int = 30) -> List[str]:
    """Get blog posts from the last N days"""
    metadata = load_metadata()
    cutoff = datetime.now() - timedelta(days=days)
    
    # For now, return most recent N posts
    # In production, would filter by actual publish date
    recent_posts = metadata.get("blog_urls", [])[:20]  # Top 20 most recent
    return recent_posts

def get_video_count() -> int:
    """Count total videos tracked"""
    metadata = load_metadata()
    return len(metadata.get("video_ids", []))

def get_training_count() -> int:
    """Count total trainings"""
    trainings_dir = DATA_DIR / "trainings"
    return len(list(trainings_dir.glob("*.json")))

def get_stats() -> Dict[str, Any]:
    """Generate stats for README"""
    metadata = load_metadata()
    changes = load_changes()
    
    # Count changes in last 7 days
    whats_new = changes.get("whats_new_7_days", {})
    blog_count = len(whats_new.get("new_blog_posts", []))
    video_count_recent = len(whats_new.get("new_videos", []))
    doc_count = len(whats_new.get("new_docs", []))
    
    # Total counts
    total_blogs = len(metadata.get("blog_urls", []))
    total_videos = get_video_count()
    total_trainings = get_training_count()
    total_docs = len([k for k in metadata.get("content_hashes", {}).keys() if k.startswith("docs/")])
    
    # Last updated
    last_updated = metadata.get("last_updated", "")
    if last_updated:
        dt = datetime.fromisoformat(last_updated.replace("Z", "+00:00"))
        last_updated_formatted = dt.strftime("%B %d, %Y at %H:%M UTC")
    else:
        last_updated_formatted = "Unknown"
    
    return {
        "recent_changes": {
            "blog_posts": blog_count,
            "videos": video_count_recent,
            "docs": doc_count,
            "total": blog_count + video_count_recent + doc_count
        },
        "totals": {
            "blogs": total_blogs,
            "videos": total_videos,
            "trainings": total_trainings,
            "docs": total_docs
        },
        "last_updated": last_updated_formatted
    }

def main():
    """Main analysis"""
    stats = get_stats()
    
    print("=" * 60)
    print("CONTENT ANALYSIS SUMMARY")
    print("=" * 60)
    print()
    print(f"📊 Recent Changes (Last 7 days):")
    print(f"  - Blog posts: {stats['recent_changes']['blog_posts']}")
    print(f"  - Videos: {stats['recent_changes']['videos']}")
    print(f"  - Docs: {stats['recent_changes']['docs']}")
    print(f"  - Total: {stats['recent_changes']['total']}")
    print()
    print(f"📚 Total Content Tracked:")
    print(f"  - Blog articles: {stats['totals']['blogs']}+")
    print(f"  - Videos: {stats['totals']['videos']}")
    print(f"  - Training courses: {stats['totals']['trainings']}")
    print(f"  - Documentation files: {stats['totals']['docs']}")
    print()
    print(f"🕒 Last scrape: {stats['last_updated']}")
    print()
    print("=" * 60)
    
    # Output JSON for programmatic use
    print()
    print("JSON Output:")
    print(json.dumps(stats, indent=2))

if __name__ == "__main__":
    main()
