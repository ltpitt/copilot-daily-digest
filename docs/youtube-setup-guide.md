# YouTube Data API v3 Setup Guide

This guide walks you through setting up YouTube Data API v3 access for the copilot-daily-digest project.

## ⚠️ Important: API is OPTIONAL

The project works perfectly with **YouTube RSS feeds by default** (no API key needed). The API is only used for optional enrichment features like:
- Video duration filtering
- View counts and engagement metrics  
- Extended video metadata

**You can skip this setup** if you don't need these features.

---

## Quick Status Check

### ✅ Already Completed (Code Setup)
All code and configuration files are already in place:
- ✅ `requirements.txt` includes `google-api-python-client>=2.100.0`
- ✅ `config/youtube.yml` configured with GitHub channel
- ✅ `scripts/test_youtube_api.py` test script created
- ✅ `docs/youtube-api-quota.md` quota documentation
- ✅ Directory structure created (`data/videos/`)
- ✅ `.gitignore` configured for security

### ⚠️ Manual Steps Needed (Your Action Required)
You need to complete these steps in Google Cloud Console and GitHub:
1. Create Google Cloud project
2. Enable YouTube Data API v3
3. Create API credentials
4. Add API key to GitHub Secrets

---

## Step-by-Step Manual Setup

### Step 1: Create Google Cloud Project

1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Sign in with your Google account
3. Click "Select a project" → "New Project"
4. Enter project details:
   - **Project name**: `copilot-daily-digest`
   - **Organization**: (optional, leave as "No organization")
5. Click **"Create"**
6. Wait for project creation (takes a few seconds)
7. Note your **Project ID** (shown after creation)

### Step 2: Enable YouTube Data API v3

1. In Google Cloud Console, ensure your project is selected
2. Navigate to: **"APIs & Services"** → **"Library"**
   - Or use direct link: https://console.cloud.google.com/apis/library
3. In the search box, type: `YouTube Data API v3`
4. Click on **"YouTube Data API v3"** from the results
5. Click the **"Enable"** button
6. Wait for API to be enabled (takes a few seconds)

### Step 3: Create API Credentials

1. Navigate to: **"APIs & Services"** → **"Credentials"**
   - Or use direct link: https://console.cloud.google.com/apis/credentials
