# What's New with GitHub Copilot

> Latest updates from the last 30 days

**Last Updated**: May 06, 2026

This page highlights significant Copilot updates from the past 30 days. Content older than 30 days moves to [CHANGELOG.md](CHANGELOG.md).

---

## This Week (Last 7 Days)

### Recent Updates

#### 1. [Code-to-cloud risk visibility with Microsoft Defender for Cloud is now generally available](https://github.blog/changelog/2026-05-05-code-to-cloud-risk-visibility-with-microsoft-defender-for-cloud-is-now-generally-available)
*May 5, 2026*

This integration is now generally available. Since entering public preview, we've heard valuable feedback from customers, and we've shipped follow-up improvements that bring artifact and runtime context closer to the GitHub Advanced Security alert experience.

#### 2. [Dependency scanning with GitHub MCP Server is in public preview](https://github.blog/changelog/2026-05-05-dependency-scanning-with-github-mcp-server-is-in-public-preview)
*May 5, 2026*

The GitHub MCP Server can now scan your code changes for vulnerable dependencies before you commit or open a pull request. You'll catch known vulnerabilities while you write code with MCP-compatible IDEs and AI coding agents. It's now in public preview for repositories with Dependabot alerts enabled.

#### 3. [Secret scanning with GitHub MCP Server is now generally available](https://github.blog/changelog/2026-05-05-secret-scanning-with-github-mcp-server-is-now-generally-available)
*May 5, 2026*

GitHub secret scanning in the GitHub MCP (Model Context Protocol) server is now generally available. When you use an MCP-compatible AI coding agent or IDE (like GitHub Copilot CLI or Visual Studio Code), you can scan your code for exposed secrets before you commit or open a pull request, so leaked credentials don't make it into your repository in the first place.

#### 4. [Deprecation notice: code_scanning_upload field will be removed from rate_limit API endpoint](https://github.blog/changelog/2026-05-05-deprecation-notice-code_scanning_upload-field-will-be-removed-from-rate_limit-api-endpoint)
*May 5, 2026*

On May 19, 2026, we'll remove the code_scanning_upload field from the rate_limit REST API endpoint response. The code_scanning_upload field in the rate_limit response has been a source of confusion. While it appeared as a separate rate limit category, it shares the same limit pool as core.

#### 5. [What is TanStack AI? The new open source toolkit](https://www.youtube.com/shorts/wS8CV85RTO8)
*May 5, 2026*

The team behind some of the most popular React libraries just released the alpha for TanStack AI. Dubbed the "Switzerland of AI tooling," this open source, framework-agnostic toolkit lets you build AI applications without vendor lock-in.

---

## Last 30 Days

### Significant Updates

1. **[Jueves de Quack con Lesly Zerna, desarrolladora de currículo en DeepLearning.AI](https://www.youtube.com/watch?v=FXu1WpzSsIU)**
	*May 4, 2026*

	Spec-Driven Development: el SPEC.md como cerebro de tus agentes Invitada: Lesly Zerna, desarrolladora de currículo en DeepLearning.AI
Si dejas que el agente decida todo, el proyecto pierde el rumbo.

2. **[Upcoming deprecation of GPT-5.2 and GPT-5.2-Codex](https://github.blog/changelog/2026-05-01-upcoming-deprecation-of-gpt-5-2-and-gpt-5-2-codex)**
	*May 1, 2026*

	Copilot Enterprise administrators may need to enable access to alternative models through their model policies in Copilot settings. As an administrator, you can verify availability by checking your individual Copilot settings and confirming that the policy is enabled for the specific model. Once enabled, you'll see the model in the Copilot Chat model selector in VS Code and on github.com.

3. **[The Download: Linux 486 retirement, DeepSeek v4, TanStack AI & more](https://www.youtube.com/watch?v=PpL7vQupWqM)**
	*May 1, 2026*

	Welcome back to The Download. This week, we cover France's massive move to migrate its government ministries to Linux for digital sovereignty.

4. **[GitHub Copilot in Visual Studio — April update](https://github.blog/changelog/2026-04-30-github-copilot-in-visual-studio-april-update)**
	*Apr 30, 2026*

	The April 2026 update to Visual Studio centers on agentic workflows: cloud agent sessions launch directly from the IDE, custom agents gain user-level support, and a new Debugger agent validates fixes against live runtime behavior. Here's what's new with GitHub Copilot in Visual Studio 2026.

5. **[Copilot cloud agent starts 20% faster with Actions custom images](https://github.blog/changelog/2026-04-27-copilot-cloud-agent-starts-20-faster-with-actions-custom-images)**
	*Apr 27, 2026*

	Copilot cloud agent now starts up over 20% faster, thanks to optimized runner environments built with GitHub Actions custom images. When you assign an issue to Copilot, start a task from the Agents tab, or mention @copilot in a pull request, the agent spins up a cloud-based environment to do its work.

6. **[Copilot Student GPT-5.3-Codex removal from model picker](https://github.blog/changelog/2026-04-27-copilot-student-gpt-5-3-codex-removal-from-model-picker)**
	*Apr 27, 2026*

	Starting today, in our Copilot Student plan, we are removing GPT-5.3-Codex from the model picker. It remains available through auto model selection. Auto model selection is built to match each request with the strongest model for the job, which means less time toggling settings and more time coding.

7. **[GitHub Copilot code review will start consuming GitHub Actions minutes on June 1, 2026](https://github.blog/changelog/2026-04-27-github-copilot-code-review-will-start-consuming-github-actions-minutes-on-june-1-2026)**
	*Apr 27, 2026*

	Developers and engineering teams worldwide use GitHub Copilot for high-quality, agent-powered code reviews on every pull request. We understand that any change is significant to our customers, especially when it relates to billing, so we are sharing this update early to help you plan and prepare. The sections below outline what is changing, why, and how to plan accordingly.

8. **[Changes to Notification Retention and Archived Repository Watches](https://github.blog/changelog/2026-04-24-changes-to-notification-retention-and-archived-repository-watches)**
	*Apr 24, 2026*

	GitHub has updated its notification retention policy and behavior for archived repository watches. Developers can check the changelog for details on what changes and how to update their notification preferences accordingly.

9. **[GPT-5.5 Is Generally Available for GitHub Copilot](https://github.blog/changelog/2026-04-24-gpt-5-5-is-generally-available-for-github-copilot)**
	*Apr 24, 2026*

	OpenAI's GPT-5.5 model is now generally available across all GitHub Copilot experiences. Developers can select it from the model picker in Copilot Chat and benefit from its improved reasoning and code generation capabilities.

10. **[Inline Agent Mode in Preview and More in GitHub Copilot for JetBrains IDEs](https://github.blog/changelog/2026-04-24-inline-agent-mode-in-preview-and-more-in-github-copilot-for-jetbrains-ides)**
	*Apr 24, 2026*

	JetBrains IDE users can now try the new inline agent mode in public preview, bringing agentic Copilot capabilities directly into the editor. This release also includes additional improvements and refinements to the GitHub Copilot experience across the JetBrains IDE family.

---

## Older Updates

See [CHANGELOG.md](CHANGELOG.md) for the full historical timeline.

---

_All dates are complete and sorted newest first. For a full list of updates, see [CHANGELOG.md](CHANGELOG.md)._
