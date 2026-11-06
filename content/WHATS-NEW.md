# What's New with GitHub Copilot

> Latest updates from the last 30 days

**Last Updated**: November 06, 2026

This page highlights significant Copilot updates from the past 30 days. Content older than 30 days moves to [CHANGELOG.md](CHANGELOG.md).

---

## ⚠️ Action Required

*Deprecations and breaking changes from the last 30 days. See [Deprecations & Breaking Changes](DEPRECATIONS.md) for the full list.*

No deprecations or breaking changes in the last 30 days. ✅

---

## This Week (Last 7 Days)

### [Secret scanning upgrades detectors, adds SpaceX as partner](https://github.blog/changelog/2026-11-05-secret-scanning-upgrades-detectors-adds-spacex-as-partner)
*Nov 5, 2026*

This update expands secret scanning's detection coverage:
New partner: SpaceX is now a secret scanning partner. New detector: GitHub now detects starlink_public_api_v2_secret. Upgraded detectors: Alibaba, AWS, Google, OpenVSX, Pydantic Services, and Tencent detectors include additional false-positive filtering.

### [New pull request overview page in public preview](https://github.blog/changelog/2026-11-05-new-pull-request-overview-page-in-public-preview)
*Nov 5, 2026*

On a long pull request, checking what's blocking often means scrolling past dozens of comments and timeline events just to reach the merge box. And once you're there, you still need to work out what to do next. As people need to review more and more pull requests, time spent scrolling adds up.

### [Usage metrics API adds code review details and addressed rate](https://github.blog/changelog/2026-11-05-usage-metrics-api-adds-code-review-details-and-addressed-rate)
*Nov 5, 2026*

The enterprise and organization repository-level Copilot usage metrics reports now show what happens to Copilot code review feedback. A new copilot_code_review object on each repos-1-day row reports how many Copilot-reviewed pull requests merged without a later change request from a person and how many Copilot code review comments developers acted on.

### [Usage metrics API flags telemetry and version gaps](https://github.blog/changelog/2026-11-05-usage-metrics-api-flags-telemetry-and-version-gaps)
*Nov 5, 2026*

The Copilot usage metrics API now shows which users are missing client telemetry or are running IDE or extension versions below the usage metrics minimums. New per-user fields appear in enterprise and organization user reports, and daily affected-user counts appear in enterprise and organization reports.

### [CodeQL 2.27.4 improves accuracy and query metadata](https://github.blog/changelog/2026-11-04-codeql-2-27-4-improves-accuracy-and-query-metadata)
*Nov 4, 2026*

CodeQL is the static analysis engine behind GitHub code scanning, which finds and remediates security issues in your code. We've recently released CodeQL 2.27.4 with query accuracy improvements across several languages, stronger security checks when you bundle or publish a pack, and corrections to query metadata.

---

## Last 30 Days

### [GitHub Copilot is now available in Xcode’s coding assistant](https://github.blog/changelog/2026-11-04-github-copilot-is-now-available-in-xcodes-coding-assistant)
*Nov 4, 2026*

You can now work with GitHub Copilot directly in Xcode's built-in coding assistant, bringing Copilot into your native Xcode workflow. The integration is now in public preview, available starting with Xcode 27.3 beta. This gives you another way to use Copilot in Xcode.

### [BYOK and enterprise custom models in the Copilot usage API](https://github.blog/changelog/2026-11-03-byok-and-enterprise-custom-models-in-the-copilot-usage-api)
*Nov 3, 2026*

The Copilot usage metrics API now shows bring your own key (BYOK) usage across GitHub Copilot, so you can separate it from Copilot-hosted model usage. Reports cover two kinds of BYOK:
Local BYOK is configured by developers in their client. Requests go from Copilot CLI or the GitHub Copilot app directly to the developer's provider key or local model.

### [Arnis turns any place on Earth into a Minecraft world](https://github.blog/open-source/maintainers/arnis-turns-any-place-on-earth-into-a-minecraft-world/)
*Nov 3, 2026*

Louis Erbkamm knows his way around Arnis, the smallest town in Germany, but he's never set foot in it. Where the boats are&hellip; I know the city pretty well, but I haven't been there yet.

### [Dependabot version updates support Agent Package Manager](https://github.blog/changelog/2026-11-03-dependabot-version-updates-support-agent-package-manager)
*Nov 3, 2026*

You can now keep your AI agent skills, prompts, and instructions up to date with Dependabot version updates for Agent Package Manager (APM). Dependabot opens pull requests to update supported git dependencies declared in apm.yml and regenerates apm.lock.yaml when it's present. This support covers version updates, not security updates.

### [GitHub Copilot is now available in JetBrains Air](https://github.blog/changelog/2026-11-03-github-copilot-is-now-available-in-jetbrains-air)
*Nov 3, 2026*

You can now delegate coding tasks, guide execution, and review results with GitHub Copilot in JetBrains Air. The integration uses the Agent Client Protocol (ACP) and supports tasks in your JetBrains IDE or in the cloud. Use Copilot in Air alongside the GitHub Copilot plugin and choose the workflow that works best for you.

### [GitHub Copilot app, Universe releases](https://github.blog/changelog/2026-10-28-github-copilot-app-universe-releases)
*Oct 28, 2026*

Work doesn't always fit in a single repository or session. A feature can span several repositories. A launch plan can pull in specs, designs, and assets without touching a repository at all.

### [Security extension for the GitHub Copilot app](https://github.blog/changelog/2026-10-28-security-extension-for-the-github-copilot-app)
*Oct 28, 2026*

You can now work through your repository's GitHub code scanning alerts without leaving the GitHub Copilot app. The new GitHub security extension, now in public preview, lets you find the alerts that matter most and ask Copilot to explain or help fix them. Until now, fixing a code scanning alert meant switching between the alert on github.com and the code in your editor.

### [GitHub intelligence puts your code, context, and history to work](https://github.blog/changelog/2026-10-28-github-intelligence-puts-your-code-context-and-history-to-work)
*Oct 28, 2026*

Agents should understand more than your codebase—they should understand how your team works. Your preferences, repository conventions, skills, and custom instructions guide how changes should be made, while code in related repositories can show how the pieces fit together. Without that context, agents spend time rediscovering knowledge and can miss your team's conventions.

### [GitHub Universe 2026: Evolving every layer of the stack](https://github.blog/news-insights/company-news/github-universe-2026-evolving-every-layer-of-the-stack/)
*Oct 28, 2026*

Our jobs as developers are changing. In a couple of years, we've gone from writing every line of code to working with AI assistants to orchestrating fleets of agents. But the goal hasn't changed: ship completed software work.

### [GitHub Enterprise now includes access to GitHub Copilot](https://github.blog/changelog/2026-10-28-github-enterprise-now-includes-access-to-github-copilot)
*Oct 28, 2026*

Enterprises working with a GitHub or Microsoft account team can now get Copilot included with GitHub Enterprise for every licensed user. Previously, you had to manage two things: how many Copilot seats you were paying for and how much AI usage those users consumed. With Copilot included in the platform, usage against your enterprise budget is the primary thing to manage.

---

## Older Updates

See [CHANGELOG.md](CHANGELOG.md) for the full historical timeline.

---

_All dates are complete and sorted newest first. For a full list of updates, see [CHANGELOG.md](CHANGELOG.md)._
