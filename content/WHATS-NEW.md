# What's New with GitHub Copilot

> Latest updates from the last 30 days

**Last Updated**: April 27, 2026

This page highlights significant Copilot updates from the past 30 days. Content older than 30 days moves to [CHANGELOG.md](CHANGELOG.md).

---

> ## ⚠️ Important Billing Change — Action Required by June 1, 2026
>
> **GitHub Copilot code review will start consuming GitHub Actions minutes on June 1, 2026.**
> This affects all paid Copilot plans (Pro, Pro+, Business, Enterprise). Reviews on private repositories will draw from your included Actions minutes, with overages billed at standard Actions rates.
>
> **What to do now:** Review your current Actions usage, check spending limits, and share this update with your billing administrators.
> → [Read the full announcement](https://github.blog/changelog/2026-04-27-github-copilot-code-review-will-start-consuming-github-actions-minutes-on-june-1-2026)

---

## This Week (Last 7 Days)

### Recent Updates

#### 1. [GitHub Copilot code review will start consuming GitHub Actions minutes on June 1, 2026](https://github.blog/changelog/2026-04-27-github-copilot-code-review-will-start-consuming-github-actions-minutes-on-june-1-2026)
*Apr 27, 2026*

Starting June 1, 2026, Copilot code reviews will be billed in two ways: as AI Credits under the new usage-based billing model, and by consuming GitHub Actions minutes from your existing plan entitlement for reviews run on private repositories. This change affects Copilot Pro, Pro+, Business, and Enterprise plans — including reviews triggered by non-licensed users billed through direct org billing. Public repositories are unaffected, as Actions minutes remain free. To prepare, review your current Actions usage in billing settings, confirm spending limits are set appropriately, and share this update with your billing administrators and engineering leads before the June 1 deadline.

#### 2. [Copilot cloud agent starts 20% faster with Actions custom images](https://github.blog/changelog/2026-04-27-copilot-cloud-agent-starts-20-faster-with-actions-custom-images)
*Apr 27, 2026*

Copilot cloud agent now starts up over 20% faster, thanks to optimized runner environments built with GitHub Actions custom images. When you assign an issue to Copilot, start a task from the Agents tab, or mention @copilot in a pull request, the agent spins up a cloud-based environment to do its work.

#### 3. [Copilot Student GPT-5.3-Codex removal from model picker](https://github.blog/changelog/2026-04-27-copilot-student-gpt-5-3-codex-removal-from-model-picker)
*Apr 27, 2026*

Starting today, in our Copilot Student plan, we are removing GPT-5.3-Codex from the model picker. It remains available through auto model selection. Auto model selection is built to match each request with the strongest model for the job, which means less time toggling settings and more time coding.

#### 4. [Changes to notification retention and archived repository watches](https://github.blog/changelog/2026-04-24-changes-to-notification-retention-and-archived-repository-watches)
*Apr 24, 2026*

Two updates will change the way GitHub notifications and repository watches are retained. These updates are rolling out soon, and are expected to be completed over the next few months. Web notifications will be retained for three months, reduced from five months.

#### 5. [GPT-5.5 is generally available for GitHub Copilot](https://github.blog/changelog/2026-04-24-gpt-5-5-is-generally-available-for-github-copilot)
*Apr 24, 2026*

GPT-5.5, OpenAI's latest GPT model, is now rolling out on GitHub Copilot. In our early testing, GPT-5.5 delivers its strongest performance on complex, multi-step agentic coding task and resolves real-world coding challenges previous GPT models couldn't. Note that this model is launching with a 7.5&times; premium request multiplier as part of promotional pricing.

---

## Last 30 Days

### Significant Updates

1. **[Inline agent mode in preview and more in GitHub Copilot for JetBrains IDEs](https://github.blog/changelog/2026-04-24-inline-agent-mode-in-preview-and-more-in-github-copilot-for-jetbrains-ides)**
	*Apr 24, 2026*

	This update introduces inline agent mode in preview, enhancements to Next Edit Suggestions, global auto approve, and more flexible controls for terminal commands and file edits. It also includes several user experience refinements and quality improvements across GitHub Copilot for JetBrains IDEs.
	 
	 
	Inline agent mode is now available in public preview.

2. **[Notice about upcoming new format for GitHub App installation tokens](https://github.blog/changelog/2026-04-24-notice-about-upcoming-new-format-for-github-app-installation-tokens)**
	*Apr 24, 2026*

	Starting April 27th 2026 and over the coming weeks, we will begin a staged rollout that updates the format of newly minted GitHub App installation tokens, making them more performant and improving the reliability of our API surface. If your application expects or relies on installation tokens being exactly 40 characters long, it may not handle this new token format correctly.

3. **[2026 04 23 Better Debugging With Github Copilot On The Web](https://github.blog/changelog/2026-04-23-better-debugging-with-github-copilot-on-the-web)**
	*Apr 23, 2026*

	Explore the latest update: 2026 04 23 Better Debugging With Github Copilot On The Web.

4. **[Copilot Chat improvements for pull requests](https://github.blog/changelog/2026-04-23-copilot-chat-improvements-for-pull-requests)**
	*Apr 23, 2026*

	GitHub Copilot Chat now provides richer context and new capabilities when you're working with diffs and pull requests. You can access this functionality by asking a question about a pull request in github.com/copilot, or via the global Copilot navigation, which allows you to open chat over any GitHub surface.

5. **[Copilot cloud agent fields added to usage metrics](https://github.blog/changelog/2026-04-23-copilot-cloud-agent-fields-added-to-usage-metrics)**
	*Apr 23, 2026*

	Following the Copilot coding agent to Copilot cloud agent rename, the Copilot usage metrics API now includes a new used_copilot_cloud_agent field in user-level reports. This boolean field mirrors the existing used_copilot_coding_agent flag under the updated product name.

6. **[2026 04 23 Dependabot Graphs For Python](https://github.blog/changelog/2026-04-23-dependabot-graphs-for-python)**
	*Apr 23, 2026*

	Explore the latest update: 2026 04 23 Dependabot Graphs For Python.

7. **[Global pull requests dashboard moves to opt-out public preview](https://github.blog/changelog/2026-04-23-global-pull-requests-dashboard-moves-to-opt-out-public-preview)**
	*Apr 23, 2026*

	The new global pull requests dashboard will be on by default for all GitHub users as the new experience transitions to an opt-out public preview. The new dashboard and inbox view give you a unified place to manage all of your pull requests. Since the opt-in preview launched, we've shipped a wave of improvements based on your feedback.

8. **[2026 04 23 View And Manage Agent Sessions From Issues And Projects](https://github.blog/changelog/2026-04-23-view-and-manage-agent-sessions-from-issues-and-projects)**
	*Apr 23, 2026*

	Explore the latest update: 2026 04 23 View And Manage Agent Sessions From Issues And Projects.

9. **[2026 04 22 Github Copilot For Jira Our Latest Enhancements](https://github.blog/changelog/2026-04-22-github-copilot-for-jira-our-latest-enhancements)**
	*Apr 22, 2026*

	Explore the latest update: 2026 04 22 Github Copilot For Jira Our Latest Enhancements.

10. **[2026 04 22 Pausing New Self Serve Signups For Github Copilot Business](https://github.blog/changelog/2026-04-22-pausing-new-self-serve-signups-for-github-copilot-business)**
	*Apr 22, 2026*

	Explore the latest update: 2026 04 22 Pausing New Self Serve Signups For Github Copilot Business.

---

## Older Updates

See [CHANGELOG.md](CHANGELOG.md) for the full historical timeline.

---

_All dates are complete and sorted newest first. For a full list of updates, see [CHANGELOG.md](CHANGELOG.md)._
