# What's New with GitHub Copilot

> Latest updates from the last 30 days

**Last Updated**: August 28, 2026

This page highlights significant Copilot updates from the past 30 days. Content older than 30 days moves to [CHANGELOG.md](CHANGELOG.md).

---

## ⚠️ Action Required

*Deprecations and breaking changes from the last 30 days. See [Deprecations & Breaking Changes](DEPRECATIONS.md) for the full list.*

- **Aug 18, 2026** - 🔒 **Security** - [Credential revocation and deauthorization by token type](https://github.blog/changelog/2026-08-18-credential-revocation-and-deauthorization-by-token-type)
- **Aug 11, 2026** - 🚫 **Deprecation** - [Upcoming deprecation of MAI-Code-1-Flash](https://github.blog/changelog/2026-08-11-upcoming-deprecation-of-mai-code-1-flash)
- **Aug 4, 2026** - 🗑️ **Retirement/Removal** - [Retiring the Copilot Billing Preview app](https://github.blog/changelog/2026-08-04-retiring-the-copilot-billing-preview-app)
- **Aug 4, 2026** - 🚫 **Deprecation** - [Upcoming deprecation of GitHub Spark on github.com](https://github.blog/changelog/2026-08-04-upcoming-deprecation-of-github-spark-on-github-com)
- **Jul 31, 2026** - 🚫 **Deprecation** - [Gemini 2.5 Pro and Gemini 3 Flash deprecated](https://github.blog/changelog/2026-07-31-gemini-2-5-pro-and-gemini-3-flash-deprecated)
- **Jul 31, 2026** - 🚫 **Deprecation** - [Upcoming August 2026 model deprecations in GitHub Copilot](https://github.blog/changelog/2026-07-31-upcoming-august-2026-model-deprecations-in-github-copilot)
- **Jul 30, 2026** - 🗑️ **Retirement/Removal** - [GitHub Models is now retired](https://github.blog/changelog/2026-07-30-github-models-is-now-retired)

---

## This Week (Last 7 Days)

### [Copilot code review: Resolution reasons and expanded capabilities](https://github.blog/changelog/2026-08-27-copilot-code-review-resolution-reasons-and-expanded-capabilities)
*Aug 27, 2026*

Copilot code review now supports automatic reviews on bot-authored pull requests, including those created by the Copilot cloud agent. It also adds support for very large pull requests, expanding where teams can rely on automated review feedback. You can now record a resolution reason when dismissing a Copilot code review comment for better review traceability.

### [Better label management on issues is generally available](https://github.blog/changelog/2026-08-27-label-archiving-is-generally-available)
*Aug 27, 2026*

We're making it easier to keep labels organized and find the right one, especially in repositories with long and growing label lists. You can now find the right label faster with suggestions based on what a repository has been using recently. You can also see Recent labels based on your own usage, making it easier to label issues without searching through the full list.

### [Actions retention will cover checks, workflow runs, and statuses](https://github.blog/changelog/2026-08-27-actions-retention-will-cover-checks-workflow-runs-and-statuses)
*Aug 27, 2026*

Starting October 1, 2026, checks, workflow runs, and statuses will be governed by the same Actions retention setting that already controls how long artifacts and logs are kept, with a default of 90 days. Until now, checks, workflow runs, and statuses were retained for 400+ days regardless of your retention configuration.

### [RDT: Trying the new GitHub Copilot Teams and Slack Integration](https://www.youtube.com/watch?v=Q3Q4ywUrY2A)
*Aug 27, 2026*

This livestream walks through the new GitHub Copilot integration for Microsoft Teams and Slack. It shows how teams can bring Copilot-assisted collaboration into day-to-day communication channels. Watch for practical examples of keeping code discussions and agentic workflows connected across tools.

### [GitHub Apps can now access enterprise billing data](https://github.blog/changelog/2026-08-26-github-apps-can-now-access-enterprise-billing-data)
*Aug 26, 2026*

Enterprise owners can now grant a GitHub App access to enterprise billing data. When you create or configure a GitHub App, you can select the enterprise billing permission and choose one of two levels: read or read and write. Previously, the only way to read usage or manage budgets and cost centers through the API was a personal access token belonging to an enterprise owner or billing manager.

---

## Last 30 Days

### [Enterprise-managed settings now support autoUpdate for plugin marketplaces](https://github.blog/changelog/2026-08-26-enterprise-managed-settings-now-support-autoupdate-for-plugin-marketplaces)
*Aug 26, 2026*

You can now opt individual plugin marketplaces into automatic updates by setting autoUpdate: true on an extraKnownMarketplaces entry in enterprise managed settings. Supported clients automatically check the marketplace and update installed plugins sourced from it, reducing manual maintenance for organization customizations.

### [GitHub Copilot app for Beginners: Automate Dependabot pull request triage](https://github.blog/ai-and-ml/github-copilot/github-copilot-app-for-beginners-automate-dependabot-pull-request-triage/)
*Aug 26, 2026*

This beginner-focused guide shows how to use the GitHub Copilot app to triage Dependabot pull requests faster. It covers practical ways to evaluate update urgency, reduce review noise, and make safer merge decisions. Teams managing high dependency volume can use this workflow to stay secure without slowing delivery.

### [Global model policy generally available](https://github.blog/changelog/2026-08-26-global-model-policy-generally-available)
*Aug 26, 2026*

In July, we announced a default model policy for generally available GitHub Copilot models on Copilot Business and Copilot Enterprise plans. Starting today, we're gradually rolling out enforcement of the policy through September 1, so it will take effect at different times for different enterprises. Previously unconfigured and new generally available models will inherit the global policy state.

### [GitHub Copilot app Customize tab is generally available](https://github.blog/changelog/2026-08-25-github-copilot-app-customize-tab-is-generally-available)
*Aug 25, 2026*

GitHub Copilot is more useful when it works with the tools, knowledge, and workflows your team already relies on. The new Customize tab in the GitHub Copilot app brings MCP servers, plugins, skills, and canvases together in one place. Explore featured customizations, browse by type, and find new ways to tailor Copilot to how you and your team work.

### [Block users directly from security advisories](https://github.blog/changelog/2026-08-25-block-users-directly-from-security-advisories)
*Aug 25, 2026*

You can now block a user directly from a security advisory page in public repositories owned by either an organization or a personal account. This brings the streamlined moderation experience available for issues and pull requests to security advisories. Security advisories contain user-created content and, like other collaborative surfaces, can attract spam or abuse.

### [Rule insights dashboard generally available](https://github.blog/changelog/2026-08-25-rule-insights-dashboard-generally-available)
*Aug 25, 2026*

The rule insights dashboard is now generally available at both the repository and organization levels. You get a visual, high-level view of how GitHub evaluates and enforces your GitHub repository rulesets, so you can spot trends and report on governance without stitching data together by hand. The organization-level dashboard we shipped in public preview is now generally available.

### [GitHub Copilot app for beginners: using the diff, terminal, and browser](https://www.youtube.com/watch?v=IyWlcES85Zw)
*Aug 25, 2026*

This beginner video demonstrates how to review AI-generated changes using the diff, terminal, and browser views in the GitHub Copilot app. It explains how to validate code updates without constantly switching tools. New users will learn a repeatable workflow for faster and safer change verification.

### [How GitHub's tiny wins team fixes developer paper cuts](https://www.youtube.com/shorts/c44_HuUuTtY)
*Aug 24, 2026*

This short highlights GitHub’s Tiny Wins team and how it removes everyday friction in developer workflows. It shares examples of incremental product improvements that collectively save time for maintainers and contributors. The clip offers a useful lens on how small platform changes can create outsized productivity gains.

### [local.ai: hardware benchmarking for local AI models](https://www.youtube.com/shorts/Qqtv9lANW7k)
*Aug 23, 2026*

This video introduces local.ai, a benchmarking approach for evaluating local AI models beyond raw token speed. It compares task quality, total runtime, hardware costs, and energy usage to guide model selection. Developers experimenting with on-device AI can use these tradeoffs to choose a model that matches real-world constraints.

### [GitHub OAuth apps now support refresh tokens and multiple callback URLs](https://www.youtube.com/shorts/k7VtVpvwIvM)
*Aug 22, 2026*

This changelog video explains new OAuth capabilities, including short-lived access tokens and long-lived refresh tokens. It also covers support for multiple callback URLs, which helps teams manage development, staging, and production app environments. The update improves both security posture and deployment flexibility for GitHub OAuth apps.

---

## Older Updates

See [CHANGELOG.md](CHANGELOG.md) for the full historical timeline.

---

_All dates are complete and sorted newest first. For a full list of updates, see [CHANGELOG.md](CHANGELOG.md)._
