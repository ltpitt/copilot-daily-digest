# Task: Implement Monolithic Inline Agent Pattern

## Overview

Instead of delegating to external agents via issue assignment, run all agent logic inline within a single session using direct Python scripts and tool calls. This is the **currently working approach** used in manual execution.

## Prerequisites

- Python 3.11+ with virtual environment
- All dependencies from `requirements.txt` installed
- GitHub Actions with appropriate permissions

## Architecture

```
GitHub Actions Trigger
    ↓
Single Agent Session (GitHub Actions or VS Code Copilot)
    ↓
Direct Python Script Execution
    ├── Phase 1: Data Collection (6 scripts)
    ├── Phase 2: Change Detection (1 script)
    ├── Phase 3: Content Generation (read data → update markdown)
    ├── Phase 4: Content Validation (1 script)
    ├── Phase 5: Link Validation (1 script)
    └── Phase 6: Summary & Commit
```

## Implementation Steps

### Step 1: Create Orchestration Script

Create `scripts/run_full_workflow.py`:

```python
#!/usr/bin/env python3
"""
Monolithic workflow orchestrator.
Runs all phases sequentially without inter-agent delegation.
"""
import subprocess
import sys
import json
from pathlib import Path

def run_script(script_path: str) -> bool:
    """Run a Python script and return success status."""
    print(f"\n{'='*60}")
    print(f"Running: {script_path}")
    print('='*60)
    
    result = subprocess.run(
        [sys.executable, script_path],
        capture_output=False
    )
    return result.returncode == 0

def main():
    scripts_dir = Path(__file__).parent
    
    # Phase 1: Data Collection
    phase1_scripts = [
        "fetch_docs.py",
        "fetch_blog.py",
        "fetch_youtube.py",
        "fetch_trainings.py",
        "fetch_github_next.py",
        "enrich_blog_dates.py"
    ]
    
    print("\n" + "="*60)
    print("PHASE 1: DATA COLLECTION")
    print("="*60)
    
    for script in phase1_scripts:
        if not run_script(str(scripts_dir / script)):
            print(f"⚠️  Warning: {script} had issues (continuing)")
    
    # Phase 2: Change Detection
    print("\n" + "="*60)
    print("PHASE 2: CHANGE DETECTION")
    print("="*60)
    
    run_script(str(scripts_dir / "detect_changes.py"))
    
    # Load changes
    changes_file = scripts_dir.parent / "data" / "changes-summary.json"
    if changes_file.exists():
        with open(changes_file) as f:
            changes = json.load(f)
        total = changes.get("total_changes", 0)
        print(f"\n📊 Total changes detected: {total}")
        
        if total == 0:
            print("✅ No changes detected. Workflow complete.")
            return 0
    
    # Phase 3: Content Generation
    print("\n" + "="*60)
    print("PHASE 3: CONTENT GENERATION")
    print("="*60)
    print("Content generation requires AI assistance to properly format")
    print("Run this script, then manually update content files based on")
    print("the detected changes in data/changes-summary.json")
    
    # Phase 4: Content Validation
    print("\n" + "="*60)
    print("PHASE 4: CONTENT VALIDATION")
    print("="*60)
    
    run_script(str(scripts_dir / "validate_whats_new.py"))
    
    # Phase 5: Link Validation
    print("\n" + "="*60)
    print("PHASE 5: LINK VALIDATION")
    print("="*60)
    
    run_script(str(scripts_dir / "validate_links.py"))
    
    print("\n" + "="*60)
    print("WORKFLOW COMPLETE")
    print("="*60)
    print("Next steps:")
    print("1. Review content files for AI-generated updates")
    print("2. Commit changes: git add -A && git commit -m 'Daily digest update'")
    print("3. Push to remote: git push")
    
    return 0

if __name__ == "__main__":
    sys.exit(main())
```

### Step 2: Update GitHub Actions Workflow

Replace the issue-creation approach with direct execution:

```yaml
name: Daily Digest Update

on:
  schedule:
    - cron: '0 6 * * *'  # Daily at 6 AM UTC
  workflow_dispatch:

jobs:
  update-digest:
    runs-on: ubuntu-latest
    
    steps:
      - uses: actions/checkout@v4
      
      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.11'
      
      - name: Install dependencies
        run: pip install -r requirements.txt
      
      - name: Run data collection and change detection
        run: python scripts/run_full_workflow.py
      
      - name: Check for changes
        id: changes
        run: |
          if [ -n "$(git status --porcelain)" ]; then
            echo "has_changes=true" >> $GITHUB_OUTPUT
          else
            echo "has_changes=false" >> $GITHUB_OUTPUT
          fi
      
      - name: Commit and push
        if: steps.changes.outputs.has_changes == 'true'
        run: |
          git config user.name "github-actions[bot]"
          git config user.email "github-actions[bot]@users.noreply.github.com"
          git add -A
          git commit -m "📰 Daily digest update - $(date +'%Y-%m-%d')"
          git push
```

### Step 3: Add Content Generation Scripts

For automated content generation, create specialized scripts:

```python
# scripts/generate_whats_new.py
"""Generate WHATS-NEW.md from detected changes."""
# ... implementation based on data/changes-summary.json
```

## Advantages

✅ **Works now** - No API limitations or authentication complexity
✅ **Predictable** - Deterministic Python scripts with known behavior
✅ **Debuggable** - Full logs, can run locally
✅ **No secrets needed** - Uses standard `GITHUB_TOKEN`

## Disadvantages

❌ **No AI reasoning** - Content generation requires manual AI assistance
❌ **Less flexible** - Can't adapt to novel situations
❌ **Maintenance burden** - Changes require code updates

## When to Use

- When Copilot assignment API isn't available
- For deterministic, well-defined workflows
- When full automation is more important than AI flexibility

## Status

- [x] Orchestration script created (basic version)
- [ ] Full orchestration script with all phases
- [ ] Content generation scripts
- [ ] GitHub Actions workflow updated
- [ ] End-to-end test passed
