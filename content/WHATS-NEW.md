# What's New with GitHub Copilot

> Latest updates from the last 30 days

**Last Updated**: September 11, 2026

This page highlights significant Copilot updates from the past 30 days. Content older than 30 days moves to [CHANGELOG.md](CHANGELOG.md).

---

## ⚠️ Action Required

*Deprecations and breaking changes from the last 30 days. See [Deprecations & Breaking Changes](DEPRECATIONS.md) for the full list.*

- **Sep 10, 2026** - 🚫 **Deprecation** - [MAI-Code-1-Flash deprecated](https://github.blog/changelog/2026-09-10-mai-code-1-flash-deprecated)
- **Sep 3, 2026** - 🚫 **Deprecation** - [Upcoming deprecation of selected GitHub Copilot models](https://github.blog/changelog/2026-09-03-upcoming-deprecation-of-selected-github-copilot-models)
- **Aug 31, 2026** - 🚫 **Deprecation** - [Selected GitHub Copilot models deprecated](https://github.blog/changelog/2026-08-31-selected-github-copilot-models-deprecated)

---

## This Week (Last 7 Days)

### [AI Scan for pull request APIs in public preview](https://github.blog/changelog/2026-09-10-ai-scan-for-pull-request-apis-in-public-preview)
*Sep 10, 2026*

You can now manage GitHub code scanning's AI Scan for pull request enablement with REST API endpoints at the organization and repository levels. This public preview gives teams a programmatic way to roll out AI-powered security detections for pull requests across select repositories without manually configuring each setting in the GitHub UI.

### [Control GitHub Actions cache access with cache-mode](https://github.blog/changelog/2026-09-10-control-github-actions-cache-access-with-cache-mode)
*Sep 10, 2026*

You can now use cache-mode to apply least-privilege access to the GitHub Actions cache at the workflow or job level. By granting each workflow or job only the cache access it needs, you can prevent unnecessary restores or saves and help protect trusted workflows from cache poisoning. This capability is now generally available on all plans.

### [MAI-Code-1-Flash deprecated](https://github.blog/changelog/2026-09-10-mai-code-1-flash-deprecated)
*Sep 10, 2026*

We have deprecated MAI-Code-1-Flash across GitHub Copilot experiences as of September 10, 2026. Teams using the model should move to MAI-Code-1.1-Flash and confirm any enterprise model policies allow that replacement. Updating now will prevent interruptions in chat, editing, and completion workflows.

### [Xcode 27 runner image now runs on macOS 27](https://github.blog/changelog/2026-09-10-xcode-27-runner-image-now-runs-on-macos-27)
*Sep 10, 2026*

You can now validate your Apple apps against macOS 27 using the Xcode 27 runner image for GitHub-hosted macOS runners, available in public preview. The image previously ran on macOS 26. How you target the image stays the same.

### [GitHub Copilot app for Beginners: Using the diff, terminal, and browser](https://github.blog/ai-and-ml/github-copilot/github-copilot-app-for-beginners-using-the-diff-terminal-and-browser/)
*Sep 10, 2026*

Learn how to review diffs, run commands, and preview apps without leaving the GitHub Copilot app. The guide shows how the app's built-in panels help you verify agent-generated changes before you accept them.

---

## Last 30 Days

### [Refreshed repository pull requests page in public preview](https://github.blog/changelog/2026-09-10-refreshed-repository-pull-requests-page-in-public-preview)
*Sep 10, 2026*

GitHub's refreshed repository pull requests page is now in public preview with stronger filtering and a compact presentation mode. It is designed to help teams scan, sort, and manage larger PR queues more efficiently.

### [Enterprise managed permissions for GitHub Copilot agent operations](https://github.blog/changelog/2026-09-09-enterprise-managed-permissions-for-github-copilot-agent-operations)
*Sep 9, 2026*

If you administer GitHub Copilot Business or GitHub Copilot Enterprise, you can now centrally control which agent operations are blocked, require human approval, or can proceed without a prompt. Managed permissions cover shell commands, file reads and edits, and network domains. This gives you fine-grained guardrails for sensitive operations without disabling agent workflows.

### [npm extends recovery-code security holds to all accounts](https://github.blog/changelog/2026-09-09-npm-extends-recovery-code-security-holds-to-all-accounts)
*Sep 9, 2026*

This change applies to all npm accounts. During the hold, publishing and other security-sensitive writes, including creating access tokens, are paused. You can still sign in as well as browse and install packages.

### [CodeQL 2.27.0 adds support for Linux ARM64](https://github.blog/changelog/2026-09-09-codeql-2-27-0-adds-support-for-linux-arm64)
*Sep 9, 2026*

CodeQL 2.27.0 adds native Linux ARM64 support, a new Rust security query, and broader framework coverage for Java/Kotlin and C#. The release also improves analysis accuracy and makes it easier to use private registry configurations with GitHub code scanning.

### [Block pull requests with exposed secrets from merging](https://github.blog/changelog/2026-09-09-block-pull-requests-with-exposed-secrets-from-merging)
*Sep 9, 2026*

Repository rulesets allow you to add scalable protections across your repositories. Starting today, you can use them to block pull requests from merging when they introduce secret scanning alerts. Teams can enable this requirement for selected repositories so exposed secrets must be resolved before a pull request can merge.

### [GitHub Advanced Security expands trial availability](https://github.blog/changelog/2026-09-09-github-advanced-security-expands-trial-availability)
*Sep 9, 2026*

More GitHub Enterprise Cloud customers can now start a self-serve GitHub Advanced Security trial to evaluate GitHub Code Security and GitHub Secret Protection. Eligibility has expanded from enterprises with up to 100 licenses to enterprises with up to 300 licenses. To set up a GitHub Advanced Security trial, go to the Enterprise "Billing and licensing" page.

### [Attach images and videos to issues and PRs with GitHub CLI](https://www.youtube.com/watch?v=YHHjEet47_4)
*Sep 9, 2026*

This demo shows how the GitHub CLI's --attach flag can add screenshots and videos directly to issues, pull requests, and comments. It also walks through an automated Playwright workflow that captures failure evidence and posts before-and-after media to a PR.

### [Enterprise-managed sandbox in Copilot for JetBrains](https://github.blog/changelog/2026-09-08-enterprise-managed-sandbox-in-copilot-for-jetbrains)
*Sep 8, 2026*

This JetBrains update adds enterprise-managed sandbox policies, cross-file cursor jumps for next edit suggestions, and better project-wide chat context. It also improves policy diagnostics, model selection, and the connection between Copilot CLI sessions and JetBrains IDEs.

### [How to teach GitHub Copilot about your codebase | Tutorial for Beginners](https://www.youtube.com/watch?v=QGakvawJc2M)
*Sep 8, 2026*

Episode 8 of the beginner series explains how to teach the GitHub Copilot app your repository's conventions, scripts, and code style. It walks through custom instructions, reusable skills, custom agents, and MCP integrations such as browser testing. Developers new to the app will come away with practical ways to make Copilot follow local standards and automate repeatable project tasks.

### [GPT-6 Astra is generally available in GitHub Copilot](https://github.blog/changelog/2026-09-04-gpt-6-astra-is-generally-available-in-github-copilot)
*Sep 4, 2026*

GPT-6 Astra is now generally available in GitHub Copilot for long-horizon and agentic coding tasks. GitHub says the model plans and validates as it works, helping it complete complex tasks with fewer steps than prior OpenAI models.

---

## Older Updates

See [CHANGELOG.md](CHANGELOG.md) for the full historical timeline.

---

_All dates are complete and sorted newest first. For a full list of updates, see [CHANGELOG.md](CHANGELOG.md)._
