---
name: change-detection
description: Detect meaningful changes in collected data to determine if content updates are needed. Use after data collection to identify new/updated docs, blog posts, videos, and trainings.
---

# Change Detection

Detect what's new in collected data by comparing against previous metadata.

## Prerequisites

Python environment is auto-configured via `.github/workflows/copilot-setup-steps.yml`.

## Usage

```bash
python3 scripts/detect_changes.py
```

## Output

Creates `data/changes-summary.json` with:

- `has_changes` (boolean) - Whether any changes detected
- `new_docs` (array) - New or updated documentation files
- `new_blog_posts` (array) - New blog posts
- `new_videos` (array) - New YouTube videos
- `new_trainings` (array) - New training courses
- `counts` (object) - Total counts by type

## Decision Making

Check if content update is needed:

```bash
# Check for changes
if grep -q '"has_changes": true' data/changes-summary.json; then
  echo "Changes detected - proceed with content generation"
else
  echo "No changes - skip content update"
fi
```

## How It Works

Script compares current data against `data/metadata.json`:
- Docs: Compares file hashes
- Blog: Compares URLs
- Videos: Compares video IDs
- Trainings: Compares training IDs

## Important Notes

- Run AFTER data collection completes
- Script updates `data/metadata.json` with new hashes/IDs
- Deterministic: Same data state = same detection result
