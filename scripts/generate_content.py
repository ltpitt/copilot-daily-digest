#!/usr/bin/env python3
"""
Generate all content files from fresh data.
This script reads data from data/ directory and generates content files.
"""
import json
import os
from datetime import datetime, timedelta
from pathlib import Path
from typing import Dict, List, Any
import re
import feedparser
import certifi
import requests

# Base paths
BASE_DIR = Path(__file__).parent.parent
DATA_DIR = BASE_DIR / "data"
CONTENT_DIR = BASE_DIR / "content"

# RSS Feed URLs
GITHUB_BLOG_FEED = "https://github.blog/tag/github-copilot/feed/"
GITHUB_CHANGELOG_FEED = "https://github.blog/changelog/feed/"

def fetch_rss_content() -> Dict[str, Dict]:
    """
    Fetch current blog content from RSS feeds to supplement missing data files.
    Returns a dictionary mapping URLs to blog post data with full content.
    """
    blog_content = {}
    
    try:
        # Fetch GitHub Blog RSS
        response = requests.get(GITHUB_BLOG_FEED, timeout=30, verify=certifi.where())
        feed = feedparser.parse(response.content)
        
        for entry in feed.entries:
            url = entry.get('link', '').strip()
            if url:
                # Extract content
                content = ""
                if 'content' in entry and entry.content:
                    content = entry.content[0].get('value', '') if isinstance(entry.content, list) else entry.content.get('value', '')
                
                blog_content[url] = {
                    'title': entry.get('title', '').strip(),
                    'url': url,
                    'summary': entry.get('summary', '').strip(),
                    'content': content,
                    'published': entry.get('published', '')
                }
        
        # Fetch Changelog RSS
        response = requests.get(GITHUB_CHANGELOG_FEED, timeout=30, verify=certifi.where())
        feed = feedparser.parse(response.content)
        
        for entry in feed.entries:
            url = entry.get('link', '').strip()
            title = entry.get('title', '').lower()
            # Include all changelog entries (filtering by copilot happens earlier in the pipeline)
            if url:
                content = ""
                if 'content' in entry and entry.content:
                    content = entry.content[0].get('value', '') if isinstance(entry.content, list) else entry.content.get('value', '')
                
                # Only add if not already in blog_content (prefer full blog posts)
                if url not in blog_content:
                    blog_content[url] = {
                        'title': entry.get('title', '').strip(),
                        'url': url,
                        'summary': entry.get('summary', '').strip(),
                        'content': content,
                        'published': entry.get('published', '')
                    }
    except Exception as e:
        print(f"Warning: Could not fetch RSS content: {e}")
    
    return blog_content

