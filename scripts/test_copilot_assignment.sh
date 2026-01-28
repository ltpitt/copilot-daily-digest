#!/bin/bash

# Test script for Copilot CLI workflow
# This script demonstrates using the standalone Copilot CLI to work on issues

set -e  # Exit on error

echo "🧪 Testing Copilot CLI Workflow"
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

# Step 1: Install Copilot CLI
echo "Step 1: Installing Copilot CLI..."
if command -v copilot &> /dev/null; then
    echo "✓ Copilot CLI already installed"
else
    npm install -g @github/copilot
    echo "✓ Copilot CLI installed"
fi
echo ""

# Step 2: Create a test issue
echo "Step 2: Creating test issue..."
ISSUE_URL=$(gh issue create \
    --title "🧪 Test Issue for Copilot CLI - $(date +'%Y-%m-%d %H:%M:%S')" \
    --body "This is a test issue to verify the Copilot CLI workflow.

## Test Task
Please create a simple test file called \`COPILOT_TEST.md\` in the root with:
- Current date
- Confirmation that Copilot CLI is working

After creating the file, commit it and create a pull request." \
    --label "test")

# Extract issue number from URL
ISSUE_NUMBER=$(echo "$ISSUE_URL" | sed -n 's|.*/issues/\([0-9]*\)$|\1|p')
echo "✓ Created issue #$ISSUE_NUMBER: $ISSUE_URL"
echo ""

# Step 3: Use Copilot CLI to work on the issue
echo "Step 3: Delegating work to Copilot CLI for issue #$ISSUE_NUMBER..."
echo "Note: This will use the standalone 'copilot' CLI tool"
echo ""

# Note: In a real scenario, you would run:
# copilot -p "Work on issue #$ISSUE_NUMBER in this repository" --allow-tool 'write' --allow-tool 'shell(git:*)' --allow-all-urls
# For this test, we'll just demonstrate the command
echo "Command that would be run:"
echo "  copilot -p \"Work on issue #$ISSUE_NUMBER\" --allow-tool 'write' --allow-tool 'shell(git:*)' --allow-all-urls"
echo ""
echo "⚠️  Skipping actual copilot CLI execution in test mode"
echo ""

# Step 4: Clean up
echo "Step 4: Closing test issue #$ISSUE_NUMBER..."
gh issue close "$ISSUE_NUMBER"
echo "✓ Test issue closed"
echo ""

echo "=============================================="
echo "✅ Test workflow completed successfully!"
echo ""
echo "Summary:"
echo "- Created test issue #$ISSUE_NUMBER"
echo "- Demonstrated Copilot CLI command structure"
echo "- Closed test issue"
echo ""
echo "To use Copilot CLI in production:"
echo "  1. Install: npm install -g @github/copilot"
echo "  2. Authenticate via GITHUB_TOKEN environment variable"
echo "  3. Use programmatic mode: copilot -p \"your prompt\" --allow-tool 'write' --allow-all-urls"
