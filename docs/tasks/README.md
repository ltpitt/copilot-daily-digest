# Implementation Tasks

This directory contains detailed implementation instructions for different approaches to automating the Copilot Daily Digest workflow.

## Background

Programmatic assignment of GitHub Issues to the Copilot coding agent from GitHub Actions has limitations:
- `GITHUB_TOKEN` is a machine token, not a user token
- The Copilot assignment API requires user-level authentication
- Simple `gh issue edit --add-assignee "copilot"` does not work

These tasks document alternative approaches.

## Available Tasks

| Task | Complexity | Status | Recommendation |
|------|------------|--------|----------------|
| [PAT + GraphQL](TASK-PAT-GRAPHQL-ASSIGNMENT.md) | Medium | Untested | ⭐ Best for full automation |
| [GitHub App](TASK-GITHUB-APP-ASSIGNMENT.md) | High | Blocked | Not recommended (user token required) |
| [Inline Monolithic](TASK-INLINE-MONOLITHIC-AGENT.md) | Low | Working | ⭐ Best for reliability |

## Quick Decision Guide

**Want full Copilot automation with AI reasoning?**
→ Try [PAT + GraphQL](TASK-PAT-GRAPHQL-ASSIGNMENT.md) approach

**Want reliable, deterministic updates?**
→ Use [Inline Monolithic](TASK-INLINE-MONOLITHIC-AGENT.md) approach

**Need fine-grained permissions?**
→ [GitHub App](TASK-GITHUB-APP-ASSIGNMENT.md) won't work for Copilot assignment due to user token requirement

## Issue Trackers to Watch

Monitor these for platform updates on Copilot assignment:

- **GitHub Community Discussions**: https://github.com/orgs/community/discussions
- **GitHub Copilot Feedback**: https://github.com/orgs/community/discussions/categories/copilot
- **GitHub Actions Feedback**: https://github.com/orgs/community/discussions/categories/actions
- **GitHub Changelog**: https://github.blog/changelog/
- **GitHub Public Roadmap**: https://github.com/orgs/github/projects/4247

## Usage

To assign a task to Copilot coding agent:

1. Create a new issue with the task file contents
2. Manually assign to Copilot (or use PAT approach if implemented)
3. Monitor the PR created by Copilot
4. Review and merge

## Cleanup Note

The following stale documentation was removed (2025-01-30):
- `docs/COPILOT_AUTO_ASSIGNMENT.md` - Documented a solution that was never deployed
- `docs/COPILOT_ASSIGNMENT_TESTING.md` - Testing guide for non-existent implementation
