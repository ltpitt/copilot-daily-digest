"""
Example integration of metadata tracking with fetch_docs.py

This shows how to integrate the metadata system with the existing scraper.
"""

from metadata import (
    add_blog_url,
    add_video_id,
    get_changes_summary,
    is_content_changed,
    load_metadata,
    update_content_hash,
)


def scrape_with_metadata_tracking():
    """
    Example of how to integrate metadata tracking with scraping.

    This demonstrates the workflow:
    1. Load metadata before scraping
    2. Fetch content
    3. Check if content changed
    4. Update metadata if changed
    5. Log results
    """

    print("Starting scrape with metadata tracking...")
    print("-" * 50)

    # Load existing metadata
    metadata = load_metadata()
    print(f"Loaded metadata version: {metadata['version']}")

    # Simulate fetching documentation
    print("\n1. Fetching documentation...")
    doc_url = "https://docs.github.com/copilot/overview"
    doc_path = "docs/copilot-overview.md"

    # In real implementation, this would fetch actual content:
    # content = fetch_doc(doc_url)
    content = "# GitHub Copilot Overview\n\nThis is the documentation content..."

    # Check if content has changed
    if is_content_changed(doc_path, content):
        print(f"  ✓ Content changed for {doc_path}")
        # In real implementation, save the content to file
        # save_doc(doc_path, content)
        # Update metadata with new hash
        update_content_hash(doc_path, content)
        print(f"  ✓ Updated metadata for {doc_path}")
    else:
        print(f"  - No changes detected for {doc_path}")

    # Simulate fetching YouTube videos
    print("\n2. Fetching YouTube videos...")
    # In real implementation:
    # videos = fetch_youtube_feed()
    videos = [
        {"id": "dQw4w9WgXcQ", "title": "Copilot Tutorial 1"},
        {"id": "jNQXAC9IVRw", "title": "Copilot Tutorial 2"},
    ]

    new_videos = 0
    for video in videos:
        if add_video_id(video["id"]):
            print(f"  ✓ New video: {video['title']} ({video['id']})")
            new_videos += 1
        else:
            print(f"  - Duplicate video: {video['id']}")

    print(f"  Found {new_videos} new videos")

    # Simulate fetching blog posts
    print("\n3. Fetching blog posts...")
    # In real implementation:
    # posts = fetch_github_blog()
    posts = [
        {
            "url": "https://github.blog/2025-12-01-copilot-features/",
            "title": "New Copilot Features",
        },
        {"url": "https://github.blog/2025-12-05-copilot-updates/", "title": "Copilot Updates"},
    ]

    new_posts = 0
    for post in posts:
        if add_blog_url(post["url"]):
            print(f"  ✓ New blog post: {post['title']}")
            # In real implementation, save post content
            post_path = f"blog/{post['url'].split('/')[-2]}.json"
            post_content = f"Blog post content for {post['title']}"
            update_content_hash(post_path, post_content)
            new_posts += 1
        else:
            print(f"  - Duplicate blog post: {post['url']}")

    print(f"  Found {new_posts} new blog posts")

    # Get final summary
    print("\n4. Scrape Summary")
    print("-" * 50)
    summary = get_changes_summary()
    for key, value in summary.items():
        print(f"  {key}: {value}")

    print("\n✅ Scrape completed with metadata tracking")


if __name__ == "__main__":
    scrape_with_metadata_tracking()
