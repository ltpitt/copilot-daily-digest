# Copilot Auto-Assignment Testing Guide

This guide documents the testing procedure for the automatic assignment of issues to GitHub Copilot.

## Overview

The workflow now automatically assigns created issues to `@copilot` to ensure the Copilot agent can immediately start working on them.

## Implementation Details

### GitHub Actions Workflow Changes

The `.github/workflows/daily-agent.yml` workflow has been modified to:

1. **Create an issue** with the content update task
2. **Capture the issue number** from the created issue URL
3. **Automatically assign** the issue to `@copilot` using `gh issue edit --add-assignee`

### Key Changes

1. Added `id: create_issue` to the "Create Issue for Publisher Agent" step
2. Modified the issue creation to capture the `ISSUE_URL` and extract the issue number
3. Added `ISSUE_NUMBER` to `$GITHUB_OUTPUT` for use in subsequent steps
4. Created a new step "Assign Issue to Copilot" that:
   - Runs only when changes are detected (same condition as issue creation)
   - Uses the `GH_TOKEN` environment variable
   - Calls `gh issue edit --add-assignee "copilot"` to assign the issue

## Testing Procedure

### Prerequisites

- `gh` CLI installed and authenticated
- Write access to the repository
- Issues permission enabled

### Automated Testing

Run the automated test script:

```bash
./scripts/test_copilot_assignment.sh
```

This script performs the complete test workflow:

1. ✅ Creates a test issue
2. ✅ Assigns the issue to @copilot
3. ✅ Verifies the assignment
4. ✅ Waits for potential PR creation
5. ✅ Cleans up any PRs created
6. ✅ Closes the test issue
7. ✅ Verifies repository state

### Manual Testing

#### Step 1: Create a Test Issue

```bash
gh issue create \
  --title "🧪 Test Issue for Copilot Assignment - $(date +'%Y-%m-%d %H:%M:%S')" \
  --body "This is a test issue to verify the automatic assignment workflow.

@copilot Please respond to confirm you can see and work on this issue." \
  --label "test"
```

**Expected Output:** Issue URL (e.g., `https://github.com/ltpitt/copilot-daily-digest/issues/123`)

#### Step 2: Assign to Copilot

Extract the issue number from the URL and assign it:

```bash
ISSUE_NUMBER=123  # Replace with your issue number
gh issue edit $ISSUE_NUMBER --add-assignee "copilot"
```

**Expected Output:** Success message confirming assignment

#### Step 3: Verify Assignment

```bash
gh issue view $ISSUE_NUMBER --json assignees --jq '.assignees[].login'
```

**Expected Output:** Should include `copilot` in the list

#### Step 4: Monitor Copilot Activity

Wait a few moments and check if Copilot creates a PR:

```bash
gh pr list --author "copilot" --state all --json number,title
```

**Expected Output:** May show a PR created by Copilot for the test issue

#### Step 5: Clean Up

If a PR was created:

```bash
PR_NUMBER=456  # Replace with the PR number
gh pr close $PR_NUMBER --delete-branch
```

Close the test issue:

```bash
gh issue close $ISSUE_NUMBER
```

#### Step 6: Verify Clean State

Verify no test artifacts remain:

```bash
# Check for test issues
gh issue list --label "test" --state all

# Check for copilot PRs
gh pr list --author "copilot" --state all

# Check repository status
git status
```

**Expected Output:** 
- Test issue should be closed
- Any test PRs should be closed
- Repository should be clean (no uncommitted changes)

## Testing the GitHub Action

### Manual Trigger Test

To test the actual workflow:

```bash
# Trigger the workflow manually
gh workflow run daily-agent.yml

# Monitor the run
gh run watch

# Or list recent runs
gh run list --workflow=daily-agent.yml --limit 5
```

### Verify Workflow Behavior

After triggering:

1. Check that an issue was created (if changes detected)
2. Verify the issue is assigned to @copilot
3. Monitor for Copilot's response and PR creation
4. Review the workflow logs

```bash
# View the latest run
gh run view

# Check issues created by the workflow
gh issue list --author "github-actions[bot]" --state all --limit 5
```

## Validation Checklist

- [ ] Test issue created successfully
- [ ] Issue assigned to @copilot
- [ ] Assignment verified via `gh issue view`
- [ ] Copilot received the assignment (check for activity)
- [ ] Test PR cleaned up (if created)
- [ ] Test branch deleted (if created)
- [ ] Test issue closed
- [ ] Repository in clean state
- [ ] Workflow runs successfully in GitHub Actions
- [ ] Workflow assigns issues to @copilot automatically

## Troubleshooting

### Issue: `gh` CLI not authenticated

**Solution:**
```bash
gh auth login
```

Follow the prompts to authenticate.

### Issue: Permission denied when assigning

**Error:** `Resource not accessible by integration`

**Cause:** The `GITHUB_TOKEN` lacks `issues: write` permission.

**Solution:** Ensure the workflow has proper permissions:
```yaml
permissions:
  issues: write
```

This is already configured in the workflow.

### Issue: Cannot find copilot user

**Error:** `User not found: copilot`

**Cause:** Using wrong username for Copilot.

**Solution:** The correct assignee is `copilot` (without @). The workflow uses:
```bash
gh issue edit $ISSUE_NUMBER --add-assignee "copilot"
```

### Issue: Assignment succeeds but Copilot doesn't respond

**Possible Causes:**
- Copilot is busy with other tasks
- The issue body doesn't contain clear instructions
- Copilot may require specific trigger patterns

**Solution:** Ensure the issue body includes:
- Clear `@copilot` mention
- Specific task description
- Relevant context and files

## References

- [GitHub REST API - Issue Assignees](https://docs.github.com/en/rest/issues/assignees)
- [GitHub CLI Documentation](https://cli.github.com/manual/)
- [GitHub Actions - Workflow Syntax](https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions)
