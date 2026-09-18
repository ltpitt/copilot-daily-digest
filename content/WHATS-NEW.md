# What's New with GitHub Copilot

> Latest updates from the last 30 days

**Last Updated**: September 18, 2026

This page highlights significant Copilot updates from the past 30 days. Content older than 30 days moves to [CHANGELOG.md](CHANGELOG.md).

---

## ⚠️ Action Required

*Deprecations and breaking changes from the last 30 days. See [Deprecations & Breaking Changes](DEPRECATIONS.md) for the full list.*

- **Sep 10, 2026** - 🚫 **Deprecation** - [MAI-Code-1-Flash deprecated](https://github.blog/changelog/2026-09-10-mai-code-1-flash-deprecated)
- **Sep 3, 2026** - 🚫 **Deprecation** - [Upcoming deprecation of selected GitHub Copilot models](https://github.blog/changelog/2026-09-03-upcoming-deprecation-of-selected-github-copilot-models)
- **Aug 31, 2026** - 🚫 **Deprecation** - [Selected GitHub Copilot models deprecated](https://github.blog/changelog/2026-08-31-selected-github-copilot-models-deprecated)

---

## This Week (Last 7 Days)

### [Agentic CLI customizations now in the usage metrics API](https://github.blog/changelog/2026-09-17-agentic-cli-customizations-now-in-the-usage-metrics-api)
*Sep 17, 2026*

GitHub Copilot expands existing CLI report coverage with agentic activity metrics for skills, custom agents, Model Context Protocol (MCP) servers, slash commands, and plugins. The fields appear in enterprise and organization per-user and aggregate 1-day reports, per-user 28-day reports, and the day_totals entries in aggregate 28-day reports.

### [Workflow execution protections in GitHub Actions generally available](https://github.blog/changelog/2026-09-17-workflow-execution-protections-in-github-actions-generally-available)
*Sep 17, 2026*

Workflow execution protections for GitHub Actions, previously in public preview, are now generally available for GitHub Enterprise, organizations, and repositories. Execution protections let you define an allowlist that controls who can trigger an Actions workflow and what events can start it. Actor rules cover the who, event rules cover the what, and actions evaluate both before a run.

### [Copilot impact dashboard now shows feature engagement](https://github.blog/changelog/2026-09-17-copilot-impact-dashboard-now-shows-feature-engagement)
*Sep 17, 2026*

The Copilot impact dashboard now shows how many active users regularly use key Copilot features. Enterprise administrators can quickly see which experiences are widely adopted and which may need more enablement.

### [Migrating the GitHub Copilot runtime to Rust, using Copilot](https://github.blog/ai-and-ml/generative-ai/migrating-the-github-copilot-runtime-to-rust-using-copilot/)
*Sep 17, 2026*

The GitHub Copilot CLI, GitHub Copilot app, and GitHub Copilot SDK are all backed by the Copilot agent runtime, an agentic harness that can be embedded into applications and services. Using the GitHub Copilot app and the Copilot CLI, we completely rewrote the runtime into more than 800,000 lines of production Rust.

### [Ubuntu 26 generally available and latest migration](https://github.blog/changelog/2026-09-17-ubuntu-26-generally-available-and-latest-migration)
*Sep 17, 2026*

The Ubuntu 26.04 runner image for GitHub Actions is now out of public preview and fully supported for production workflows on both x64 and arm64. As part of this release, the ubuntu-latest label will migrate to Ubuntu 26.04, giving you the latest supported Ubuntu release by default. To run your workflows on the new image, set runs-on: ubuntu-26.04 or runs-on: ubuntu-26.04-arm in your workflow file.

---

## Last 30 Days

### [Will tech companies hire developers who do not use AI?](https://www.youtube.com/shorts/Q7uO3vWP1h4)
*Sep 17, 2026*

Can refusing to use AI tools cost you a job offer? In this GitHub Podcast clip, the team discusses interview trends where employers increasingly expect practical AI fluency from candidates. It highlights how developers can stay competitive by showing they can evaluate and apply AI tools in day-to-day work.

### [Code scanning AI Scan no longer requires CodeQL default setup](https://github.blog/changelog/2026-09-16-code-scanning-ai-scan-no-longer-requires-codeql-default-setup)
*Sep 16, 2026*

You can now use AI Scan for pull requests to find security vulnerabilities, even when CodeQL default setup isn't enabled on a repository. Previously, AI Scan for pull requests only ran on repositories where CodeQL default setup was configured.

### [Copilot budget increase requests are generally available](https://github.blog/changelog/2026-09-16-copilot-budget-increase-requests-are-generally-available)
*Sep 16, 2026*

Previously, when a member used all the Copilot AI credits available to them, they were blocked from Copilot features that consume credits. This release adds a flow for them to request more budget the moment they hit the limit. You can approve, adjust, or deny that request without leaving your settings.

### [Automate SSO authorization for classic PATs and SSH keys](https://github.blog/changelog/2026-09-16-automate-sso-authorization-for-classic-pats-and-ssh-keys)
*Sep 16, 2026*

Enterprise admins can now automate SSO authorization for existing classic personal access tokens (PATs) and SSH keys for organizations in GitHub Enterprise Cloud, replacing manual per-organization authorization by your developers. These GitHub Apps can then call the new API to bulk-authorize a classic PAT or an SSH key for up to 50 organizations in a single request.

### [SCIM user responses now include a profileUrl attribute](https://github.blog/changelog/2026-09-16-scim-user-responses-now-include-a-profileurl-attribute)
*Sep 16, 2026*

SCIM user responses from GitHub now include the standard profileUrl attribute defined by RFC 7643, containing the absolute URL of the GitHub account linked to the external identity. Previously, matching a SCIM record to the corresponding GitHub account required extra lookups or inference.

### [How Project HydraFusion reduces the cost of frontier AI](https://www.youtube.com/watch?v=1asMXES_5jY)
*Sep 16, 2026*

Everyone's racing to build a better model. HydraFusion optimizes the path instead, orchestrating existing models per request rather than picking just one, and reduces the cost of frontier AI.

### [AI hot takes: should developers still read code? | S02E03 | The GitHub Podcast](https://www.youtube.com/watch?v=myjyHt4ycDg)
*Sep 16, 2026*

In this episode of the GitHub Podcast, Cassidy and GPS tackle some of the biggest AI developer hot takes floating around social media.

### [GitHub Copilot suggests custom properties definitions](https://github.blog/changelog/2026-09-15-github-copilot-suggests-custom-properties-definitions)
*Sep 15, 2026*

GitHub Copilot can now suggest allowed values when you create a custom property for repositories in your organization. This feature is in public preview for GitHub Copilot Business and Copilot Enterprise plans. Custom properties let enterprise and organization admins attach governance metadata to repositories, which you can then use to target repositories with rulesets.

### [How to continue GitHub Copilot app sessions in VS Code](https://www.youtube.com/watch?v=dNCGfpDho0U)
*Sep 15, 2026*

Want to direct an AI agent in the app but finish coding in your favorite editor? This beginner-friendly walkthrough shows how to move an active GitHub Copilot app session into VS Code without losing context. Use it to keep your workflow fluid between planning in chat and implementation in your IDE.

### [3 ways to streamline AI code reviews across your team](https://www.youtube.com/watch?v=NiMpZ4gW2dQ)
*Sep 15, 2026*

AI coding tools can increase output, but review queues often become the bottleneck. This video explains three practical ways teams can reduce review fatigue, improve throughput, and keep pull request quality high as AI-assisted changes scale up.

---

## Older Updates

See [CHANGELOG.md](CHANGELOG.md) for the full historical timeline.

---

_All dates are complete and sorted newest first. For a full list of updates, see [CHANGELOG.md](CHANGELOG.md)._
