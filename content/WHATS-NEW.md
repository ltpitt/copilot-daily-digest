# What's New with GitHub Copilot

> Latest updates from the last 30 days

**Last Updated**: April 08, 2026

This page highlights significant Copilot updates from the past 30 days. Content older than 30 days moves to [CHANGELOG.md](CHANGELOG.md).

---

## This Week (Last 7 Days)

### Recent Updates

#### 1. [Code scanning: Batch apply security alert suggestions on pull requests](https://github.blog/changelog/2026-04-07-code-scanning-batch-apply-security-alert-suggestions-on-pull-requests)
*Apr 7, 2026*

GitHub code scanning alerts on pull requests are now easier to address with bulk actions. You can now apply fixes for code scanning alerts in the Files changed tab by adding them to a batch, helping you interact with multiple alerts faster.

#### 2. [Dependabot alerts are now assignable to AI agents for remediation](https://github.blog/changelog/2026-04-07-dependabot-alerts-are-now-assignable-to-ai-agents-for-remediation)
*Apr 7, 2026*

Some dependency vulnerabilities require more than a version bump—they need code changes across your project. You can now assign Dependabot alerts to AI coding agents, including Copilot, Claude, and Codex, to analyze the vulnerability and open a draft pull request with a proposed fix.

#### 3. [Dependabot version updates now support the Nix ecosystem](https://github.blog/changelog/2026-04-07-dependabot-version-updates-now-support-the-nix-ecosystem)
*Apr 7, 2026*

Dependabot now supports Nix flakes. Add nix as a package ecosystem in your dependabot.yml file. Dependabot will then monitor your flake.lock inputs and open pull requests when newer commits are available upstream.

#### 4. [Prioritize security alerts with runtime context from Dynatrace](https://github.blog/changelog/2026-04-07-prioritize-security-alerts-with-runtime-context-from-dynatrace)
*Apr 7, 2026*

You can now use runtime context from Dynatrace to prioritize GitHub Advanced Security alerts based on deployed artifacts and runtime risk in your Kubernetes environment. When you connect Dynatrace to GitHub, you'll see deployment context for container images that Dynatrace maps to your repositories, along with runtime risk signals.

#### 5. [Copilot CLI now supports BYOK and local models](https://github.blog/changelog/2026-04-07-copilot-cli-now-supports-byok-and-local-models)
*Apr 7, 2026*

GitHub Copilot CLI now lets you connect your own model provider or run fully local models instead of using GitHub-hosted model routing. This means you can use the models and providers you're already paying for, operate in air-gapped environments, and maintain direct control over your LLM spend, all while keeping the same agentic terminal experience.

---

## Last 30 Days

### Significant Updates

1. **[Code scanning: Batch apply security alert suggestions on pull requests](https://github.blog/changelog/2026-04-07-code-scanning-batch-apply-security-alert-suggestions-on-pull-requests)**
	*Apr 7, 2026*

	GitHub code scanning alerts on pull requests are now easier to address with bulk actions. You can now apply fixes for code scanning alerts in the Files changed tab by adding them to a batch, helping you interact with multiple alerts faster.

2. **[Dependabot alerts are now assignable to AI agents for remediation](https://github.blog/changelog/2026-04-07-dependabot-alerts-are-now-assignable-to-ai-agents-for-remediation)**
	*Apr 7, 2026*

	Some dependency vulnerabilities require more than a version bump—they need code changes across your project. You can now assign Dependabot alerts to AI coding agents, including Copilot, Claude, and Codex, to analyze the vulnerability and open a draft pull request with a proposed fix.

3. **[Dependabot version updates now support the Nix ecosystem](https://github.blog/changelog/2026-04-07-dependabot-version-updates-now-support-the-nix-ecosystem)**
	*Apr 7, 2026*

	Dependabot now supports Nix flakes. Add nix as a package ecosystem in your dependabot.yml file. Dependabot will then monitor your flake.lock inputs and open pull requests when newer commits are available upstream.

4. **[Prioritize security alerts with runtime context from Dynatrace](https://github.blog/changelog/2026-04-07-prioritize-security-alerts-with-runtime-context-from-dynatrace)**
	*Apr 7, 2026*

	You can now use runtime context from Dynatrace to prioritize GitHub Advanced Security alerts based on deployed artifacts and runtime risk in your Kubernetes environment. When you connect Dynatrace to GitHub, you'll see deployment context for container images that Dynatrace maps to your repositories, along with runtime risk signals.

5. **[Copilot CLI now supports BYOK and local models](https://github.blog/changelog/2026-04-07-copilot-cli-now-supports-byok-and-local-models)**
	*Apr 7, 2026*

	GitHub Copilot CLI now lets you connect your own model provider or run fully local models instead of using GitHub-hosted model routing. This means you can use the models and providers you're already paying for, operate in air-gapped environments, and maintain direct control over your LLM spend, all while keeping the same agentic terminal experience.

6. **[npm trusted publishing now supports CircleCI](https://github.blog/changelog/2026-04-06-npm-trusted-publishing-now-supports-circleci)**
	*Apr 6, 2026*

	Maintainers publishing from CircleCI workflows can now eliminate stored credentials entirely and authenticate directly through their CI/CD pipeline. With this expansion, trusted publishing now covers a large majority of npm publishers by CI provider. Configuration is available through the npm website and the npm trust CLI command.

7. **[Copilot usage metrics now identify active and passive Copilot code review users](https://github.blog/changelog/2026-04-06-copilot-usage-metrics-now-identify-active-and-passive-copilot-code-review-users)**
	*Apr 6, 2026*

	Copilot usage metrics now indicate which users have Copilot code review (CCR) activity, and whether that activity was active or passive. Enterprise and organization admins can see how users engage with Copilot code review on daily and 28-day user-level reports, enabling a clearer picture of CCR adoption and engagement.

8. **[GitHub Copilot CLI combines model families for a second opinion](https://github.blog/ai-and-ml/github-copilot/github-copilot-cli-combines-model-families-for-a-second-opinion/)**
	*Apr 6, 2026*

	When you ask a coding agent to build a data pipeline, it may not use the best structure. But what if the agent got a second opinion before it executed the plan? Today, in GitHub Copilot CLI, we're introducing Rubber Duck in experimental mode.

9. **[Organization firewall settings for Copilot cloud agent](https://github.blog/changelog/2026-04-03-organization-firewall-settings-for-copilot-cloud-agent)**
	*Apr 3, 2026*

	Copilot cloud agent includes a built-in agent firewall to control Copilot's internet access and help protect against prompt injection and data exfiltration. Until now, the firewall was configured at the repository level by repository admins. Organization admins can now manage the agent firewall across all repositories in their organization.

10. **[Organization runner controls for Copilot cloud agent](https://github.blog/changelog/2026-04-03-organization-runner-controls-for-copilot-cloud-agent)**
	*Apr 3, 2026*

	Each time Copilot cloud agent works on a task, it starts a new development environment powered by GitHub Actions. By default, this runs on a standard GitHub-hosted runner, but teams can also customize the agent environment to use large runners or self-hosted runners for faster performance, access to internal resources, and more.

---

## Older Updates

See [CHANGELOG.md](CHANGELOG.md) for the full historical timeline.

---

_All dates are complete and sorted newest first. For a full list of updates, see [CHANGELOG.md](CHANGELOG.md)._
