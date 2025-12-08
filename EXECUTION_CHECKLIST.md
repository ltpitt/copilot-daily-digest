# Task 1.1 Execution Checklist

This checklist tracks the execution of repository restructuring Task 1.1.

## Pre-Migration Checklist

- [ ] Repository is at `/home/runner/work/copilot-daily-digest/copilot-daily-digest`
- [ ] Working directory is repository root
- [ ] No uncommitted changes (run `git status`)
- [ ] Current branch noted (for rollback if needed)

## Migration Execution

### Option A: Quick Setup (Recommended)
- [ ] Run: `bash quick_setup.sh`
- [ ] Review output for errors
- [ ] Verify completion message

### Option B: Python Script
- [ ] Run: `python migrate_structure.py --dry-run` (preview)
- [ ] Review preview output
- [ ] Run: `python migrate_structure.py` (execute)
- [ ] Verify completion message

## Post-Migration Verification

### 1. Directory Structure
- [ ] `data/` directory exists
- [ ] `data/docs/` directory exists (contains files from old raw_docs/)
- [ ] `data/blog/` directory exists
- [ ] `data/feeds/` directory exists
- [ ] `data/videos/` directory exists
- [ ] `data/changelogs/` directory exists
- [ ] `content/` directory exists (contains copied content files)
- [ ] `templates/` directory exists
- [ ] All directories have `.gitkeep` files

### 2. Files
- [ ] `data/metadata.json` exists and is valid JSON
- [ ] `content/README.md` exists (if root README.md existed)
- [ ] `content/cheatsheet.md` exists (if root cheatsheet.md existed)
- [ ] `content/changelog.md` exists (if root changelog.md existed)
- [ ] old `raw_docs/` directory removed or empty

### 3. Git Status
- [ ] Run: `git status`
- [ ] Verify new directories are tracked
- [ ] Verify `data/metadata.json` is tracked
- [ ] Verify data files are ignored (if any exist)
- [ ] Verify `.gitkeep` files are tracked

### 4. .gitignore
- [ ] `.gitignore` contains rules for `data/docs/*.md`
- [ ] `.gitignore` contains rules for `data/blog/*.json`
- [ ] `.gitignore` contains rules for `data/videos/*.json`
- [ ] `.gitignore` contains rules for `data/feeds/*.xml`
- [ ] `.gitignore` contains exception for `!data/metadata.json`
- [ ] `.gitignore` contains exception for `!data/**/.gitkeep`

## File Reference Updates

### scraper/fetch_docs.py (if exists)
- [ ] File exists at `scraper/fetch_docs.py`
- [ ] Search for `raw_docs` references: `grep -n "raw_docs" scraper/fetch_docs.py`
- [ ] Replace all `raw_docs` with `data/docs`
- [ ] Verify no remaining `raw_docs` references

### .github/workflows/daily-agent.yml (if exists)
- [ ] File exists at `.github/workflows/daily-agent.yml`
- [ ] Search for `raw_docs` references: `grep -n "raw_docs" .github/workflows/daily-agent.yml`
- [ ] Update paths to use new structure
- [ ] Add `data/metadata.json` to commit steps
- [ ] Verify workflow syntax: `yaml validate` or similar

### .github/copilot-instructions.md (if exists)
- [ ] File exists at `.github/copilot-instructions.md`
- [ ] Search for `raw_docs` references: `grep -n "raw_docs" .github/copilot-instructions.md`
- [ ] Update directory structure documentation
- [ ] Add new `data/`, `content/`, `templates/` structure
- [ ] Verify formatting

### Global Search
- [ ] Run: `grep -r "raw_docs" . --exclude-dir=.git --exclude-dir=data`
- [ ] Review all found references
- [ ] Update or verify each reference
- [ ] Confirm no unintended references remain

## Testing

### If scraper exists
- [ ] Run: `python scraper/fetch_docs.py`
- [ ] Check for errors
- [ ] Verify output goes to `data/docs/`
- [ ] Check `data/docs/` contents: `ls -la data/docs/`
- [ ] Verify files are properly ignored by git

### If workflow exists
- [ ] Trigger workflow manually (GitHub Actions → Run workflow)
- [ ] Monitor workflow execution
- [ ] Check logs for path errors
- [ ] Verify workflow completion
- [ ] Check committed changes

### Git Tracking
- [ ] Run: `git status`
- [ ] Verify `data/metadata.json` is tracked
- [ ] Verify `.gitkeep` files are tracked
- [ ] Verify data files are ignored (if any exist)
- [ ] Run: `git diff --cached` to review changes

## Final Commit

- [ ] Review all changes: `git status`
- [ ] Review diff: `git diff`
- [ ] Stage all changes: `git add .`
- [ ] Verify staged: `git status`
- [ ] Commit with message:
  ```
  Task 1.1: Restructure repository directories
  
  - Created new directory structure (data/, content/, templates/)
  - Moved raw_docs/ → data/docs/
  - Copied content files to content/
  - Created metadata.json for change tracking
  - Updated .gitignore for new structure
  - Updated file references in scripts and workflows
  ```
- [ ] Push: `git push origin <branch>`

## Acceptance Criteria Verification

Per issue requirements:

- [ ] All new directories created with proper structure
- [ ] `raw_docs/` content moved to `data/docs/`
- [ ] Content files moved to `content/` directory
- [ ] `metadata.json` initialized in `data/`
- [ ] `.gitignore` updated to handle data files appropriately
- [ ] All scripts and workflows updated with new paths
- [ ] No broken file references remain
- [ ] Repository structure matches the diagram in ROADMAP.md

## Rollback Plan (if needed)

If something goes wrong:

```bash
# Discard all changes
git reset --hard HEAD

# Clean untracked files and directories
git clean -fd

# Verify clean state
git status
```

## Sign-Off

- [ ] All checklist items completed
- [ ] All tests passing
- [ ] No errors in logs
- [ ] Changes pushed to repository
- [ ] Task marked as complete

**Completed by:** ________________  
**Date:** ________________  
**Commit SHA:** ________________

## Notes

Use this space for any issues encountered or special notes:

```
[Add notes here]
```
