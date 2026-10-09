# What's New with GitHub Copilot

> Latest updates from the last 30 days

**Last Updated**: October 09, 2026

This page highlights significant Copilot updates from the past 30 days. Content older than 30 days moves to [CHANGELOG.md](CHANGELOG.md).

---

## ⚠️ Action Required

*Deprecations and breaking changes from the last 30 days. See [Deprecations & Breaking Changes](DEPRECATIONS.md) for the full list.*

- **Oct 2, 2026** - 🚫 **Deprecation** - [Selected models in GitHub Copilot deprecated](https://github.blog/changelog/2026-10-02-selected-models-in-github-copilot-deprecated)
- **Sep 10, 2026** - 🚫 **Deprecation** - [Mai Code 1 Flash Deprecated](https://github.blog/changelog/2026-09-10-mai-code-1-flash-deprecated)

---

## This Week (Last 7 Days)

### [Screen readers can navigate timelines as lists](https://github.blog/changelog/2026-10-08-screen-readers-can-navigate-timelines-as-lists)
*Oct 8, 2026*

Screen readers can now navigate issue and pull request timelines as a list. When you move through a timeline, assistive technology can announce the list structure, item count, current position, and how to move between events. This makes it easier to understand long histories and jump to relevant updates without relying on visual scanning.

### [Draft pull requests count toward pull request limits](https://github.blog/changelog/2026-10-08-draft-pull-requests-count-toward-pull-request-limits)
*Oct 8, 2026*

Maintainers are seeing more low-quality contributions in their repositories and need better ways to manage them. You can now configure pull request limits to also include draft pull requests. Previously, draft pull requests didn't count toward a user's limit.

### [Triage role users or higher can now archive pull requests](https://github.blog/changelog/2026-10-08-triage-role-users-or-higher-can-now-archive-pull-requests)
*Oct 8, 2026*

Users with the triage role or higher in a repository can now archive and unarchive pull requests. Previously, archiving was limited to repository administrators, requiring trusted triagers to hand routine moderation work to someone with higher permissions. Maintainers increasingly rely on triagers to keep pull request queues healthy without granting them permission to change code.

### [How to run GitHub Copilot agent sessions across any device | GitHub Copilot Day](https://www.youtube.com/watch?v=KT6p0MNXoCE)
*Oct 8, 2026*

Agent sessions shouldn't be locked into a single code editor or terminal window. Patrick Nikoletich explains how GitHub's shared agent runtime, Copilot SDK, and Agent Host Protocol let developers move active sessions seamlessly across multiple...

### [Local sandboxing for GitHub Copilot now generally available](https://github.blog/changelog/2026-10-07-local-sandboxing-for-github-copilot-now-generally-available)
*Oct 7, 2026*

Local sandboxing for GitHub Copilot is now generally available in GitHub Copilot CLI, the GitHub Copilot app, and VS Code sessions using Agent Host. Local sandboxes give developers a secure execution boundary for agentic workflows on their own machines.

---

## Last 30 Days

### [Discover local models in GitHub Copilot CLI](https://github.blog/changelog/2026-10-07-discover-local-models-in-github-copilot-cli)
*Oct 7, 2026*

GitHub Copilot CLI makes it easier to choose a local model without leaving your existing workflow. Starting in CLI version 1.0.94-0, use /model to discover supported models from a running local Ollama instance, alongside your configured models and cloud models provided by GitHub Copilot. Discovery doesn't automatically add models.

### [Claude Haiku 5.5 in GitHub Copilot](https://github.blog/changelog/2026-10-07-claude-haiku-5-5-in-github-copilot)
*Oct 7, 2026*

Claude Haiku 5.5, Anthropic's newest lightweight model, is now generally available in GitHub Copilot. It is designed for fast, high-volume work like subagents, quick edits, and terminal tasks. In early testing, Haiku 5.5 matched Claude Sonnet 5 on many coding tasks while using significantly fewer tokens and steps.

### [Purpose-built model for leaked secret detection](https://github.blog/changelog/2026-10-07-purpose-built-model-for-leaked-secret-detection)
*Oct 7, 2026*

Secret protection should keep pace with the way you build software, whether you write code yourself or work with an AI agent. With our new purpose-built model, we're bringing context-aware detection into more developer workflows to help you catch secrets before they're exposed.

### [Intelligent local model routing is coming to GitHub Copilot](https://www.youtube.com/watch?v=QIHnmqYU614)
*Oct 7, 2026*

GitHub Copilot is extending intelligent model orchestration from the cloud down to your local machine. Copilot can automatically discover installed local models from providers like Ollama and...

### [Code scanning AI Scan enablement status in security overview](https://github.blog/changelog/2026-10-06-code-scanning-ai-scan-enablement-status-in-security-overview)
*Oct 6, 2026*

Organization and enterprise administrators can now see AI Scan for pull requests enablement status in the security overview coverage view. The code scanning summary shows enabled and not enabled repository counts, while repository rows show each repository's effective AI Scan enablement.

### [Update your IDE to restore agent activity in Copilot usage metrics](https://github.blog/changelog/2026-10-06-update-your-ide-to-restore-agent-activity-in-copilot-usage-metrics)
*Oct 6, 2026*

If your Copilot usage metrics have shown agent activity or agent lines of code falling while Copilot usage kept growing, we've found the cause, and a fix is rolling out to each IDE. Several IDEs recently moved Copilot agent sessions to the Copilot SDK. Those sessions didn't identify which IDE they came from, so usage metrics couldn't attribute them correctly.

### [Stacked pull requests generally available](https://github.blog/changelog/2026-10-06-stacked-pull-requests-generally-available)
*Oct 6, 2026*

GitHub stacked pull requests are now generally available. Break large changes into smaller, focused pull requests that you can review independently and merge together. Since the feature went into public preview, repositories using stacks have seen a 9% increase in merged code compared to peers.

### [ScreenMind: Vision, Audio & Chat with Local AI | Open Source Friday](https://www.youtube.com/watch?v=N_cGKFGMxxc)
*Oct 6, 2026*

What if one local AI model could understand your screen, transcribe meetings, and answer questions about what you’ve seen?

### [How GitHub PR limits help maintainers stop AI slop](https://www.youtube.com/shorts/8VslAmTPo3I)
*Oct 6, 2026*

Low-quality pull requests and automated spam, often referred to as AI slop, have become a major burden for open-source maintainers.

### [ReviewBench: An open benchmark for AI code review](https://github.blog/ai-and-ml/github-copilot/reviewbench-an-open-benchmark-for-ai-code-review/)
*Oct 5, 2026*

Agentic code review is becoming an essential piece of how development happens. It helps you inspect pull requests, catch issues, and decide what deserves attention before code ships. But the quality of existing AI reviewers can be hard to measure, and you need to know the strengths of a reviewer before you know if it will help you.

---

## Older Updates

See [CHANGELOG.md](CHANGELOG.md) for the full historical timeline.

---

_All dates are complete and sorted newest first. For a full list of updates, see [CHANGELOG.md](CHANGELOG.md)._
