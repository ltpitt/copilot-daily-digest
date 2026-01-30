# Task: Implement Copilot Assignment via PAT + GraphQL

## Overview

Implement programmatic assignment of GitHub Issues to the Copilot coding agent using a Personal Access Token (PAT) and the GraphQL API with special headers.

## Prerequisites

- Repository admin access to add secrets
- A GitHub Personal Access Token (classic) with `repo` scope
- Understanding of GraphQL mutations

## Implementation Steps

### Step 1: Create Personal Access Token

1. Go to GitHub Settings → Developer settings → Personal access tokens → Tokens (classic)
2. Generate new token with these scopes:
   - `repo` (full control of private repositories)
   - `write:org` (if organization repo)
3. Copy the token value

### Step 2: Add Repository Secret

```bash
gh secret set COPILOT_ASSIGNMENT_PAT --body "ghp_your_token_here"
```

Or via GitHub UI: Settings → Secrets and variables → Actions → New repository secret

### Step 3: Get Copilot Bot ID

Run this GraphQL query to get the `copilot-swe-agent` bot ID:

```graphql
query {
  user(login: "copilot-swe-agent[bot]") {
    id
    databaseId
  }
}
```

Or use the REST API:
```bash
curl -H "Authorization: Bearer $GITHUB_TOKEN" \
  "https://api.github.com/users/copilot-swe-agent%5Bbot%5D"
```

### Step 4: Create Assignment Script

Create `scripts/assign_to_copilot.sh`:

```bash
#!/bin/bash
set -euo pipefail

ISSUE_NUMBER="$1"
REPO="${GITHUB_REPOSITORY:-ltpitt/copilot-daily-digest}"

# GraphQL mutation to assign Copilot to an issue
curl -X POST https://api.github.com/graphql \
  -H "Authorization: Bearer $COPILOT_ASSIGNMENT_PAT" \
  -H "Content-Type: application/json" \
  -H "GraphQL-Features: issues_copilot_assignment_api_support" \
  -d @- <<EOF
{
  "query": "mutation AssignCopilot(\$issueId: ID!, \$agentId: ID!) { updateIssue(input: { id: \$issueId, agentAssignments: { agentId: \$agentId, action: ASSIGN } }) { issue { id } } }",
  "variables": {
    "issueId": "$(gh api graphql -f query='query { repository(owner: \"${REPO%/*}\", name: \"${REPO#*/}\") { issue(number: $ISSUE_NUMBER) { id } } }' -q '.data.repository.issue.id')",
    "agentId": "COPILOT_BOT_ID_HERE"
  }
}
EOF
```

### Step 5: Update GitHub Actions Workflow

Modify `.github/workflows/daily-agent.yml`:

```yaml
- name: Assign Issue to Copilot
  if: steps.changes.outputs.has_changes == 'true'
  env:
    COPILOT_ASSIGNMENT_PAT: ${{ secrets.COPILOT_ASSIGNMENT_PAT }}
    GH_TOKEN: ${{ secrets.GITHUB_TOKEN }}
  run: |
    chmod +x scripts/assign_to_copilot.sh
    ./scripts/assign_to_copilot.sh "${{ steps.create_issue.outputs.ISSUE_NUMBER }}"
```

## Security Considerations

⚠️ **Risk**: PAT has user-level permissions, broader than `GITHUB_TOKEN`
- Consider using a machine user account with minimal permissions
- Rotate the PAT regularly
- Monitor Actions audit logs for unexpected usage

## Verification

After implementation, test with:

```bash
# Create test issue
ISSUE_URL=$(gh issue create --title "Test Copilot Assignment" --body "Testing automated assignment")
ISSUE_NUM=$(echo "$ISSUE_URL" | grep -oE '[0-9]+$')

# Run assignment
./scripts/assign_to_copilot.sh "$ISSUE_NUM"

# Verify (check GitHub UI - Copilot should appear as assignee)
gh issue view "$ISSUE_NUM" --json assignees

# Cleanup
gh issue close "$ISSUE_NUM"
```

## References

- [GitHub Docs: Assign issues to Copilot using the API](https://docs.github.com/en/copilot/how-tos/use-copilot-agents/coding-agent/create-a-pr#assign-issues-to-copilot-using-the-api)
- [GitHub GraphQL API](https://docs.github.com/en/graphql)

## Status

- [ ] PAT created and stored as secret
- [ ] Bot ID retrieved
- [ ] Assignment script created
- [ ] Workflow updated
- [ ] End-to-end test passed
