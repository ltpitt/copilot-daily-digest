# What's New with GitHub Copilot

> Latest updates from the last 30 days

**Last Updated**: April 23, 2026

This page highlights significant Copilot updates from the past 30 days. Content older than 30 days moves to [CHANGELOG.md](CHANGELOG.md).

---

## This Week (Last 7 Days)

### Recent Updates

#### 1. [Copilot cloud agent fields added to usage metrics](https://github.blog/changelog/2026-04-23-copilot-cloud-agent-fields-added-to-usage-metrics)
*Apr 23, 2026*

Following the Copilot coding agent to Copilot cloud agent rename, the Copilot usage metrics API now includes a new used_copilot_cloud_agent field in user-level reports. This boolean field mirrors the existing used_copilot_coding_agent flag under the updated product name.

#### 2. [Better debugging with GitHub Copilot on the web](https://github.blog/changelog/2026-04-23-better-debugging-with-github-copilot-on-the-web)
*Apr 23, 2026*

GitHub Copilot Chat in github.com helps you get to the root cause of an error faster when you paste a stack trace. Copilot recognizes stack traces more reliably and will guide you through a structured root-cause analysis using the stack trace plus your repository's code context, helping you move from "where it crashed" to "why it happened".

#### 3. [Dependabot-based dependency graphs for Python](https://github.blog/changelog/2026-04-23-dependabot-graphs-for-python)
*Apr 23, 2026*

Python projects will now see more complete and accurate transitive dependency trees in their dependency graphs and Software Bills of Materials (SBOMs). This feature is based on a new type of Dependabot job that builds a dependency snapshot and uploads it to the Dependency Submission API.

#### 4. [Fixing merge conflicts and PRs with Copilot cloud agent | GitHub Checkout](https://www.youtube.com/watch?v=ws_3hiXLKjQ)
*Apr 23, 2026*

Merge conflicts, failing tests, messy PRs. What if you could just ask Copilot to fix all of it? 
Tim Rogers is back to show with Copilot Cloud Agent: private sessions before you open a PR, model choice, and just say "@Copilot fix the merge...

#### 5. [Pausing new self-serve signups for GitHub Copilot Business](https://github.blog/changelog/2026-04-22-pausing-new-self-serve-signups-for-github-copilot-business)
*Apr 22, 2026*

As part of our ongoing efforts to ensure a reliable and sustainable Copilot experience for all users, we are pausing new self-serve signups for GitHub Copilot Business for organizations on GitHub Free and GitHub Team plans. Existing Copilot Business customers are not affected and can continue adding seats and using the service as they normally would.

---

## Last 30 Days

### Significant Updates

1. **[Copilot cloud agent fields added to usage metrics](https://github.blog/changelog/2026-04-23-copilot-cloud-agent-fields-added-to-usage-metrics)**
	*Apr 23, 2026*

	Following the Copilot coding agent to Copilot cloud agent rename, the Copilot usage metrics API now includes a new used_copilot_cloud_agent field in user-level reports. This boolean field mirrors the existing used_copilot_coding_agent flag under the updated product name.

2. **[Better debugging with GitHub Copilot on the web](https://github.blog/changelog/2026-04-23-better-debugging-with-github-copilot-on-the-web)**
	*Apr 23, 2026*

	GitHub Copilot Chat in github.com helps you get to the root cause of an error faster when you paste a stack trace. Copilot recognizes stack traces more reliably and will guide you through a structured root-cause analysis using the stack trace plus your repository's code context, helping you move from "where it crashed" to "why it happened".

3. **[Dependabot-based dependency graphs for Python](https://github.blog/changelog/2026-04-23-dependabot-graphs-for-python)**
	*Apr 23, 2026*

	Python projects will now see more complete and accurate transitive dependency trees in their dependency graphs and Software Bills of Materials (SBOMs). This feature is based on a new type of Dependabot job that builds a dependency snapshot and uploads it to the Dependency Submission API.

4. **[Fixing merge conflicts and PRs with Copilot cloud agent | GitHub Checkout](https://www.youtube.com/watch?v=ws_3hiXLKjQ)**
	*Apr 23, 2026*

	Merge conflicts, failing tests, messy PRs. What if you could just ask Copilot to fix all of it? 
Tim Rogers is back to show with Copilot Cloud Agent: private sessions before you open a PR, model...

5. **[Pausing new self-serve signups for GitHub Copilot Business](https://github.blog/changelog/2026-04-22-pausing-new-self-serve-signups-for-github-copilot-business)**
	*Apr 22, 2026*

	As part of our ongoing efforts to ensure a reliable and sustainable Copilot experience for all users, we are pausing new self-serve signups for GitHub Copilot Business for organizations on GitHub Free and GitHub Team plans. Existing Copilot Business customers are not affected and can continue adding seats and using the service as they normally would.

6. **[Bring your own language model key in VS Code now available](https://github.blog/changelog/2026-04-22-bring-your-own-language-model-key-in-vs-code-now-available)**
	*Apr 22, 2026*

	Copilot Business and Enterprise users can now use bring your own language model key (BYOK) in Visual Studio Code. BYOK lets teams reuse their API keys to access models from providers like Anthropic, Gemini, OpenAI, OpenRouter, and Azure, as well as locally running models through Ollama and Foundry Local.

7. **[Copilot code review user counts now aggregate in usage metrics API](https://github.blog/changelog/2026-04-22-copilot-code-review-user-counts-now-aggregate-in-usage-metrics-api)**
	*Apr 22, 2026*

	Following the launch of Copilot code review active and passive user identification, enterprise and organization usage reports in the Copilot usage metrics API now include aggregated active and passive user counts for Copilot code review. Passive users are those whose reviews were auto-triggered by a repository or organization policy, with no active signal in the same period.

8. **[GitHub Copilot for Jira: Our latest enhancements](https://github.blog/changelog/2026-04-22-github-copilot-for-jira-our-latest-enhancements)**
	*Apr 22, 2026*

	Since our last update, we've continued to invest in making the GitHub Copilot cloud agent for Jira integration more powerful and customizable. These improvements give teams greater control over how Copilot works within their existing Jira workflows. You can now specify in the Jira ticket a custom agent from your GitHub repository to be used when fulfilling the task.

9. **[Upcoming change to Copilot usage metrics report download URLs](https://github.blog/changelog/2026-04-22-upcoming-change-to-copilot-usage-metrics-report-download-urls)**
	*Apr 22, 2026*

	We are migrating the download URLs for Copilot usage metrics reports from Azure Front Door domains to a stable, GitHub-owned custom domain. This change will improve URL stability and make firewall and proxy allowlist management easier for enterprise customers.

10. **[GitHub CLI: Opt-out usage telemetry](https://github.blog/changelog/2026-04-22-github-cli-opt-out-usage-telemetry)**
	*Apr 22, 2026*

	With the release of v2.91.0, GitHub CLI sends pseudonymous usage telemetry to help us improve the product. We want you to understand what we send and why. As adoption of GitHub CLI grows, we need visibility into how you use features in practice.

---

## Older Updates

See [CHANGELOG.md](CHANGELOG.md) for the full historical timeline.

---

_All dates are complete and sorted newest first. For a full list of updates, see [CHANGELOG.md](CHANGELOG.md)._
