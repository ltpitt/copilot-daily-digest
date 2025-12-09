# Task: Synthesize GitHub Copilot Content

## Python Environment Setup

**CRITICAL**: This project uses a Python virtual environment (`.venv`). Always use the venv Python interpreter when running scripts.

### Running Python Scripts
```bash
# ✅ CORRECT - Use venv's Python directly
.venv/bin/python scraper/fetch_docs.py
.venv/bin/python scraper/fetch_blog.py
.venv/bin/python scraper/detect_changes.py

# ❌ WRONG - Do NOT use system Python
python scraper/fetch_docs.py

# ❌ WRONG - Source doesn't persist in terminal commands
source .venv/bin/activate && python scraper/fetch_docs.py
```

### Installing Dependencies
```bash
# ✅ CORRECT - Use venv's pip directly
.venv/bin/python -m pip install -r requirements.txt

# ❌ WRONG - System pip
pip install -r requirements.txt
```

### Why This Matters
- macOS has externally-managed Python environments that prevent system-wide package installation
- The virtual environment (`.venv`) is isolated and contains all project dependencies
- Using `.venv/bin/python` directly ensures correct environment without activation issues

### SSL Certificate Issues
If you encounter SSL certificate errors with feedparser or urllib:
```bash
# macOS SSL certificate fix
.venv/bin/python -m pip install --upgrade certifi

# If still failing, feedparser may need SSL context configuration
# See fetch_youtube.py for implementation using requests + feedparser workaround
```

---

## Goal
Read the latest content from multiple sources and generate comprehensive documentation:
- `content/README.md`: Overview of Copilot Coding Agent usage
- `content/cheatsheet.md`: Slash commands, variables, setup tips
- `content/changelog.md`: Recent updates and features
- `content/videos.md`: Video library and tutorials

## Data Sources
- `data/docs/` - Official GitHub documentation (Markdown files)
- `data/blog/` - GitHub Blog posts (JSON files)
- `data/videos/` - YouTube videos from GitHub channel (JSON files)
- `data/changes-summary.json` - Summary of what's new

## Constraints
- Use only the content in the `data/` directory
- Output must be clear, concise, and developer-friendly
- Format all files in Markdown
- Highlight new features prominently

## Video Content

When generating video content (videos.md):
1. Read all JSON files from `data/videos/`
2. Categorize by topic (Getting Started, Features, Tutorials, Updates, Extensions, Agents)
3. Show "What's New This Week" at the top
4. Include thumbnail, title, date, duration, description for each video
5. Sort by date within categories (newest first)
6. Add statistics section (total videos, latest video, etc.)

## Format Guidelines
- Use emojis sparingly but effectively (📰 🎥 ✨ 📚)
- Keep content scannable with clear headers and lists
- Link to original sources
- Date all content updates
- Maintain consistent formatting across all files
