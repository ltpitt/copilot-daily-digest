# YouTube API Quota Usage

## Overview

This project uses **YouTube RSS feeds by default** (no API key needed, no quota limits).

The YouTube Data API v3 is **OPTIONAL** and only used for enrichment when:
- You want video duration, view counts, like counts
- You need advanced filtering beyond RSS capabilities
- You want to fetch older videos beyond the RSS feed limit (last ~15 videos)

## Daily Quota Limit

**Free tier**: 10,000 units/day
- Resets at midnight Pacific Time (PT)
- Sufficient for our needs (we use ~1.5% per day)
- No billing required

## Quota Costs (per operation)

| Operation | Cost | Our Usage |
|-----------|------|-----------|
| `search().list` | 100 units | 1-2 times/day |
| `videos().list` | 1 unit per video | 50-100 videos/day |
| `channels().list` | 1 unit | Rarely used |

## Our Usage Estimate

**Daily RSS-only mode (default)**:
- Cost: 0 units (RSS feeds are free)
- Frequency: Multiple times per day
- **Total**: 0 units/day

**Daily API enrichment mode (optional)**:
- Search for new videos: 1-2 × 100 = 100-200 units
- Fetch video details (50 videos avg): 50 × 1 = 50 units
  - Note: Estimate based on GitHub channel posting ~1-3 videos/week
  - Actual usage depends on channels enabled and posting frequency
- **Total**: ~150-250 units/day
- **Percentage**: 1.5-2.5% of daily quota

## Quota Management

### Check Remaining Quota
1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Navigate to: APIs & Services → Dashboard
3. Click on "YouTube Data API v3"
4. View quota usage graph

### Monitor Usage
- Check logs for API call counts
- Alert if approaching 80% of daily limit (8,000 units)
- Implement caching to reduce repeated calls
- Use RSS feeds when possible

### Rate Limiting Strategy
```python
# Example: Check quota before API calls
if get_api_calls_today() > 8000:
    # Fall back to RSS-only mode
    use_rss_only()
else:
    # Safe to use API enrichment
    use_api_enrichment()
```

## Cost Analysis

**Free tier is sufficient** because:
- RSS provides 90% of needed data
- API only used for optional enrichment
- We're well under quota limits
- No billing setup required

**If quota exceeded**:
- Project automatically falls back to RSS-only mode
- No data loss, just less metadata
- Quota resets at midnight PT

## Best Practices

1. **Use RSS feeds first** (default behavior)
2. **Enable API enrichment only when needed**
3. **Cache API responses** to avoid duplicate calls
4. **Batch API requests** when possible
5. **Monitor quota usage** in Google Cloud Console
6. **Implement graceful degradation** (RSS fallback)
7. **Don't commit API keys** to version control

## Setting Up API Access (Optional)

Only needed if you want API enrichment features:

### 1. Create Google Cloud Project
- Go to https://console.cloud.google.com/
- Create new project: "copilot-daily-digest"
- Note the project ID

### 2. Enable YouTube Data API v3
- Navigate to "APIs & Services" → "Library"
- Search for "YouTube Data API v3"
- Click "Enable"

### 3. Create API Credentials
- Go to "APIs & Services" → "Credentials"
- Click "Create Credentials" → "API Key"
- Copy the API key
- (Recommended) Restrict key to YouTube Data API v3
- (Recommended) Add IP restrictions for production

### 4. Add API Key to GitHub Secrets
- Go to repository: Settings → Secrets and variables → Actions
- Create new secret: `YOUTUBE_API_KEY`
- Paste the API key

### 5. Enable API in Config
Edit `config/youtube.yml`:
```yaml
api:
  enabled: true  # Change from false to true
```

### 6. Test API Access
```bash
# Install dependencies
pip install -r requirements.txt

# Set API key (locally)
export YOUTUBE_API_KEY="your-api-key-here"

# Test API access
python scripts/test_youtube_api.py

# Expected output:
# ✅ YouTube API working!
# ✅ Test search returned 1 results
```

## Security Notes

- **NEVER** commit API key to git
- Use environment variables or GitHub Secrets
- Rotate key if accidentally exposed
- Add IP/referrer restrictions in Google Cloud Console
- Monitor for unusual usage patterns
- Local config override: `config/youtube-local.yml` (gitignored)

## Reference Links

- [YouTube Data API Documentation](https://developers.google.com/youtube/v3)
- [Quota Calculator](https://developers.google.com/youtube/v3/determine_quota_cost)
- [API Key Best Practices](https://cloud.google.com/docs/authentication/api-keys)
- [RSS Feed Format](https://developers.google.com/youtube/v3/guides/using_rss_feeds)
