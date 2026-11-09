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

### [GitHub Universe 2026 closing keynote: open source voices, demos, and the craft of coding](https://www.youtube.com/watch?v=Gh-hg7lwA0o)
*Oct 30, 2026*

We are ending GitHub Universe 2026 the way it started: with the people who build in the open. Join Maggie Appleton, Martin Woodward, and Jocelyn Velarde for a closing keynote featuring open-source voices, unexpected demos, and reflections on why people code. The session explores how community-driven software, creative experiments, and open collaboration continue to shape software development.

### [Webhook IP ranges added to the Meta API](https://github.blog/changelog/2026-10-29-webhook-ip-ranges-added-to-the-meta-api)
*Oct 29, 2026*

We're adding IP ranges for GitHub webhook deliveries on github.com. The Meta API now includes these additional ranges in the hooks field.

### [Can you commit to the answer? Git trivia at GitHub Universe 2026](https://www.youtube.com/shorts/-qx1qD_3hus)
*Oct 29, 2026*

You can commit to code, but can you commit to the answer under pressure? We put attendees on the spot at GitHub Universe 2026 to test their knowledge of Git commands, repositories, and internal storage objects.

### [Playing Super Mona on the GitHub Universe 2026 badge](https://www.youtube.com/shorts/5pK-8AL_wVs)
*Oct 29, 2026*

Did you know the GitHub Universe 2026 conference badge has hidden capacitive gaming buttons on the back? In this quick demo, Martin Woodward shows how to install Super Mona directly onto your badge using the GitHub Copilot app.

### [Everything announced at GitHub Universe 2026: opening keynote recap](https://www.youtube.com/watch?v=xbCa0aa4tRM)
*Oct 29, 2026*

Missed the opening keynote at GitHub Universe 2026? Catch up on major announcements and live demos, including the GitHub Copilot app, third-party connectors, and Copilot Fusion. The session also covers Copilot Projects for coordinating agents across repositories, Code Review Max, and architectural updates to Git.

### [GitHub Universe 2026 opening keynote recap in 90 seconds](https://www.youtube.com/shorts/A_N9HM237BA)
*Oct 29, 2026*

Missed the GitHub Universe 2026 opening keynote? Here is everything announced in 60 seconds, from 225 million developers on the platform to major architectural upgrades.

### [Repository plugin defaults and enterprise plugin controls generally available](https://github.blog/changelog/2026-10-28-repository-plugin-defaults-and-enterprise-plugin-controls-generally-available)
*Oct 28, 2026*

Repository plugin defaults and enterprise-managed plugin controls are now generally available in VS Code, Copilot CLI, and the GitHub Copilot app. Trusted repositories can install and enable default plugins for contributors. Enterprises can require plugins, block plugins, and restrict installation to approved marketplaces.

### [GitHub Copilot in VS Code, Universe releases](https://github.blog/changelog/2026-10-28-github-copilot-in-vs-code-universe-releases)
*Oct 28, 2026*

This year, we focused on giving you more choice in how you work with GitHub Copilot in Visual Studio Code: which models you use, where your agents run, and how you stay involved. Keep work moving without staying at your desk or in one tool.

### [Route and orchestrate models with GitHub Copilot Fusion](https://github.blog/changelog/2026-10-28-route-and-orchestrate-models-with-github-copilot-fusion)
*Oct 28, 2026*

GitHub Copilot Fusion is generally available. Instead of picking a model for each task, choose Copilot Fusion and let Copilot intelligently route and orchestrate which models it uses for you.

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

### [Build shared workflows for your team with Copilot Automations](https://github.blog/changelog/2026-10-28-build-shared-workflows-for-your-team-with-copilot-automations)
*Oct 28, 2026*

Shared Copilot Automations are rolling out, enabling teams to build and maintain AI-powered workflows together. With Copilot Automations, you can combine prompts, triggers, and tools to design workflows around the way your team works. Copilot runs autonomously in the cloud, using only the tools you've allowed.

### [Generate and edit images directly in Copilot](https://github.blog/changelog/2026-10-28-generate-and-edit-images-directly-in-copilot)
*Oct 28, 2026*

You can now generate and edit images using natural language in GitHub Copilot. When you ask for an image, your selected reasoning model calls a dedicated image-generation tool powered by GPT Image 2.5 Flare, previews the result inline, and saves it to your project.

---

## Older Updates

See [CHANGELOG.md](CHANGELOG.md) for the full historical timeline.

---

_All dates are complete and sorted newest first. For a full list of updates, see [CHANGELOG.md](CHANGELOG.md)._
