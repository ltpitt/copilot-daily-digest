# Task: Synthesize GitHub Copilot Content for Engineers

## Mission
**Help engineers stay current with GitHub Copilot Coding Agent through curated, actionable intelligence.**

Engineers need to:
- ✅ Get started fast (Quick Start in 5 minutes)
- ✅ Stay updated without information overload (top 3-5 changes only)
- ✅ Learn best practices from real examples (extracted from blog posts)
- ✅ Dive deeper when needed (links to sources)

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

## Python Coding Standards

**CRITICAL**: This project follows PEP 8 and uses Ruff for automatic formatting and linting.

### Code Style Rules

1. **Imports must be at the top of the file** (PEP 8)
   - ❌ WRONG: Imports inside functions
   - ✅ CORRECT: All imports at module level

2. **Use Ruff for formatting and linting**
   ```bash
   # Format all Python files
   .venv/bin/ruff format scraper/
   
   # Check and auto-fix linting issues
   .venv/bin/ruff check --fix scraper/
   ```

### Why Ruff?

- **Fast**: Written in Rust, 10-100x faster than Black/flake8
- **Comprehensive**: Replaces Black, isort, flake8, and more in one tool
- **Modern**: Enforces PEP 8, best practices, and modern Python idioms
- **Auto-fix**: Automatically fixes most issues including import ordering

---

## Content Architecture

We generate **5 content files** with distinct purposes:

### 1. content/README.md - Engineer's Daily Companion (Newspaper Style)
**Purpose**: Daily digest with highlights, news, and quick links  
**Audience**: Engineers who want quick updates and actionable tips  
**Style**: Brief, scannable, curated - newspaper digest format

**CRITICAL**: Quick Start section should be BRIEF (3-4 lines) with a link to content/STARTER-KIT.md for full tutorial. Do NOT include step-by-step instructions here.

### 2. content/REFERENCE.md - Complete Reference
**Purpose**: Comprehensive documentation for deep dives  
**Audience**: Engineers who need full command lists, complete changelog, all videos  
**Style**: Exhaustive, organized, searchable

### 3. content/changelog.md - Feature Timeline
**Purpose**: Chronological history of all updates  
**Audience**: Engineers who want to see what's changed over time  
**Style**: Timeline format, newest first, links to sources

### 4. content/cheatsheet.md - Quick Reference Guide
**Purpose**: Fast lookup for commands and shortcuts  
**Audience**: Engineers who need quick command/shortcut reference  
**Style**: Tables, code blocks, concise bullets

### 5. content/STARTER-KIT.md - Best Practices & Getting Started
**Purpose**: Comprehensive onboarding and best practices guide  
**Audience**: Engineers new to GitHub Copilot or wanting to level up  
**Style**: Educational, structured workshop format, links to courses

---

## Data Sources
- `data/docs/` - Official GitHub documentation (14 Markdown files)
- `data/blog/` - GitHub Blog posts (19 JSON files with full HTML content)
- `data/videos/` - YouTube videos from GitHub channel (6 JSON files)
- `data/github-next/` - **EXPERIMENTAL** GitHub Next projects (JSON files)
- `data/changes-summary.json` - What changed since last scrape (with diff summaries)
- `data/metadata.json` - Version history and timestamps

### ⚠️ GitHub Next - Special Handling Required

**Source**: `https://githubnext.com/` - GitHub's experimental research team

**CRITICAL**: Content from GitHub Next is **experimental/research** and requires special treatment:

1. **Always mark as experimental**:
   - Use 🔬 emoji for GitHub Next content
   - Add disclaimer: "⚠️ Experimental - May not become official features"
   - Never present as official roadmap or documentation

2. **Appropriate language**:
   - ✅ "GitHub Next is exploring..."
   - ✅ "Experimental project investigating..."
   - ✅ "Research prototype for..."
   - ❌ "GitHub will launch..."
   - ❌ "Coming soon to Copilot..."
   - ❌ "Official feature..."

3. **Status awareness**:
   - Projects have statuses: "Completed", "WIP", "Napkin sketch", "Research prototype", "Open sourced"
   - "Completed" ≠ shipped to production (may still be experimental)
   - Many experiments are discontinued
   - Only a small subset become official features

4. **Context for engineers**:
   - Useful for inspiration and understanding GitHub's research direction
   - Not reliable for planning production implementations
   - Treat as "glimpse into potential future" not "roadmap"

