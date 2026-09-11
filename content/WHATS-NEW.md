# What's New with GitHub Copilot

> Latest updates from the last 30 days

**Last Updated**: September 11, 2026

This page highlights significant Copilot updates from the past 30 days. Content older than 30 days moves to [CHANGELOG.md](CHANGELOG.md).

---

## ⚠️ Action Required

*Deprecations and breaking changes from the last 30 days. See [Deprecations & Breaking Changes](DEPRECATIONS.md) for the full list.*

- **Sep 10, 2026** - 🚫 **Deprecation** - [MAI-Code-1-Flash deprecated](https://github.blog/changelog/2026-09-10-mai-code-1-flash-deprecated)
- **Sep 3, 2026** - 🚫 **Deprecation** - [Upcoming deprecation of selected GitHub Copilot models](https://github.blog/changelog/2026-09-03-upcoming-deprecation-of-selected-github-copilot-models)
- **Aug 31, 2026** - 🚫 **Deprecation** - [Selected Github Copilot Models Deprecated](https://github.blog/changelog/2026-08-31-selected-github-copilot-models-deprecated)

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

We have deprecated MAI-Code-1-Flash across all GitHub Copilot experiences (including Copilot Chat, inline edits, ask and agent modes, and code completions) today, September 10, 2026. Model
Deprecation date
Suggested alternative
MAI-Code-1-Flash
2026-09-10
MAI-Code-1.1-Flash
Please update your workflows and integrations to use a supported model.

### [Xcode 27 runner image now runs on macOS 27](https://github.blog/changelog/2026-09-10-xcode-27-runner-image-now-runs-on-macos-27)
*Sep 10, 2026*

You can now validate your Apple apps against macOS 27 using the Xcode 27 runner image for GitHub-hosted macOS runners, available in public preview. The image previously ran on macOS 26. How you target the image stays the same.

### [GitHub Copilot app for Beginners: Using the diff, terminal, and browser](https://github.blog/ai-and-ml/github-copilot/github-copilot-app-for-beginners-using-the-diff-terminal-and-browser/)
*Sep 10, 2026*

When an agent makes a change to your code, you want to review it, run it, and see what changed. Great news: now you can do all three without having to leave the GitHub Copilot app. Before, doing those three jobs would mean having to bounce between your editor, terminal window, and web browser.

---

## Last 30 Days

### [Refreshed repository pull requests page in public preview](https://github.blog/changelog/2026-09-10-refreshed-repository-pull-requests-page-in-public-preview)
*Sep 10, 2026*

A refreshed repository-level pull request listing page is now in public preview for all GitHub users. It brings powerful filtering, compact presentation mode, and more.

### [Attach images to PRs and Issues with GitHub CLI](https://www.youtube.com/watch?v=2-lA7Escqns)
*Sep 10, 2026*

In this stream we'll explore the new attach flag in the GitHub CLI. Attach images to PR's and Issues with GitHub CLI

### [Enterprise managed permissions for GitHub Copilot agent operations](https://github.blog/changelog/2026-09-09-enterprise-managed-permissions-for-github-copilot-agent-operations)
*Sep 9, 2026*

If you administer GitHub Copilot Business or GitHub Copilot Enterprise, you can now centrally control which agent operations are blocked, require human approval, or can proceed without a prompt. Managed permissions cover shell commands, file reads and edits, and network domains. This gives you fine-grained guardrails for sensitive operations without disabling agent workflows.

### [npm extends recovery-code security holds to all accounts](https://github.blog/changelog/2026-09-09-npm-extends-recovery-code-security-holds-to-all-accounts)
*Sep 9, 2026*

This change applies to all npm accounts. During the hold, publishing and other security-sensitive writes, including creating access tokens, are paused. You can still sign in as well as browse and install packages.

### [CodeQL 2.27.0 adds support for Linux ARM64](https://github.blog/changelog/2026-09-09-codeql-2-27-0-adds-support-for-linux-arm64)
*Sep 9, 2026*

CodeQL 2.27.0 is now available on Linux ARM64, adds a new Rust security query, expanded framework coverage for Java/Kotlin and C#, and analysis accuracy improvements across multiple languages. CodeQL is the static analysis engine behind GitHub code scanning, which helps you find and remediate security issues in your code. CodeQL CLI
You can now run CodeQL natively on Linux arm64.

### [Block pull requests with exposed secrets from merging](https://github.blog/changelog/2026-09-09-block-pull-requests-with-exposed-secrets-from-merging)
*Sep 9, 2026*

Repository rulesets allow you to easily add scalable protections across your repositories. Starting today, you can use repository rulesets to block pull requests from merging when the pull request introduces secret scanning alerts. You can enable the new rule require secret scanning alerts are resolved on pull requests for selected repositories.

### [GitHub Advanced Security expands trial availability](https://github.blog/changelog/2026-09-09-github-advanced-security-expands-trial-availability)
*Sep 9, 2026*

More GitHub Enterprise Cloud customers can now start a self-serve GitHub Advanced Security trial to evaluate GitHub Code Security and GitHub Secret Protection. Eligibility has expanded from enterprises with up to 100 licenses to enterprises with up to 300 licenses. To set up a GitHub Advanced Security trial, go to the Enterprise "Billing and licensing" page.

### [Attach images and videos to issues and PRs with GitHub CLI](https://www.youtube.com/watch?v=YHHjEet47_4)
*Sep 9, 2026*

Need to attach proof of work to automated pull requests and bug reports? The GitHub CLI now includes the --attach flag, making it easy to upload screenshots and videos directly to issues, PRs, and...

### [Enterprise-managed sandbox in Copilot for JetBrains](https://github.blog/changelog/2026-09-08-enterprise-managed-sandbox-in-copilot-for-jetbrains)
*Sep 8, 2026*

This update brings support for enterprise-managed sandbox policies, cross-file cursor jumps for next edit suggestions, global project context in chat, enterprise policy diagnostics, and a new connection between terminal Copilot CLI sessions and JetBrains IDEs. It also improves model selection, the chat experience, and reliability across MCP servers and agent sessions.

### [How to teach GitHub Copilot about your codebase | Tutorial for Beginners](https://www.youtube.com/watch?v=QGakvawJc2M)
*Sep 8, 2026*

Every project has its own conventions, scripts, and code style. In episode 8 of our beginner series, discover how to teach the GitHub Copilot app your specific project standards.

---

## Older Updates

See [CHANGELOG.md](CHANGELOG.md) for the full historical timeline.

---

_All dates are complete and sorted newest first. For a full list of updates, see [CHANGELOG.md](CHANGELOG.md)._
