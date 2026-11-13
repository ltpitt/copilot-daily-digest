# What's New with GitHub Copilot

> Latest updates from the last 30 days

**Last Updated**: November 13, 2026

This page highlights significant Copilot updates from the past 30 days. Content older than 30 days moves to [CHANGELOG.md](CHANGELOG.md).

---

## ⚠️ Action Required

*Deprecations and breaking changes from the last 30 days. See [Deprecations & Breaking Changes](DEPRECATIONS.md) for the full list.*

- **Nov 12, 2026** - 🗑️ **Retirement/Removal** - [Actions for ARM32 Linux & Windows retirement](https://github.blog/changelog/2026-11-12-actions-for-arm32-linux-windows-retirement)
- **Oct 19, 2026** - [GitHub Copilot models deprecated on October 19, 2026](https://github.blog/changelog/2026-10-19-github-copilot-models-deprecated-on-october-19-2026)
- **Oct 15, 2026** - [Upcoming deprecation of selected GitHub Copilot models in mid-November](https://github.blog/changelog/2026-10-15-upcoming-deprecation-of-selected-github-copilot-models-in-mid-november)

---

## This Week (Last 7 Days)

### [Actions for ARM32 Linux & Windows retirement](https://github.blog/changelog/2026-11-12-actions-for-arm32-linux-windows-retirement)
*Nov 12, 2026*

GitHub Actions hosted runners will be ending support for ARM32 job execution on Windows and Linux by 8th Dec 2026. This follows our end of support for node20 where Node 24 does not support ARM32. This includes the removal of support on hosted runners for native AArch32 User-space execution.

### [Build once, run on any agent: A practical guide to agent skills](https://github.blog/ai-and-ml/github-copilot/build-once-run-on-any-agent-a-practical-guide-to-agent-skills/)
*Nov 12, 2026*

Agent skills package repeatable task instructions in versioned directories centered on a `SKILL.md` file, making them reviewable and reusable across agent hosts. Tools, project context, credentials, and permissions still come from each host, so a skill can guide work without granting access.

### [Public monitoring alerts now have direct links](https://github.blog/changelog/2026-11-12-public-monitoring-alerts-now-have-direct-links)
*Nov 12, 2026*

You can now access individual public monitoring alerts with a direct link to each alert. In your enterprise's Public monitoring view, click an alert number to open the alert. You can use its URL to bookmark the finding or share it with teammates who have access.

### [Issue types and fields are available for personal accounts](https://github.blog/changelog/2026-11-11-issue-types-and-fields-are-available-for-personal-accounts)
*Nov 11, 2026*

Personal repositories now support issue types and custom fields, bringing structured planning tools to individual developers and open-source maintainers. Owners can configure categories and fields from account settings to organize issues consistently across repositories.

### [A more informative GitHub dashboard](https://github.blog/changelog/2026-11-10-a-more-informative-github-dashboard)
*Nov 10, 2026*

GitHub has redesigned its dashboard to surface more work with less scrolling. Developers can pin Feed or Home, see six pull requests and issues by default, scan single-line titles, and hide an empty agent-sessions section.

---

## Last 30 Days

### [GitHub App support for Enterprise Copilot seat management](https://github.blog/changelog/2026-11-10-github-app-support-for-enterprise-copilot-seat-management)
*Nov 10, 2026*

Enterprise GitHub Apps can now call the enterprise-level Copilot seat management APIs to control which users and enterprise teams are assigned Copilot seats. The Copilot seat management APIs are accessible with a new enterprise fine-grained permission for Apps: Enterprise Copilot license management.

### [C++ language server now auto-configures MSBuild builds](https://github.blog/changelog/2026-11-10-c-language-server-now-auto-configures-msbuild-builds)
*Nov 10, 2026*

The Microsoft C++ Language Server for GitHub Copilot CLI now bundles its MSBuild compile commands extractor and invokes it automatically. An agent no longer needs to discover and run a separate configuration skill before it can get precise code intelligence for your project. For more information, including the installation instructions, see the main repository page.

### [Gemini 4 Carbon in GitHub Copilot](https://github.blog/changelog/2026-11-10-gemini-4-carbon-in-github-copilot)
*Nov 10, 2026*

Gemini 4 Carbon, Google's latest model, is now generally available in GitHub Copilot. It is designed for complex coding, agentic, and reasoning tasks, with a focus on secure code generation and security-focused work. This model is billed at provider list pricing under usage-based billing.

### [Dependabot alerts will pause on inactive repositories](https://github.blog/changelog/2026-11-10-dependabot-alerts-will-pause-on-inactive-repositories)
*Nov 10, 2026*

Starting December 8, 2026, GitHub will turn off Dependabot alerts on most repositories with no activity in the past year. Their existing alerts are archived, not deleted, and you can restore them at any time. With vulnerability discovery and alert volume growing quickly, this keeps Dependabot fast and reliable for the repositories you're actively developing.

### [Claude Fable 5.2 in GitHub Copilot](https://github.blog/changelog/2026-11-09-claude-fable-5-2-in-github-copilot)
*Nov 9, 2026*

Claude Fable 5.2, Anthropic's newest Fable model, is now generally available in GitHub Copilot. You can use it for complex, multistep coding tasks across large codebases. In early testing, Fable 5.2 solved more tasks than Claude Fable 5.1 while using fewer steps and tool calls.

### [Beyond code generation: A developer’s guide to agentic engineering](https://github.blog/ai-and-ml/github-copilot/beyond-code-generation-a-developers-guide-to-agentic-engineering/)
*Nov 6, 2026*

GitHub's guide applies Copilot across a four-stage Plan, Build, Verify, and Observe workflow, from requirements and implementation through review and production monitoring. It explains where agents can help at each stage and why developers still need to steer decisions and verify results.

### [Copilot code review: API management and review overview updates](https://github.blog/changelog/2026-11-06-copilot-code-review-api-management-and-review-overview-updates)
*Nov 6, 2026*

You can now manage GitHub Copilot code review settings through the REST and GraphQL APIs, from enterprise policy down to individual repositories. Copilot's review overview comment is now more compact, and this update includes fixes for billing, automatic reviews, and reliability. These updates are available to Copilot Pro, Pro+, Max, Business, and Enterprise plans.

### [GitHub Copilot weekly releases — November 2](https://github.blog/changelog/2026-11-06-github-copilot-weekly-releases-november-2)
*Nov 6, 2026*

This week, Copilot comes to JetBrains Air and Xcode's coding assistant, with updates to help you manage pull requests, settings, and agent sessions. Set up Agent Merge directly from a pull request to have Copilot merge it when it's ready. It now stays enabled while required checks or rules are pending.

### [@GitHub in Slack and Teams is generally available and more](https://github.blog/changelog/2026-11-06-github-copilot-in-slack-and-teams-is-generally-available)
*Nov 6, 2026*

Turn conversations into code with @GitHub in Slack and Teams! Investigate bugs, create issues, implement changes, and open pull requests—all without leaving your conversation. Turn team discussions into working code.

### [Copilot impact dashboard adds chat and VS Code agent usage](https://github.blog/changelog/2026-11-06-copilot-impact-dashboard-adds-chat-and-vs-code-agent-usage)
*Nov 6, 2026*

The Agent adoption chart in the Copilot impact dashboard now includes Copilot Chat and the VS Code Agents window, so you can see engagement across nine Copilot experiences. The adoption cohort called "Passive users" is now "Chat-first users", which better describes who is in it. The enterprise and organization 28-day usage metrics reports include the same two features.

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

The GitHub Universe closing keynote brings together open-source voices, unexpected demos, and reflections on why people code. Maggie Appleton, Martin Woodward, and Jocelyn Velarde discuss how community-driven software, creative experiments, and open collaboration shape software development.

### [Webhook IP ranges added to the Meta API](https://github.blog/changelog/2026-10-29-webhook-ip-ranges-added-to-the-meta-api)
*Oct 29, 2026*

GitHub added IP ranges for webhook deliveries on github.com to the `hooks` field in the Meta API. The new ranges help consumers account for webhook traffic from GitHub.

### [Can you commit to the answer? Git trivia at GitHub Universe 2026](https://www.youtube.com/shorts/-qx1qD_3hus)
*Oct 29, 2026*

GitHub Universe attendees test their knowledge of Git commands, repositories, and internal storage objects in this quick trivia challenge. Questions cover topics such as forks, `git blame`, and Git's blob objects.

### [Playing Super Mona on the GitHub Universe 2026 badge](https://www.youtube.com/shorts/5pK-8AL_wVs)
*Oct 29, 2026*

Martin Woodward demonstrates the hidden capacitive gaming buttons on the GitHub Universe 2026 badge. The short demo shows how to install Super Mona on the badge using the GitHub Copilot app.

### [Everything announced at GitHub Universe 2026: opening keynote recap](https://www.youtube.com/watch?v=xbCa0aa4tRM)
*Oct 29, 2026*

Catch up on GitHub Universe announcements and demos, including the GitHub Copilot app, third-party connectors, and Copilot Fusion. The recap also covers Copilot Projects for coordinating agents across repositories, Code Review Max, and Git architecture updates.

### [GitHub Universe 2026 opening keynote recap in 90 seconds](https://www.youtube.com/shorts/A_N9HM237BA)
*Oct 29, 2026*

This short recap highlights GitHub Universe announcements, from the platform's 225 million developers to major architectural upgrades. It offers a quick overview of the opening keynote for viewers short on time.

### [Repository plugin defaults and enterprise plugin controls generally available](https://github.blog/changelog/2026-10-28-repository-plugin-defaults-and-enterprise-plugin-controls-generally-available)
*Oct 28, 2026*

Repository plugin defaults and enterprise-managed plugin controls are now generally available in VS Code, Copilot CLI, and the GitHub Copilot app. Trusted repositories can enable default plugins, while enterprises can require or block plugins and limit installations to approved marketplaces.

### [GitHub Copilot in VS Code, Universe releases](https://github.blog/changelog/2026-10-28-github-copilot-in-vs-code-universe-releases)
*Oct 28, 2026*

GitHub Copilot in Visual Studio Code adds more choice in models, agent environments, and ways to stay involved. These updates help developers keep work moving across tools and locations.

### [Route and orchestrate models with GitHub Copilot Fusion](https://github.blog/changelog/2026-10-28-route-and-orchestrate-models-with-github-copilot-fusion)
*Oct 28, 2026*

GitHub Copilot Fusion is generally available and can route and orchestrate models for a task. Developers can choose Fusion instead of selecting a model themselves for each piece of work.

### [GitHub Copilot app, Universe releases](https://github.blog/changelog/2026-10-28-github-copilot-app-universe-releases)
*Oct 28, 2026*

The GitHub Copilot app is expanding to support work across multiple repositories or sessions. Launch plans can also combine specifications, designs, and assets without requiring a repository.

### [Security extension for the GitHub Copilot app](https://github.blog/changelog/2026-10-28-security-extension-for-the-github-copilot-app)
*Oct 28, 2026*

The GitHub security extension brings repository code scanning alerts into the Copilot app, where developers can ask Copilot to explain or help fix them. Its public preview helps connect findings on GitHub.com with code in the editor.

### [GitHub intelligence puts your code, context, and history to work](https://github.blog/changelog/2026-10-28-github-intelligence-puts-your-code-context-and-history-to-work)
*Oct 28, 2026*

GitHub intelligence aims to help agents understand how a team works, not just how its code is structured. Repository conventions, skills, custom instructions, and related repositories can give agents context to follow established practices.

### [GitHub Universe 2026: Evolving every layer of the stack](https://github.blog/news-insights/company-news/github-universe-2026-evolving-every-layer-of-the-stack/)
*Oct 28, 2026*

GitHub outlined a vision for an end-to-end software delivery system that evolves across the development stack. The announcement describes a shift from writing code line by line toward using AI assistants and orchestrating agents while focusing on shipping complete software.

### [GitHub Enterprise now includes access to GitHub Copilot](https://github.blog/changelog/2026-10-28-github-enterprise-now-includes-access-to-github-copilot)
*Oct 28, 2026*

Enterprises working with a GitHub or Microsoft account team can now include Copilot for every licensed user through GitHub Enterprise. The change replaces separate Copilot seat management with a focus on tracking usage against the enterprise budget.

### [Build shared workflows for your team with Copilot Automations](https://github.blog/changelog/2026-10-28-build-shared-workflows-for-your-team-with-copilot-automations)
*Oct 28, 2026*

Shared Copilot Automations let teams build and maintain AI-powered workflows by combining prompts, triggers, and approved tools. Copilot runs these workflows in the cloud, using only the tools the team allows.

### [Generate and edit images directly in Copilot](https://github.blog/changelog/2026-10-28-generate-and-edit-images-directly-in-copilot)
*Oct 28, 2026*

Developers can generate and edit images in GitHub Copilot with natural-language requests. Copilot's selected reasoning model uses an image-generation tool powered by GPT Image 2.5 Flare, previews the result inline, and saves it to the project.

---

## Older Updates

See [CHANGELOG.md](CHANGELOG.md) for the full historical timeline.

---

_All dates are complete and sorted newest first. For a full list of updates, see [CHANGELOG.md](CHANGELOG.md)._
