# What's New with GitHub Copilot

> Latest updates from the last 30 days

**Last Updated**: November 27, 2026

This page highlights significant Copilot updates from the past 30 days. Content older than 30 days moves to [CHANGELOG.md](CHANGELOG.md).

---

## ⚠️ Action Required

*Deprecations and breaking changes from the last 30 days. See [Deprecations & Breaking Changes](DEPRECATIONS.md) for the full list.*

- **Nov 12, 2026** - 🗑️ **Retirement/Removal** - [Actions For Arm32 Linux Windows Retirement](https://github.blog/changelog/2026-11-12-actions-for-arm32-linux-windows-retirement)

---

## This Week (Last 7 Days)

### [Copilot code review billing will default to the organization](https://github.blog/changelog/2026-11-25-copilot-code-review-billing-will-default-to-the-organization)
*Nov 25, 2026*

If you haven't chosen how to bill Copilot code review for members with a Copilot license, those reviews will be billed to your organization starting December 30, 2026. To keep billing unchanged, select Member before then. This change applies to organizations and enterprises with Copilot Business or Copilot Enterprise.

### [How to choose the next safe step in application modernization](https://github.blog/ai-and-ml/github-copilot/how-to-choose-the-next-safe-step-in-application-modernization/)
*Nov 25, 2026*

A request to modernize an application often starts with a technology question: Which framework should replace the old one? Before you choose, find out what still works. Then collect evidence that can act as a regression net for that behavior and show where modernization is necessary.

### [More predictable notifications on GitHub.com](https://github.blog/changelog/2026-11-24-more-predictable-notifications-on-github-com)
*Nov 24, 2026*

Starting December 1, 2026, we're migrating notifications on GitHub.com over the course of a week to make subscriptions more predictable, correct unexpected behavior, and support the growing scale of activity. During the rollout, notifications may behave differently for different users. No action is required, but the changes below may affect how you manage and filter notifications.

### [Issue statuses and repository boards are in public preview](https://github.blog/changelog/2026-11-23-issue-statuses-and-repository-boards-are-in-public-preview)
*Nov 23, 2026*

Open or closed doesn't always tell you where an issue stands. You can now use more specific statuses to give your team and agents shared context about what's in flight and what to work on next, then visualize your progress with repository boards. Track progress directly on an issue.

### [Usage reports will include a user ID column starting December 1](https://github.blog/changelog/2026-11-23-usage-reports-will-include-a-user-id-column-starting-december-1)
*Nov 23, 2026*

Starting December 1, 2026, usage reports that include a username column will also include a user_id column next to it. Every column after username will move one position to the right. This change applies to the detailed usage report, the AI usage report, and the premium request usage report, including exports you create with the GitHub REST API.

---

## Last 30 Days

### [Code coverage uploads now flag invalid report formats](https://github.blog/changelog/2026-11-23-code-coverage-uploads-now-flag-invalid-report-formats)
*Nov 23, 2026*

The GitHub Code Quality `upload-code-coverage` action now checks that your coverage report is in Cobertura XML format. Unsupported reports fail in the Actions workflow with a clear error instead of appearing to succeed without showing coverage on pull requests. If this happens, configure your test framework to produce Cobertura XML or convert the report before uploading it.

### [Pin your favorite repositories to your dashboard](https://github.blog/changelog/2026-11-20-pin-your-favorite-repositories-to-your-dashboard)
*Nov 20, 2026*

Editor's note (November 23, 2026): We have temporarily rolled back this change while we improve the experience based on user feedback. Choose which repositories appear on the Dashboard with the new Favorite repositories section. If the new dashboard experience isn't enabled, Top repositories remains unchanged.

### [GitHub Enterprise Server 3.23 release candidate](https://github.blog/changelog/2026-11-20-github-enterprise-server-3-23-release-candidate)
*Nov 20, 2026*

GitHub Enterprise Server (GHES) 3.23 is now available as a release candidate with capabilities spanning project management, security, and infrastructure. Teams can create more precise GitHub Projects views by combining filters with logical `OR`, explicit `AND`, and parentheses, while enterprises can preview AI secret detection entirely within their network. The release also expands malicious-package detection and Dependabot cooldown controls; administrators can review the release notes before downloading the candidate.

### [Security advisory permissions are now generally available](https://github.blog/changelog/2026-11-20-security-advisory-permissions-are-now-generally-available)
*Nov 20, 2026*

Organization owners can now let people work on repository security advisories, including private vulnerability reports, through custom repository roles. You no longer have to make them repository administrators or give them the organization-wide security manager role.

### [Connect Supabase, Box, Calendly, and more to Copilot](https://github.blog/changelog/2026-11-18-connect-supabase-box-calendly-and-more-to-copilot)
*Nov 18, 2026*

You can now connect eight more services to Copilot using GitHub-verified MCP servers, or connectors, available in public preview. They join more than 25 services you can already connect, like Slack, Figma, and Sentry. To see the full list, open Customize in the Copilot app or browse the Copilot customization page.

### [Gemini 4 Neon in GitHub Copilot](https://github.blog/changelog/2026-11-18-gemini-4-neon-in-github-copilot)
*Nov 18, 2026*

Gemini 4 Neon is now generally available in GitHub Copilot. It is designed for agentic coding, multistep tool use, and knowledge work. According to Google, Gemini 4 Neon delivers quality close to Gemini 4 Carbon at a lower token cost per task.

### [Customize GitHub Copilot for your team](https://github.blog/changelog/2026-11-18-customize-github-copilot-for-your-team)
*Nov 18, 2026*

You can now share the GitHub Copilot plugins your team relies on without asking every member to repeat the same setup. Team customizations are generally available for organization teams. Team maintainers and organization owners can select approved Agent Plugins as team defaults.

### [Copilot code review: Adaptive effort, secret detection, and more](https://github.blog/changelog/2026-11-17-copilot-code-review-adaptive-effort-secret-detection-and-more)
*Nov 17, 2026*

GitHub Copilot code review now helps you catch more issues earlier, with less effort. Adaptive matches review depth to each pull request, so routine changes get a quick pass and risky changes get a deeper look. Reviews can also draw on related repositories and flag exposed secrets before they reach your main branch.

### [GitHub Copilot Fusion updates: more availability, benchmarks, and models](https://github.blog/changelog/2026-11-17-github-copilot-fusion-updates-more-availability-benchmarks-and-models)
*Nov 17, 2026*

Today, we're expanding GitHub Copilot Fusion with new models, available on more Copilot surfaces, and results on two public Terminal-Bench leaderboards, giving you more ways to use Fusion and compare its performance. Copilot Fusion is coming to more places you use Copilot.

### [MAI Code 2 and MAI Code 2 Flash in GitHub Copilot](https://github.blog/changelog/2026-11-17-mai-code-2-and-mai-code-2-flash-in-github-copilot)
*Nov 17, 2026*

The next generation of Microsoft AI (MAI) coding models has arrived in GitHub Copilot. Introducing MAI Code 2 and MAI Code 2 Flash, two new models that represent a major step forward for the MAI-Code family, expanding from lightweight coding assistance to complex, agentic software engineering.

---

## Older Updates

See [CHANGELOG.md](CHANGELOG.md) for the full historical timeline.

---

_All dates are complete and sorted newest first. For a full list of updates, see [CHANGELOG.md](CHANGELOG.md)._
