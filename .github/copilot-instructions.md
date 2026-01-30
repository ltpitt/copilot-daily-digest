# GitHub Copilot Daily Digest - Workflow Instructions

## Mission

Help engineers stay current with GitHub Copilot through modular, topic-focused documentation that is automatically updated daily. Transform collected data into a newspaper-style digest that is fresh, pleasing, and relevant to read.

## Architecture Overview

```
GitHub Action (daily-agent.yml)
    │
    └─► Creates issue for Copilot Coding Agent
            │
            ▼
    Issue assigned to Copilot
            │
            ▼
    copilot-setup-steps.yml runs FIRST
    │   ├── Checkout code
    │   ├── Setup Python 3.11
    │   ├── Install dependencies
    │   ├── fetch_docs.py → data/docs/*.md
    │   ├── fetch_blog.py → data/blog/*.json
    │   ├── fetch_youtube.py → data/videos/*.json
    │   ├── fetch_trainings.py → data/trainings/*.json
    │   ├── fetch_github_next.py → data/github-next/*.json
    │   ├── enrich_blog_dates.py → data/blog/url_dates.json
    │   └── detect_changes.py → data/changes-summary.json
    │
    ▼
YOU (This Agent) - same environment, fresh data ready
    │
    ├─► Phase 1: Verify Data
    ├─► Phase 2: Generate Content
    ├─► Phase 3: Validate Quality
    └─► Phase 4: Report Completion
```

**Key Principle**: `copilot-setup-steps.yml` fetches fresh data before you start. The data is already in `data/` when you begin working.

---

## Your Workflow

When assigned an issue, execute these phases sequentially:

### Phase 1: Verify Data Availability

Check that required data exists:

```
data/
├── changes-summary.json    # What's new (REQUIRED)
├── metadata.json           # Version tracking
├── blog/*.json            # Blog posts with dates
├── docs/*.md              # Documentation files
├── videos/*.json          # Video metadata
├── trainings/*.json       # Training courses
└── github-next/*.json     # Experimental projects
```

**If `data/changes-summary.json` shows `has_changes: false`**: Report "No updates needed" and close the issue.

**If critical data is missing**: Report the missing sources. Do NOT speculate about content.

### Phase 2: Generate Content Files

Generate/update these 9 files in `content/` directory:

| File | Purpose |
|------|---------|
| README.md | Navigation hub with stats |
| GETTING-STARTED.md | Quick setup + best practices |
| WHATS-NEW.md | Last 30 days updates |
| VIDEOS.md | Categorized video library |
| EXPERIMENTAL.md | GitHub Next projects |
| TRAININGS.md | Courses & certifications |
| CHANGELOG.md | Complete timeline |
| COMMANDS.md | Quick reference |
| REFERENCE.md | Docs index |

**Workflow**:
1. Read `data/changes-summary.json` to identify what's new
2. Read new/updated data files
3. Generate each content file following the specifications below
4. Update "Last updated" timestamps

### Phase 3: Validate Quality

Run validation scripts:

```bash
# Validate dates and chronological ordering in WHATS-NEW.md
python3 scripts/validate_whats_new.py

# Validate all links
python3 scripts/validate_links.py
```

Fix any issues found before completing.

### Phase 4: Report Completion

Provide a summary:
- Files updated
- Count of new items (X blog posts, Y videos, Z trainings)
- Key content highlights
- Any issues encountered

---

## Content Specifications

### content/README.md
**Purpose**: Navigation hub and statistics (50-100 lines)

**Structure**:
- Welcome message
- Browse by Topic (links to all 8 other files)
- Current Stats (X updates, Y videos, Z trainings)
- Official Resources
- Last Updated timestamp

### content/GETTING-STARTED.md
**Purpose**: Onboarding + best practices (200-300 lines)

**Structure**:
- 5-minute quick setup (4 steps)
- 5-7 actionable best practices from recent blog posts
- Each tip: Problem/Solution format with code examples
- Source links for each tip
- Next steps links

### content/WHATS-NEW.md
**Purpose**: Recent updates from last 30 days (300-400 lines)

**Structure**:
- This Week (Last 7 Days): TOP 3-5 most significant
- This Month (Last 30 Days): TOP 10 most significant
- Older Updates (if relevant)
- Link to CHANGELOG.md

**CRITICAL Date Requirements**:
- ALL dates must be complete: "Dec 8, 2025" ✅
- NEVER incomplete: "Dec 2025" ❌
- Sort: newest first (reverse chronological)
- Use `data/blog/url_dates.json` for date lookups

### content/VIDEOS.md
**Purpose**: Categorized video library

**Categories** (check in this priority order):
1. **Getting Started** - "getting started", "intro", "introduction", "basics", "beginner"
2. **Features & Updates** - "feature", "announcement", "release", "introducing", "what's new"
3. **Tutorials** - "tutorial", "how to", "guide", "walkthrough", "demo"
4. **Agents** - "agent", "coding agent", "workspace agent", "autonomous", "agentic"
5. **Extensions** - "extension", "plugin", "integration", "api", "vscode", "jetbrains"
6. **Other** - Everything else

