# What's New with GitHub Copilot

> Latest updates from the last 30 days

**Last Updated**: June 26, 2026

This page highlights significant Copilot updates from the past 30 days. Content older than 30 days moves to [CHANGELOG.md](CHANGELOG.md).

---

## This Week (Last 7 Days)

### [Actions steps can now be run in parallel](https://github.blog/changelog/2026-06-25-actions-steps-can-now-be-run-in-parallel)
*Jun 25, 2026*

GitHub Actions now lets you run workflow steps concurrently with native `background`, `wait`, and `wait-all` support. Teams can speed up long workflows without falling back to shell hacks that mix logs together and make failures harder to debug.

### [Copilot code review: Analysis depth and efficiency updates](https://github.blog/changelog/2026-06-25-copilot-code-review-analysis-depth-and-efficiency-updates)
*Jun 25, 2026*

Copilot code review now relies on the built-in file exploration tools from the Copilot CLI and SDK, which improves cost efficiency without changing how you request reviews. Organizations testing Medium analysis depth also get more control over how deeply reviews investigate a change.

### [GitHub Copilot for Jira is now generally available](https://github.blog/changelog/2026-06-25-github-copilot-for-jira-is-now-generally-available)
*Jun 25, 2026*

GitHub Copilot for Jira has reached general availability after adding model selection, Confluence context through MCP, custom agents, and richer Jira-specific guidance. The GA release also focuses on giving teams more visibility and control over agent sessions tied to planning work.

### [Enterprise-managed settings now support strictKnownMarketplaces in VS Code and GitHub Copilot CLI](https://github.blog/changelog/2026-06-25-enterprise-managed-settings-now-support-strictknownmarketplaces-in-vs-code-and-the-cli)
*Jun 25, 2026*

Enterprise admins can now restrict plugin installation in VS Code and the GitHub Copilot CLI to approved marketplaces only. This preview setting gives security and platform teams a cleaner way to enforce tool governance before plugins ever run.

### [Evaluating performance and efficiency of the GitHub Copilot agentic harness across models and tasks](https://github.blog/ai-and-ml/github-copilot/evaluating-performance-and-efficiency-of-the-github-copilot-agentic-harness-across-models-and-tasks/)
*Jun 25, 2026*

GitHub shared new benchmark results showing how its agentic harness balances task success, token efficiency, and model flexibility across more than 20 supported models. The post is especially useful if you want to understand how Copilot's shared SDK layer shapes real-world agent performance beyond raw model quality.

---

## Last 30 Days

### [More control over your GitHub-hosted runners](https://github.blog/changelog/2026-06-25-more-control-over-your-github-hosted-runners)
*Jun 25, 2026*

GitHub Actions administrators can now disable standard runner labels and add macOS runners to runner groups. The update makes it easier to lock down access, manage concurrency, and apply tighter governance to hosted infrastructure.

### [npm adds preventive account protection for high-impact accounts](https://github.blog/changelog/2026-06-25-npm-adds-preventive-account-protection-for-high-impact-accounts)
*Jun 25, 2026*

npm now places high-impact accounts into a 72-hour read-only state after sensitive changes such as email updates or 2FA recovery. That safeguard is designed to slow account takeovers and reduce the chance that attackers can quickly publish malicious packages.

### [Red Hat Enterprise Linux runner images are now in public preview](https://github.blog/changelog/2026-06-25-red-hat-enterprise-linux-runner-images-are-now-in-public-preview)
*Jun 25, 2026*

GitHub-hosted larger runners now offer RHEL 9 and RHEL 10 images in public preview. Organizations that standardize on Red Hat can use those images as a base for custom runner environments without maintaining their own infrastructure.

### [Changes to model selection for Free and Student plans](https://github.blog/changelog/2026-06-24-changes-to-model-selection-for-free-and-student-plans)
*Jun 24, 2026*

Copilot Free and Student plans now use auto model selection as the only model-picking experience. The change simplifies onboarding by letting Copilot choose the best available model for each task while keeping plan-specific access rules in place.

### [Self-service credential revocation for incident response](https://github.blog/changelog/2026-06-24-self-service-credential-revocation-for-incident-response)
*Jun 24, 2026*

GitHub Enterprise owners can now trigger break-glass credential revocation when an account or token is compromised. This gives incident responders a faster path to shutting down access across an enterprise before an active attack spreads.

### [How physicists at CERN use GitHub to analyze data](https://www.youtube.com/shorts/Ci8etZO6zyo)
*Jun 24, 2026*

This short video shows how CERN researchers use GitHub to coordinate open source analysis at massive scale. It is a quick reminder that collaborative review, shared code, and transparent workflows matter well beyond traditional software teams.

### [I automated my job (and it made me a better leader)](https://github.blog/developer-skills/github/i-automated-my-job-and-it-made-me-a-better-leader/)
*Jun 23, 2026*

This leadership-focused essay explains how a senior engineering leader uses dozens of small automations to reduce coordination overhead. It offers practical ideas for turning scattered status checks and follow-ups into repeatable workflows that protect time for deeper work.

### [GitHub Copilot app support for BYOK](https://github.blog/changelog/2026-06-23-github-copilot-app-support-for-byok)
*Jun 23, 2026*

The GitHub Copilot app now supports bring your own key, letting you run agent sessions against model providers you already manage. Models from those providers show up directly in the picker, while keys stay stored in the local OS keychain instead of being exposed in the UI.

### [Copilot CLI: New terminal interface is generally available](https://github.blog/changelog/2026-06-23-copilot-cli-new-terminal-interface-is-generally-available)
*Jun 23, 2026*

The redesigned GitHub Copilot CLI interface is now generally available with tabs for issues, pull requests, and other GitHub workflows. It turns the terminal into a more complete control surface for coding, reviewing, and repository management without constant context switching.

### [New in GitHub Copilot CLI: Bring GitHub right into your terminal](https://www.youtube.com/watch?v=YpgA1hJsNF8)
*Jun 23, 2026*

This walkthrough demos the new Copilot CLI terminal experience in action, including the tabbed interface, slash commands, and built-in GitHub workflows. Watch it if you want a quick visual tour of how the updated CLI supports end-to-end work from the command line.

---

## Older Updates

See [CHANGELOG.md](CHANGELOG.md) for the full historical timeline.

---

_All dates are complete and sorted newest first. For a full list of updates, see [CHANGELOG.md](CHANGELOG.md)._
