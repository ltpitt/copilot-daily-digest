# Task 1.1: Restructure Repository Directories

**Phase**: 1 - Foundation & Infrastructure  
**Priority**: HIGH  
**Estimated Effort**: 1-2 hours  
**Assigned Agent**: `infrastructure-architect`

## Context
The repository currently has a flat structure with `raw_docs/` containing scraped content. We need to create a proper directory hierarchy to separate raw data, generated content, and templates.

## Objective
Create a well-organized directory structure that separates concerns:
- `data/` - All raw scraped/fetched content (some gitignored)
- `content/` - Generated user-facing markdown files
- `templates/` - Content generation templates for consistency

## Tasks

### 1. Create new directory structure
```
├── data/
│   ├── docs/
│   ├── blog/
│   ├── feeds/
│   ├── videos/
│   └── changelogs/
├── content/
└── templates/
```

### 2. Move existing content
- Move `raw_docs/` → `data/docs/`
- Move root-level `README.md`, `cheatsheet.md`, `changelog.md` → `content/`
- Update any references to old paths in scripts and workflows

### 3. Create placeholder files
- Add `data/.gitkeep` files for empty directories
- Create `data/metadata.json` with initial structure:
```json
{
  "last_updated": null,
  "content_hashes": {},
  "video_ids": [],
  "blog_urls": [],
  "doc_versions": {}
}
```

### 4. Update .gitignore
Add appropriate rules for data files:
```
# Raw data (keep metadata and structure)
data/docs/*.md
data/blog/*.json
data/videos/*.json
data/feeds/*.xml

# Keep metadata
!data/metadata.json
```

### 5. Update file references
- Update `scraper/fetch_docs.py` to use `data/docs/` instead of `raw_docs/`
- Update `.github/workflows/daily-agent.yml` paths
- Update `.github/copilot-instructions.md` to reference new structure

## Acceptance Criteria
- [ ] All new directories created with proper structure
- [ ] `raw_docs/` content moved to `data/docs/`
- [ ] Content files moved to `content/` directory
- [ ] `metadata.json` initialized in `data/`
- [ ] `.gitignore` updated to handle data files appropriately
- [ ] All scripts and workflows updated with new paths
- [ ] No broken file references remain
- [ ] Repository structure matches the diagram in ROADMAP.md

## Dependencies
None - this is the first task and enables all others.

## Testing
1. Run existing scraper: `python scraper/fetch_docs.py`
2. Verify files are created in correct locations
3. Run GitHub Actions workflow (dry run if possible)
4. Verify no path errors in logs

## Notes
- Keep this PR focused - only directory restructuring, no feature additions
- Ensure backward compatibility during transition
- Document the new structure in a comment on the PR
