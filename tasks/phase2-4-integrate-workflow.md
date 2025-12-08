# Task 2.4: Integrate YouTube with Main Workflow

**Phase**: 2 - YouTube Integration  
**Priority**: MEDIUM  
**Estimated Effort**: 1-2 hours  
**Assigned Agent**: GitHub Copilot Coding Agent

## Context
Now that we have YouTube scraping and video page generation working, we need to integrate these into the main GitHub Actions workflow and update the Copilot agent instructions to include video content.

## Objective
Integrate YouTube scraping into the daily workflow and ensure the Publisher agent uses video data when generating content.

## Tasks

### 1. Update GitHub Actions workflow
Edit `.github/workflows/daily-agent.yml`:

```yaml
name: Daily Copilot Digest

on:
  schedule:
    - cron: '0 13 * * *'  # Daily at 1 PM UTC
  workflow_dispatch:

jobs:
  fetch-and-detect:
    runs-on: ubuntu-latest
    
    steps:
      - uses: actions/checkout@v4
      
      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.11'
      
      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt
      
      # Fetch all content sources
      - name: Fetch GitHub Docs
        run: python scraper/fetch_docs.py
      
      - name: Fetch GitHub Blog (RSS)
        run: python scraper/fetch_blog.py
      
      - name: Fetch YouTube Videos (RSS)
        env:
          YOUTUBE_API_KEY: ${{ secrets.YOUTUBE_API_KEY }}
        run: python scraper/fetch_youtube.py
      
      # Detect changes
      - name: Detect Changes
        id: changes
        run: |
          python scraper/detect_changes.py > changes.txt
          cat changes.txt
          
          # Check if there are changes
          if grep -q "has_changes: true" data/changes-summary.json; then
            echo "HAS_CHANGES=true" >> $GITHUB_OUTPUT
          else
            echo "HAS_CHANGES=false" >> $GITHUB_OUTPUT
          fi
      
      # Commit data files
      - name: Commit Data Files
        if: steps.changes.outputs.HAS_CHANGES == 'true'
        run: |
          git config user.name "github-actions[bot]"
          git config user.email "github-actions[bot]@users.noreply.github.com"
          git add data/
          git commit -m "chore: update scraped data [$(date +'%Y-%m-%d')]"
          git push
      
      # Trigger Publisher Agent (only if changes detected)
      - name: Create Issue for Publisher Agent
        if: steps.changes.outputs.HAS_CHANGES == 'true'
        env:
          GH_TOKEN: ${{ secrets.GITHUB_TOKEN }}
        run: |
          # Read change summary
          SUMMARY=$(cat data/changes-summary.json | jq -r '.summary_text')
          
          # Create issue for Publisher agent
          gh issue create \
            --title "📰 Content Update Required - $(date +'%Y-%m-%d')" \
            --body "## Changes Detected

          $SUMMARY

          @copilot Please generate updated content files from the latest data in \`data/\` directory.

          **What to do:**
          1. Read all data from \`data/docs/\`, \`data/blog/\`, \`data/videos/\`
          2. Generate updated \`content/README.md\` (main digest)
          3. Generate updated \`content/changelog.md\` (feature timeline)
          4. Generate updated \`content/cheatsheet.md\` (quick reference)
          5. Generate updated \`content/videos.md\` (video library)
          6. Create a PR with all changes

          **Assigned to:** Publisher Agent" \
            --label "automation,content-update"
      
      - name: No Changes Detected
        if: steps.changes.outputs.HAS_CHANGES == 'false'
        run: echo "ℹ️ No changes detected. Skipping content generation."
```

### 2. Update Publisher agent instructions
Edit `.github/agents/publisher.agent.md`:

