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
- **🔍 Change Detection** - Intelligent tracking to identify what's new
- **🤖 AI-Powered Content** - GitHub Copilot Coding Agent generates human-readable summaries
- **⚡ Daily Automation** - Runs automatically via GitHub Actions

## 📖 Documentation

- **[Main Digest](content/README.md)** - Overview and recent highlights
- **[Changelog](content/changelog.md)** - Timeline of features and updates
- **[Cheatsheet](content/cheatsheet.md)** - Quick reference guide
- **[Video Library](content/videos.md)** - Curated video tutorials
- **[Starter Kit](STARTER-KIT.md)** - Best practices and getting started guide

## 🚀 How It Works

The repository updates automatically via GitHub Actions:

### Daily Workflow

1. **Fetch Content** (Daily at 1 PM UTC)
   - GitHub Documentation
   - GitHub Blog (RSS)
   - YouTube Videos (RSS with optional API enrichment)

2. **Detect Changes**
   - Compare with previous versions
   - Track what's new across all sources
   - Generate change summary

3. **Generate Content** (if changes detected)
   - Publisher Agent creates issue
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

## 📦 Installation

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
python scraper/fetch_docs.py

# Fetch blog posts
python scraper/fetch_blog.py

# Fetch YouTube videos
python scraper/fetch_youtube.py

# Detect changes
python scraper/detect_changes.py

# Generate video page
python scraper/generate_videos.py
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
│   ├── changelog.md
│   ├── cheatsheet.md
│   └── videos.md
├── data/                    # Scraped data (raw)
│   ├── docs/
│   ├── blog/
│   ├── videos/
│   ├── metadata.json
│   └── changes-summary.json
├── scraper/                 # Scraping scripts
│   ├── fetch_docs.py
│   ├── fetch_blog.py
│   ├── fetch_youtube.py
│   ├── detect_changes.py
│   └── generate_videos.py
├── scripts/                 # Utility scripts
│   └── test_full_workflow.sh
└── config/                  # Configuration files
    └── youtube.yml
```

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
- **Discussions**: [GitHub Discussions](https://github.com/ltpitt/copilot-daily-digest/discussions)

---

<div align="center">
  <strong>Built with ❤️ using GitHub Copilot Coding Agent</strong>
  <br>
  <sub>Keeping you updated on the future of AI-assisted development</sub>
</div>
