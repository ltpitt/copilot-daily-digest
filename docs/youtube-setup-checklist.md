# YouTube Data API v3 Setup Checklist

Quick reference checklist for setting up YouTube Data API v3 access.

## Pre-Setup (Already Completed ✅)

- [x] `requirements.txt` updated with `google-api-python-client>=2.100.0`
- [x] `config/youtube.yml` created with configuration
- [x] `scripts/test_youtube_api.py` test script created
- [x] `docs/youtube-api-quota.md` documentation created
- [x] `data/videos/` directory structure created
- [x] `.gitignore` configured for security
- [x] Dependencies tested and working
- [x] Test script validated (graceful failure without API key)

## Manual Setup Steps (User Action Required)

### Step 1: Google Cloud Project
- [ ] Go to https://console.cloud.google.com/
- [ ] Create new project named "copilot-daily-digest"
- [ ] Note the project ID
- [ ] Verify project is created successfully

### Step 2: Enable API
- [ ] Navigate to "APIs & Services" → "Library"
- [ ] Search for "YouTube Data API v3"
- [ ] Click "Enable"
- [ ] Verify API is enabled (green checkmark)

### Step 3: Create Credentials
- [ ] Go to "APIs & Services" → "Credentials"
- [ ] Click "Create Credentials" → "API Key"
- [ ] Copy the API key to a secure location
- [ ] (Optional) Click "Edit API key"
- [ ] (Optional) Restrict to "YouTube Data API v3"
- [ ] (Optional) Add IP restrictions if needed
- [ ] Click "Save"

### Step 4: Add to GitHub Secrets
- [ ] Go to https://github.com/ltpitt/copilot-daily-digest/settings/secrets/actions
- [ ] Click "New repository secret"
- [ ] Name: `YOUTUBE_API_KEY`
- [ ] Value: (paste API key from Step 3)
- [ ] Click "Add secret"
- [ ] Verify secret appears in the list

## Verification (Optional)

### Local Testing
- [ ] Install dependencies: `pip install -r requirements.txt`
- [ ] Set environment variable: `export YOUTUBE_API_KEY="your-key"`
- [ ] Run test: `python scripts/test_youtube_api.py`
- [ ] Verify output: "✅ YouTube API working!"

### GitHub Actions Testing
- [ ] Trigger a workflow run manually
- [ ] Check workflow logs for YouTube API access
- [ ] Verify no API key errors
- [ ] Confirm video metadata is being enriched

## Post-Setup (Optional)

### Enable API Enrichment
- [ ] Edit `config/youtube.yml`
- [ ] Change `api.enabled` from `false` to `true`
- [ ] Commit and push changes
- [ ] Verify workflows use API enrichment

### Monitor Quota
- [ ] Go to Google Cloud Console
- [ ] Navigate to "APIs & Services" → "Dashboard"
- [ ] Click "YouTube Data API v3"
- [ ] View quota usage graphs
- [ ] Set up alerts for high usage (optional)

## Security Review

- [ ] API key is NOT in any code files
- [ ] API key is NOT in any commit history
- [ ] API key is in GitHub Secrets only
- [ ] Local config files are gitignored
- [ ] API key has restrictions enabled (recommended)
- [ ] Monitoring is set up for unusual usage

## Troubleshooting

If issues arise:
- [ ] Check `docs/youtube-setup-guide.md` for detailed help
- [ ] Review `docs/youtube-api-quota.md` for quota info
- [ ] Check Google Cloud Console for API status
- [ ] Review GitHub Actions logs for errors
- [ ] Verify API key is correct and active

## Completion Status

**Overall Status**: 
- ✅ Code setup: COMPLETE
- ⚠️ Manual setup: PENDING (user action required)

**Estimated Time**: 15-30 minutes for manual steps

**Next Action**: User should complete Steps 1-4 above

---

**Note**: The API is OPTIONAL. The project works with RSS feeds by default. API enrichment adds duration, views, and other metadata but is not required for basic functionality.

**Last Updated**: 2025-12-08
