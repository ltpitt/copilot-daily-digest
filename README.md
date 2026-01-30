# 📰 GitHub Copilot Daily Digest

[![Daily Digest](https://github.com/ltpitt/copilot-daily-digest/actions/workflows/daily-agent.yml/badge.svg)](https://github.com/ltpitt/copilot-daily-digest/actions/workflows/daily-agent.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![GitHub Copilot](https://img.shields.io/badge/GitHub%20Copilot-Powered-purple.svg)](https://github.com/features/copilot)
[![Made with ❤️](https://img.shields.io/badge/Made%20with-%E2%9D%A4%EF%B8%8F-red.svg)](https://github.com/ltpitt/copilot-daily-digest)

> **Your automated source for the latest GitHub Copilot news, tutorials, and updates!**

Stay up-to-date with GitHub Copilot through automated daily digests that aggregate content from official documentation, blog posts, and video tutorials.

## 🌟 Features

- **📚 Documentation Tracking** - Monitors official GitHub Copilot documentation for updates
- **📝 Blog Integration** - Fetches latest articles from the GitHub Blog RSS feed
- **🎥 Video Library** - Curates YouTube videos from GitHub's official channel
- **🔬 GitHub Next Tracking** - Monitors experimental projects (with appropriate disclaimers)
- **🔍 Change Detection** - Intelligent tracking to identify what's new
- **🤖 AI-Powered Content** - GitHub Copilot Coding Agent generates human-readable summaries
- **⚡ Daily Automation** - Runs automatically via GitHub Actions

## 📖 Documentation

- **[Main Digest](content/README.md)** - Daily newspaper-style digest with latest updates and highlights
- **[Starter Kit](content/STARTER-KIT.md)** - Complete getting started guide with step-by-step tutorials
- **[Changelog](content/CHANGELOG.md)** - Timeline of features and updates
- **[Commands & Shortcuts](content/COMMANDS.md)** - Quick reference guide
- **[Video Library](content/VIDEOS.md)** - Curated video tutorials

## 🚀 How It Works

The repository updates automatically via GitHub Actions:

### Daily Workflow

1. **Fetch Content** (Daily)
   - GitHub Documentation
   - GitHub Blog (RSS)
   - YouTube Videos (RSS with optional API enrichment)
   - GitHub Next Projects (experimental research)

2. **Detect Changes**
   - Compare with previous versions
   - Track what's new across all sources
   - Generate change summary

3. **Generate Content** (if changes detected)
   - Publisher Agent creates issue
   - **Issue automatically assigned to @copilot**
   - Agent generates all content files
   - Agent creates PR for review

4. **Review & Merge**
   - Review PR created by Publisher Agent
   - Merge when ready
   - Updated content goes live

## 🛠️ Tech Stack

- **Python 3.11+** - Core scraping and processing
- **GitHub Actions** - Automation and scheduling
- **GitHub Copilot Coding Agent** - AI-powered content generation
- **feedparser** - RSS feed parsing
- **BeautifulSoup4** - HTML parsing
- **YouTube Data API v3** - Optional video enrichment

## 📦 Installation (in case you want to check it locally)

```bash
# Clone the repository
git clone https://github.com/ltpitt/copilot-daily-digest.git
cd copilot-daily-digest

# Install dependencies
pip install -r requirements.txt

# Optional: Set YouTube API key for enrichment
export YOUTUBE_API_KEY="your-api-key-here"
```

## 🧪 Testing

### Test Full Workflow Locally

```bash
# Run the complete workflow
./scripts/test_full_workflow.sh
```

### Test Individual Components

```bash
# Fetch documentation
python scripts/fetch_docs.py

# Fetch blog posts
python scripts/fetch_blog.py

# Fetch YouTube videos
python scripts/fetch_youtube.py

# Fetch GitHub Next projects (experimental)
python scripts/fetch_github_next.py

# Detect changes
python scripts/detect_changes.py

# Generate video page
python scripts/generate_videos.py
```

### Test GitHub Actions Workflow

```bash
# Manual trigger
gh workflow run daily-agent.yml

# Monitor workflow
gh run list --workflow=daily-agent.yml

# View latest run
gh run view
```

### Test Copilot Assignment

```bash
# Test automatic copilot assignment
./scripts/test_copilot_assignment.sh
```

See Copilot Assignment Testing Guide (link removed: file not found) for detailed testing instructions.

# View latest run
gh run view
```

## ⚙️ Configuration

### YouTube API (Optional)

For enhanced video metadata (duration, views), add your YouTube API key to GitHub Secrets:

1. Go to repository Settings → Secrets and variables → Actions
2. Add `YOUTUBE_API_KEY` with your API key
3. The scraper will automatically use RSS as primary source with API enrichment

### Workflow Schedule

Edit `.github/workflows/daily-agent.yml` to customize the schedule:

```yaml
schedule:
  - cron: '0 13 * * *'  # Daily at 1 PM UTC
```

## 📊 Project Structure

```
copilot-daily-digest/
├── .github/
│   ├── agents/              # Custom agent definitions
│   │   ├── publisher.agent.md
│   │   ├── content-generator.agent.md
│   │   └── youtube-specialist.agent.md
│   ├── workflows/
│   │   └── daily-agent.yml  # Main automation workflow
│   └── copilot-instructions.md
├── content/                 # Generated content (user-facing)
│   ├── README.md
│   ├── GETTING-STARTED.md
│   ├── WHATS-NEW.md
│   ├── VIDEOS.md
│   ├── TRAININGS.md
│   ├── CHANGELOG.md
│   ├── COMMANDS.md
│   ├── REFERENCE.md
│   └── STARTER-KIT.md
├── data/                    # Scraped data (raw)
│   ├── docs/
│   ├── blog/
│   ├── videos/
│   ├── github-next/        # Experimental projects (with disclaimers)
│   ├── metadata.json
│   └── changes-summary.json
├── scripts/                 # Scraping scripts
│   ├── fetch_docs.py
│   ├── fetch_blog.py
│   ├── fetch_youtube.py
│   ├── fetch_github_next.py  # GitHub Next experimental projects
│   ├── detect_changes.py
│   └── generate_videos.py
├── scripts/                 # Utility scripts
│   └── test_full_workflow.sh
└── config/                  # Configuration files
    └── youtube.yml
```

## 🔬 GitHub Next - Experimental Content

This digest includes experimental projects from **GitHub Next** (https://githubnext.com/), GitHub's research team exploring future possibilities.

### ⚠️ Important Disclaimer

**GitHub Next projects are experimental research** and should be treated with care:

- Many experiments are discontinued and never become official features
- "Completed" status does **not** mean production-ready
- Projects are **not** official roadmap commitments
- Content is clearly marked as experimental in all generated content
- Useful for inspiration and understanding research direction

### How We Handle GitHub Next Content

1. **Always marked with 🔬 emoji** to indicate experimental nature
2. **Separate section** from official docs and blog posts
3. **Clear disclaimers** in every mention
4. **Project status included** (WIP, Completed, Napkin sketch, etc.)
5. **Cautious language**: "exploring", "researching", "prototype"

## 🤝 Contributing

Contributions are welcome! This project uses GitHub Copilot Coding Agent for automation.

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test locally with `./scripts/test_full_workflow.sh`
5. Submit a pull request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **GitHub Copilot Team** - For building an amazing AI coding assistant
- **GitHub Actions** - For reliable automation
- **Open Source Community** - For the excellent tools and libraries

## 📬 Contact

- **Author**: [ltpitt](https://github.com/ltpitt)
- **Issues**: [GitHub Issues](https://github.com/ltpitt/copilot-daily-digest/issues)

---

<div align="center">
  <strong>Built with ❤️ using GitHub Copilot Coding Agent</strong>
  <br>
  <sub>Keeping you updated on the future of AI-assisted development</sub>
</div>
