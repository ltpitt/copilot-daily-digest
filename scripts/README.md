# Scripts Directory

This directory contains utility scripts for testing and maintenance.

## Available Scripts

### `test_copilot_assignment.sh`

Tests the complete workflow for automatic copilot issue assignment.

**Purpose**: Verify that the automatic assignment of issues to @copilot works correctly.

**Usage**:
```bash
# Ensure gh CLI is authenticated
gh auth login

# Run the test
./scripts/test_copilot_assignment.sh
```

**What it does**:
1. Creates a test issue
2. Assigns it to @copilot
3. Verifies the assignment
4. Waits for potential PR creation by copilot
5. Cleans up any created PRs and branches
6. Closes the test issue
7. Verifies repository is in clean state

**Expected Output**:
```
🧪 Testing Copilot Issue Assignment Workflow
==============================================

✓ gh CLI is installed and authenticated
✓ Created issue #123: https://github.com/ltpitt/copilot-daily-digest/issues/123
✓ Issue assigned to @copilot
✓ Issue is correctly assigned to copilot
...
✅ Test workflow completed successfully!
```

**See also**: `docs/COPILOT_ASSIGNMENT_TESTING.md` for detailed testing documentation.

### `test_full_workflow.sh`

Tests the complete data fetching and change detection workflow.

**Usage**:
```bash
./scripts/test_full_workflow.sh
```

### `test_youtube_api.py`

Tests YouTube Data API v3 connectivity.

**Purpose**: Verify that your API key (if configured) is working correctly.

**Note**: This is OPTIONAL - the project works with RSS feeds by default. The API is only needed for enrichment features (duration, view counts, etc).

**Usage**:
```bash
# Set API key (optional)
export YOUTUBE_API_KEY="your-api-key-here"

# Run test
python scripts/test_youtube_api.py
```

**Expected Output (without API key)**:
```
⚠️  YOUTUBE_API_KEY not found in environment
ℹ️  This is OPTIONAL - the project works with RSS feeds by default
ℹ️  API is only needed for enrichment (duration, view counts, etc)
```

**Expected Output (with API key)**:
```
✅ YouTube API working!
✅ Test search returned 1 results
✅ Sample video: [Video Title]
```

### `validate_links.py`

Validates all links in content markdown files.

**Purpose**: Ensure all internal and external links are working.

**Usage**:
```bash
python scripts/validate_links.py
```

**See also**: `scripts/README_VALIDATE_LINKS.md`

### `validate_whats_new.py`

Validates the WHATS-NEW.md file for freshness and correctness.

**Purpose**: Ensure WHATS-NEW.md only contains recent updates (last 30 days).

**Usage**:
```bash
python scripts/validate_whats_new.py
```

**See also**: `scripts/README_VALIDATE_WHATS_NEW.md`

## Adding New Scripts

When adding new scripts:
1. Use `#!/usr/bin/env python3` or `#!/bin/bash` shebang
2. Add docstring/comments explaining purpose
3. Make executable: `chmod +x scripts/your_script.sh`
4. Document in this README
5. Follow existing error handling patterns

