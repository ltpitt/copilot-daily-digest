# Task: Implement Copilot Assignment via GitHub App

## Overview

Implement programmatic assignment of GitHub Issues to the Copilot coding agent using a custom GitHub App with user-to-server OAuth token flow.

## Prerequisites

- Organization or repository admin access
- Ability to create and install GitHub Apps
- Understanding of OAuth 2.0 flows

## Implementation Steps

### Step 1: Create GitHub App

1. Go to GitHub Settings → Developer settings → GitHub Apps → New GitHub App
2. Configure the app:
   - **Name**: `copilot-daily-digest-automation`
   - **Homepage URL**: `https://github.com/ltpitt/copilot-daily-digest`
   - **Callback URL**: Not needed for server-to-server
   - **Webhook**: Disable (not needed)
   - **Permissions**:
     - Repository permissions:
       - Issues: Read & Write
       - Contents: Read
     - Organization permissions: None needed
   - **Where can this app be installed?**: Only on this account

3. After creation, note:
   - App ID
   - Generate and download private key (.pem file)

### Step 2: Install the App

1. Go to the app's settings page
2. Click "Install App"
3. Select the `copilot-daily-digest` repository
4. Confirm installation

### Step 3: Store Credentials as Secrets

```bash
# Store App ID
gh secret set COPILOT_APP_ID --body "123456"

# Store private key (base64 encoded for multiline)
base64 -i path/to/private-key.pem | gh secret set COPILOT_APP_PRIVATE_KEY
```

### Step 4: Create Token Generation Script

Create `scripts/get_app_token.sh`:

```bash
#!/bin/bash
set -euo pipefail

APP_ID="$COPILOT_APP_ID"
PRIVATE_KEY=$(echo "$COPILOT_APP_PRIVATE_KEY" | base64 -d)
INSTALLATION_ID="$1"

# Generate JWT
NOW=$(date +%s)
IAT=$((NOW - 60))
EXP=$((NOW + 600))

HEADER=$(echo -n '{"alg":"RS256","typ":"JWT"}' | base64 | tr -d '=' | tr '/+' '_-' | tr -d '\n')
PAYLOAD=$(echo -n "{\"iat\":$IAT,\"exp\":$EXP,\"iss\":\"$APP_ID\"}" | base64 | tr -d '=' | tr '/+' '_-' | tr -d '\n')

SIGNATURE=$(echo -n "$HEADER.$PAYLOAD" | openssl dgst -sha256 -sign <(echo "$PRIVATE_KEY") | base64 | tr -d '=' | tr '/+' '_-' | tr -d '\n')

JWT="$HEADER.$PAYLOAD.$SIGNATURE"

# Get installation access token
curl -s -X POST \
  -H "Authorization: Bearer $JWT" \
  -H "Accept: application/vnd.github+json" \
  "https://api.github.com/app/installations/$INSTALLATION_ID/access_tokens" \
  | jq -r '.token'
```

### Step 5: Create Assignment Script

Create `scripts/assign_to_copilot_app.sh`:

```bash
#!/bin/bash
set -euo pipefail

ISSUE_NUMBER="$1"
REPO="${GITHUB_REPOSITORY:-ltpitt/copilot-daily-digest}"
INSTALLATION_ID="YOUR_INSTALLATION_ID"  # Get from API or app settings

# Get app token
TOKEN=$(./scripts/get_app_token.sh "$INSTALLATION_ID")

# Note: GitHub App tokens may not support agent assignment
# This requires user-to-server token which needs OAuth flow
# See: https://docs.github.com/en/apps/creating-github-apps/authenticating-with-a-github-app/generating-a-user-access-token-for-a-github-app

echo "⚠️  GitHub App tokens are installation tokens, not user tokens"
echo "Agent assignment requires user-level authentication"
echo "Consider using PAT approach instead (TASK-PAT-GRAPHQL-ASSIGNMENT.md)"
```

### Step 6: Update GitHub Actions Workflow

```yaml
- name: Generate App Token
  id: app_token
  env:
    COPILOT_APP_ID: ${{ secrets.COPILOT_APP_ID }}
    COPILOT_APP_PRIVATE_KEY: ${{ secrets.COPILOT_APP_PRIVATE_KEY }}
  run: |
    TOKEN=$(./scripts/get_app_token.sh "$INSTALLATION_ID")
    echo "::add-mask::$TOKEN"
    echo "token=$TOKEN" >> $GITHUB_OUTPUT

- name: Assign Issue to Copilot
  if: steps.changes.outputs.has_changes == 'true'
  env:
    GH_TOKEN: ${{ steps.app_token.outputs.token }}
  run: |
    ./scripts/assign_to_copilot_app.sh "${{ steps.create_issue.outputs.ISSUE_NUMBER }}"
```

## Known Limitations

⚠️ **Critical**: GitHub's documentation states that Copilot assignment requires a **user token**, not an installation token:

> "Make sure you're authenticating with the API using a user token, for example a personal access token or a GitHub App user-to-server token."

This means:
1. Standard GitHub App installation tokens **won't work**
2. You need OAuth user-to-server token flow
3. This requires user interaction (OAuth consent)
4. Not suitable for fully automated workflows

## Recommendation

Unless you need fine-grained permission control, **use the PAT approach** documented in `TASK-PAT-GRAPHQL-ASSIGNMENT.md` instead. It's simpler and fully automated.

## References

- [GitHub Docs: Creating a GitHub App](https://docs.github.com/en/apps/creating-github-apps/about-creating-github-apps/about-creating-github-apps)
- [GitHub Docs: Authenticating as a GitHub App](https://docs.github.com/en/apps/creating-github-apps/authenticating-with-a-github-app/about-authentication-with-a-github-app)
- [GitHub Docs: User-to-server tokens](https://docs.github.com/en/apps/creating-github-apps/authenticating-with-a-github-app/generating-a-user-access-token-for-a-github-app)

## Status

- [ ] GitHub App created
- [ ] App installed on repository
- [ ] Credentials stored as secrets
- [ ] Token generation script created
- [ ] Assignment script created
- [ ] **Blocked**: User token requirement research
