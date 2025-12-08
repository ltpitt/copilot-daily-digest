# Scripts Directory

This directory contains utility scripts for testing and maintenance.

## Available Scripts

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

## Adding New Scripts

When adding new scripts:
1. Use `#!/usr/bin/env python3` shebang
2. Add docstring explaining purpose
3. Make executable: `chmod +x scripts/your_script.py`
4. Document in this README
5. Follow existing error handling patterns
