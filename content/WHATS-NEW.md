# What's New with GitHub Copilot

> Latest updates from the last 30 days

**Last Updated**: June 12, 2026

This page highlights significant Copilot updates from the past 30 days. Content older than 30 days moves to [CHANGELOG.md](CHANGELOG.md).

---

## This Week (Last 7 Days)

### Recent Updates

#### 1. [Agentic workflows no longer need a personal access token](https://github.blog/changelog/2026-06-11-agentic-workflows-no-longer-need-a-personal-access-token)
*Jun 11, 2026*

You can now use GitHub Agentic Workflows with GitHub Actions's built-in GITHUB_TOKEN. This means that you no longer need to create and store a personal access token (PAT), eliminating the operational and security risks of managing long-lived PATs for automations at scale.

#### 2. [AI usage report updates](https://github.blog/changelog/2026-06-11-ai-usage-report-updates)
*Jun 11, 2026*

Your AI usage reports now reflect GitHub AI Credits usage in the standard report fields. To monitor AI credit usage going forward, use quantity for AI credit quantity and gross_amount for the dollar amount. These fields now provide the same signal that aic_quantity and aic_gross_amount previously provided during the preview period.

#### 3. [Bot-created pull requests can run workflows if approved](https://github.blog/changelog/2026-06-11-bot-created-pull-requests-can-run-workflows-if-approved)
*Jun 11, 2026*

Pull requests created by the github-actions[bot] are now able to run your CI/CD workflows with user approval. Requiring approval is a security measure to ensure generated code does not automatically run workflows which may have access to sensitive information. This matches the behavior of Copilot-generated pull requests.

#### 4. [Copilot CLI: Configure everything from one place with /settings](https://github.blog/changelog/2026-06-11-copilot-cli-configure-everything-from-one-place-with-settings)
*Jun 11, 2026*

GitHub Copilot CLI now has a unified, schema-driven home for configuration. The new /settings slash command combines the scattered commands like /theme, /streamer-mode, and /experimental with options that previously required manually editing your settings file into a single, discoverable surface.

#### 5. [GitHub Agentic Workflows is now in public preview](https://github.blog/changelog/2026-06-11-github-agentic-workflows-is-now-in-public-preview)
*Jun 11, 2026*

GitHub Agentic Workflows is now in public preview. With agentic workflows, you can automate reasoning-based tasks like issue triage, CI failure analysis, and documentation updates by leveraging coding agents inside GitHub Actions. Define your automation in natural language Markdown files, and GitHub Agentic Workflows compiles them into standard Actions YAML.

---

## Last 30 Days

### Significant Updates

