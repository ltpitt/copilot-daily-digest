#!/bin/bash

# Test script for Copilot notification workflow
# This script demonstrates the complete workflow for notifying Copilot via comment

set -e  # Exit on error

echo "🧪 Testing Copilot Issue Notification Workflow"
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
    --title "🧪 Test Issue for Copilot Notification - $(date +'%Y-%m-%d %H:%M:%S')" \
    --body "This is a test issue to verify the automatic notification workflow.

## Test Task
Please verify this issue triggers @copilot via comment notification.

This is a test issue and can be closed after verification." \
    --label "test")

# Extract issue number from URL
ISSUE_NUMBER=$(echo "$ISSUE_URL" | sed -n 's|.*/issues/\([0-9]*\)$|\1|p')
echo "✓ Created issue #$ISSUE_NUMBER: $ISSUE_URL"
echo ""

# Step 2: Notify Copilot via comment
echo "Step 2: Notifying @copilot on issue #$ISSUE_NUMBER..."
gh issue comment "$ISSUE_NUMBER" --body "@copilot Please start working on this issue."
echo "✓ Comment posted to notify @copilot"
echo ""

# Step 3: Verify the comment
echo "Step 3: Verifying comment..."
ALL_COMMENTS=$(gh issue view "$ISSUE_NUMBER" --json comments --jq '.comments[].body')
if echo "$ALL_COMMENTS" | grep -q "@copilot"; then
    echo "✓ Comment with @copilot mention posted successfully"
else
    echo "❌ Comment not found"
    exit 1
fi
echo ""

# Step 4: Wait for copilot to potentially create a PR
echo "Step 4: Waiting 10 seconds to check if copilot creates a PR..."
sleep 10

# Check for PRs created by copilot
echo "Looking for PRs created by copilot for issue #$ISSUE_NUMBER..."
COPILOT_PRS=$(gh pr list --state all --author "copilot" --json number,title,headRefName)

if [ -n "$COPILOT_PRS" ] && [ "$COPILOT_PRS" != "[]" ]; then
    echo "✓ Found PR(s) created by copilot:"
    echo "$COPILOT_PRS" | jq .
    
    # Get the most recent PR by copilot
    PR_NUMBER=$(echo "$COPILOT_PRS" | jq -r '.[0].number')
    PR_BRANCH=$(echo "$COPILOT_PRS" | jq -r '.[0].headRefName')
    
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
echo "- Posted comment to notify @copilot"
echo "- Verified comment was posted"
if [ -n "$PR_NUMBER" ]; then
    echo "- Cleaned up PR #$PR_NUMBER and branch $PR_BRANCH"
fi
echo "- Closed test issue"
echo ""
echo "To manually verify, run:"
echo "  gh issue list --state closed --limit 5"
echo "  gh pr list --state closed --limit 5"
