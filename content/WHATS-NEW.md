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

#### 2. [New runner images in public preview](https://github.blog/changelog/2026-06-11-new-runner-images-in-public-preview)
*Jun 11, 2026*

Two new GitHub-hosted runner images for GitHub Actions are now available in public preview for all users, giving you early access to test your workflows on the latest platforms before they reach general availability. The Ubuntu 26.04 image is now available for both x64 and arm64 architectures. To start using it, update your workflow file to use runs-on: ubuntu-26.04 or runs-on: ubuntu-26.04-arm.

#### 3. [Copilot CLI: Configure everything from one place with /settings](https://github.blog/changelog/2026-06-11-copilot-cli-configure-everything-from-one-place-with-settings)
*Jun 11, 2026*

GitHub Copilot CLI now has a unified, schema-driven home for configuration. The new /settings slash command combines the scattered commands like /theme, /streamer-mode, and /experimental with options that previously required manually editing your settings file into a single, discoverable surface.

#### 4. [AI usage report updates](https://github.blog/changelog/2026-06-11-ai-usage-report-updates)
*Jun 11, 2026*

Your AI usage reports now reflect GitHub AI Credits usage in the standard report fields. To monitor AI credit usage going forward, use quantity for AI credit quantity and gross_amount for the dollar amount. These fields now provide the same signal that aic_quantity and aic_gross_amount previously provided during the preview period.

#### 5. [GitHub Enterprise Server 3.21 is now generally available](https://github.blog/changelog/2026-06-11-github-enterprise-server-3-21-is-now-generally-available)
*Jun 11, 2026*

GitHub Enterprise Server (GHES) 3.21 enhances deployment efficiency, monitoring capabilities, code security, and policy management. Here are a few highlights in the 3.21 release:
Organization custom properties are now generally available, giving enterprise administrators a way to tag organizations with metadata and automatically target enterprise rulesets.

---

## Last 30 Days

### Significant Updates

1. **[Bot-created pull requests can run workflows if approved](https://github.blog/changelog/2026-06-11-bot-created-pull-requests-can-run-workflows-if-approved)**
	*Jun 11, 2026*

	Pull requests created by the github-actions[bot] are now able to run your CI/CD workflows with user approval. Requiring approval is a security measure to ensure generated code does not automatically run workflows which may have access to sensitive information. This matches the behavior of Copilot-generated pull requests.

2. **[GitHub Agentic Workflows is now in public preview](https://github.blog/changelog/2026-06-11-github-agentic-workflows-is-now-in-public-preview)**
	*Jun 11, 2026*

	GitHub Agentic Workflows is now in public preview. With agentic workflows, you can automate reasoning-based tasks like issue triage, CI failure analysis, and documentation updates by leveraging coding agents inside GitHub Actions. Define your automation in natural language Markdown files, and GitHub Agentic Workflows compiles them into standard Actions YAML.

3. **[Copilot Chat now sees your agent sessions](https://github.blog/changelog/2026-06-10-copilot-chat-now-sees-your-agent-sessions)**
	*Jun 10, 2026*

	We've improved the handoff experience between Copilot Chat and Copilot cloud agent on the web. We've also enabled new functionality which allows you to search and query past agent sessions in chat. When you kick off an agent session by asking chat to create a session, create a pull request, or do deep research on a repository, chat now reflects the status of your in-progress session.

4. **[Give GitHub Copilot CLI real code intelligence with language servers](https://github.blog/ai-and-ml/github-copilot/give-github-copilot-cli-real-code-intelligence-with-language-servers/)**
	*Jun 10, 2026*

	Ever watched GitHub Copilot CLI extract a JAR file to a temporary directory, grep through .class files, and piece together an API signature from raw bytecode? The agent is resourceful, but without a language server, that's the best it can do. The Language Server Protocol (LSP) is the standard that powers go to definition, find references, and type resolution in editors like VS Code.

5. **[Manage sub-issues, types, and dependencies from GitHub CLI](https://github.blog/changelog/2026-06-10-manage-sub-issues-types-and-dependencies-from-github-cli)**
	*Jun 10, 2026*

	GitHub CLI now exposes issue types, parent and sub-issue relationships, and issue dependencies directly from the terminal. This means you can structure and track work without dropping into the browser or writing raw gh api scripts. These are exactly the workflows that both developers, and the coding agents that increasingly rely on gh as their interface to GitHub, run every day.

6. **[From one-off prompts to workflows: How to use custom agents in GitHub Copilot CLI](https://github.blog/ai-and-ml/github-copilot/from-one-off-prompts-to-workflows-how-to-use-custom-agents-in-github-copilot-cli/)**
	*Jun 9, 2026*

	Developers work across many surfaces like the CLI, IDE, and GitHub. The terminal is often where they turn to move fast, automate tasks, or work directly with systems and scripts. Tools like the GitHub Copilot CLI already make this easier.

7. **[Jueves de Quack: De pilotos a escala: GitHub Copilot en itti](https://www.youtube.com/watch?v=Z5Nf-xXupzQ)**
	*Jun 9, 2026*

	En itti se propusieron un reto ambicioso: aumentar la productividad del ciclo de desarrollo en un 40%. En esta sesión, Javier Durán, Senior Manager AI en itti, compartirá cómo el equipo está usando...

8. **[How to undo a mistake on GitHub](https://www.youtube.com/shorts/a1oRZ1kAA6M)**
	*Jun 9, 2026*

	Accidentally committed code you didn't mean to? Don't stress, because GitHub has a few easy ways to help you undo it depending on your workflow.

9. **[Answering the most common GitHub beginner questions](https://www.youtube.com/watch?v=ZgARMqR3qq8)**
	*Jun 8, 2026*

	Welcome back to GitHub for beginners! In this episode, our engineers sit down to answer the most frequently asked questions we get from new developers.

10. **[Check out the new GitHub shop spring collection](https://www.youtube.com/shorts/y3apXW8bFNg)**
	*Jun 7, 2026*

	The GitHub shop is officially launching its new spring 2026 collection, and it is built for wherever developers end up, not just sitting at a desk.

---

## Older Updates

See [CHANGELOG.md](CHANGELOG.md) for the full historical timeline.

---

_All dates are complete and sorted newest first. For a full list of updates, see [CHANGELOG.md](CHANGELOG.md)._
