# File Reference Updates - Repository Restructuring

This document lists all file references that need to be updated after restructuring the repository.

## Files to Update

### 1. `scraper/fetch_docs.py`

**What to change:**
- Replace all references to `raw_docs/` with `data/docs/`

**Example changes:**
```python
# OLD
output_dir = "raw_docs/"
output_file = os.path.join("raw_docs", filename)

# NEW
output_dir = "data/docs/"
output_file = os.path.join("data", "docs", filename)
```

**Search for:**
- `raw_docs`
- `raw_docs/`
- `"raw_docs"`
- `'raw_docs'`

### 2. `.github/workflows/daily-agent.yml`

**What to change:**
- Update any paths that reference `raw_docs/`
- Add references to new `data/`, `content/`, `templates/` directories

**Example changes:**
```yaml
# OLD
- name: Check for changes
  run: |
    if [ -n "$(git status raw_docs/ --porcelain)" ]; then
      echo "changes=true" >> $GITHUB_OUTPUT
    fi

# NEW
- name: Check for changes
  run: |
    if [ -n "$(git status data/ --porcelain)" ]; then
      echo "changes=true" >> $GITHUB_OUTPUT
    fi
```

**Also add:**
```yaml
- name: Commit changes
  run: |
    git add data/metadata.json
    git add content/
    git commit -m "Update content" || echo "No changes"
```

### 3. `.github/copilot-instructions.md`

**What to change:**
- Update directory structure documentation
- Reference new `data/`, `content/`, `templates/` structure

**Add this structure documentation:**
```markdown
## Repository Structure

```
copilot-daily-digest/
├── data/                          # All raw fetched data (mostly gitignored)
│   ├── docs/                     # Scraped documentation
│   ├── blog/                     # Blog post data
│   ├── feeds/                    # RSS/Atom feed data
│   ├── videos/                   # YouTube metadata
│   ├── changelogs/               # Changelog data
│   └── metadata.json             # Change tracking (committed)
│
├── content/                       # Generated user-facing content
│   ├── README.md                 # Main digest
│   ├── cheatsheet.md            # Copilot cheatsheet
│   └── changelog.md             # Changelog
│
└── templates/                     # Content generation templates
```

## Data Sources

When referencing content:
- **Raw data**: Use `data/` subdirectories
- **Generated content**: Use `content/` directory
- **Templates**: Use `templates/` directory
```

### 4. Other Potential Files

Check these files if they exist:
- `README.md` - Update any structure diagrams
- `ROADMAP.md` - Update directory structure references
- `docs/` - Any documentation files
- Any Python scripts in `scripts/` directory
- Any other workflow files in `.github/workflows/`

## Automated Search

To find all references to `raw_docs`:

```bash
# Search in all files
grep -r "raw_docs" . --exclude-dir=.git

# Search in Python files
find . -name "*.py" -type f -exec grep -l "raw_docs" {} \;

# Search in YAML files
find . -name "*.yml" -o -name "*.yaml" -type f -exec grep -l "raw_docs" {} \;

# Search in Markdown files
find . -name "*.md" -type f -exec grep -l "raw_docs" {} \;
```

## Testing After Updates

After making these changes, test:

```bash
# 1. Run scraper (if exists)
python scraper/fetch_docs.py

# 2. Check output location
ls -la data/docs/

# 3. Verify git tracking
git status data/

# 4. Test workflow (if possible)
# Use GitHub Actions "Run workflow" button
```

## Checklist

- [ ] Updated `scraper/fetch_docs.py`
- [ ] Updated `.github/workflows/daily-agent.yml`
- [ ] Updated `.github/copilot-instructions.md`
- [ ] Updated `README.md` (if contains structure docs)
- [ ] Updated `ROADMAP.md` (if contains structure docs)
- [ ] Searched for all `raw_docs` references
- [ ] Tested scraper runs successfully
- [ ] Verified files go to correct location
- [ ] Tested workflow (if possible)
- [ ] Committed all changes
