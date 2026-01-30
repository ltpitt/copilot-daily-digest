---
name: content-validation
description: Validate generated content for quality issues. Use after content generation to check date formatting, chronological ordering, and link validity in markdown files.
---

# Content Validation

Validate generated content for common quality issues.

## Prerequisites

Python environment is auto-configured via `.github/workflows/copilot-setup-steps.yml`.

## Available Validators

### 1. WHATS-NEW.md Validation

Validates date formatting and chronological ordering in WHATS-NEW.md:

```bash
python3 scripts/validate_whats_new.py
```

**Checks:**
- All article dates are complete (Month Day, Year format)
- No incomplete dates like "Dec 2025" without day
- Articles sorted in reverse chronological order (newest first)
- Dates match their section (This Week, This Month, Older)

**Exit codes:**
- 0 = All validations passed
- 1 = Validation errors found

### 2. Link Validation

Validates all internal and external links:

```bash
python3 scripts/validate_links.py
```

See the link-validation skill for full details.

## When to Use

- After generating WHATS-NEW.md
- After editing content files
- Before creating pull requests
- When link errors are reported

## Typical Workflow

```bash
# Generate content
python3 scripts/generate_videos.py

# Validate dates and ordering
python3 scripts/validate_whats_new.py

# Validate all links
python3 scripts/validate_links.py

# Review any errors and fix
```

## Important Notes

- Run validators AFTER content generation
- Fix errors before committing
- Validators return non-zero exit codes on errors
