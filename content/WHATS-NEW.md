# What's New with GitHub Copilot

> Latest updates from the last 30 days

**Last Updated**: July 10, 2026

This page highlights significant Copilot updates from the past 30 days. Content older than 30 days moves to [CHANGELOG.md](CHANGELOG.md).

---

## This Week (Last 7 Days)

### [Organization-level targeting for GitHub Code Quality](https://github.blog/changelog/2026-07-09-organization-level-targeting-for-github-code-quality)
*Jul 9, 2026*

Organization owners can now target a subset of repositories when enabling or disabling GitHub Code Quality, rather than applying it to every repository at once. This gives you more granular control on where you enable or disable Code Quality across your organization. From the "Code Quality" section of your organization settings, you can select repositories by:
Custom properties.

### [OpenAI’s GPT-5.6 Sol, Terra, and Luna are now available in GitHub Copilot](https://github.blog/changelog/2026-07-09-openais-gpt-5-6-sol-terra-and-luna-are-now-available-in-github-copilot)
*Jul 9, 2026*

OpenAI's GPT-5.6 family is now rolling out in GitHub Copilot. GPT-5.6 comes in three variants, Sol, Terra, and Luna, so you can match the model to the job, whether that's reasoning over a large codebase, everyday agentic coding, or fast, cost-efficient assistance. GPT-5.6 Sol: The highest reasoning ceiling in the family.

### [Ask Copilot for a repository overview](https://github.blog/changelog/2026-07-09-ask-copilot-for-a-repository-overview)
*Jul 9, 2026*

You can now ask GitHub Copilot for a high-level overview of any repository you're exploring for the first time. When you visit the home page of a repository you haven't contributed to before on github.com, Copilot offers to generate an overview for you.

### [Bring Your Own Key to the GitHub Copilot app, now available for all Copilot plans](https://www.youtube.com/watch?v=r1Sy8ij_xWQ)
*Jul 9, 2026*

The GitHub Copilot app now supports bring your own key (BYOK), allowing you to connect custom model providers directly to your workflow. In this tutorial, we show you how to set up local models using Ollama and switch between them in the model...

### [Innersource security advisories are generally available](https://github.blog/changelog/2026-07-08-innersource-security-advisories-are-generally-available)
*Jul 8, 2026*

GitHub Advanced Security enterprise customers can now publish internal security advisories. Innersource advisories work similarly to GitHub's open source advisories, but their visibility is restricted to repositories owned by the enterprise. There is a new REST API endpoint to manage innersource vulnerabilities, including operations to create, update, or withdraw vulnerabilities.

---

## Last 30 Days

### [setup-java v5.5.0: signature verification, Kona JDK, and Maven fixes](https://github.blog/changelog/2026-07-08-setup-java-v5-5-0-signature-verification-kona-jdk-and-maven-fixes)
*Jul 8, 2026*

The actions/setup-java v5.5.0 release adds cryptographic signature verification for downloaded JDKs, support for a new distribution, and several quality-of-life improvements for Maven users. Here's what changed since v5.4.0.
Verify JDK download signatures: Set verify-signature: true and the action downloads the detached GPG signature and validates the JDK archive before installing it.

### [GitHub Copilot in Visual Studio Code, June 2026 releases](https://github.blog/changelog/2026-07-08-github-copilot-in-visual-studio-code-june-2026-releases)
*Jul 8, 2026*

This changelog covers VS Code v1.123 through v1.127, shipped throughout June and early July 2026. The latest VS Code releases build on the Copilot experience developers use every day, making it easier to manage agent work, understand usage, choose the right models, and stay in the flow.

### [GitHub Mobile: Fix merge conflicts with Copilot cloud agent](https://github.blog/changelog/2026-07-08-github-mobile-fix-merge-conflicts-with-copilot-cloud-agent)
*Jul 8, 2026*

GitHub Mobile now supports fixing pull request merge conflicts with Copilot cloud agent, making it easier to unblock pull requests while you're on the go. When a pull request has merge conflicts, you can now start the Copilot workflow directly from the pull request merge box on mobile.

### [Deploy managed Copilot settings via MDM in VS Code and CLI](https://github.blog/changelog/2026-07-08-deploy-managed-copilot-settings-via-mdm-in-vs-code-and-cli)
*Jul 8, 2026*

Enterprise administrators can now deliver managed GitHub Copilot settings directly to devices through native mobile device management (MDM) and file-based configuration, in addition to the existing server-managed channel. This is generally available for GitHub Copilot CLI and VS Code.

### [npm install-time security and GAT bypass2fa deprecation](https://github.blog/changelog/2026-07-08-npm-install-time-security-and-gat-bypass2fa-deprecation)
*Jul 8, 2026*

This major release turns on the install-time security defaults we announced in June, and it's also where we begin a deprecation of the most sensitive uses of 2FA-bypass granular access tokens (GATs). All of these were available behind warnings in npm 11.16.0+, so you can prepare before upgrading.

### [Enterprise-managed OpenTelemetry export for VS Code and CLI](https://github.blog/changelog/2026-07-08-enterprise-managed-opentelemetry-export-for-vs-code-and-cli)
*Jul 8, 2026*

Organizations can now mandate where GitHub Copilot sends OpenTelemetry (OTel) data, so telemetry flows to an approved collector without each developer setting OTEL_* environment variables. The configuration is delivered through the telemetry block in enterprise-managed settings and applies to both the Copilot Chat extension in VS Code and the agent host process that powers Copilot CLI.

### [How GitHub Copilot enables zero DNS configuration for GitHub Pages](https://github.blog/ai-and-ml/github-copilot/how-github-copilot-enables-zero-dns-configuration-for-github-pages/)
*Jul 8, 2026*

Custom domains make a project feel real. But for many developers, DNS, the last mile, is also the most frustrating: A records, CNAME entries, TTLs, and that long wait where you're never quite sure if the internet is broken or you are.

### [How to manage Copilot spend across your enterprise](https://www.youtube.com/watch?v=AzuGe_cuCvg)
*Jul 8, 2026*

Managing GitHub Copilot across a large enterprise requires flexible budgeting that aligns with your organizational structure.

### [Add review cycles and time to adoption phases in the usage API](https://github.blog/changelog/2026-07-07-add-review-cycles-and-time-to-adoption-phases-in-the-usage-api)
*Jul 7, 2026*

The Copilot usage metrics API now reports two additional code-review velocity metrics for each AI adoption phase, extending the adoption phase cohorts fields available in the enterprise and organization reports. Alongside the existing per-phase merge time and merge counts, you can now compare how quickly pull requests are reviewed and how many review cycles they take across your adoption cohorts.

### [Kimi K2.7 now available for Copilot Business and Enterprise](https://github.blog/changelog/2026-07-07-kimi-k2-7-now-available-for-copilot-business-and-enterprise)
*Jul 7, 2026*

On July 1, 2026, we announced Kimi K2.7 would be available to Copilot Pro, Pro+, and Max plans. The model is now additionally available on Copilot Business and Copilot Enterprise plans. Kimi K2.7 Code, an open-weight model, is now generally available in GitHub Copilot.

---

## Older Updates

See [CHANGELOG.md](CHANGELOG.md) for the full historical timeline.

---

_All dates are complete and sorted newest first. For a full list of updates, see [CHANGELOG.md](CHANGELOG.md)._
