#!/bin/bash

# Test script for Copilot issue assignment workflow
# This script demonstrates the complete workflow for testing copilot assignment

set -e  # Exit on error

echo "🧪 Testing Copilot Issue Assignment Workflow"
echo "=============================================="
echo ""

# Check if gh is installed
if ! command -v gh &> /dev/null; then
    echo "❌ Error: gh CLI is not installed"
    exit 1
fi

# Check if gh is authenticated
if ! gh auth status &> /dev/null; then
    echo "❌ Error: gh CLI is not authenticated"
    echo "Please run: gh auth login"
    exit 1
fi

echo "✓ gh CLI is installed and authenticated"
echo ""

# Step 1: Create a test issue
echo "Step 1: Creating test issue..."
ISSUE_URL=$(gh issue create \
    --title "🧪 Test Issue for Copilot Assignment - $(date +'%Y-%m-%d %H:%M:%S')" \
    --body "This is a test issue to verify the automatic assignment workflow.

## Test Task
Please verify this issue was automatically assigned to @copilot.

@copilot Please respond to confirm you can see and work on this issue.

This is a test issue and can be closed after verification." \
    --label "test")

# Extract issue number from URL
ISSUE_NUMBER=$(echo "$ISSUE_URL" | grep -oP '\d+$')
echo "✓ Created issue #$ISSUE_NUMBER: $ISSUE_URL"
echo ""

# Step 2: Assign the issue to copilot
echo "Step 2: Assigning issue #$ISSUE_NUMBER to @copilot..."
gh issue edit "$ISSUE_NUMBER" --add-assignee "copilot"
echo "✓ Issue assigned to @copilot"
echo ""

# Step 3: Verify the assignment
echo "Step 3: Verifying assignment..."
ASSIGNEES=$(gh issue view "$ISSUE_NUMBER" --json assignees --jq '.assignees[].login')
if echo "$ASSIGNEES" | grep -q "copilot"; then
    echo "✓ Issue is correctly assigned to copilot"
else
    echo "❌ Issue is not assigned to copilot"
    exit 1
fi
echo ""

# Step 4: Wait for copilot to potentially create a PR
echo "Step 4: Waiting 10 seconds to check if copilot creates a PR..."
sleep 10

# Check for PRs created by copilot
echo "Looking for PRs created by copilot for issue #$ISSUE_NUMBER..."
COPILOT_PRS=$(gh pr list --state all --author "copilot" --json number,title,headRefName --jq ".[] | select(.title | contains(\"#$ISSUE_NUMBER\")) | {number, title, headRefName}")

if [ -n "$COPILOT_PRS" ]; then
    echo "✓ Found PR(s) created by copilot:"
    echo "$COPILOT_PRS"
    
    # Extract PR number and branch
    PR_NUMBER=$(echo "$COPILOT_PRS" | jq -r '.number')
    PR_BRANCH=$(echo "$COPILOT_PRS" | jq -r '.headRefName')
    
    echo ""
    echo "Step 5: Cleaning up - Closing PR #$PR_NUMBER..."
    gh pr close "$PR_NUMBER" --delete-branch
    echo "✓ PR #$PR_NUMBER closed and branch $PR_BRANCH deleted"
else
    echo "ℹ️  No PR created by copilot yet (this is expected if copilot hasn't started working)"
fi
echo ""

# Step 6: Close and clean up the test issue
echo "Step 6: Closing test issue #$ISSUE_NUMBER..."
gh issue close "$ISSUE_NUMBER"
echo "✓ Test issue closed"
echo ""

# Step 7: Verify repository state
echo "Step 7: Verifying repository state..."
echo "Checking for any remaining test issues..."
TEST_ISSUES=$(gh issue list --label "test" --state all --json number,title | jq -r '.[] | "\(.number): \(.title)"')
if [ -n "$TEST_ISSUES" ]; then
    echo "⚠️  Found test issues:"
    echo "$TEST_ISSUES"
else
    echo "✓ No test issues found"
fi
echo ""

echo "=============================================="
echo "✅ Test workflow completed successfully!"
echo ""
echo "Summary:"
echo "- Created test issue #$ISSUE_NUMBER"
echo "- Assigned to @copilot"
echo "- Verified assignment"
if [ -n "$PR_NUMBER" ]; then
    echo "- Cleaned up PR #$PR_NUMBER and branch $PR_BRANCH"
fi
echo "- Closed test issue"
echo ""
echo "To manually verify, run:"
echo "  gh issue list --state closed --limit 5"
echo "  gh pr list --state closed --limit 5"