def load_json(filepath: Path) -> Dict:
    """Load JSON file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        return json.load(f)

def load_all_json_in_dir(directory: Path) -> List[Dict]:
    """Load all JSON files in a directory."""
    items = []
    if directory.exists():
        for file in directory.glob("*.json"):
            if file.name != "url_dates.json":
                items.append(load_json(file))
    return items

def format_date(date_str: str) -> str:
    """Format ISO date to 'Month Day, Year' (e.g., 'Feb 2, 2026')."""
    dt = datetime.fromisoformat(date_str.replace('Z', '+00:00'))
    # Format: Jan 2, 2026 (no leading zero on day)
    return dt.strftime('%b %-d, %Y')

def get_video_category(video: Dict) -> str:
    """Categorize video based on title and description."""
    text = (video.get('title', '') + ' ' + video.get('description', '')).lower()
    
    # Check in priority order
    if any(kw in text for kw in ['getting started', 'intro', 'introduction', 'basics', 'beginner']):
        return 'Getting Started'
    elif any(kw in text for kw in ['feature', 'announcement', 'release', 'introducing', "what's new"]):
        return 'Features & Updates'
    elif any(kw in text for kw in ['tutorial', 'how to', 'guide', 'walkthrough', 'demo']):
        return 'Tutorials'
    elif any(kw in text for kw in ['agent', 'coding agent', 'workspace agent', 'autonomous', 'agentic']):
        return 'Agents'
    elif any(kw in text for kw in ['extension', 'plugin', 'integration', 'api', 'vscode', 'jetbrains']):
        return 'Extensions'
    else:
        return 'Other'

def clean_html(text: str) -> str:
    """Remove HTML tags and clean up text."""
    # Remove HTML tags
    text = re.sub(r'<[^>]+>', '', text)
    # Clean up HTML entities
    text = text.replace('&nbsp;', ' ').replace('&#8217;', "'").replace('&mdash;', '—')
    text = text.replace('&ldquo;', '"').replace('&rdquo;', '"')
    text = text.replace('&amp;', '&').replace('&rsquo;', "'")
    return text.strip()

def extract_readable_summary(blog_post: Dict) -> str:
    """
    Extract a clean, journalistic summary from a blog post.
    
    Returns a 2-3 sentence summary that:
    - Removes boilerplate ("The post X appeared first on...")
    - Extracts key content from the full article
    - Provides enough context for readers to decide if they want to read more
    """
    # Try to get content first (better than summary)
    content = blog_post.get('content', '')
    summary = blog_post.get('summary', '')
    
    # Clean HTML from content
    clean_content = clean_html(content) if content else ''
    clean_summary = clean_html(summary) if summary else ''
    
    # Remove the RSS boilerplate from summary
    if clean_summary:
        # Remove "The post ... appeared first on The GitHub Blog" pattern
        clean_summary = re.sub(r'The post .+? appeared first on .+?\.', '', clean_summary)
        clean_summary = clean_summary.strip()
    
    # If we have good content, extract first 2-3 sentences
    if clean_content and len(clean_content) > 100:
        # Split into sentences (improved sentence splitting)
        # This handles common abbreviations and doesn't split on them
        sentences = re.split(r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?|!)\s+', clean_content)
        # Filter out very short sentences (likely fragments)
        good_sentences = [s.strip() for s in sentences if len(s.strip()) > 30]
        
        # Take first 2-3 sentences, up to ~350 characters total
        result = []
        char_count = 0
        for sentence in good_sentences[:5]:  # Look at first 5 sentences
            sentence_len = len(sentence)
            # Add sentence if it keeps us under 400 chars and we have < 3 sentences
            if len(result) < 3 and (char_count + sentence_len) < 400:
                result.append(sentence)
                char_count += sentence_len
            elif len(result) >= 2:  # We have at least 2 sentences, that's enough
                break
        
        if result and len(result) >= 2:
            return ' '.join(result)
        elif result and len(result) == 1 and len(result[0]) > 100:
            # If we only got 1 sentence but it's substantial, use it
            return result[0]
    
    # Fallback to cleaned summary if it exists and is substantial
    if clean_summary and len(clean_summary) > 50:
        # Make sure it's not just a title repetition
        title = blog_post.get('title', '')
        if title.lower() not in clean_summary.lower() or len(clean_summary) > len(title) + 20:
            return clean_summary
    
    # Last resort: return title with a note
    title = blog_post.get('title', 'this update')
    return f"Explore the latest update: {title}."

def clean_video_description(description: str, max_length: int = 200) -> str:
    """Clean and truncate video description."""
    if not description:
        return ""
    
    # Clean HTML
    clean_desc = clean_html(description)
    
    # Truncate at sentence boundary if possible
    if len(clean_desc) > max_length:
        # Try to find last sentence ending before max_length
        truncated = clean_desc[:max_length]
        last_period = truncated.rfind('.')
        last_exclaim = truncated.rfind('!')
        last_question = truncated.rfind('?')
        last_sentence_end = max(last_period, last_exclaim, last_question)
        
        if last_sentence_end > max_length * 0.6:  # If we found a good break point
            return clean_desc[:last_sentence_end + 1]
        else:
            # Otherwise truncate at word boundary
            truncated = clean_desc[:max_length].rsplit(' ', 1)[0]
            return truncated + "..."
    
    return clean_desc

def main():
    """Generate all content files."""
    
    # Load data
    print("Loading data...")
    changes = load_json(DATA_DIR / "changes-summary.json")
    url_dates = load_json(DATA_DIR / "blog" / "url_dates.json")
    
    # Fetch current RSS content to supplement blog data
    print("Fetching fresh RSS content...")
    rss_content = fetch_rss_content()
    print(f"Fetched {len(rss_content)} blog posts from RSS")
    
    # Load all data files
    blog_posts = load_all_json_in_dir(DATA_DIR / "blog")
    videos = load_all_json_in_dir(DATA_DIR / "videos")
    trainings = load_all_json_in_dir(DATA_DIR / "trainings")
    github_next = load_all_json_in_dir(DATA_DIR / "github-next")
    
    # If we don't have blog post files, create them from url_dates and RSS
    if not blog_posts:
        print("No blog post files found, creating from URL dates and RSS...")
        blog_posts = []
        for url, date_str in url_dates['url_dates'].items():
            if url in rss_content:
                blog_posts.append(rss_content[url])
            else:
                # Create minimal entry from URL
                # Extract title from URL, handling trailing slashes
                url_clean = url.rstrip('/')
                slug = url_clean.split('/')[-1] if url_clean else 'update'
                title = slug.replace('-', ' ').title()
                blog_posts.append({
                    'url': url,
                    'title': title,
                    'summary': '',
                    'content': ''
                })
    else:
        # Enrich existing blog posts with RSS content
        for post in blog_posts:
            url = post.get('url', '')
            if url in rss_content and not post.get('content'):
                post['content'] = rss_content[url].get('content', '')
                if not post.get('summary'):
                    post['summary'] = rss_content[url].get('summary', '')
    
    # Sort videos by date (newest first)
    videos.sort(key=lambda x: x.get('published', ''), reverse=True)
    
    # Sort blog posts by date (newest first)
    blog_posts_with_dates = []
    for post in blog_posts:
        url = post.get('url', '')
        date_str = url_dates['url_dates'].get(url)
        if date_str:
            post['date_iso'] = date_str
            blog_posts_with_dates.append(post)
    blog_posts_with_dates.sort(key=lambda x: x.get('date_iso', ''), reverse=True)
    
    # Get current timestamp (timezone-aware)
    from datetime import timezone
    now = datetime.now(timezone.utc)
    last_updated = now.strftime('%B %d, %Y')
    
    # Calculate 7 and 30 days ago
    seven_days_ago = now - timedelta(days=7)
    thirty_days_ago = now - timedelta(days=30)
    
    # Filter recent items
    from datetime import timezone
    recent_videos_7d = [v for v in videos if datetime.fromisoformat(v['published'].replace('Z', '+00:00')) >= seven_days_ago]
    recent_videos_30d = [v for v in videos if datetime.fromisoformat(v['published'].replace('Z', '+00:00')) >= thirty_days_ago]
    recent_blog_7d = [p for p in blog_posts_with_dates if datetime.fromisoformat(p['date_iso']).replace(tzinfo=timezone.utc) >= seven_days_ago]
    recent_blog_30d = [p for p in blog_posts_with_dates if datetime.fromisoformat(p['date_iso']).replace(tzinfo=timezone.utc) >= thirty_days_ago]
    
    print(f"Total blog posts: {len(blog_posts_with_dates)}")
    print(f"Total videos: {len(videos)}")
    print(f"Total trainings: {len(trainings)}")
    print(f"Total GitHub Next projects: {len(github_next)}")
    print(f"Recent blog posts (7d): {len(recent_blog_7d)}, (30d): {len(recent_blog_30d)}")
    print(f"Recent videos (7d): {len(recent_videos_7d)}, (30d): {len(recent_videos_30d)}")
    
    # Generate content files
    print("\nGenerating content files...")
    
    # Generate README.md
    generate_readme(blog_posts_with_dates, videos, trainings, github_next, last_updated)
    
    # Generate WHATS-NEW.md
    generate_whats_new(recent_blog_7d, recent_blog_30d, recent_videos_7d, recent_videos_30d, url_dates, last_updated)
    
    # Generate VIDEOS.md
    generate_videos(videos, last_updated)
    
    # Generate TRAININGS.md
    generate_trainings(trainings, last_updated)
    
    # Generate EXPERIMENTAL.md
    generate_experimental(github_next, last_updated)
    
    # Generate CHANGELOG.md
    generate_changelog(blog_posts_with_dates, videos, url_dates, last_updated)
    
    print("\nContent generation complete!")

def generate_readme(blog_posts, videos, trainings, github_next, last_updated):
    """Generate README.md."""
    print("  - README.md")
    
    # Count total updates (blog + videos)
    total_updates = len(blog_posts) + len(videos)
    
    content = f"""
