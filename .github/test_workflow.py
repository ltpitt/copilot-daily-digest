#!/usr/bin/env python3
"""
Test script to validate the daily-agent.yml workflow configuration.
This script checks that the workflow is properly configured for auto-assignment.
"""

import yaml
import sys


def validate_workflow():
    """Validate the daily-agent.yml workflow configuration."""
    
    print("🔍 Validating daily-agent.yml workflow...\n")
    
    # Load workflow
    with open('.github/workflows/daily-agent.yml', 'r') as f:
        workflow = yaml.safe_load(f)
    
    errors = []
    warnings = []
    
    # 1. Check workflow name
    if workflow.get('name') != 'Daily Copilot Digest':
        errors.append("Workflow name should be 'Daily Copilot Digest'")
    else:
        print("✓ Workflow name is correct")
    
    # 2. Check permissions
    permissions = workflow.get('permissions', {})
    if permissions.get('issues') != 'write':
        errors.append("Workflow needs 'issues: write' permission")
    else:
        print("✓ Issues write permission is set")
    
    # 3. Check job structure
    if 'create-issue' not in workflow.get('jobs', {}):
        errors.append("Missing 'create-issue' job")
        return errors, warnings
    
    job = workflow['jobs']['create-issue']
    steps = job.get('steps', [])
    
    if len(steps) < 2:
        errors.append(f"Expected at least 2 steps, found {len(steps)}")
        return errors, warnings
    
    print("✓ Job structure is valid")
    
    # 4. Check first step (issue creation)
    first_step = steps[0]
    if first_step.get('id') != 'create-issue':
        errors.append("First step should have id 'create-issue'")
    else:
        print("✓ First step has correct id")
    
    # Check that it outputs issue_number
    run_script = first_step.get('run', '')
    if 'issue_number=' not in run_script or 'GITHUB_OUTPUT' not in run_script:
        errors.append("First step should output 'issue_number' to GITHUB_OUTPUT")
    else:
        print("✓ First step outputs issue_number")
    
    # 5. Check second step (assignment)
    second_step = steps[1]
    if 'uses' not in second_step:
        errors.append("Second step should use an action")
    elif 'github-script' not in second_step['uses']:
        errors.append("Second step should use 'actions/github-script'")
    else:
        print("✓ Second step uses github-script action")
    
    # Check the script contains assignment logic
    script = second_step.get('with', {}).get('script', '')
    if 'addAssignees' not in script:
        errors.append("Second step should call 'addAssignees' API")
    else:
        print("✓ Second step calls addAssignees API")
    
    if 'copilot-swe-agent[bot]' not in script:
        warnings.append("Assignee should be 'copilot-swe-agent[bot]'")
    else:
        print("✓ Assignee is set to 'copilot-swe-agent[bot]'")
    
    # Check error handling
    if 'catch' not in script or 'core.warning' not in script:
        warnings.append("Consider adding error handling with try/catch and core.warning")
    else:
        print("✓ Error handling is implemented")
    
    # 6. Check triggers
    # Note: 'on' is a Python keyword, so YAML loader uses True as key
    triggers = workflow.get(True, {}) if True in workflow else workflow.get('on', {})
    if 'workflow_dispatch' not in triggers:
        warnings.append("Consider adding 'workflow_dispatch' for manual triggering")
    else:
        print("✓ Manual triggering is enabled")
    
    return errors, warnings


def main():
    """Main entry point."""
    errors, warnings = validate_workflow()
    
    print("\n" + "="*60)
    
    if warnings:
        print("\n⚠️  Warnings:")
        for warning in warnings:
            print(f"   - {warning}")
    
    if errors:
        print("\n❌ Errors:")
        for error in errors:
            print(f"   - {error}")
        print("\n💥 Validation FAILED")
        return 1
    
    if warnings:
        print("\n✅ Validation PASSED (with warnings)")
        return 0
    
    print("\n🎉 Validation PASSED - All checks successful!")
    return 0


if __name__ == '__main__':
    sys.exit(main())
