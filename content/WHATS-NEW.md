# What's New with GitHub Copilot

> Latest updates from the last 30 days

**Last Updated**: October 02, 2026

This page highlights significant Copilot updates from the past 30 days. Content older than 30 days moves to [CHANGELOG.md](CHANGELOG.md).

---

## ⚠️ Action Required

*Deprecations and breaking changes from the last 30 days. See [Deprecations & Breaking Changes](DEPRECATIONS.md) for the full list.*

- **Oct 1, 2026** - 🗑️ **Retirement/Removal** - [GitHub Actions: macOS 14 runner image retirement](https://github.blog/changelog/2026-10-01-github-actions-macos-14-runner-image-retirement)
- **Sep 10, 2026** - 🚫 **Deprecation** - [Mai Code 1 Flash Deprecated](https://github.blog/changelog/2026-09-10-mai-code-1-flash-deprecated)
- **Sep 3, 2026** - 🚫 **Deprecation** - [Upcoming Deprecation Of Selected Github Copilot Models](https://github.blog/changelog/2026-09-03-upcoming-deprecation-of-selected-github-copilot-models)

---

## This Week (Last 7 Days)

### [GitHub Actions: macOS 14 runner image retirement](https://github.blog/changelog/2026-10-01-github-actions-macos-14-runner-image-retirement)
*Oct 1, 2026*

The macOS 14 runner image will be retired on November 2, 2026. Update your workflow files to use one of the following macOS arm64 labels:
macos-latest (macos-26)
macos-15
macos-latest-xlarge (macos-26-xlarge)
macos-15-xlarge
For up-to-date information about available tools and software, see the runner images repository. If you run into problems or need help, contact GitHub Support.

### [GitHub Copilot can now interact with desktop apps with computer use](https://github.blog/changelog/2026-10-01-github-copilot-can-now-interact-with-desktop-apps)
*Oct 1, 2026*

Computer use is now available in public preview in GitHub Copilot CLI and the GitHub Copilot app on macOS and Windows. Copilot can interact with desktop applications on your behalf (e.g., reading accessible app content and visual context, clicking controls, entering and editing text, pressing keys, scrolling, dragging, and navigating workflows across applications).

### [Dynamic workflows in Copilot CLI and the Copilot app](https://github.blog/changelog/2026-10-01-dynamic-workflows-in-copilot-cli-and-the-copilot-app)
*Oct 1, 2026*

Dynamic workflows are now available in Copilot CLI, the GitHub Copilot app, and the GitHub Copilot SDK. These let you define an orchestration in code to get the reliability and observability that complex, multi-agent work demands. A dynamic workflow is a program that defines how a task is carried out.

### [Actions retention now covers checks, runs, and statuses](https://github.blog/changelog/2026-10-01-actions-retention-now-covers-checks-runs-and-statuses)
*Oct 1, 2026*

As previously announced, checks, workflow runs, and statuses are now governed by the same GitHub Actions retention setting that controls how long artifacts and logs are kept. These records are automatically cleaned up when they exceed the retention period configured for your enterprise, organization, or repository.

### [GitHub Copilot in VS Code, September 2026 releases](https://github.blog/changelog/2026-10-01-github-copilot-in-vs-code-september-2026-releases)
*Oct 1, 2026*

This changelog covers VS Code v1.136 through v1.140, shipped throughout September 2026. September's releases streamline agent-driven development from implementation through pull request merge. Automations handle repeatable tasks, agent merge helps land changes, and improved session management keeps work organized.

---

## Last 30 Days

### [Code coverage uploads no longer fail CI for new branches](https://github.blog/changelog/2026-10-01-code-coverage-uploads-no-longer-fail-ci-for-new-branches)
*Oct 1, 2026*

Code coverage uploads from the GitHub Code Quality upload-code-coverage action no longer fail CI when you push a branch that doesn't yet have an open pull request. Previously, the coverage API required a pull request number for any push to a non-default branch.

### [Accessibility statements highlighted on repository overview](https://github.blog/changelog/2026-10-01-accessibility-statements-highlighted-on-repository-overview)
*Oct 1, 2026*

You can now find an ACCESSIBILITY.md file in your repository's root, the .github/ directory, or the docs/ directory highlighted on the repository overview. You can also add or propose an accessibility statement from a public repository's Community Standards page. This improvement is available on all GitHub plans on github.com and will be available in GitHub Enterprise Server 3.24.

### [Rate limits for private vulnerability reports](https://github.blog/changelog/2026-10-01-rate-limits-for-private-vulnerability-reports)
*Oct 1, 2026*

Open source maintainers are receiving more low-quality and automated vulnerability reports, which can bury the reports that matter. Rate limits cap how many new reports a single account can submit in a day, both to your repository and across GitHub. This helps protect you from bulk and automated submissions, while legitimate researchers can still reach you.

### [Structured forms for private vulnerability reports](https://github.blog/changelog/2026-10-01-structured-forms-for-private-vulnerability-reports)
*Oct 1, 2026*

Private vulnerability reports can now use a structured form that asks reporters for the details you need to assess a vulnerability, including a reproducible proof of concept. A single free-text box made it easy to submit low-quality or AI-generated reports and hard for you to find the signal in them.

### [HydraFusion in VS Code and the GitHub Copilot app](https://github.blog/changelog/2026-09-30-hydrafusion-in-vs-code-and-the-github-copilot-app)
*Sep 30, 2026*

The HydraFusion research preview is now available in Visual Studio Code and the GitHub Copilot app, expanding beyond Copilot CLI. HydraFusion appears in the model picker, but rather than being a single model, it orchestrates multiple models. HydraFusion treats workflow selection as an optimization problem.

### [How GitHub's Tiny Wins team tackles the AI slop problem | S02E04 | The GitHub Podcast](https://www.youtube.com/watch?v=PWjo4VWhmqY)
*Sep 30, 2026*

Open source maintainers are facing an influx of low-quality contributions across their repositories. In this episode of The GitHub Podcast, Cassidy and GPS sit down with Camilla Moraes, product...

### [GPT-6.1 Sol in GitHub Copilot](https://github.blog/changelog/2026-09-29-gpt-6-1-sol-in-github-copilot)
*Sep 29, 2026*

GPT-6.1 Sol, the latest model from OpenAI, is now generally available and rolling out in GitHub Copilot. You can use it for agentic coding and terminal workflows with strong multistep coding performance and efficient token use. In early testing, it reliably completed tasks while using noticeably fewer tokens and steps than earlier models in the GPT-6 and GPT-5.6 families.

### [Claude Sonnet 5.5 in GitHub Copilot](https://github.blog/changelog/2026-09-28-claude-sonnet-5-5-in-github-copilot)
*Sep 28, 2026*

Claude Sonnet 5.5, Anthropic's newest Sonnet model, is now generally available in GitHub Copilot. It is designed for well-scoped everyday work like building features and fixing bugs. In our early testing, Sonnet 5.5 stood out for its efficiency, matching Claude Sonnet 5 on coding tasks while using significantly fewer steps, tokens, and tool calls.

### [How GitHub Copilot app fixes CI failures automatically](https://www.youtube.com/shorts/SAC1vJk6EGw)
*Sep 28, 2026*

Tired of your code passing locally but failing in continuous integration? The GitHub Copilot app stays involved after you open a pull request, fixing CI failures and addressing reviewer comments...

### [How to use GitHub Copilot with WSL on Windows](https://www.youtube.com/watch?v=4VnQGyKtMk0)
*Sep 27, 2026*

Build software on Windows using the Linux environments and tools you already rely on. In this video, see how to connect the GitHub Copilot app to Windows Subsystem for Linux (WSL) and run coding...

---

## Older Updates

See [CHANGELOG.md](CHANGELOG.md) for the full historical timeline.

---

_All dates are complete and sorted newest first. For a full list of updates, see [CHANGELOG.md](CHANGELOG.md)._
