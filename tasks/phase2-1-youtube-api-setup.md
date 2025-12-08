# Task 2.1: Set Up YouTube Data API v3

**Phase**: 2 - YouTube Integration  
**Priority**: HIGH  
**Estimated Effort**: 1 hour  
**Assigned Agent**: GitHub Copilot Coding Agent

## Context
We need to fetch YouTube videos from GitHub's channel programmatically. YouTube provides RSS feeds, but the Data API v3 offers more metadata and filtering options. The free tier provides 10,000 quota units per day, which is sufficient for our needs.

## Objective
Set up YouTube Data API v3 access and prepare for video scraping.

## Tasks

### 1. Create Google Cloud Project
- Go to https://console.cloud.google.com/
- Create new project: "copilot-daily-digest"
- Note the project ID

### 2. Enable YouTube Data API v3
- Navigate to "APIs & Services" → "Library"
- Search for "YouTube Data API v3"
- Click "Enable"

### 3. Create API credentials
- Go to "APIs & Services" → "Credentials"
- Click "Create Credentials" → "API Key"
- Copy the API key
- (Optional) Restrict key to YouTube Data API v3
- (Optional) Add application restrictions (HTTP referrers or IP)

### 4. Add API key to GitHub Secrets
- Go to repository: Settings → Secrets and variables → Actions
- Create new secret: `YOUTUBE_API_KEY`
- Paste the API key

### 5. Add google-api-python-client to requirements
Update `requirements.txt`:
```txt
# Existing
requests>=2.31.0
beautifulsoup4>=4.12.0
lxml>=4.9.0
loguru>=0.7.0

# Phase 1 additions
feedparser>=6.0.10
python-dateutil>=2.8.2
pyyaml>=6.0.1

# Phase 2 - YouTube
google-api-python-client>=2.100.0
```

### 6. Create YouTube configuration file
Create `config/youtube.yml`:
```yaml
# YouTube API Configuration
api:
  version: "v3"
  service_name: "youtube"
  quota_limit: 10000  # Daily quota limit

channels:
  - id: "UC7c3Kb6jYCRj4JOHHZTxKsQ"  # @GitHub
    name: "GitHub"
    enabled: true
  
  # Optional channels (can enable later)
  - id: "UCs5Y5_7XK8HLDX0SLNwkd3w"  # @VisualStudioCode
    name: "Visual Studio Code"
    enabled: false
  
  - id: "UCrhJmfAGQ5K81XQ8_od1iTg"  # @MSFTReactor
    name: "Microsoft Reactor"
    enabled: false

filters:
  keywords:
    - "copilot"
    - "github copilot"
    - "ai"
    - "agent"
    - "coding agent"
    - "workspace"
    - "extensions"
  
  # Filter by days - only fetch videos from last N days
  max_age_days: 90
  
  # Filter by duration - skip very short videos (< 60s)
  min_duration_seconds: 60

output:
  directory: "data/videos"
  filename_format: "{date}_{video_id}.json"
```

### 7. Test API access
Create `scripts/test_youtube_api.py`:
```python
#!/usr/bin/env python3
"""Test YouTube API access"""

import os
from googleapiclient.discovery import build

def test_youtube_api():
    api_key = os.getenv("YOUTUBE_API_KEY")
    if not api_key:
        print("❌ YOUTUBE_API_KEY not found in environment")
        return False
    
    try:
        youtube = build("youtube", "v3", developerKey=api_key)
        
        # Test with a simple search
        request = youtube.search().list(
            part="snippet",
            channelId="UC7c3Kb6jYCRj4JOHHZTxKsQ",  # GitHub channel
            maxResults=1,
            type="video"
        )
        response = request.execute()
        
        print("✅ YouTube API working!")
        print(f"Test search returned {len(response.get('items', []))} results")
        return True
    
    except Exception as e:
        print(f"❌ YouTube API test failed: {e}")
        return False

if __name__ == "__main__":
    test_youtube_api()
```

### 8. Document quota usage
Create `docs/youtube-api-quota.md`:
```markdown
# YouTube API Quota Usage

## Daily Quota Limit
- Free tier: 10,000 units/day
- Resets at midnight Pacific Time (PT)

## Quota Costs (per operation)
- search().list: 100 units
- videos().list: 1 unit
- channels().list: 1 unit

## Our Usage Estimate
- Daily search for new videos: ~100 units
- Fetch video details (50 videos): ~50 units
- **Total**: ~150 units/day
- **Percentage**: 1.5% of daily quota

## Quota Management
- Check remaining quota: Console → APIs & Services → Dashboard
- Monitor usage in logs
- Alert if approaching 80% of daily limit
- Implement caching to reduce API calls

## Cost
- Free tier is sufficient for our needs
- No billing required unless quota exceeded
```

## Acceptance Criteria
- [ ] Google Cloud project created
- [ ] YouTube Data API v3 enabled
- [ ] API key created and secured
- [ ] API key added to GitHub Secrets as `YOUTUBE_API_KEY`
- [ ] `google-api-python-client` added to `requirements.txt`
- [ ] `config/youtube.yml` created with channel IDs and filters
- [ ] Test script confirms API access works
- [ ] Quota usage documented
- [ ] No API key exposed in code or logs

## Dependencies
None - can be done independently.

## Testing
```bash
# Install dependencies
pip install -r requirements.txt

# Set API key (locally)
export YOUTUBE_API_KEY="your-api-key-here"

# Test API access
python scripts/test_youtube_api.py

# Expected output:
# ✅ YouTube API working!
# Test search returned 1 results
```

## Security Notes
- **NEVER** commit API key to git
- Add `config/youtube-local.yml` to `.gitignore` for local testing
- Use GitHub Secrets for CI/CD
- Rotate key if accidentally exposed
- Consider adding IP/referrer restrictions in Google Cloud Console

## Reference Links
- [YouTube Data API Documentation](https://developers.google.com/youtube/v3)
- [API Key Best Practices](https://cloud.google.com/docs/authentication/api-keys)
- [Quota Calculator](https://developers.google.com/youtube/v3/determine_quota_cost)