# GitHub Copilot Daily Digest

Welcome to your daily, modular, and up-to-date resource for all things GitHub Copilot!

## Browse by Topic
- [Getting Started](GETTING-STARTED.md)
- [What's New (Last 30 Days)](WHATS-NEW.md)
- [Videos Library](VIDEOS.md)
- [Experimental Features](EXPERIMENTAL.md)
- [Trainings & Certifications](TRAININGS.md)
- [Changelog (Full History)](CHANGELOG.md)
- [Commands Reference](COMMANDS.md)
- [Documentation Index](REFERENCE.md)

## Current Stats
- **Total Updates:** {total_updates} (see [What's New](WHATS-NEW.md))
- **Videos:** {len(videos)} (see [Videos](VIDEOS.md))
- **Trainings:** {len(trainings)} (see [Trainings](TRAININGS.md))
- **Experimental Projects:** {len(github_next)} (see [Experimental](EXPERIMENTAL.md))

## Official Resources
- [GitHub Copilot Docs](https://docs.github.com/copilot)
- [GitHub Copilot Blog](https://github.blog/tag/copilot/)
- [GitHub Next](https://githubnext.com/)
- [GitHub Skills](https://skills.github.com/)
- [Microsoft Learn](https://learn.microsoft.com/training/)

---
_Last updated: {last_updated}_
"""
    
    with open(CONTENT_DIR / "README.md", 'w', encoding='utf-8') as f:
        f.write(content.strip() + '\n')

def generate_whats_new(blog_7d, blog_30d, videos_7d, videos_30d, url_dates, last_updated):
    """Generate WHATS-NEW.md."""
    print("  - WHATS-NEW.md")
    
    content = f"""
# What's New with GitHub Copilot

> Latest updates from the last 30 days

**Last Updated**: {last_updated}

This page highlights significant Copilot updates from the past 30 days. Content older than 30 days moves to [CHANGELOG.md](CHANGELOG.md).

---

## This Week (Last 7 Days)

"""
    
    # Combine blog and video updates for this week
    week_items = []
    
    for post in blog_7d:
        week_items.append({
            'date': post['date_iso'],
            'type': 'blog',
            'title': post['title'],
            'url': post['url'],
            'post': post  # Store full post for summary extraction
        })
    
    for video in videos_7d:
        week_items.append({
            'date': video['published'][:10],  # Get YYYY-MM-DD
            'type': 'video',
            'title': video['title'],
            'url': video['url'],
            'description': video.get('description', '')
        })
    
    # Sort by date (newest first)
    week_items.sort(key=lambda x: x['date'], reverse=True)
    
    # Take top 3-5 most significant
    top_week = week_items[:5]
    
    if top_week:
        content += f"### Recent Updates\n\n"
        for i, item in enumerate(top_week, 1):
            date_formatted = format_date(item['date'])
            content += f"#### {i}. [{item['title']}]({item['url']})\n"
            content += f"*{date_formatted}*\n\n"
            if item['type'] == 'blog':
                # Use improved summary extraction
                summary = extract_readable_summary(item['post'])
                content += f"{summary}\n"
            else:
                # Clean video description
                desc = clean_video_description(item.get('description', ''), max_length=250)
                if desc:
                    content += f"{desc}\n"
            content += "\n"
    else:
        content += "No updates this week.\n\n"
    
    content += "---\n\n## Last 30 Days\n\n"
    
    # Combine all 30-day items
    month_items = []
    
    for post in blog_30d:
        month_items.append({
            'date': post['date_iso'],
            'type': 'blog',
            'title': post['title'],
            'url': post['url'],
            'post': post
        })
    
    for video in videos_30d:
        month_items.append({
            'date': video['published'][:10],
            'type': 'video',
            'title': video['title'],
            'url': video['url'],
            'description': video.get('description', '')
        })
    
    # Sort by date (newest first)
    month_items.sort(key=lambda x: x['date'], reverse=True)
    
    # Take top 10 most significant
    top_month = month_items[:10]
    
    if top_month:
        content += "### Significant Updates\n\n"
        for i, item in enumerate(top_month, 1):
            date_formatted = format_date(item['date'])
            content += f"{i}. **[{item['title']}]({item['url']})**\n"
            content += f"\t*{date_formatted}*\n\n"
            if item['type'] == 'blog':
                # Use improved summary extraction
                summary = extract_readable_summary(item['post'])
                # Indent for markdown list
                indented_summary = '\t' + summary.replace('\n', '\n\t')
                content += f"{indented_summary}\n"
            else:
                # Clean video description
                desc = clean_video_description(item.get('description', ''), max_length=200)
                if desc:
                    content += f"\t{desc}\n"
            content += "\n"
    else:
        content += "No updates in the last 30 days.\n\n"
    
    content += """---

## Older Updates

See [CHANGELOG.md](CHANGELOG.md) for the full historical timeline.

---

_All dates are complete and sorted newest first. For a full list of updates, see [CHANGELOG.md](CHANGELOG.md)._
"""
    
    with open(CONTENT_DIR / "WHATS-NEW.md", 'w', encoding='utf-8') as f:
        f.write(content.strip() + '\n')

def generate_videos(videos, last_updated):
    """Generate VIDEOS.md."""
    print("  - VIDEOS.md")
    
    # Categorize videos
    categorized = {}
    for video in videos:
        category = get_video_category(video)
        if category not in categorized:
            categorized[category] = []
        categorized[category].append(video)
    
    # Count videos in each category
    category_counts = {cat: len(vids) for cat, vids in categorized.items()}
    
    # Recent videos (last 30 days)
    from datetime import timezone
    now = datetime.now(timezone.utc)
    thirty_days_ago = now - timedelta(days=30)
    recent_videos = [v for v in videos if datetime.fromisoformat(v['published'].replace('Z', '+00:00')) >= thirty_days_ago]
    
    content = f"""# GitHub Copilot Video Library

> **Last Updated**: {last_updated}

> **📊 Library Stats**
> - 📚 **{len(videos)}** total videos
> - 🆕 **{len(recent_videos)}** new this month
> - 📂 **Categories**: {', '.join([f'{cat} ({count})' for cat, count in category_counts.items()])}

---

## Quick Navigation

- [🆕 Recent Uploads](#recent-uploads-last-30-days)
- [📂 Browse by Category](#browse-by-category)
"""
    
    # Add category links
    for category in ['Getting Started', 'Features & Updates', 'Tutorials', 'Agents', 'Extensions', 'Other']:
        if category in categorized:
            count = len(categorized[category])
            content += f"  - [{category}](#{category.lower().replace(' ', '-').replace('&', '')}) ({count})\n"
    
    content += "\n---\n\n## Recent Uploads (Last 30 Days)\n\n"
    
    if recent_videos:
        content += f"*{len(recent_videos)} videos published in the last 30 days*\n\n"
        for video in recent_videos:
            date_formatted = format_date(video['published'])
            content += f"### [{video['title']}]({video['url']})\n\n"
            content += f"**Published**: {date_formatted} | **Channel**: {video.get('channel_name', 'GitHub')}\n\n"
            desc = video.get('description', '')[:300]
            if desc:
                content += f"{desc}...\n\n"
            content += f"[Watch on YouTube →]({video['url']})\n\n---\n\n"
    else:
        content += "No new videos this month.\n\n"
    
    content += "## Browse by Category\n\n"
    
    # Define category descriptions
    category_info = {
        'Getting Started': {
            'desc': 'New to GitHub Copilot? Start here with introductory content and beginner-friendly guides.',
            'when': "You're exploring Copilot for the first time or onboarding new team members."
        },
        'Features & Updates': {
            'desc': 'Discover new features, product announcements, capability releases, and the latest updates.',
            'when': 'You want to stay current with new capabilities and improvements.'
        },
        'Tutorials': {
            'desc': 'Step-by-step guides and walkthroughs to help you master specific workflows and techniques.',
            'when': "You're ready to dive deep into specific features or workflows."
        },
        'Agents': {
            'desc': 'Explore autonomous coding agents, advanced AI-powered workflows, and agentic capabilities.',
            'when': "You're interested in multi-file editing, autonomous task completion, or custom agents."
        },
        'Extensions': {
            'desc': 'Learn about Copilot extensions, integrations, APIs, and third-party plugins.',
            'when': 'You want to extend Copilot or integrate it with other tools.'
        },
        'Other': {
            'desc': 'Additional videos that don\'t fit into other categories.',
            'when': "You're looking for miscellaneous Copilot content."
        }
    }
    
    # Generate category sections
    for category in ['Getting Started', 'Features & Updates', 'Tutorials', 'Agents', 'Extensions', 'Other']:
        if category not in categorized:
            continue
        
        vids = categorized[category]
        info = category_info.get(category, {})
        
        content += f"\n## {category}\n\n"
        content += f"*{info.get('desc', '')}*\n\n"
        content += f"**When to watch**: {info.get('when', '')}\n\n"
        
        for video in vids:
            date_formatted = format_date(video['published'])
            content += f"### [{video['title']}]({video['url']})\n\n"
            content += f"**Published**: {date_formatted}\n\n"
            desc = video.get('description', '')[:200]
            if desc:
                content += f"{desc}...\n\n"
            content += f"[Watch on YouTube →]({video['url']})\n\n---\n\n"
    
    content += """
## More Resources

- [GitHub Copilot Documentation](https://docs.github.com/en/copilot)
- [GitHub Blog](https://github.blog/tag/github-copilot/)
- [GitHub YouTube Channel](https://www.youtube.com/github)
- [Back to Digest Home](README.md)
"""
    
    with open(CONTENT_DIR / "VIDEOS.md", 'w', encoding='utf-8') as f:
        f.write(content.strip() + '\n')

def generate_trainings(trainings, last_updated):
    """Generate TRAININGS.md."""
    print("  - TRAININGS.md")
    
    # Organize by provider
    by_provider = {}
    for training in trainings:
        provider = training.get('provider', 'Other')
        if provider not in by_provider:
            by_provider[provider] = []
        by_provider[provider].append(training)
    
    content = f"""# GitHub Copilot Trainings & Certifications

> **Last Updated**: {last_updated}

Master GitHub Copilot with these official courses, certifications, and curated learning paths.

---

## Quick Stats

- **Total Courses**: {len(trainings)}
- **Free Courses**: {len([t for t in trainings if t.get('is_free', False)])}
- **Certifications**: {len([t for t in trainings if t.get('certification', False)])}

---

## Official GitHub Courses

"""
    
    # GitHub Skills courses
    if 'GitHub Skills' in by_provider:
        for course in by_provider['GitHub Skills']:
            content += f"### [{course['title']}]({course['url']})\n\n"
            content += f"**Provider**: {course['provider']} | **Level**: {course['level']}\n\n"
            content += f"{course['description']}\n\n"
            content += f"- **Format**: {course['format']}\n"
            content += f"- **Duration**: {course.get('estimated_time', 'N/A')}\n"
            content += f"- **Cost**: {'Free' if course.get('is_free') else 'Paid'}\n"
            content += f"- **Topics**: {', '.join(course.get('topics', []))}\n\n"
            content += "---\n\n"
    
    # GitHub certifications
    if 'GitHub' in by_provider:
        for course in by_provider['GitHub']:
            if course.get('certification'):
                content += f"### [{course['title']}]({course['url']})\n\n"
                content += f"**Provider**: {course['provider']} | **Level**: {course['level']}\n\n"
                content += f"{course['description']}\n\n"
                content += f"- **Format**: {course['format']}\n"
                content += f"- **Duration**: {course.get('estimated_time', 'N/A')}\n"
                content += f"- **Topics**: {', '.join(course.get('topics', []))}\n\n"
                content += "---\n\n"
    
    content += "## Microsoft Learn Modules\n\n"
    
    # Microsoft Learn courses
    if 'Microsoft Learn' in by_provider:
        for course in by_provider['Microsoft Learn']:
            content += f"### [{course['title']}]({course['url']})\n\n"
            content += f"**Provider**: {course['provider']} | **Level**: {course['level']}\n\n"
            content += f"{course['description']}\n\n"
            content += f"- **Format**: {course['format']}\n"
            content += f"- **Duration**: {course.get('estimated_time', 'N/A')}\n"
            content += f"- **Cost**: {'Free' if course.get('is_free') else 'Paid'}\n"
            content += f"- **Topics**: {', '.join(course.get('topics', []))}\n\n"
            content += "---\n\n"
    
    content += "## Curated Courses\n\n"
    
    # Udemy and other courses
    for provider in ['Udemy']:
        if provider in by_provider:
            for course in by_provider[provider]:
                content += f"### [{course['title']}]({course['url']})\n\n"
                content += f"**Provider**: {course['provider']} | **Level**: {course['level']}\n\n"
                content += f"{course['description']}\n\n"
                content += f"- **Format**: {course['format']}\n"
                content += f"- **Duration**: {course.get('estimated_time', 'N/A')}\n"
                content += f"- **Cost**: {'Free' if course.get('is_free') else 'Paid'}\n"
                if 'rating' in course:
                    content += f"- **Rating**: {course['rating']}/5.0\n"
                if 'students' in course:
                    content += f"- **Students**: {course['students']}\n"
                content += f"- **Topics**: {', '.join(course.get('topics', []))}\n"
                if 'note' in course:
                    content += f"\n*Note: {course['note']}*\n"
                content += "\n---\n\n"
    
    content += """## Learning Paths

### Beginner Path
1. [Introduction to GitHub Copilot (Microsoft Learn)](https://learn.microsoft.com/en-us/training/modules/introduction-to-github-copilot/)
2. [Introduction to GitHub Copilot (GitHub Skills)](https://github.com/skills/copilot-intro)
3. Practice with hands-on coding

### Intermediate Path
1. [GitHub Copilot Fundamentals (Microsoft Learn)](https://learn.microsoft.com/en-us/training/paths/copilot/)
2. [Expand Your Team with Copilot (GitHub Skills)](https://github.com/skills/expand-your-team-with-copilot/)
3. [Challenge project - Build a minigame with GitHub Copilot](https://learn.microsoft.com/en-us/training/modules/challenge-project-create-mini-game-with-copilot/)

### Advanced Path
1. Complete the intermediate path
2. Earn [GitHub Foundations Certification](https://resources.github.com/learn/certifications/)
3. Build real-world projects with Copilot

---

## More Resources

- [GitHub Copilot Documentation](https://docs.github.com/en/copilot)
- [GitHub Blog](https://github.blog/tag/github-copilot/)
- [Back to Digest Home](README.md)
"""
    
    with open(CONTENT_DIR / "TRAININGS.md", 'w', encoding='utf-8') as f:
        f.write(content.strip() + '\n')

def generate_experimental(github_next, last_updated):
    """Generate EXPERIMENTAL.md."""
    print("  - EXPERIMENTAL.md")
    
    # Categorize by status
    by_status = {}
    for project in github_next:
        status = project.get('status', 'Unknown')
        if status not in by_status:
            by_status[status] = []
        by_status[status].append(project)
    
    content = f"""# Experimental Features

> **About GitHub Next**: GitHub's research lab exploring future possibilities.
> These are experimental prototypes, not production features.

**Last Updated**: {last_updated}

**⚠️ Important**: Projects here are research experiments. Many are discontinued.
They do not represent official product roadmap.

---

## Active Experiments

"""
    
    # Active statuses
    active_statuses = ['WIP', 'Research prototype', 'Napkin sketch']
    
    for status in active_statuses:
        if status in by_status:
            for project in by_status[status]:
                content += f"### [{project['title']}]({project['url']}) (Status: {status})\n\n"
                content += f"{project['description']}\n\n"
                content += f"→ [Explore this experiment]({project['url']})\n\n"
    
    content += "---\n\n## Product (Graduated from Experiments)\n\n"
    
    if 'Product' in by_status:
        for project in by_status['Product']:
            content += f"### [{project['title']}]({project['url']})\n\n"
            content += f"{project['description']}\n\n"
            content += f"This experiment has graduated to a production feature.\n\n"
            content += f"→ [Learn more]({project['url']})\n\n"
    
    content += "---\n\n## Archived Experiments\n\n"
    
    if 'Completed' in by_status:
        for project in by_status['Completed']:
            content += f"### [{project['title']}]({project['url']})\n\n"
            content += f"{project['description']}\n\n"
    
    content += """---

## Learn More

- [GitHub Next Website](https://githubnext.com/)
- [GitHub Blog](https://github.blog/tag/github-next/)
- [Back to Digest Home](README.md)

---

*Remember: These are experimental prototypes exploring future possibilities, not official product features.*
"""
    
    with open(CONTENT_DIR / "EXPERIMENTAL.md", 'w', encoding='utf-8') as f:
        f.write(content.strip() + '\n')

def generate_changelog(blog_posts, videos, url_dates, last_updated):
    """Generate CHANGELOG.md."""
    print("  - CHANGELOG.md")
    
    # Combine blog and video items
    all_items = []
    
    for post in blog_posts:
        all_items.append({
            'date': post['date_iso'],
            'type': 'Blog',
            'title': post['title'],
            'url': post['url']
        })
    
    for video in videos:
        all_items.append({
            'date': video['published'][:10],
            'type': 'Video',
            'title': video['title'],
            'url': video['url']
        })
    
    # Sort by date (newest first)
    all_items.sort(key=lambda x: x['date'], reverse=True)
    
    # Group by month
    by_month = {}
    for item in all_items:
        month_key = item['date'][:7]  # YYYY-MM
        if month_key not in by_month:
            by_month[month_key] = []
        by_month[month_key].append(item)
    
    content = f"""# GitHub Copilot Changelog

> Complete historical timeline of features, updates, and improvements

**Last Updated**: {last_updated}

This file contains the complete history of GitHub Copilot updates tracked by this repository. For recent updates (last 30 days), see [WHATS-NEW.md](WHATS-NEW.md).

---

"""
    
    # Generate month sections (newest first)
    for month_key in sorted(by_month.keys(), reverse=True):
        items = by_month[month_key]
        
        # Parse month
        year, month = month_key.split('-')
        month_name = datetime(int(year), int(month), 1).strftime('%B %Y')
        
        content += f"## {month_name}\n\n"
        
        for item in items:
            date_formatted = format_date(item['date'])
            content += f"- **{date_formatted}** - [{item['title']}]({item['url']}) ({item['type']})\n"
        
        content += "\n"
    
    content += """---

_For recent updates, see [WHATS-NEW.md](WHATS-NEW.md)._
"""
    
    with open(CONTENT_DIR / "CHANGELOG.md", 'w', encoding='utf-8') as f:
        f.write(content.strip() + '\n')

if __name__ == '__main__':
    main()