**Structure**:
- Statistics (total videos, recent uploads, categories)
- Recent Uploads (Last 30 Days) - newest first
- By Category - each with videos sorted by date

### content/EXPERIMENTAL.md
**Purpose**: GitHub Next experimental projects

**MANDATORY Requirements**:
```markdown
# 🔬 Experimental Features

> **About GitHub Next**: GitHub's research lab exploring future possibilities.
> These are experimental prototypes, not production features.

**⚠️ Important**: Projects here are research experiments. Many are discontinued.
They do not represent official product roadmap.

## Active Experiments

### 🧪 [Project Name] (Status: WIP)
Brief description emphasizing experimental nature.
→ [Try it out](url)

## Archived Experiments
[Completed or inactive projects]
```

**Language Rules**:
- ✅ Use: "exploring", "experimenting with", "research prototype"
- ❌ Avoid: "will launch", "coming soon", "official feature"

### content/TRAININGS.md
**Purpose**: Learning resources catalog (400-500 lines)

**Structure**:
- Official GitHub Courses (GitHub Skills)
- Microsoft Learn Modules
- Certifications
- Curated Courses (Udemy rating >= 4.5)
- Learning Paths (Beginner → Advanced)

### content/CHANGELOG.md
**Purpose**: Complete chronological history (unlimited)

**Structure**:
- Organized by month (newest first)
- Each entry: date, type, title, link
- Never remove old entries

### content/COMMANDS.md
**Purpose**: Quick reference (200-300 lines)

**Structure**:
- Slash commands table
- Keyboard shortcuts by IDE
- Chat variables table
- Chat participants table

### content/REFERENCE.md
**Purpose**: Documentation index (100-200 lines)

**Structure**:
- Docs grouped by category
- Brief descriptions
- Direct links to official docs

---

## Date Handling (CRITICAL)

For WHATS-NEW.md and CHANGELOG.md:

1. **Load date mapping**: Read `data/blog/url_dates.json`
2. **Look up dates**: For each blog URL, find ISO date (YYYY-MM-DD)
3. **Skip if missing**: Do NOT use incomplete dates
4. **Sort**: Newest first
5. **Format**: "Dec 8, 2025" (Month Day, Year - no leading zeros)

**Validation**:
- ✅ "Dec 8, 2025" - Complete
- ❌ "Dec 2025" - Missing day
- ❌ "December 2025" - Missing day

---

## Anchor Link Rules

GitHub strips emojis from anchor IDs. Do NOT use emojis in headings that are link targets.

```markdown
<!-- ✅ CORRECT -->
## Official GitHub Courses
[Jump](#official-github-courses)

<!-- ❌ WRONG -->
## 🎓 Official GitHub Courses
[Jump](#official-github-courses)  <!-- Link fails -->
```

---

## Link Validation

Run `python3 scripts/validate_links.py` after generating content.

**Categories**:
- **Real broken links**: Fix or remove
- **Template placeholders**: Ignore (in .github/ directories)
- **Redirects**: Update to canonical URL

**Quality**:
- Use relative paths for internal links
- Prefer HTTPS for external links
- Use canonical URLs

---

## Writing Style

**Clarity**:
- Clear, concise language
- Short paragraphs and bullet points
- Technical terms used correctly

**Developer-focused**:
- Action-oriented
- Concrete examples
- Always include "Last updated"
- Link to original sources

**Consistency**:
- Same terminology across files
- Consistent date formatting
- Consistent heading styles

---

## Quality Checklist

Before completing:

- [ ] All links properly formatted
- [ ] All dates complete (Month Day, Year)
- [ ] WHATS-NEW.md sorted newest to oldest
- [ ] GitHub Next content has disclaimers
- [ ] No emojis in anchor-targeted headings
- [ ] `python3 scripts/validate_whats_new.py` passes
- [ ] `python3 scripts/validate_links.py` passes
- [ ] "Last updated" timestamp current
- [ ] No duplicate entries

---

## Error Handling

**Missing data**: Report specifically what's missing. Do not speculate.

**Incomplete dates**: Use `data/blog/url_dates.json`. Skip articles with no date.

**GitHub Next disclaimers**: Always add experimental disclaimers. Never present as official.

**Broken links**: Fix in content files. Re-run validation to confirm.

---

## Python Environment

Python 3.11 is pre-configured via `.github/workflows/copilot-setup-steps.yml`:
- Dependencies from `requirements.txt` installed
- No manual venv activation needed

Available scripts:
- `python3 scripts/validate_links.py` - Link validation
- `python3 scripts/validate_whats_new.py` - Date/ordering validation

---

## Data Sources Reference

| Source | Location | Fields |
|--------|----------|--------|
| Blog posts | `data/blog/*.json` | title, url, date, summary, tags |
| Date mapping | `data/blog/url_dates.json` | URL → ISO date |
| Documentation | `data/docs/*.md` | Markdown with frontmatter |
| Videos | `data/videos/*.json` | video_id, title, url, date, description |
| Trainings | `data/trainings/*.json` | title, url, provider, level, format |
| GitHub Next | `data/github-next/*.json` | title, url, status, experimental:true |
| Changes | `data/changes-summary.json` | has_changes, new/updated lists |
