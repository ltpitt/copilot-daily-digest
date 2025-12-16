# WHATS-NEW.md Validation Script

## Purpose

Validates `content/WHATS-NEW.md` for correct date formatting and chronological ordering.

Prevents issues like:
- Incomplete dates (e.g., "Dec 2025" without day)
- Incorrect article ordering (not newest-first)
- Articles in wrong sections (e.g., Dec 10 in "This Month" instead of "This Week")

## Checks Performed

### 1. Complete Dates ✓
Ensures all article dates include day, month, and year:

**✅ Valid:**
- "Dec 8, 2025"
- "Nov 6, 2025"

**❌ Invalid:**
- "Dec 2025" (missing day)
- "December 2025" (missing day)
- "2025-12-08" (ISO format in display)

### 2. Chronological Order ✓
Verifies articles are sorted newest to oldest:

**✅ Correct Order:**
```markdown
### Article A (Dec 12, 2025)  ← Newest
### Article B (Dec 11, 2025)
### Article C (Dec 10, 2025)  ← Oldest
```

**❌ Incorrect Order:**
```markdown
### Article A (Dec 10, 2025)  ← Older
### Article B (Dec 12, 2025)  ← Newer (wrong!)
```

### 3. Section Date Ranges ✓
Confirms articles are in correct sections based on dates:

- **"This Week"** = Last 7 days
- **"This Month"** = Days 8-30
- **"Older Updates"** = Older than 30 days

## Usage

```bash
cd /path/to/copilot-daily-digest
python3 scripts/validate_whats_new.py
```

## Exit Codes

- `0` - All validations passed ✅
- `1` - Validation errors found ❌

## Example Output

### Success
```
📋 Validating content/WHATS-NEW.md

✓ Found 11 articles
Checking for complete dates...
  ✓ All dates are complete
Checking chronological order...
  ✓ Articles are correctly ordered (newest first)
Checking section date ranges...
  ✓ All articles are in correct sections

✅ ALL VALIDATIONS PASSED
```

### Failure
```
📋 Validating content/WHATS-NEW.md

✓ Found 11 articles
Checking for complete dates...
  ❌ 2 incomplete date(s) found
Checking chronological order...
  ❌ 1 ordering issue(s) found
Checking section date ranges...
  ✓ All articles are in correct sections

❌ VALIDATION FAILED: 3 error(s) found

  • Line 44: Incomplete date 'Dec 2025' in 'Custom Agents'. Must include day (e.g., 'Dec 8, 2025')
  • Line 59: Incomplete date 'Dec 2025' in 'Mission Control'. Must include day (e.g., 'Dec 8, 2025')
  • Lines 30-44: Incorrect order. 'Article A' (Dec 3, 2025) should come AFTER 'Article B' (Dec 8, 2025). Articles must be sorted newest first.
```

## CI/CD Integration

Add to workflow before content generation:

```yaml
- name: Validate WHATS-NEW.md
  run: python3 scripts/validate_whats_new.py
```

Or as a pre-commit hook:

```bash
#!/bin/sh
python3 scripts/validate_whats_new.py
exit $?
```

## When to Run

- **Before committing** changes to WHATS-NEW.md
- **In CI/CD** before deploying content
- **After content generation** by agents
- **Manual review** when dates seem incorrect

## Related Files

- `content/WHATS-NEW.md` - File being validated
- `scraper/enrich_blog_dates.py` - Ensures dates are available
- `data/blog/url_dates.json` - Source of truth for blog dates
- `.github/agents/content-generator.agent.md` - Agent instructions for date formatting
- `.github/agents/publisher.agent.md` - Agent instructions for date validation

## Maintenance

This script requires no configuration or updates. It automatically:
- Detects current date for section validation
- Parses standard date formats
- Reports errors with line numbers and helpful messages

## Troubleshooting

**Problem**: Script reports "File not found"
- **Solution**: Run from repository root, not scripts directory

**Problem**: False positives for section dates
- **Solution**: Check system date is correct (script uses current date)

**Problem**: Script doesn't catch an issue
- **Solution**: File an issue with example - validation logic may need enhancement