5. **Content placement**:
   - Separate section from official docs/blog
   - Clear visual distinction (border, background, emoji)
   - Explicitly labeled as experimental in every mention

---

## Content Generation Rules: README.md (Newspaper Style)

### Structure
```markdown
# GitHub Copilot: Your Daily Companion

> Last updated: [DATE] | 📰 [N] updates this week

## 🚀 Quick Start
[BRIEF 3-4 line summary with link to STARTER-KIT.md]

## 📰 What's New This Week
[TOP 3-5 significant changes only]

## 💡 Best Practices
[Actionable tips from blog posts]

## 🎥 Featured Videos
[1-2 most relevant to recent updates]

---

**Need more?**
- 📖 [Complete Reference](REFERENCE.md)
- 📚 [Official Docs](https://docs.github.com/copilot)
```

**CRITICAL**: Do NOT include detailed step-by-step tutorials in README.md. Keep Quick Start to 3-4 lines maximum with a clear link to content/STARTER-KIT.md for full details.

### What's New This Week - Curation Rules
**AI TASK: Extract TOP 3-5 most significant changes**

Sources:
- `data/changes-summary.json` - Check `docs.changed` array
- `data/blog/*.json` - Parse newest blog posts (published in last 7 days)
- `data/metadata.json` - Use `doc_versions[].history` to identify major changes

Selection criteria:
1. **Prioritize new features** over doc updates
   - Blog posts about new features = HIGH priority
   - Doc changes with `added_lines > 50` = MEDIUM priority
   - Minor doc updates = LOW priority (skip)

2. **Look for these keywords** in blog post content:
   - "new feature", "announcing", "now available", "introduces"
   - "coding agent", "mission control", "agent mode", "copilot cli"
   - Examples: "Model picker for coding agent" (HIGH priority)

3. **Recency matters**
   - Items from last 7 days = Featured
   - Items from last 30 days = Include if significant
   - Older items = Skip (already covered)

4. **Avoid duplicates**
   - If blog post + doc update cover same feature, use blog post (more context)

Format each item:
```markdown
**[Feature Name]** ([Date])
- [One-sentence description]
- [Key benefit or use case]
→ [Try it now](link) | [Learn more](link)
```

### Best Practices - Extraction Rules
**AI TASK: Extract 3-5 actionable tips from blog posts**

Sources:
- `data/blog/*.json` - Parse the `content` field (HTML)

What to look for in blog post HTML:
1. **Explicit tips sections**:
   - Look for: "best practice", "tip:", "pro tip", "try this:"
   - Example: "Tip: Write comments that explain why, not just what"

2. **Prompt patterns**:
   - Look for: "prompt pattern:", "here's an example:", "use this prompt:"
   - Example: "Add Redis caching to userSessionService with 30s TTL..."

3. **Command examples**:
   - Look for code blocks with: `copilot`, `@github`, mission control commands
   - Example: `copilot fix tests` - Locate failing tests and propose fixes

4. **Do/Don't comparisons**:
   - Look for: "before/after", "instead of", "avoid"
   - Example: "Use small increments. Avoid 'rewrite entire app in one shot'"

Format:
```markdown
- **[Tip title]**: [Actionable description with specific example]
  → Source: [Blog post title](link)
```

**Quality checks**:
- Each tip must be ACTIONABLE (engineer can try it immediately)
- Include concrete examples, not vague advice
- Attribute source with link

### Featured Videos - Selection Rules
**AI TASK: Pick 1-2 most relevant videos**

Sources:
- `data/videos/*.json` - Check `published` date and `title`

Selection criteria:
1. **Align with What's New**:
   - If "What's New" mentions "Model picker", find video about model selection
   - If "What's New" mentions "MCP integration", find video about MCP

2. **Recency**:
   - Videos published in last 7 days = Priority
   - Older videos = Use only if highly relevant to current updates

3. **Content type preference**:
   - Tutorials > Announcements > General overviews
   - "How to" > "Introducing"

Format:
```markdown
### [Video Title](url)
[![thumbnail](thumbnail_url)](url)

**Published**: [Date] | **Duration**: [if available]

[First 2 sentences of description]

[Watch on YouTube →](url)
```

---

## Content Generation Rules: REFERENCE.md