2. Click **"Create Credentials"** → **"API Key"**
3. A dialog appears showing your new API key
4. **Copy the API key** (you'll need it in Step 4)
5. Click **"Edit API key"** to add security restrictions (recommended)

#### Recommended Security Settings

Add these restrictions to your API key for better security:

**API restrictions:**
- Select: **"Restrict key"**
- Check: **"YouTube Data API v3"**
- Click **"OK"**

**Application restrictions (optional but recommended):**
- For local development: No restrictions
- For GitHub Actions: Add GitHub Actions IP ranges
- For production: Add your server's IP addresses

6. Click **"Save"**

### Step 4: Add API Key to GitHub Secrets

1. Go to your GitHub repository: `ltpitt/copilot-daily-digest`
2. Navigate to: **Settings** → **Secrets and variables** → **Actions**
   - Or use direct link: https://github.com/ltpitt/copilot-daily-digest/settings/secrets/actions
3. Click **"New repository secret"**
4. Enter secret details:
   - **Name**: `YOUTUBE_API_KEY`
   - **Secret**: (paste the API key from Step 3)
5. Click **"Add secret"**

**Security Note**: The API key is now securely stored and will be available to GitHub Actions workflows.

---

## Verification Steps

### Test Locally (Optional)

If you want to test the API access on your local machine:

```bash
# Navigate to project directory
cd /path/to/copilot-daily-digest

# Install dependencies (if not already installed)
pip install -r requirements.txt

# Set API key as environment variable
export YOUTUBE_API_KEY="your-api-key-here"

# Run test script
python scripts/test_youtube_api.py
```

**Expected output:**
```
✅ YouTube API working!
✅ Test search returned 1 results
✅ Sample video: [video title]
```

### Test in GitHub Actions

The API will be automatically used by GitHub Actions workflows when:
1. The `YOUTUBE_API_KEY` secret is set (Step 4 completed)
2. The workflow runs on schedule or manually
3. The YouTube fetching script executes

You can monitor workflow runs at:
https://github.com/ltpitt/copilot-daily-digest/actions

---

## Troubleshooting

### ❌ "API key not found in environment"
- **Local**: Make sure you exported `YOUTUBE_API_KEY` in your terminal
- **GitHub Actions**: Verify the secret is added in repository settings

### ❌ "YouTube API test failed: API key not valid"
- Verify you copied the entire API key (no spaces or truncation)
- Check that YouTube Data API v3 is enabled in Google Cloud Console
- Wait a few minutes for API key activation (can take 1-5 minutes)

### ❌ "Quota exceeded"
- Check quota usage in Google Cloud Console
- Our usage is ~150 units/day (1.5% of 10,000 quota)
- Quota resets at midnight Pacific Time
- If repeatedly exceeded, consider adding more filtering in `config/youtube.yml`

### ❌ "This API project is not authorized to use this API"
- Ensure YouTube Data API v3 is enabled (Step 2)
- Try disabling and re-enabling the API
- Create a new API key if issue persists

---

## Quota Management

### Free Tier Limits
- **Daily quota**: 10,000 units/day
- **Cost per search**: 100 units
- **Cost per video detail**: 1 unit
- **Our usage**: ~150 units/day (1.5% of quota)

### Monitor Usage
1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Navigate to: **APIs & Services** → **Dashboard**
3. Click on **"YouTube Data API v3"**
4. View quota usage graphs

### Best Practices
- ✅ Use RSS feeds as primary data source (already implemented)
- ✅ Use API only for enrichment (already implemented)
- ✅ Cache API responses to avoid duplicates
- ✅ Monitor quota in Google Cloud Console
- ✅ Alert if approaching 80% of quota (8,000 units)

---

## Security Best Practices

### ✅ What We've Done
- API key stored in GitHub Secrets (encrypted)
- Never committed to version control
- Local config files gitignored (`config/*-local.yml`)
- Test script doesn't log API key
- Graceful fallback to RSS if API unavailable

### ✅ What You Should Do
- Restrict API key to YouTube Data API v3 only
- Add IP restrictions if using from fixed locations
- Rotate API key if accidentally exposed
- Monitor API usage for anomalies
- Use separate API keys for dev/prod

### 🚨 If API Key Is Compromised
1. Immediately delete the API key in Google Cloud Console
2. Create a new API key
3. Update GitHub Secret with new key
4. Review API usage logs for unauthorized access
5. Enable stricter restrictions on new key

---

## Cost Analysis

### Free Tier (Current Usage)
- **Cost**: $0/month
- **Quota**: 10,000 units/day
- **Our usage**: ~150 units/day
- **Percentage**: 1.5% of quota
- **Sufficient**: ✅ Yes

### If Quota Is Exceeded
- **Additional units**: $0.0004 per unit after 10,000
- **Example**: 20,000 units/day = $4/month
- **Not needed**: Our usage is well within free tier

**Recommendation**: Free tier is more than sufficient. No billing setup needed.

---

## Next Steps After Setup

Once you've completed the manual steps:

1. ✅ API key is in GitHub Secrets
2. ✅ GitHub Actions workflows can access YouTube API
3. ✅ Video scraping will include enriched metadata
4. ✅ Quota monitoring is available in Google Cloud Console

### Enable API Enrichment

Edit `config/youtube.yml` and set:
```yaml
api:
  enabled: true  # Change from false to true
```

Commit and push this change to enable API features.

### What Happens Next

The daily automation workflow will:
1. Fetch videos from RSS feeds (primary method)
2. Use API to enrich with duration, views, etc. (if enabled)
3. Filter videos based on keywords and age
4. Save metadata to `data/videos/`
5. Generate content pages

---

## Reference Links

- [YouTube Data API v3 Documentation](https://developers.google.com/youtube/v3)
- [API Key Best Practices](https://cloud.google.com/docs/authentication/api-keys)
- [Quota Calculator](https://developers.google.com/youtube/v3/determine_quota_cost)
- [Google Cloud Console](https://console.cloud.google.com/)
- [GitHub Secrets Documentation](https://docs.github.com/en/actions/security-guides/encrypted-secrets)

---

## Support

If you encounter issues:
1. Check the [Troubleshooting](#troubleshooting) section above
2. Review `docs/youtube-api-quota.md` for quota details
3. Check GitHub Actions logs for error messages
4. Open an issue in the repository with error details

---

**Last Updated**: 2025-12-08
**Status**: Ready for manual setup steps
