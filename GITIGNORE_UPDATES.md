# .gitignore Updates for Repository Restructuring

## Lines to ADD to .gitignore

Add these lines to handle the new `data/` directory structure while keeping metadata and directory structure in git:

```gitignore
# Raw data (NEW structure - keep metadata and structure)
data/docs/*.md
data/docs/*.html
data/blog/*.json
data/videos/*.json
data/feeds/*.xml
data/feeds/*.json
data/changelogs/*.json

# Keep metadata and structure
!data/metadata.json
!data/**/.gitkeep
```

## Full Recommended .gitignore

If you want to replace the entire file, here's a complete version:

```gitignore
# Python
__pycache__/
*.pyc
*.pyo
*.py[cod]
*$py.class

# Virtual Environment
.venv/
venv/
env/

# Pytest
.pytest_cache/
.coverage

# Logs
*.log
scraper.log
logs/

# Temporary files
*.tmp
.temp/

# Raw documentation (OLD - for backward compatibility during transition)
raw_docs/*.md
raw_docs/*.html
!raw_docs/.gitkeep

# Raw data (NEW structure - keep metadata and structure)
data/docs/*.md
data/docs/*.html
data/blog/*.json
data/videos/*.json
data/feeds/*.xml
data/feeds/*.json
data/changelogs/*.json

# Keep metadata and structure
!data/metadata.json
!data/**/.gitkeep

# IDE
.vscode/
.idea/
*.swp

# OS
.DS_Store
Thumbs.db

# Environment variables
.env
.env.local
secrets.yml
```

## How to Apply

### Option 1: Manual Addition
Open `.gitignore` and add the lines under "Lines to ADD" section above.

### Option 2: Complete Replace
If you want the full recommended version, replace the entire `.gitignore` file with the "Full Recommended" version above.

### Option 3: Use Migration Script
The `migrate_structure.py` script will automatically update `.gitignore` with these rules.
