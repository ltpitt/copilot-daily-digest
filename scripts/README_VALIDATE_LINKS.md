# Link Validation Script

Comprehensive link validation tool for markdown files in the repository.

## Overview

`validate_links.py` checks all links in markdown files and reports broken or invalid links. It validates both:
- **Internal links**: Relative paths to other files in the repository
- **External links**: HTTP/HTTPS URLs to external resources

## Features

- ✅ Validates markdown files in key directories (content, docs, scripts, tasks, .github)
- ✅ Tests internal relative links (file existence)
- ✅ Tests external HTTP/HTTPS links (HTTP status codes)
- ✅ Retry logic for flaky connections (3 retries with backoff)
- ✅ Detailed JSON report with broken link details
- ✅ Command-line summary with counts
- ✅ Exit code 0 (all valid) or 1 (broken links found)

## Usage

### Basic Usage

```bash
# Run from repository root
python3 scripts/validate_links.py
```

### Example Output

```
Link Validation Script
======================================================================
Base path: /home/runner/work/copilot-daily-digest/copilot-daily-digest

Found 47 markdown files to check

Checking: README.md
  ✓ Line 25: content/README.md
  ✓ Line 26: content/STARTER-KIT.md
  ✗ Line 229: https://example.com/broken - HTTP 404

...

======================================================================
LINK VALIDATION REPORT
======================================================================
Files checked:     47
Total links:       341
Internal links:    93
External links:    191
Valid links:       235
Broken links:      3
Skipped links:     57

BROKEN LINKS:
----------------------------------------------------------------------

File: README.md:229
Type: external
URL:  https://example.com/broken
Error: HTTP 404

======================================================================
```

## Report File

The script generates `link-validation-report.json` with detailed information:

```json
{
  "total_files": 47,
  "total_links": 341,
  "internal_links": 93,
  "external_links": 191,
  "valid_links": 235,
  "broken_links": [
    {
      "file": "README.md",
      "line": 229,
      "url": "https://example.com/broken",
      "text": "Example Link",
      "error": "HTTP 404",
      "type": "external"
    }
  ],
  "skipped_links": 57
}
```

## What Gets Validated

### Directories Checked
- `content/` - Generated content files
- `docs/` - Documentation
- `scraper/` - Scraper documentation
- `scripts/` - Script documentation
- `tasks/` - Task documentation
- `.github/` - GitHub configuration and agent files
- Root markdown files (README.md, etc.)

### Link Types

**Internal Links** (relative paths):
- `./file.md` - Relative to current directory
- `../file.md` - Relative to parent directory
- `content/file.md` - Relative path
- Checks if target file exists on disk

**External Links** (HTTP/HTTPS):
- `https://example.com/page` - Full URL
- Tests HTTP status code (HEAD request, fallback to GET)
- Follows redirects
- Reports 4xx/5xx errors

### Skipped Links
- Internal anchors only: `#section`
- Email links: `mailto:user@example.com`
- Phone links: `tel:+1234567890`

## Template Placeholders

Some files contain example link formats (not actual links):
- `.github/agents/` - Agent instruction examples
- `docs/` - Documentation templates
- `tasks/` - Task templates

Common placeholders that are **intentionally not real links**:
- `url` - Generic URL placeholder
- `link` - Generic link placeholder
- `thumbnail_url` - Image placeholder
- `image-url` - Image placeholder

These are reported as "broken" but should be **ignored** as they're documentation examples.

## Integration

### GitHub Actions

Add to `.github/workflows/daily-agent.yml`:

```yaml
- name: Validate Links
  run: |
    python3 scripts/validate_links.py
    if [ $? -ne 0 ]; then
      echo "⚠️ Broken links found - see link-validation-report.json"
      # Don't fail the build, just warn
    fi
```

### Pre-commit Hook

Create `.git/hooks/pre-commit`:

```bash
#!/bin/bash
python3 scripts/validate_links.py
if [ $? -ne 0 ]; then
  echo "Warning: Broken links detected"
  echo "Run: python3 scripts/validate_links.py"
  # Allow commit but warn
fi
```

### Manual Checks

Before merging PRs with markdown changes:

```bash
# Validate all links
python3 scripts/validate_links.py

# Review broken links
cat link-validation-report.json | python3 -m json.tool | grep -A 10 broken_links

# Fix broken links, then re-validate
python3 scripts/validate_links.py
```

## Troubleshooting

### Timeouts

If external links timeout frequently:
- Increase `TIMEOUT` constant in script (default: 10 seconds)
- Increase `MAX_RETRIES` constant (default: 3)

### False Positives

Some sites block HEAD requests:
- Script automatically falls back to GET request
- If still failing, the URL may block automated tools

### SSL Errors

For SSL certificate issues:
- Check if certificate is valid
- May need to update `certifi` package

## Dependencies

Required Python packages:
- `requests` - HTTP library
- `urllib3` - URL handling

Install via:
```bash
pip install -r requirements.txt
```

## Exit Codes

- `0` - All links are valid
- `1` - One or more broken links found

Use in scripts:
```bash
python3 scripts/validate_links.py
if [ $? -eq 0 ]; then
  echo "All links valid"
else
  echo "Broken links found"
  exit 1
fi
```
