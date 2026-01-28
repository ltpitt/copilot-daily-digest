#!/bin/bash

# Test script for Copilot agent task workflow
# This script demonstrates the complete workflow for creating agent tasks with Copilot CLI

set -e  # Exit on error

echo "🧪 Testing Copilot Agent Task Workflow"
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

# Step 1: Create a test task description file
echo "Step 1: Creating test task description..."
cat > /tmp/test-task.md << 'EOF'
# Test Task for Copilot Agent

This is a test task to verify the agent task creation workflow.

## Task Description
Please create a simple test file called `TEST.md` in the root of the repository with the following content:
- Current date
- A brief description of this test
- Confirmation that the agent task workflow is working

After creating the file, commit it with the message "test: verify agent task workflow" and create a pull request.
EOF

echo "✓ Created task description file"
echo ""

# Step 2: Create agent task using Copilot CLI
echo "Step 2: Creating agent task with Copilot CLI..."
gh agent-task create -F /tmp/test-task.md
echo "✓ Agent task created"
echo ""

# Step 3: List recent agent tasks
echo "Step 3: Listing recent agent tasks..."
gh agent-task list | head -5
echo ""

echo "=============================================="
echo "✅ Test workflow completed successfully!"
echo ""
echo "Summary:"
echo "- Created test task description file"
echo "- Created agent task using gh agent-task create"
echo "- Listed recent agent tasks"
echo ""
echo "To manually verify, run:"
echo "  gh agent-task list"
echo "  gh pr list --state all --limit 5"
