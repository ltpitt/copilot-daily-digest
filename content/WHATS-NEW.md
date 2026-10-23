# What's New with GitHub Copilot

> Latest updates from the last 30 days

**Last Updated**: October 23, 2026

This page highlights significant Copilot updates from the past 30 days. Content older than 30 days moves to [CHANGELOG.md](CHANGELOG.md).

---

## ⚠️ Action Required

*Deprecations and breaking changes from the last 30 days. See [Deprecations & Breaking Changes](DEPRECATIONS.md) for the full list.*

- **Oct 19, 2026** - 🚫 **Deprecation** - [GitHub Copilot models deprecated on October 19, 2026](https://github.blog/changelog/2026-10-19-github-copilot-models-deprecated-on-october-19-2026)
- **Oct 15, 2026** - 🚫 **Deprecation** - [Upcoming deprecation of selected GitHub Copilot models in mid-November](https://github.blog/changelog/2026-10-15-upcoming-deprecation-of-selected-github-copilot-models-in-mid-november)

---

## This Week (Last 7 Days)

### [Global default for Copilot features generally available](https://github.blog/changelog/2026-10-22-global-default-for-copilot-features-generally-available)
*Oct 22, 2026*

GitHub is rolling out enforcement of its global default policy for generally available Copilot features and supported client capabilities on Business and Enterprise plans through October 26. Organizations may see the policy take effect at different times during the rollout.

### [Public monitoring now available with data residency](https://github.blog/changelog/2026-10-22-public-monitoring-now-available-with-data-residency)
*Oct 22, 2026*

Public monitoring is now available in public preview for GitHub Enterprise Cloud with data residency (GHEC DR). Public monitoring extends secret scanning beyond internal repositories by monitoring public commits across github.com, attributing exposed credentials back to your enterprise in real time.

### [Custom skills, agents, and MCP servers in usage metrics API](https://github.blog/changelog/2026-10-22-custom-skills-agents-and-mcp-servers-in-usage-metrics-api)
*Oct 22, 2026*

Copilot usage metrics now show the names of the skills, custom agents, Model Context Protocol (MCP) servers, slash commands, and plugins that your organization creates, instead of grouping them under other or custom. This builds on the agentic CLI customization metrics released in September.

### [Industry comparisons in the Copilot impact dashboard](https://github.blog/changelog/2026-10-22-industry-comparisons-in-the-copilot-impact-dashboard)
*Oct 22, 2026*

The Copilot impact dashboard now includes an "Industry comparison" section. Enterprises, and organizations that aren't owned by an enterprise, can compare their Copilot agentic adoption and leverage with aggregated benchmarks from participating peers. Participation is opt-in and disabled by default.

### [GitHub Copilot in Visual Studio — September update](https://github.blog/changelog/2026-10-22-github-copilot-in-visual-studio-september-update-2)
*Oct 22, 2026*

The September Visual Studio update adds pull-request exploration from chat, support for a team's preferred AI model, and fixes for vulnerable packages flagged by the IDE. These improvements bring Copilot into review and dependency-maintenance workflows without leaving Visual Studio.

---

## Last 30 Days

### [Stop waiting on pull request reviews with GitHub Copilot approvals](https://www.youtube.com/shorts/exBCpV9eJnc)
*Oct 22, 2026*

Copilot can review a pull request and submit an assessment that counts toward merge protection rules. Combining its review with a single human approval can satisfy branch requirements while reducing delays.

### [GitHub CLI: Opt in to expiring, auto-refreshing OAuth tokens](https://github.blog/changelog/2026-10-21-github-cli-opt-in-to-expiring-auto-refreshing-oauth-tokens)
*Oct 21, 2026*

You can now use expiring, automatically refreshing OAuth credentials in GitHub CLI as part of a public preview. When you opt in, gh stores an expiring access token alongside a rotating refresh token and automatically refreshes the token whenever it is needed. You stay authenticated without reauthenticating, and a leaked access token becomes unusable within hours instead of lasting indefinitely.

### [Inside GitHub's September updates: Project HydraFusion, sandboxing, and PR approvals](https://www.youtube.com/watch?v=ZQ0Qq6LlAmI)
*Oct 21, 2026*

This episode reviews September's major platform updates, including Project HydraFusion's expansion to VS Code and the Copilot app, local sandboxing, automated code review approvals, and bulk autofix for up to 25 CodeQL quality findings. The discussion explains how these changes improve model visibility, review workflows, and security remediation.

### [Updates to GitHub secret scanning](https://github.blog/changelog/2026-10-20-updates-to-github-secret-scanning)
*Oct 20, 2026*

This update covers improvements and bug fixes for GitHub secret scanning. On November 12, 2026, the business field in affected secret_scanning_alert.* and secret_scanning_push_protection.bypass audit log events will change from the enterprise display name to the enterprise slug.

### [How 3 Java Champions are using GitHub Copilot for increased productivity](https://github.blog/ai-and-ml/github-copilot/how-3-java-champions-are-using-github-copilot-for-increased-productivity/)
*Oct 20, 2026*

AI coding tools can generate code quickly, but speed alone does not solve the hardest software engineering problems. Developers still need to provide context, validate results, protect maintainability, and remain accountable for what ships. To learn how experienced developers strike that balance, we spoke with three Java Champions, all with over a decade of experience in using Java.

### [Bulk migrate branch protections to rulesets for a repository](https://github.blog/changelog/2026-10-20-bulk-migrate-branch-protections-to-rulesets-for-a-repository)
*Oct 20, 2026*

Repository administrators can now convert all branch protection rules to rulesets in a single action, building on the existing single-rule migration. Use **Settings → Rulesets** and select **Import branch protection rules** to migrate them together.

### [Fix GitHub issues without leaving JetBrains IntelliJ using GitHub Copilot](https://www.youtube.com/shorts/Y9dEqpQeD8w)
*Oct 20, 2026*

The video demonstrates installing the Copilot plugin, finding an open issue, and generating an implementation plan in JetBrains IntelliJ. It then shows the coding agent implementing the fix and explaining its changes in Ask mode.

### [Copilot model policy API for enterprise, orgs, and teams](https://github.blog/changelog/2026-10-19-copilot-model-policy-api-for-enterprise-orgs-and-teams)
*Oct 19, 2026*

You can now use the REST API to retrieve and update Copilot model policies for enterprises, enterprise teams, agent apps, and organizations. Enterprise policies can delegate model control to organizations in organization mode, or to teams and apps in enterprise teams mode.

### [GitHub Copilot models deprecated on October 19, 2026](https://github.blog/changelog/2026-10-19-github-copilot-models-deprecated-on-october-19-2026)
*Oct 19, 2026*

As of today, October 19, 2026, we have deprecated the following models across most GitHub Copilot experiences (including Copilot Chat, inline edits, ask and agent modes, and code completions). These deprecations were announced on September 18, 2026.

### [How to continue a GitHub Copilot app session in VS Code](https://github.blog/ai-and-ml/github-copilot/how-to-continue-a-github-copilot-app-session-in-vs-code/)
*Oct 19, 2026*

Move an active agent session from the GitHub Copilot app to VS Code without losing its conversation, code changes, or working context. The guide shows how to continue in your editor to inspect details, make edits, and run the project locally.

---

## Older Updates

See [CHANGELOG.md](CHANGELOG.md) for the full historical timeline.

---

_All dates are complete and sorted newest first. For a full list of updates, see [CHANGELOG.md](CHANGELOG.md)._
