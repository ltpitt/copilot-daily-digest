# What's New with GitHub Copilot

> Latest updates from the last 30 days

**Last Updated**: November 06, 2026

This page highlights significant Copilot updates from the past 30 days. Content older than 30 days moves to [CHANGELOG.md](CHANGELOG.md).

---

## ⚠️ Action Required

*Deprecations and breaking changes from the last 30 days. See [Deprecations & Breaking Changes](DEPRECATIONS.md) for the full list.*

- **Oct 19, 2026** - [GitHub Copilot models deprecated on October 19, 2026](https://github.blog/changelog/2026-10-19-github-copilot-models-deprecated-on-october-19-2026)
- **Oct 15, 2026** - [Upcoming deprecation of selected GitHub Copilot models in mid-November](https://github.blog/changelog/2026-10-15-upcoming-deprecation-of-selected-github-copilot-models-in-mid-november)

---

## This Week (Last 7 Days)

### [Secret scanning upgrades detectors, adds SpaceX as partner](https://github.blog/changelog/2026-11-05-secret-scanning-upgrades-detectors-adds-spacex-as-partner)
*Nov 5, 2026*

Secret scanning now includes SpaceX as a partner and detects the Starlink public API v2 secret. GitHub also upgraded detectors for Alibaba, AWS, Google, OpenVSX, Pydantic Services, and Tencent with additional false-positive filtering.

### [New pull request overview page in public preview](https://github.blog/changelog/2026-11-05-new-pull-request-overview-page-in-public-preview)
*Nov 5, 2026*

The new overview page brings blockers and next steps into clearer view on long pull requests, so reviewers spend less time scrolling through comments and timeline events. It is now available in public preview.

### [Usage metrics API adds code review details and addressed rate](https://github.blog/changelog/2026-11-05-usage-metrics-api-adds-code-review-details-and-addressed-rate)
*Nov 5, 2026*

Repository-level Copilot usage metrics now include a `copilot_code_review` object on each `repos-1-day` row. It reports how many Copilot-reviewed pull requests merged without a later human change request and how many Copilot review comments developers addressed.

### [Usage metrics API flags telemetry and version gaps](https://github.blog/changelog/2026-11-05-usage-metrics-api-flags-telemetry-and-version-gaps)
*Nov 5, 2026*

The Copilot usage metrics API now identifies users missing client telemetry or running IDE and extension versions below the supported minimums. Enterprise and organization reports include per-user details and daily counts of affected users, helping administrators spot gaps in their usage data.

### [CodeQL 2.27.4 improves accuracy and query metadata](https://github.blog/changelog/2026-11-04-codeql-2-27-4-improves-accuracy-and-query-metadata)
*Nov 4, 2026*

CodeQL 2.27.4 improves query accuracy across several languages and strengthens security checks when bundling or publishing a pack. The release also corrects query metadata used by GitHub code scanning.

---

## Last 30 Days

### [GitHub Copilot is now available in Xcode’s coding assistant](https://github.blog/changelog/2026-11-04-github-copilot-is-now-available-in-xcodes-coding-assistant)
*Nov 4, 2026*

GitHub Copilot is now available in Xcode's built-in coding assistant, bringing Copilot into the native Xcode workflow. The integration is in public preview starting with Xcode 27.3 beta.

### [BYOK and enterprise custom models in the Copilot usage API](https://github.blog/changelog/2026-11-03-byok-and-enterprise-custom-models-in-the-copilot-usage-api)
*Nov 3, 2026*

The Copilot usage metrics API now reports bring-your-own-key (BYOK) and enterprise custom model usage, separating it from Copilot-hosted model usage. This gives administrators a clearer view of requests routed through developers' own provider keys or local models.

### [Arnis turns any place on Earth into a Minecraft world](https://github.blog/open-source/maintainers/arnis-turns-any-place-on-earth-into-a-minecraft-world/)
*Nov 3, 2026*

Arnis turns real-world locations into Minecraft worlds, and its creator Louis Erbkamm built the first version in his free time. The story explores how GitHub Copilot helps him maintain the project on his own, despite never having visited the town that inspired it.

### [Dependabot version updates support Agent Package Manager](https://github.blog/changelog/2026-11-03-dependabot-version-updates-support-agent-package-manager)
*Nov 3, 2026*

Dependabot version updates now keep supported agent skills, prompts, and instructions declared in `apm.yml` current. It opens pull requests for Git dependencies and regenerates `apm.lock.yaml` when present; security updates are not included.

### [GitHub Copilot is now available in JetBrains Air](https://github.blog/changelog/2026-11-03-github-copilot-is-now-available-in-jetbrains-air)
*Nov 3, 2026*

GitHub Copilot in JetBrains Air lets you delegate coding tasks, guide execution, and review results in your IDE or in the cloud. The Agent Client Protocol (ACP) integration complements the existing GitHub Copilot plugin, giving developers another way to work with coding agents.

### [GitHub Copilot app, Universe releases](https://github.blog/changelog/2026-10-28-github-copilot-app-universe-releases)
*Oct 28, 2026*

The GitHub Copilot app is expanding to support work that spans multiple repositories or sessions. Launch plans can also bring together specifications, designs, and assets without requiring a repository.

### [Security extension for the GitHub Copilot app](https://github.blog/changelog/2026-10-28-security-extension-for-the-github-copilot-app)
*Oct 28, 2026*

The GitHub security extension brings repository code scanning alerts into the Copilot app, where you can ask Copilot to explain or help fix them. The public preview reduces the need to switch between alerts on GitHub.com and code in your editor.

### [GitHub intelligence puts your code, context, and history to work](https://github.blog/changelog/2026-10-28-github-intelligence-puts-your-code-context-and-history-to-work)
*Oct 28, 2026*

GitHub intelligence aims to help agents understand how a team works, not just how its code is structured. Preferences, repository conventions, skills, custom instructions, and related repositories can provide context that helps agents follow established practices.

### [GitHub Universe 2026: Evolving every layer of the stack](https://github.blog/news-insights/company-news/github-universe-2026-evolving-every-layer-of-the-stack/)
*Oct 28, 2026*

GitHub outlined a vision for an end-to-end software delivery system that evolves across the development stack. The announcement reflects a shift from writing code line by line toward using AI assistants and orchestrating agents, while keeping the goal of shipping finished software.

### [GitHub Enterprise now includes access to GitHub Copilot](https://github.blog/changelog/2026-10-28-github-enterprise-now-includes-access-to-github-copilot)
*Oct 28, 2026*

Enterprises working with a GitHub or Microsoft account team can now include Copilot for every licensed user through GitHub Enterprise. This replaces separate Copilot seat management with a focus on tracking usage against the enterprise budget.

---

## Older Updates

See [CHANGELOG.md](CHANGELOG.md) for the full historical timeline.

---

_All dates are complete and sorted newest first. For a full list of updates, see [CHANGELOG.md](CHANGELOG.md)._
