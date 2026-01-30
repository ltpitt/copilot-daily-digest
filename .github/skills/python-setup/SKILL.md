---
name: python-setup
description: Sets up Python environment with dependencies for running GitHub Copilot Daily Digest scrapers (fetch_docs.py, fetch_blog.py, fetch_youtube.py, fetch_trainings.py, detect_changes.py). Use when initializing the project, running scrapers, or fixing import errors.
---

# Python Environment Setup for Scrapers

This skill helps set up and verify the Python environment needed to run data collection scripts.

## When to use this skill

- First-time project setup
- Before running any scraper scripts
- When encountering `ModuleNotFoundError` or import errors
- When Python dependencies are outdated

## Required Dependencies

All dependencies are defined in `requirements.txt`:

```txt
feedparser>=6.0.10
beautifulsoup4>=4.12.0
requests>=2.31.0
PyYAML>=6.0
```

## Setup Steps

### 1. Verify Python Installation

```bash
python3 --version
```

Expected: Python 3.8 or higher

### 2. Install Dependencies

```bash
cd /path/to/copilot-daily-digest
pip install -r requirements.txt
```

### 3. Verify Installation

Run this test command to check all imports:

```bash
python3 -c "import feedparser, bs4, requests, yaml; print('✅ All dependencies installed successfully')"
```

### 4. Run Data Collection

Once setup is complete, run scrapers in this order:

```bash
# Fetch all data sources
python3 scripts/fetch_docs.py
python3 scripts/fetch_blog.py
python3 scripts/fetch_youtube.py
python3 scripts/fetch_trainings.py

# Enrich blog post dates
python3 scripts/enrich_blog_dates.py

# Detect changes
python3 scripts/detect_changes.py

# Generate videos page
python3 scripts/generate_videos.py
```

## Troubleshooting

### Import Errors

If you see errors like:
```
ModuleNotFoundError: No module named 'feedparser'
```

**Solution**: Create a python virtual environment and use `pip install -r requirements.txt`

### Permission Errors

If you see:
```
PermissionError: [Errno 13] Permission denied
```

**Solution**: Create a python virtual environment and use `pip install -r requirements.txt`

```bash
python3 -m venv venv
source venv/bin/activate  # On macOS/Linux
# OR
venv\Scripts\activate     # On Windows
pip install -r requirements.txt
```

### Python Version Issues

If scripts fail with syntax errors, verify Python version:

```bash
python3 --version
```

**Required**: Python 3.8 or higher

## Quick Reference Commands

```bash
# Full setup from scratch
pip install -r requirements.txt

# Run all scrapers
python3 scripts/fetch_docs.py && \
python3 scripts/fetch_blog.py && \
python3 scripts/fetch_youtube.py && \
python3 scripts/fetch_trainings.py && \
python3 scripts/enrich_blog_dates.py && \
python3 scripts/detect_changes.py && \
python3 scripts/generate_videos.py

# Verify data collected
ls -la data/docs/*.md | wc -l     # Should show 14+ docs
ls -la data/blog/*.json | wc -l   # Should show blog posts
ls -la data/videos/*.json | wc -l # Should show videos
cat data/changes-summary.json     # Should show change summary
```

## Expected Output Structure

After successful data collection, you should have:

```
data/
├── blog/
│   ├── *.json (blog posts)
│   └── url_dates.json
├── docs/
│   └── *.md (14 documentation files)
├── videos/
│   └── *.json (video metadata)
├── trainings/
│   └── *.json (course metadata)
├── changes-summary.json
└── metadata.json
```

## Next Steps

Once Python environment is set up and data is collected:
1. Delegate to **publisher** agent for content generation
2. Run **link-validator** agent for quality assurance
3. Create pull request with updated content
