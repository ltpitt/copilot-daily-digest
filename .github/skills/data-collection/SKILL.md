---
name: data-collection
description: Guide for collecting GitHub Copilot data using deterministic Python scrapers. Use when fresh data is needed before content generation, when data/ directory is empty or outdated, or when user requests data fetch/scraping.
---

# Data Collection

Collect fresh data from multiple sources using deterministic Python scrapers.

## Prerequisites

Python environment is auto-configured via `.github/workflows/copilot-setup-steps.yml`.

**Local development:** Activate venv with `source .venv/bin/activate` and run `pip install -r requirements.txt`.

## Data Collection Scripts

Execute these scripts in order:

### 1. Fetch Documentation

```bash
python3 scripts/fetch_docs.py
```

- Fetches latest GitHub Copilot documentation
- Output: `data/docs/*.md` (14+ files)
- Deterministic: Same source = same output

### 2. Fetch Blog Posts

```bash
python3 scripts/fetch_blog.py
```

- Fetches blog posts via GitHub RSS feed
- Output: `data/blog/*.json`
- Each file contains: title, URL, date, summary, content, tags

### 3. Fetch YouTube Videos

```bash
python3 scripts/fetch_youtube.py
```

- Requires: `YOUTUBE_API_KEY` environment variable
- Fetches videos from GitHub's official channel
- Output: `data/videos/*.json`
- Each file contains: video_id, title, URL, thumbnail, date, description

### 4. Fetch Training Courses

```bash
python3 scripts/fetch_trainings.py
```

- Fetches curated training courses and certifications
- Output: `data/trainings/*.json`
- Sources: GitHub Skills, Microsoft Learn, Udemy

### 5. Enrich Blog Dates

```bash
python3 scripts/enrich_blog_dates.py
```

- Extracts publish dates from blog post URLs
- Output: `data/blog/url_dates.json`
- Critical for chronological sorting in content generation

## Verification

After collection, verify data exists:

```bash
ls data/docs/*.md | wc -l      # Should be 14+
ls data/blog/*.json | wc -l    # Should have multiple posts
ls data/videos/*.json | wc -l  # Should have videos
test -f data/blog/url_dates.json && echo "✓ Dates enriched"
```

## Quick Collection (All at Once)

```bash
python3 scripts/fetch_docs.py && \
python3 scripts/fetch_blog.py && \
python3 scripts/fetch_youtube.py && \
python3 scripts/fetch_trainings.py && \
python3 scripts/enrich_blog_dates.py
```

## Important Notes

- Scripts are deterministic - DO NOT modify them in agents
- All scripts handle HTTP errors and retries automatically
- Scripts log to stdout for debugging
- Data files are committed to git after collection
