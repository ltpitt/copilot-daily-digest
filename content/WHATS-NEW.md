# What's New with GitHub Copilot

> Latest updates from the last 30 days

**Last Updated**: June 26, 2026

This page highlights significant Copilot updates from the past 30 days. Content older than 30 days moves to [CHANGELOG.md](CHANGELOG.md).

---

## This Week (Last 7 Days)

### Recent Updates

#### 1. [Actions steps can now be run in parallel](https://github.blog/changelog/2026-06-25-actions-steps-can-now-be-run-in-parallel)
*Jun 25, 2026*

GitHub Actions now supports running steps concurrently using background. Previously, all steps in a workflow ran in sequence, with each step starting only after the previous step completed. Previously, you could run steps in a non-blocking way using shell backgrounding (&), but that often interleaved logs from multiple steps.

#### 2. [Copilot code review: Analysis depth and efficiency updates](https://github.blog/changelog/2026-06-25-copilot-code-review-analysis-depth-and-efficiency-updates)
*Jun 25, 2026*

Copilot code review now uses the built-in file exploration tools available in the Copilot CLI and SDK, significantly improving review cost efficiency with no change to your existing workflow. If you're in the Medium analysis depth public preview, you'll also see some new updates centered around configurability and visibility of review depth.

#### 3. [GitHub Copilot for Jira is now generally available](https://github.blog/changelog/2026-06-25-github-copilot-for-jira-is-now-generally-available)
*Jun 25, 2026*

GitHub Copilot for Jira is now generally available. Since launching the public preview in March 2026, we have shipped a series of enhancements based on your feedback, including model selection, Confluence context via MCP, custom agents, custom fields, space-level guidance, and review request notifications in Jira.

#### 4. [Enterprise-managed settings now support strictKnownMarketplaces in VS Code and GitHub Copilot CLI](https://github.blog/changelog/2026-06-25-enterprise-managed-settings-now-support-strictknownmarketplaces-in-vs-code-and-the-cli)
*Jun 25, 2026*

Enterprises can now control which plugins their users can install in GitHub Copilot CLI and VS Code. This setting is now available in public preview. Add strictKnownMarketplaces to your enterprise-managed settings.json, and Copilot will only allow plugins to be installed from the marketplaces you've explicitly defined.

#### 5. [Evaluating performance and efficiency of the GitHub Copilot agentic harness across models and tasks](https://github.blog/ai-and-ml/github-copilot/evaluating-performance-and-efficiency-of-the-github-copilot-agentic-harness-across-models-and-tasks/)
*Jun 25, 2026*

While the model provides&#8239;the raw&#8239;intelligence, the harness shapes how effectively that intelligence is applied. The GitHub Copilot agentic harness is a single shared component of the GitHub Copilot SDK, which powers the GitHub Copilot CLI, GitHub Copilot app, and Copilot code review, along with a wide variety of experiences across GitHub and Microsoft.

---

## Last 30 Days

### Significant Updates

1. **[More control over your GitHub-hosted runners](https://github.blog/changelog/2026-06-25-more-control-over-your-github-hosted-runners)**
	*Jun 25, 2026*

	Organizations now have more control over who can use GitHub-hosted runners in Actions. Admins can now disable the standard labels for hosted runners such as ubuntu-latest, as well as add macOS runners to runner groups. Restrict access to macOS runners: Limit which organizations, repositories, or workflows can use specific macOS runners through group-level permissions.

2. **[npm adds preventive account protection for high-impact accounts](https://github.blog/changelog/2026-06-25-npm-adds-preventive-account-protection-for-high-impact-accounts)**
	*Jun 25, 2026*

	When a high-impact account changes its email or uses a 2FA recovery code, the account is placed into a 72-hour read-only state and an alert is sent to the account's previous email address. This closes an attack vector that recent supply chain attacks have exploited: a compromised account changes its email, mints a new token, and publishes malicious versions.

3. **[Red Hat Enterprise Linux runner images are now in public preview](https://github.blog/changelog/2026-06-25-red-hat-enterprise-linux-runner-images-are-now-in-public-preview)**
	*Jun 25, 2026*

	GitHub-hosted larger runners now support Red Hat Enterprise Linux (RHEL) 9 and RHEL 10 images in public preview, introduced in partnership with Red Hat. Organizations can use these RHEL images as the foundation for custom images that include required tools, dependencies, and configurations. RHEL images are available in public preview for Linux x64 larger runners.

4. **[Changes to model selection for Free and Student plans](https://github.blog/changelog/2026-06-24-changes-to-model-selection-for-free-and-student-plans)**
	*Jun 24, 2026*

	Copilot Free and Student plans will now use Copilot auto model selection as the default and only model selection experience. Auto dynamically selects the best model for each task, removing the need for manual choice. Auto provides access to models across multiple model families, subject to plan restrictions.

5. **[Self-service credential revocation for incident response](https://github.blog/changelog/2026-06-24-self-service-credential-revocation-for-incident-response)**
	*Jun 24, 2026*

	For a timely response to security incidents involving compromised accounts or stolen credentials, GitHub Enterprise owners can now use new "break-glass" capabilities to instantly revoke all credentials for a given user. This builds on the enterprise-wide credential management tools for incident response released earlier.

6. **[How physicists at CERN use GitHub to analyze data](https://www.youtube.com/shorts/Ci8etZO6zyo)**
	*Jun 24, 2026*

	At CERN, finding the universe's smallest particles requires big collaborative efforts. 🤝
Research fellow Batoul Diab shares how the ALICE collaboration uses open source code on GitHub to analyze...

7. **[I automated my job (and it made me a better leader)](https://github.blog/developer-skills/github/i-automated-my-job-and-it-made-me-a-better-leader/)**
	*Jun 23, 2026*

	Here's the thing about senior leadership that nobody warns you about: the job isn't hard because of any single task. It's hard because your work lives in fifteen different places and your brain is the only system connecting them. Meetings bleed into each other.

8. **[GitHub Copilot app support for BYOK](https://github.blog/changelog/2026-06-23-github-copilot-app-support-for-byok)**
	*Jun 23, 2026*

	The GitHub Copilot app now supports bring your own key (BYOK), so you can run agent sessions against your own model providers, including OpenAI, Azure OpenAI, Microsoft Foundry, Anthropic, LM Studio, Ollama, and any OpenAI-compatible endpoint. Add a provider in Settings &rarr; Model Providers with your endpoint and API key, or just a host for LM Studio or Ollama.

9. **[Copilot CLI: New terminal interface is generally available](https://github.blog/changelog/2026-06-23-copilot-cli-new-terminal-interface-is-generally-available)**
	*Jun 23, 2026*

	The redesigned terminal interface for GitHub Copilot CLI that we previewed at Microsoft Build 2026 is now generally available. You get a tabbed layout for working with GitHub directly from your terminal, a new experience for configuring your tools, and a cleaner, more accessible interface throughout. An interactive Copilot CLI session now has tabs at the top of the screen.

10. **[New in GitHub Copilot CLI: Bring GitHub right into your terminal](https://www.youtube.com/watch?v=YpgA1hJsNF8)**
	*Jun 23, 2026*

	We are excited to announce new updates for the GitHub Copilot CLI that bring the power of the GitHub platform directly into your terminal environment.

---

## Older Updates

See [CHANGELOG.md](CHANGELOG.md) for the full historical timeline.

---

_All dates are complete and sorted newest first. For a full list of updates, see [CHANGELOG.md](CHANGELOG.md)._
