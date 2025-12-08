# Migration Guide - Repository Restructuring

## Overview
This guide walks through the repository restructuring process for copilot-daily-digest.

## What's Changing

### Old Structure
```
copilot-daily-digest/
├── raw_docs/           # Scraped documentation
├── README.md           # Main digest
├── cheatsheet.md      # Copilot cheatsheet
└── changelog.md       # Changelog
```

### New Structure
```
copilot-daily-digest/
├── data/                          # All raw fetched data
│   ├── docs/                     # Documentation (from raw_docs/)
│   ├── blog/                     # Blog post data
│   ├── feeds/                    # RSS/Atom feed data
│   ├── videos/                   # YouTube metadata
│   ├── changelogs/               # Changelog data
│   └── metadata.json             # Change tracking (committed)
│
├── content/                       # Generated user-facing content
│   ├── README.md                 # Main digest (copied from root)
│   ├── cheatsheet.md            # Cheatsheet (copied from root)
│   └── changelog.md             # Changelog (copied from root)
│
└── templates/                     # Content generation templates
```

## Migration Steps

### Option 1: Automated Migration (Recommended)

Run the migration script from the repository root:

```bash
# Preview changes (dry run)
python migrate_structure.py --dry-run

# Apply migration
python migrate_structure.py
```

The script will:
1. Create new directory structure
2. Move `raw_docs/` → `data/docs/`
3. Copy content files to `content/` directory
4. Create `data/metadata.json`
5. Update `.gitignore`

### Option 2: Manual Migration

If you prefer to migrate manually:

```bash
# 1. Create directories
mkdir -p data/{docs,blog,feeds,videos,changelogs}
mkdir -p content templates

# 2. Add .gitkeep files
touch data/.gitkeep
touch data/docs/.gitkeep
touch data/blog/.gitkeep
touch data/feeds/.gitkeep
touch data/videos/.gitkeep
touch data/changelogs/.gitkeep
touch content/.gitkeep
touch templates/.gitkeep

# 3. Create metadata.json
cat > data/metadata.json << 'EOF'
{
  "last_updated": null,
  "content_hashes": {},
  "video_ids": [],
  "blog_urls": [],
  "doc_versions": {}
}
EOF

# 4. Move raw_docs to data/docs
if [ -d "raw_docs" ]; then
  mv raw_docs/* data/docs/ 2>/dev/null || true
  rmdir raw_docs 2>/dev/null || true
fi

# 5. Copy content files
cp README.md content/README.md 2>/dev/null || true
cp cheatsheet.md content/cheatsheet.md 2>/dev/null || true
cp changelog.md content/changelog.md 2>/dev/null || true

# 6. Update .gitignore (see below)
```

## Update .gitignore

Add these rules to `.gitignore`:

```gitignore
# Raw data (keep metadata and structure)
data/docs/*.md
data/blog/*.json
data/videos/*.json
data/feeds/*.xml

# Keep metadata
!data/metadata.json

# Keep directory structure  
!data/**/.gitkeep
```

## Post-Migration Tasks

After running the migration, you need to update file references:

### 1. Update Scripts

If `scraper/fetch_docs.py` exists:
- Change `raw_docs/` references to `data/docs/`

### 2. Update Workflows

If `.github/workflows/daily-agent.yml` exists:
- Update any paths referencing `raw_docs/`
- Update paths to reference `data/`, `content/`, `templates/`

### 3. Update Documentation

If `.github/copilot-instructions.md` exists:
- Update directory structure documentation
- Update path references

## Verification

After migration, verify everything works:

```bash
# Check git status
git status

# Verify directory structure
ls -la data/
ls -la content/
ls -la templates/

# Check metadata.json
cat data/metadata.json

# If scraper exists, test it
python scraper/fetch_docs.py

# Check .gitignore is working
git status data/
```

## Rollback

If something goes wrong, you can rollback:

```bash
# Discard all changes
git reset --hard HEAD

# Clean untracked files
git clean -fd
```

## Troubleshooting

### "Directory not empty" errors
- Some files may remain in `raw_docs/`. Check for hidden files: `ls -la raw_docs/`
- Manually remove or move remaining files

### ".gitignore not working"
- Cached files may still be tracked. Run: `git rm -r --cached data/`
- Then commit: `git add . && git commit -m "Update .gitignore"`

### "Script fails partway through"
- The script is idempotent - you can re-run it safely
- Check error message for specific issue
- Try dry-run mode first: `python migrate_structure.py --dry-run`

## Questions?

If you encounter issues, check:
1. Repository root is correct (contains `.git/`)
2. Python 3.6+ is installed
3. You have write permissions in the directory

For more help, open an issue on GitHub.
