---
name: link-validation
description: Validate and fix broken links in markdown files. Use after editing content files, when links need verification, or when link errors are reported.
---

# Link Validation

Validate all internal and external links in content markdown files.

## Prerequisites

Python environment is auto-configured via `.github/workflows/copilot-setup-steps.yml`.

## Usage

```bash
python3 scripts/validate_links.py
```

## Output

Creates `link-validation-report.json` containing:

- `broken_links[]` - Array of broken links with:
  - `file` - File path containing the link
  - `line` - Line number
  - `url` - The broken URL
  - `error` - Error description
- `total_links` - Total links checked
- `valid_links` - Number of valid links

## Fix Process

1. Run validation script
2. Review `link-validation-report.json`
3. Categorize broken links:
   - **Real broken links** - External URLs returning 404, internal file paths that don't exist
   - **Template placeholders** - Example links in `.github/agents/`, docs/, tasks/ (ignore these)
   - **Redirects** - URLs that redirect (update to canonical URL)
4. Fix real broken links in `content/` files
5. Re-run validation to confirm all fixes

## Link Quality Guidelines

**Internal links:**
- Use relative paths from current file location
- From `content/README.md` to `content/STARTER-KIT.md`: use `STARTER-KIT.md`
- From `README.md` to `content/STARTER-KIT.md`: use `content/STARTER-KIT.md`
- Verify target file exists

**External links:**
- Prefer HTTPS over HTTP
- Use canonical URLs (avoid redirects)
- Link to stable, authoritative sources

## Important Notes

- Script validates both internal (relative) and external (HTTP/HTTPS) links
- Ignore template placeholders in agent documentation
- Focus on fixing links in `content/` directory
