# Issue Auto-Assignment Workflow

## Overview

The `daily-agent.yml` workflow automatically assigns newly created issues to `copilot-swe-agent[bot]` to ensure they are processed automatically by the Copilot Coding Agent.

## Implementation Details

### How It Works

1. **Issue Creation**: The workflow creates a new issue with the title "Content Update - YYYY-MM-DD"
2. **Issue Number Extraction**: The issue number is extracted from the created issue URL and stored as an output
3. **Automatic Assignment**: Using `actions/github-script@v7`, the workflow calls GitHub's REST API to assign the issue to `copilot-swe-agent[bot]`
4. **Error Handling**: If assignment fails, the workflow logs a warning but continues (the issue was already created successfully)

### Key Components

#### Step 1: Create Issue (Enhanced)
```yaml
- name: Create Issue for Copilot Coding Agent
  id: create-issue
  env:
    GH_TOKEN: ${{ secrets.GITHUB_TOKEN }}
  run: |
    # ... create issue ...
    # Extract issue number from URL
    ISSUE_NUMBER=$(echo "$ISSUE_URL" | grep -oP '(?<=/issues/)\d+$')
    echo "issue_number=$ISSUE_NUMBER" >> $GITHUB_OUTPUT
    echo "issue_url=$ISSUE_URL" >> $GITHUB_OUTPUT
```

#### Step 2: Assign Issue
```yaml
- name: Assign Issue to Copilot
  uses: actions/github-script@v7
  with:
    github-token: ${{ secrets.GITHUB_TOKEN }}
    script: |
      const issueNumber = ${{ steps.create-issue.outputs.issue_number }};
      const assignee = 'copilot-swe-agent[bot]';
      
      try {
        await github.rest.issues.addAssignees({
          owner: context.repo.owner,
          repo: context.repo.repo,
          issue_number: issueNumber,
          assignees: [assignee]
        });
        console.log(`✓ Successfully assigned ${assignee} to issue #${issueNumber}`);
      } catch (error) {
        console.error(`✗ Failed to assign ${assignee}`);
        core.warning(`Assignment failed: ${error.message}`);
      }
```

## Why This Implementation?

### Design Decisions

1. **actions/github-script**: Chosen over shell scripts because:
   - Native JavaScript API calls (cleaner, more maintainable)
   - Built-in error handling
   - No need to parse JSON responses manually
   - Better integration with GitHub Actions context

2. **Graceful Failure**: Assignment failures don't fail the workflow because:
   - The primary goal (issue creation) was already successful
   - Assignment is a convenience feature
   - Allows manual assignment as fallback

3. **Logging**: Comprehensive logging helps with:
   - Debugging assignment issues
   - Auditing successful assignments
   - Monitoring workflow health

## Modifying the Assignee

To change the assignee in the future:

1. Open `.github/workflows/daily-agent.yml`
2. Locate the `Assign Issue to Copilot` step
3. Change the `assignee` variable:
   ```javascript
   const assignee = 'copilot-swe-agent[bot]';  // Change this line
   ```
4. Commit and push

### Valid Assignee Formats

- Bot accounts: `username[bot]` (e.g., `copilot-swe-agent[bot]`)
- Regular users: `username` (e.g., `octocat`)
- Multiple assignees: Use array `['user1', 'user2[bot]']`

## Testing

### Manual Test
Trigger the workflow manually:
```bash
gh workflow run daily-agent.yml
```

Then check:
1. Issue was created
2. Issue has `copilot-swe-agent[bot]` assigned
3. Workflow logs show success message

### Expected Output
```
Attempting to assign issue #123 to copilot-swe-agent[bot]...
✓ Successfully assigned copilot-swe-agent[bot] to issue #123
```

## Security

- **No hardcoded tokens**: Uses `${{ secrets.GITHUB_TOKEN }}` provided by GitHub Actions
- **Minimal permissions**: Workflow only requires `issues: write`
- **No secret exposure**: All tokens are handled securely by GitHub

## Troubleshooting

### Assignment Fails

**Symptom**: Warning in logs: "Assignment failed"

**Possible Causes**:
1. Bot account doesn't have repository access
2. Repository settings block bot assignments
3. Network/API issues

**Solution**:
- Check bot permissions in repository settings
- Review workflow logs for specific error message
- Issues can still be manually assigned

### Issue Number Not Extracted

**Symptom**: Error about invalid issue number

**Possible Causes**:
1. Issue URL format changed
2. `gh` CLI output format changed

**Solution**:
- Check the issue creation step logs
- Verify the regex pattern in `grep -oP '(?<=/issues/)\d+$'`

## References

- [GitHub REST API - Add assignees](https://docs.github.com/en/rest/issues/assignees#add-assignees-to-an-issue)
- [actions/github-script](https://github.com/actions/github-script)
- [GitHub Actions - Workflow syntax](https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions)