```markdown
---
name: Publisher Agent (Editor-in-Chief)
description: Synthesizes content from all data sources and generates user-facing documentation
tools: ["runSubagent", "read", "edit", "search"]
---

# Publisher Agent

You are the Editor-in-Chief for the GitHub Copilot Daily Digest. Your role is to synthesize content from multiple data sources and create engaging, well-organized documentation.

## Data Sources

Read content from these directories:
- `data/docs/` - GitHub documentation (5 files)
- `data/blog/` - GitHub Blog posts (JSON format)
- `data/videos/` - YouTube videos (JSON format)
- `data/changes-summary.json` - What's new summary

## Content to Generate

### 1. content/README.md (Main Digest)
- Overview of GitHub Copilot
- Recent updates and highlights (from changes-summary.json)
- Links to all other content pages
- Quick navigation

### 2. content/changelog.md
- Timeline of Copilot features and updates
- Organized by date (newest first)
- Include blog posts and documentation changes

### 3. content/cheatsheet.md
- Quick reference for commands and features
- Slash commands, variables, setup tips
- Organized by category

### 4. content/videos.md
- Use video data from data/videos/
- Categorize by topic
- Include "What's New This Week" section
- OR: Delegate to content-generator agent using runSubagent

## Workflow

1. **Read all data** from data/ directory
2. **Analyze changes** from data/changes-summary.json
3. **Delegate specialized tasks** using runSubagent:
   - Use content-generator for videos.md
   - Use youtube-specialist for video categorization
4. **Generate main content** (README, changelog, cheatsheet)
5. **Create comprehensive PR** with all updates

## Editorial Guidelines

- Write in a clear, professional tone
- Highlight new features prominently
- Use emojis sparingly but effectively (📰 🎥 ✨)
- Keep content scannable (headers, lists, bullets)
- Link to original sources
- Date all content updates

## Success Criteria

- All content files updated
- Changes accurately reflected
- PR includes clear summary
- No broken links or formatting issues
```

### 3. Update Copilot instructions
Edit `.github/copilot-instructions.md`:

Add section about video content:

```markdown
## Video Content

When generating video content (videos.md):
1. Read all JSON files from `data/videos/`
2. Categorize by topic (Getting Started, Features, Tutorials, Updates, Extensions, Agents)
3. Show "What's New This Week" at the top
4. Include thumbnail, title, date, duration, description for each video
5. Sort by date within categories (newest first)
6. Add statistics section (total videos, latest video, etc.)
```

### 4. Test the full workflow locally
Create `scripts/test_full_workflow.sh`:

```bash
#!/bin/bash
set -e

echo "🧪 Testing full workflow..."

# Step 1: Fetch all content
echo "📥 Step 1: Fetching content..."
python scraper/fetch_docs.py
python scraper/fetch_blog.py
python scraper/fetch_youtube.py

# Step 2: Detect changes
echo "🔍 Step 2: Detecting changes..."
python scraper/detect_changes.py

# Step 3: Check if changes detected
if grep -q '"has_changes": true' data/changes-summary.json; then
  echo "✅ Changes detected!"
  
  # Step 4: Generate content
  echo "📝 Step 3: Generating content..."
  python scraper/generate_videos.py
  # TODO: Add other content generators
  
  echo "✅ Workflow test complete!"
else
  echo "ℹ️  No changes detected. Skipping content generation."
fi
```

Make it executable:
```bash
chmod +x scripts/test_full_workflow.sh
```

### 5. Update documentation
Update `README.md` (root) or `STARTER-KIT.md`:

```markdown
## Daily Workflow

The repository updates automatically via GitHub Actions:

1. **Fetch Content** (Daily at 1 PM UTC)
   - GitHub Docs
   - GitHub Blog (RSS)
   - YouTube Videos (RSS)

2. **Detect Changes**
   - Compare with previous versions
   - Track what's new

3. **Generate Content** (if changes detected)
   - Publisher Agent creates issue
   - Agent generates all content files
   - Agent creates PR for review

4. **Review & Merge**
   - Review PR created by Publisher Agent
   - Merge when ready
```

## Acceptance Criteria
- [ ] `.github/workflows/daily-agent.yml` updated with YouTube scraping
- [ ] Workflow runs all scrapers in sequence
- [ ] Change detection determines if Publisher needed
- [ ] Issue created for Publisher Agent when changes detected
- [ ] No issue created when no changes detected
- [ ] Publisher agent instructions include video content
- [ ] Copilot instructions updated with video guidelines
- [ ] Test script works locally
- [ ] Documentation updated with workflow explanation
- [ ] Workflow can be triggered manually (workflow_dispatch)

## Dependencies
- Requires Tasks 2.1, 2.2, 2.3 (YouTube setup, scraper, generator)
- Requires Task 1.5 (change detection)
- Recommended: Task 5.1 (Publisher agent)

## Testing
```bash
# Test locally
./scripts/test_full_workflow.sh

# Test GitHub Actions workflow (manual trigger)
gh workflow run daily-agent.yml

# Monitor workflow
gh run list --workflow=daily-agent.yml

# View latest run
gh run view
```

## Notes
- Consider adding workflow status badge to README
- YouTube API key must be in GitHub Secrets
- Test with and without API key (RSS fallback)
- Ensure workflow completes in < 5 minutes