1. **[GitHub Enterprise Server 3.21 is now generally available](https://github.blog/changelog/2026-06-11-github-enterprise-server-3-21-is-now-generally-available)**
	*Jun 11, 2026*

	GitHub Enterprise Server (GHES) 3.21 enhances deployment efficiency, monitoring capabilities, code security, and policy management. Here are a few highlights in the 3.21 release:
	Organization custom properties are now generally available, giving enterprise administrators a way to tag organizations with metadata and automatically target enterprise rulesets.

2. **[New runner images in public preview](https://github.blog/changelog/2026-06-11-new-runner-images-in-public-preview)**
	*Jun 11, 2026*

	Two new GitHub-hosted runner images for GitHub Actions are now available in public preview for all users, giving you early access to test your workflows on the latest platforms before they reach general availability. The Ubuntu 26.04 image is now available for both x64 and arm64 architectures. To start using it, update your workflow file to use runs-on: ubuntu-26.04 or runs-on: ubuntu-26.04-arm.

3. **[Dedicated security review command now available in Copilot CLI](https://github.blog/changelog/2026-06-10-dedicated-security-review-command-now-available-in-copilot-cli)**
	*Jun 10, 2026*

	You can now run a security review on your code changes directly from GitHub Copilot CLI. The new /security-review slash command is shipping as an experimental feature in public preview, giving you a fast, AI-driven way to catch security vulnerabilities before they reach production code. Actionable suggestions you can apply without leaving the terminal.

4. **[Give GitHub Copilot CLI real code intelligence with language servers](https://github.blog/ai-and-ml/github-copilot/give-github-copilot-cli-real-code-intelligence-with-language-servers/)**
	*Jun 10, 2026*

	Ever watched GitHub Copilot CLI extract a JAR file to a temporary directory, grep through .class files, and piece together an API signature from raw bytecode? The agent is resourceful, but without a language server, that's the best it can do. The Language Server Protocol (LSP) is the standard that powers go to definition, find references, and type resolution in editors like VS Code.

5. **[Copilot Chat now sees your agent sessions](https://github.blog/changelog/2026-06-10-copilot-chat-now-sees-your-agent-sessions)**
	*Jun 10, 2026*

	We've improved the handoff experience between Copilot Chat and Copilot cloud agent on the web. We've also enabled new functionality which allows you to search and query past agent sessions in chat. When you kick off an agent session by asking chat to create a session, create a pull request, or do deep research on a repository, chat now reflects the status of your in-progress session.

6. **[Manage sub-issues, types, and dependencies from GitHub CLI](https://github.blog/changelog/2026-06-10-manage-sub-issues-types-and-dependencies-from-github-cli)**
	*Jun 10, 2026*

	GitHub CLI now exposes issue types, parent and sub-issue relationships, and issue dependencies directly from the terminal. This means you can structure and track work without dropping into the browser or writing raw gh api scripts. These are exactly the workflows that both developers, and the coding agents that increasingly rely on gh as their interface to GitHub, run every day.

7. **[Security validation for third-party coding agents](https://github.blog/changelog/2026-06-09-security-validation-for-third-party-coding-agents)**
	*Jun 9, 2026*

	Security validation for third-party coding agents is now generally available. GitHub supports third-party coding agents (including Claude and OpenAI Codex) that work directly within your repositories to implement features, fix bugs, and improve test coverage. Now, code generated by these agents receives the same automatic security validation already available for GitHub Copilot cloud agent.

8. **[Claude Fable 5 is generally available for GitHub Copilot](https://github.blog/changelog/2026-06-09-claude-fable-5-is-generally-available-for-github-copilot)**
	*Jun 9, 2026*

	Claude Fable 5 from Anthropic is now available in GitHub Copilot, the first model in Anthropic's Mythos class, designed for long-horizon, autonomous coding and knowledge-work tasks. Unlike other Claude models in GitHub Copilot, Claude Fable 5 requires data retention to operate Anthropic's safety classifiers. Continue reading for more details.

9. **[From one-off prompts to workflows: How to use custom agents in GitHub Copilot CLI](https://github.blog/ai-and-ml/github-copilot/from-one-off-prompts-to-workflows-how-to-use-custom-agents-in-github-copilot-cli/)**
	*Jun 9, 2026*

	Developers work across many surfaces like the CLI, IDE, and GitHub. The terminal is often where they turn to move fast, automate tasks, or work directly with systems and scripts. Tools like the GitHub Copilot CLI already make this easier.

10. **[Enterprise-managed plugins in VS Code in public preview](https://github.blog/changelog/2026-06-05-enterprise-managed-plugins-in-vs-code-in-public-preview)**
	*Jun 5, 2026*

	Last month we launched a public preview with Copilot CLI that allows enterprise administrators the ability to configure and distribute plugins to GitHub Copilot CLI users across their enterprise. VS Code release version 1.122 adds support for this enterprise-managed capability. The baseline standards you set for your enterprise apply to every user's Copilot CLI and VS Code clients.

---

## Older Updates

See [CHANGELOG.md](CHANGELOG.md) for the full historical timeline.

---

_All dates are complete and sorted newest first. For a full list of updates, see [CHANGELOG.md](CHANGELOG.md)._
