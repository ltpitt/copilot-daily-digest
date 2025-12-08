# Task: Synthesize GitHub Copilot Content

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