### Structure
```markdown
# GitHub Copilot Complete Reference

> Last updated: [DATE]

## 📋 Quick Navigation
- [Slash Commands](#slash-commands)
- [Chat Variables](#chat-variables)
- [Keyboard Shortcuts](#keyboard-shortcuts)
- [Complete Changelog](#complete-changelog)
- [All Videos](#all-videos)

## Slash Commands
[Extract from docs/copilot-chat.md]

## Chat Variables
[Extract from docs/copilot-chat.md]

## Keyboard Shortcuts
[Extract from docs/copilot-getting-started.md]

## Complete Changelog
[Reverse chronological, ALL changes from metadata.json history]

## All Videos
[All videos from data/videos/, categorized]
```

### Changelog Generation
**AI TASK: Generate complete changelog from version history**

Sources:
- `data/metadata.json` - Use `doc_versions[].history[]` array
- `data/changes-summary.json` - Current changes

Format:
```markdown
## [DATE]

### Documentation Updates
- **[filename]**: [diff_summary] (+X lines, -Y lines)
  - [If added_lines > 50, provide brief description of what changed]

### Blog Posts
- **[title]** ([date]) - [1-sentence summary]
  → [Read more](link)

### Videos
- **[title]** ([date]) - [1-sentence summary]
  → [Watch](link)
```

---

## Content Generation Rules: content/STARTER-KIT.md

### Purpose
- Comprehensive onboarding guide for engineers
- Best practices compilation
- Workshop-style learning path
- Links to official resources and courses

### When to Update
**content/STARTER-KIT.md should be reviewed and updated when**:
- Major new features announced (e.g., new AI models, new capabilities)
- Best practices change based on recent blog posts
- New official courses or resources become available
- Workflow patterns evolve
- Significant blog posts about usage patterns published

### What to Update
1. **New Features Section**: Add major features to appropriate sections
   - Example: "Model Picker" added to comparison tables and best practices
   
2. **Best Practices**: Extract from recent blog posts
   - Look for: "best practice", "tip:", "how to use", "workflow"
   - Add concrete examples and patterns
   
3. **Resource Links**: Keep courses and documentation current
   - GitHub Skills courses
   - Official documentation
   - Blog post tutorials
   
4. **Comparison Tables**: Update if capabilities change
   - Agent Mode vs Coding Agent features
   - Model comparisons
   
5. **Workflow Section**: Reflect current automation setup
   - Match actual GitHub Actions workflow
   - Update timing and processes

### Structure to Maintain
```markdown
# GitHub AI Starter Kit

## 1. Understand the Landscape
[Copilot modes and capabilities]

## 2. Best Practices
[Extracted from blogs and docs]

## 3. Onboarding Your AI Peer Programmer
[Setup guides]

## 4. Agent Mode vs Coding Agent
[Comparison table]

## 5. Getting Started: Quick Start in 5 Minutes
[Detailed step-by-step tutorial with code examples]
[This is where the full Quick Start content belongs]

## 6. Workshop Area: First Steps & Actions
[Course links and resources]

## 7. Daily Workflow
[Automation explanation]

## 8. Further Learning
[Additional resources]
```

### Update Strategy
- **Weekly Review**: Check if any blog posts from last 7 days warrant content/STARTER-KIT.md updates
- **Feature Announcements**: Immediately update when major features launched
- **Quarterly Refresh**: Review all sections for outdated information
- **Link Validation**: Ensure all course/resource links still work

### Sources for Updates
- `data/blog/*.json` - Recent blog posts about best practices
- `data/changes-summary.json` - New features from changelogs
- `content/changelog.md` - Historical feature timeline
- Official GitHub Copilot documentation

---

## AI Synthesis Guidelines

### Quality Over Quantity
- ❌ Don't: List all 14 doc updates with generic timestamps
- ✅ Do: Highlight 3-5 significant changes with context

### Be Specific and Actionable
- ❌ Don't: "New feature available"
- ✅ Do: "Model picker lets Pro+ users choose Claude Sonnet or GPT-4 when starting coding agent tasks"

### Provide Context
- ❌ Don't: "Updated copilot-chat.md"
- ✅ Do: "Chat now auto-infers relevant participants (e.g., @terminal for CLI questions) in public preview"

### Link to Sources
- Every feature mention → Link to blog post or doc
- Every best practice → Link to source blog post
- Every video → Include watch link

### Maintain Engineer-Friendly Tone
- Brief sentences (< 25 words)
- Active voice
- Concrete examples
- No marketing fluff
- Assume technical audience

---

## Format Guidelines
- Use emojis sparingly but effectively (📰 🎥 ✨ 📚)
- Keep content scannable with clear headers and lists
- Link to original sources
- Date all content updates
- Maintain consistent formatting across files
