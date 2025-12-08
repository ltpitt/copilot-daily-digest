# Quick Start - Repository Restructuring

## TL;DR - Run This Command

```bash
bash quick_setup.sh
```

That's it! The script will handle the entire migration.

## What It Does

1. ✅ Creates new directory structure (data/, content/, templates/)
2. ✅ Moves raw_docs/ → data/docs/
3. ✅ Copies content files to content/
4. ✅ Creates metadata.json
5. ✅ Updates .gitignore
6. ✅ Updates scraper/fetch_docs.py (if exists)

## Alternative: Python Script

If you prefer Python or need more control:

```bash
# Preview changes
python migrate_structure.py --dry-run

# Run migration
python migrate_structure.py
```

## After Running

1. **Review changes:**
   ```bash
   git status
   git diff
   ```

2. **Update workflow** (if `.github/workflows/daily-agent.yml` exists):
   - Change `raw_docs/` → `data/`
   - See FILE_UPDATES.md for details

3. **Update copilot instructions** (if `.github/copilot-instructions.md` exists):
   - Update directory structure documentation
   - See FILE_UPDATES.md for details

4. **Test** (if scraper exists):
   ```bash
   python scraper/fetch_docs.py
   ls -la data/docs/
   ```

5. **Commit:**
   ```bash
   git add .
   git commit -m "Task 1.1: Restructure repository directories"
   git push
   ```

## Need Help?

- Detailed guide: See [MIGRATION.md](MIGRATION.md)
- File updates: See [FILE_UPDATES.md](FILE_UPDATES.md)
- Full summary: See [IMPLEMENTATION_SUMMARY.md](IMPLEMENTATION_SUMMARY.md)

## Troubleshooting

**Script fails?**
- Make sure you're in the repository root (where .git/ is)
- Check you have write permissions: `ls -la`
- Try the Python version: `python migrate_structure.py`

**Need to rollback?**
```bash
git reset --hard HEAD
git clean -fd
```
