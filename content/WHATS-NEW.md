# What's New with GitHub Copilot

> Latest updates from the last 30 days

**Last Updated**: September 04, 2026

This page highlights significant Copilot updates from the past 30 days. Content older than 30 days moves to [CHANGELOG.md](CHANGELOG.md).

---

## ⚠️ Action Required

*Deprecations and breaking changes from the last 30 days. See [Deprecations & Breaking Changes](DEPRECATIONS.md) for the full list.*

- **Sep 3, 2026** - 🚫 **Deprecation** - [Upcoming deprecation of selected GitHub Copilot models](https://github.blog/changelog/2026-09-03-upcoming-deprecation-of-selected-github-copilot-models)
- **Aug 31, 2026** - 🚫 **Deprecation** - [Selected GitHub Copilot models deprecated](https://github.blog/changelog/2026-08-31-selected-github-copilot-models-deprecated)

---

## This Week (Last 7 Days)

### [Reopening Copilot Business and Enterprise signups](https://github.blog/changelog/2026-09-03-reopening-copilot-business-and-enterprise-signups)
*Sep 3, 2026*

We're gradually reopening sign-ups for Copilot Business and Copilot Enterprise customers paying by credit card or PayPal over the next couple of weeks. If you've been waiting to get started with Copilot, select the plan that fits your needs. If your preferred option isn't available yet, check back soon.

### [Gemini 3.8 Flash is now available in GitHub Copilot](https://github.blog/changelog/2026-09-03-gemini-3-8-flash-is-now-available-in-github-copilot)
*Sep 3, 2026*

Gemini 3.8 Flash, Google's latest Flash model, is now available in GitHub Copilot. In our early testing, Gemini 3.8 Flash performed strongly on complex terminal-based coding tasks and demonstrated rigorous validation and persistent recovery from actionable failures. This model is billed at introductory provider pricing under usage-based billing through December 31, 2026.

### [GitHub Actions: Early September 2026 updates](https://github.blog/changelog/2026-09-03-github-actions-early-september-2026-updates)
*Sep 3, 2026*

GitHub Actions now includes three updates that give you clearer visibility and finer-grained control over your workflows. A new REST API returns when registration and runtime support end for a given runner version, so you can plan runner upgrades before a version is deprecated. Call GET /actions/runners/deprecations/{version} at the repository, organization, or enterprise level.

### [Upcoming deprecation of selected GitHub Copilot models](https://github.blog/changelog/2026-09-03-upcoming-deprecation-of-selected-github-copilot-models)
*Sep 3, 2026*

Copilot Enterprise and Copilot Business administrators may need to enable access to the alternative models through their model policies in Copilot settings. As an administrator, you can verify availability in your organization or enterprise Copilot model settings and confirm that the policy is enabled for the specific model.

### [Multiple trusted publishing configurations for npm](https://github.blog/changelog/2026-09-03-multiple-trusted-publishing-configurations-for-npm)
*Sep 3, 2026*

We're continuing to make trusted publishing smoother for npm publishers, guided by maintainers feedback. Maintainers are no longer limited to one configuration per package to separate workflows with stable, prerelease, or staging versions. Before this, maintainers had to depend on workflow workarounds or keep a long-lived token around for the paths OIDC couldn't cover.

---

## Last 30 Days

### [GitHub CLI Linux package signing key expires September 5](https://github.blog/changelog/2026-09-03-github-cli-linux-package-signing-key-expires-september-5)
*Sep 3, 2026*

The current PGP key for the GitHub CLI Linux package repositories expires on Saturday, September 5, 2026. Beginning with the first release after that date, APT and RPM repository metadata and newly published RPM packages will be signed with just the replacement key. In April, we published a keyring containing both the current and replacement keys.

### [GitHub Copilot app for Beginners: Run several agents at once](https://github.blog/ai-and-ml/github-copilot/github-copilot-app-for-beginners-run-several-agents-at-once/)
*Sep 3, 2026*

Running multiple AI agents on the same project seems like pure chaos, with too many cooks in your development kitchen. But with the GitHub Copilot app, these agents work separately and don't interfere with each other, allowing you to get more done in less time. Think of parallel agent sessions like a trip to the laundromat.

### [CodeQL 2.26.4 improves GitHub actions security detections](https://github.blog/changelog/2026-09-03-codeql-2-26-4-improves-github-actions-security-detections)
*Sep 3, 2026*

CodeQL 2.26.4 adds support for Go 1.27, improves Rust data flow alert locations, and sharpens detections across C#, Java/Kotlin, and GitHub Actions. Teams using GitHub code scanning can expect more accurate alerts and broader coverage for modern language and workflow patterns.

### [How an AI harness guides model execution](https://www.youtube.com/shorts/_yk_yg_DTeQ)
*Sep 3, 2026*

Learn how harness engineering gives AI agents the runtime, tools, and guardrails they need to work safely in a codebase. This short explains why that scaffolding matters for reliable agentic workflows in GitHub Copilot.

### [How Cboard uses open source to give people a voice | GitHub Accessibility Spotlight](https://www.youtube.com/watch?v=IknnBdcDDiQ)
*Sep 3, 2026*

In this GitHub Accessibility Spotlight, learn how Cboard grew from a single repository into a global Augmentative and Alternative Communication (AAC) platform.

### [Content exclusions generally available in Copilot app and CLI](https://github.blog/changelog/2026-09-02-content-exclusions-generally-available-in-copilot-app-and-cli)
*Sep 2, 2026*

The GitHub Copilot app and Copilot CLI now respect content exclusion policies configured by enterprise, organization, and repository administrators. Copilot won't use excluded files as context, helping you protect sensitive code across agentic workflows. This is available for Copilot Business and Copilot Enterprise customers.

### [Enterprise-managed settings support any default model](https://github.blog/changelog/2026-09-02-enterprise-managed-settings-support-any-default-model)
*Sep 2, 2026*

You can now set your preferred GitHub Copilot model as the default for new conversations through enterprise-managed settings. This lets you choose the default model that best fits your workflows. You can also customize the default by enterprise team, assigning a different default model based on team membership.

### [How we make AI coding more cost efficient without sacrificing task quality](https://github.blog/ai-and-ml/github-copilot/how-we-make-ai-coding-more-cost-efficient-without-sacrificing-task-quality/)
*Sep 2, 2026*

Output quality is important when working with AI coding agents, but true efficiency comes from getting work done quickly, efficiently, and with the right context. That's why token count of individual interactions alone isn't a meaningful measure of efficiency. The goal shouldn't be to use fewer tokens, but to tap into the right amount of context to move a task forward.

### [Demystifying AI terms: loop engineering, squads, and harness | S02E02 | The GitHub Podcast](https://www.youtube.com/watch?v=7oqYIRbB6Rc)
*Sep 2, 2026*

AI terminology is evolving fast, with new terms like loop engineering, harness engineering, and squads popping up constantly.

### [What's it like to be a maintainer of OpenClaw, the fastest growing project in GitHub history? 🦞](https://www.youtube.com/shorts/k2fgD6JbB54)
*Sep 2, 2026*

Peter Steinberger shares what it is like to maintain OpenClaw as it grows at breakneck speed. The short offers a candid look at the workload, community energy, and surprises that come with leading a breakout open source project.

---

## Older Updates

See [CHANGELOG.md](CHANGELOG.md) for the full historical timeline.

---

_All dates are complete and sorted newest first. For a full list of updates, see [CHANGELOG.md](CHANGELOG.md)._
