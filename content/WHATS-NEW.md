# What's New with GitHub Copilot

> Latest updates from the last 30 days

**Last Updated**: May 08, 2026

This page highlights significant Copilot updates from the past 30 days. Content older than 30 days moves to [CHANGELOG.md](CHANGELOG.md).

---

## This Week (Last 7 Days)

### Recent Updates

#### 1. [Agent pull requests are everywhere. Here’s how to review them.](https://github.blog/ai-and-ml/generative-ai/agent-pull-requests-are-everywhere-heres-how-to-review-them/)
*May 7, 2026*

You've probably already approved one without realizing it. But it was agent-generated—and that ease of approval is exactly the problem. A January 2026 study, "More Code, Less Reuse", found that agent-generated code introduces more redundancy and more technical debt per change than human-written code.

#### 2. [Upcoming deprecation of GPT-4.1](https://github.blog/changelog/2026-05-07-upcoming-deprecation-of-gpt-4-1)
*May 7, 2026*

GitHub will deprecate GPT-4.1 across all Copilot experiences on June 1, 2026. Teams should migrate prompts, automations, and integrations to GPT-5.5 before the cutoff to avoid disruptions. This changelog entry outlines the timeline and the supported replacement model.

#### 3. [Enterprise Live Migrations is now in public preview](https://github.blog/changelog/2026-05-07-enterprise-live-migrations-is-now-in-public-preview)
*May 7, 2026*

Enterprise Live Migrations (ELM) is now available in public preview. ELM gives enterprise administrators a new way to migrate repositories from GitHub Enterprise Server (GHES) to GitHub Enterprise Cloud with data residency, without the extended code freezes and business disruption that come with traditional migrations.

#### 4. [Claude Sonnet 4 deprecated](https://github.blog/changelog/2026-05-07-claude-sonnet-4-deprecated)
*May 7, 2026*

GitHub has deprecated Claude Sonnet 4 across Copilot experiences as of May 6, 2026. If your team still depends on that model, you should move to Claude Sonnet 4.6 to stay on a supported path. The update clarifies where this change applies, including chat, completions, and agent workflows.

#### 5. [Rubber Duck in GitHub Copilot CLI now supports more models](https://github.blog/changelog/2026-05-07-rubber-duck-in-github-copilot-cli-now-supports-more-models)
*May 7, 2026*

Rubber Duck, the cross-family review agent in GitHub Copilot CLI, is now available using a Claude-powered critic agent when your session is using a GPT model. For sessions using Claude as their orchestrator, we've upgraded the GPT model used to seek a second opinion. The same second-opinion benefits (architectural catches, subtle bugs, and cross-file conflicts) now apply to GPT-driven sessions.

---

## Last 30 Days

### Significant Updates

1. **[Repository rulesets: User bypass and branch renaming](https://github.blog/changelog/2026-05-07-repository-rulesets-user-bypass-and-branch-renaming)**
	*May 7, 2026*

	GitHub repository rulesets now support two frequently requested features: adding individual users as bypass actors and renaming branches covered by organization rulesets. You can now add individual users as bypass actors on repository-level rulesets through the UI, REST API, and GraphQL.

2. **[Rubber Duck Thursdays: Building an AI agent app](https://www.youtube.com/watch?v=zG6PJHVaUxs)**
	*May 7, 2026*

	In this stream we'll walk through build an agent for a fictional company that we can deploy to production

3. **[Validating agentic behavior when “correct” isn’t deterministic](https://github.blog/ai-and-ml/generative-ai/validating-agentic-behavior-when-correct-isnt-deterministic/)**
	*May 6, 2026*

	Modern software testing is built on a fragile assumption: correct behavior is repeatable. For deterministic code, that assumption mostly holds. But for autonomous agents like Github Copilot Coding Agent (aka Agent Mode), especially as we explore the frontiers of integrated "Computer Use," that assumption breaks down almost immediately.

4. **[Enterprise-managed plugins in GitHub Copilot CLI are now in public preview](https://github.blog/changelog/2026-05-06-enterprise-managed-plugins-in-github-copilot-cli-are-now-in-public-preview)**
	*May 6, 2026*

	Enterprise administrators can now configure and distribute plugins to GitHub Copilot CLI users across their enterprise. Set baseline standards for your enterprise and make them available in every user's Copilot CLI client.

5. **[GitHub Copilot in Visual Studio Code, April releases](https://github.blog/changelog/2026-05-06-github-copilot-in-visual-studio-code-april-releases)**
	*May 6, 2026*

	VS Code moved to weekly stable releases. This changelog covers releases v1.116 through v1.119, the releases we shipped throughout April and early May 2026. Copilot can now search by meaning in any workspace and run grep-style queries across GitHub repos and orgs.

6. **[Search and filter bar for repository security advisories](https://github.blog/changelog/2026-05-06-search-and-filter-bar-for-repository-security-advisories)**
	*May 6, 2026*

	You can now search and filter security advisories directly from your repository's Security tab. Use the new search bar and filters at the top of the advisory list to find advisories by keyword (sort, package, ecosystems, severity) so you spend less time scrolling and more time responding to what matters.

7. **[How to plan projects with GitHub Copilot CLI](https://www.youtube.com/shorts/CIgdAO8mbw0)**
	*May 6, 2026*

	Knowing what to build is easy, but figuring out how to build it can be tricky. In this short, we show you how to use the plan feature in the GitHub Copilot CLI to map out your next project.

8. **[Code To Cloud Risk Visibility With Microsoft Defender For Cloud Is Now Generally Available](https://github.blog/changelog/2026-05-05-code-to-cloud-risk-visibility-with-microsoft-defender-for-cloud-is-now-generally-available)**
	*May 5, 2026*

	GitHub and Microsoft Defender for Cloud now provide generally available code-to-cloud risk visibility. Security teams can connect findings across development and runtime contexts to prioritize risks earlier in the delivery lifecycle.

9. **[Dependency scanning with GitHub MCP Server is in public preview](https://github.blog/changelog/2026-05-05-dependency-scanning-with-github-mcp-server-is-in-public-preview)**
	*May 5, 2026*

	The GitHub MCP Server can now scan your code changes for vulnerable dependencies before you commit or open a pull request. You'll catch known vulnerabilities while you write code with MCP-compatible IDEs and AI coding agents. It's now in public preview for repositories with Dependabot alerts enabled.

10. **[Deprecation Notice Code_Scanning_Upload Field Will Be Removed From Rate_Limit Api Endpoint](https://github.blog/changelog/2026-05-05-deprecation-notice-code_scanning_upload-field-will-be-removed-from-rate_limit-api-endpoint)**
	*May 5, 2026*

	GitHub announced the upcoming removal of the `code_scanning_upload` field from the `rate_limit` API endpoint. If you monitor API limits programmatically, update your tooling now so deprecation does not break dashboards or alerts.

---

## Older Updates

See [CHANGELOG.md](CHANGELOG.md) for the full historical timeline.

---

_All dates are complete and sorted newest first. For a full list of updates, see [CHANGELOG.md](CHANGELOG.md)._
