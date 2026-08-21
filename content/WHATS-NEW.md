# What's New with GitHub Copilot

> Latest updates from the last 30 days

**Last Updated**: August 21, 2026

This page highlights significant Copilot updates from the past 30 days. Content older than 30 days moves to [CHANGELOG.md](CHANGELOG.md).

---

## This Week (Last 7 Days)

### [Windows 11 arm64 VS2026 image generally available](https://github.blog/changelog/2026-08-20-windows-11-arm64-vs2026-image-generally-available)
*Aug 20, 2026*

The Windows 11 arm64 image with Visual Studio 2026 is now generally available on standard and larger GitHub-hosted runners. To use it in GitHub Actions, update your workflow file to runs-on: windows-11-vs2026-arm. GitHub will gradually update the windows-11-arm image to use Visual Studio 2026 by default beginning September 21, 2026.

### [Pinning saved views to the repository issues sidebar is generally available and more](https://github.blog/changelog/2026-08-20-pin-projects-views-and-milestones-to-the-repository-sidebar)
*Aug 20, 2026*

You can now pin saved views to the repository issues sidebar, making the views you use most just one click away, even when the sidebar is collapsed. You can now see profile avatars for reactions on issues.

### [Track GitHub Code Quality enablement changes in the audit log](https://github.blog/changelog/2026-08-20-track-github-code-quality-enablement-changes-in-the-audit-log)
*Aug 20, 2026*

GitHub Code Quality now writes an audit log event whenever someone enables, disables, or changes its settings on a repository. Three new events give you that history:
repo.code_quality_enabled records when someone turns on Code Quality for a repository. Each event captures the repository, the actor who made the change, and when it happened.

### [Separate GitHub Actions path for GitHub Code Quality](https://github.blog/changelog/2026-08-20-separate-github-actions-path-for-github-code-quality)
*Aug 20, 2026*

A dedicated workflow path for code quality CodeQL actions workflows is now generally available. Your workflow run history and your Actions usage reports now tell GitHub Code Quality runs apart from GitHub code scanning runs.

### [Code scanning adds a mitigated alert dismissal reason](https://github.blog/changelog/2026-08-20-code-scanning-adds-a-mitigated-alert-dismissal-reason)
*Aug 20, 2026*

You can now dismiss a code scanning alert with the reason Mitigated when a vulnerability remains in the code but external controls, such as a web application firewall or network policy, mitigate its risk. For more information, see resolving code scanning alerts.

---

## Last 30 Days

### [CodeQL 2.26.3 improves GitHub Actions queries and JavaScript modeling](https://github.blog/changelog/2026-08-19-codeql-2-26-3-improves-github-actions-queries-and-javascript-modeling)
*Aug 19, 2026*

CodeQL 2.26.3 adds JavaScript, TypeScript, and Vue source modeling and improves the accuracy of several GitHub Actions queries. CodeQL is the static analysis engine behind GitHub code scanning, which helps you find and remediate security issues in your code. GitHub Actions
Analysis now recognizes untrusted data in github.event.merge_group for workflows triggered by the merge_group event.

### [Track organization code quality trends](https://github.blog/changelog/2026-08-19-track-organization-code-quality-trends)
*Aug 19, 2026*

The organization-level Code Quality dashboard now includes a Trends tab that shows how code quality has changed across your repositories over time. Instead of a point-in-time snapshot, you can see whether open findings are trending up or down and which repositories are driving the change.

### [GitHub Copilot app for Beginners: Managing your work](https://github.blog/ai-and-ml/github-copilot/github-copilot-app-for-beginners-managing-your-work/)
*Aug 19, 2026*

This is the third post in our GitHub Copilot app for Beginners series. If you're just joining us, check out, GitHub Copilot app for beginners: Getting started, where we introduced the app and how it helps you work across multiple agent sessions. Our second post goes deeper on working within a session.

### [Favorite episodes and open source picks | S02E01 | The GitHub Podcast](https://www.youtube.com/watch?v=i3i5eiTm6jU)
*Aug 19, 2026*

The GitHub podcast is back for season 2 with new co-hosts Cassidy, Marlene, and GPS! In this premiere episode, the team looks back at standout moments from season 1, including hot takes on Electron...

### [Enterprise managed settings in GitHub Copilot for JetBrains](https://github.blog/changelog/2026-08-18-enterprise-managed-settings-in-github-copilot-for-jetbrains)
*Aug 18, 2026*

GitHub Copilot for JetBrains now supports enterprise managed settings for plugin governance, MCP server access, OpenTelemetry, and permission modes. Administrators can now apply consistent controls for everyone on your enterprise's Copilot plan.

### [Credential revocation and deauthorization by token type](https://github.blog/changelog/2026-08-18-credential-revocation-and-deauthorization-by-token-type)
*Aug 18, 2026*

Building on our self-service credential revocation experiences for incident response, you can now take token-type and user-specific actions to deauthorize and revoke user credentials during a security incident. This gives you finer-grained control when responding to a compromise. Previously, credential kill-switch actions applied to all of a user's credentials at once.

### [How to run parallel AI agents in the GitHub Copilot app | Tutorial for beginners](https://www.youtube.com/watch?v=F1UwPa7lemA)
*Aug 18, 2026*

Can you really run multiple AI agents on the same project at the same time without chaos? In episode 5 of our beginner series, we show you how the GitHub Copilot app uses isolated git worktrees to...

### [How canvases make agentic workflows visible, steerable, and cost-efficient](https://github.blog/ai-and-ml/github-copilot/how-canvases-make-agentic-workflows-visible-steerable-and-cost-efficient/)
*Aug 17, 2026*

When I was in college, I joined the beta for one of the first versions of AI inline completions in VS Code. Since then, GenAI has fundamentally changed software development: hybrid teams where agents and humans work in tandem, with the developer at the center as visionary and orchestrator. We are living in that transition right now.

### [Multiple redirect URIs and token refresh for OAuth apps](https://github.blog/changelog/2026-08-14-multiple-redirect-uris-and-token-refresh-for-oauth-apps)
*Aug 14, 2026*

We've released multiple updates to the OAuth app and GitHub App platforms to support more secure app development:
OAuth apps can opt in to expiring access tokens and refresh tokens. OAuth apps can have multiple redirect URIs.
Both GitHub Apps and OAuth apps can enable wildcard matching for redirect URIs if needed. OAuth apps can now request a short-lived token during the user authentication flow.

### [How to bring your software delivery workflow into GitHub with agent apps](https://github.blog/ai-and-ml/github-copilot/how-to-bring-your-software-delivery-workflow-into-github-with-agent-apps/)
*Aug 14, 2026*

How many tabs do you have open alongside your pull request? Imagine picking up a new issue in your product's free-trial onboarding flow: make the "invite your teammates" step optional. Support keeps flagging the step as a friction point as signups increase.

---

## Older Updates

See [CHANGELOG.md](CHANGELOG.md) for the full historical timeline.

---

_All dates are complete and sorted newest first. For a full list of updates, see [CHANGELOG.md](CHANGELOG.md)._
