# What's New with GitHub Copilot

> Latest updates from the last 30 days

**Last Updated**: July 03, 2026

This page highlights significant Copilot updates from the past 30 days. Content older than 30 days moves to [CHANGELOG.md](CHANGELOG.md).

---

## This Week (Last 7 Days)

### [Rubber Duck Thursdays! Let's play with canvases in the GitHub Copilot app!](https://www.youtube.com/watch?v=cCFKtW5UiTo)
*Jul 3, 2026*

We're going to talk through the GitHub Changelog, and experiment with some new tools.

### [Improved accuracy and coverage in Copilot usage metrics reports](https://github.blog/changelog/2026-07-02-improved-accuracy-and-coverage-in-copilot-usage-metrics-reports)
*Jul 2, 2026*

We've made three improvements to the Copilot usage metrics API that make its reports more complete and accurate: GitHub Copilot CLI now reports suggested lines of code, users seen only through server-side telemetry now have their IDE identified, and AI credit consumption is now attributed more completely. GitHub Copilot CLI now reports suggested lines of code.

### [Copilot agent session streaming is now in public preview](https://github.blog/changelog/2026-07-02-copilot-agent-session-streaming-is-now-in-public-preview)
*Jul 2, 2026*

You can choose to access this data via a streaming endpoint or the REST API. To enable this, go to the Copilot subpage in AI Controls and select Enable everywhere for both "Copilot Usage Records Streaming" and "Copilot Usage Records API". You can initiate a streaming connection to an event collector or SIEM tool of your choice from your audit log settings.

### [Issue fields are now generally available](https://github.blog/changelog/2026-07-02-issue-fields-are-now-generally-available)
*Jul 2, 2026*

Issue fields are now generally available for all GitHub organizations on Free, Team, Enterprise, and GitHub Enterprise Cloud with data residency plans and will ship in GitHub Enterprise Server 3.23. Issue fields bring structured, typed metadata to issues, making it easy to track priority, effort, dates, and custom values consistently across your organization.

### [Copilot CLI no longer needs a personal access token in GitHub Actions](https://github.blog/changelog/2026-07-02-copilot-cli-no-longer-needs-a-personal-access-token-in-github-actions)
*Jul 2, 2026*

You can now run GitHub Copilot CLI in GitHub Actions using the built-in GITHUB_TOKEN. This means that you no longer need to create and store a personal access token (PAT), eliminating the operational and security risks of managing long-lived PATs for automations at scale.

---

## Last 30 Days

### [Upcoming deprecation of Gemini 2.5 Pro and Gemini 3 Flash](https://github.blog/changelog/2026-07-02-upcoming-deprecation-of-gemini-2-5-pro-and-gemini-3-flash)
*Jul 2, 2026*

Copilot Enterprise administrators may need to enable access to the alternative models through their model policies in Copilot settings. As an administrator, you can verify availability by checking your individual Copilot settings and confirming that the policy is enabled for the specific model. Once enabled, you'll see the model in the Copilot Chat model selector in VS Code and on github.com.

### [Cost centers now support AI credit pools](https://github.blog/changelog/2026-07-02-cost-centers-now-support-included-usage-caps)
*Jul 2, 2026*

You can now cap how much of your enterprise's monthly included AI credits a cost center can use. This is available through the REST API today. Management in the cost center settings UI is coming soon.

### [Secret scanning public monitoring for enterprises](https://github.blog/changelog/2026-07-01-secret-scanning-public-monitoring-for-enterprises)
*Jul 1, 2026*

GitHub is committed to empowering the developer community by helping organizations recognize and address the risks of secret leaks wherever they happen. We believe every enterprise should know the moment its secrets leak in public, no matter where it happens on GitHub. That's why public monitoring is now in public preview for enterprises with GitHub Secret Protection, at no additional cost.

### [Enterprise managed-settings.json is generally available](https://github.blog/changelog/2026-07-01-enterprise-managed-settings-json-is-generally-available)
*Jul 1, 2026*

GitHub Enterprise Cloud customers can configure AI standards through a managed-settings.json file maintained in a .github-private repository in a selected organization. This allows the enterprise to define new governance and extensibility flows that apply to Copilot clients such as VS Code or Copilot CLI.

### [Kimi K2.7 Code is generally available in GitHub Copilot](https://github.blog/changelog/2026-07-01-kimi-k2-7-is-now-available-in-github-copilot)
*Jul 1, 2026*

Kimi K2.7 Code, an open-weight model, is now generally available in GitHub Copilot. This is the first open-weight model offered as a selectable option in the Copilot model picker, giving you more choice and a lower-cost option for your coding workflows. Kimi K2.7 Code is hosted by GitHub on Microsoft Azure.

### [New C++ language server config skill for Copilot CLI](https://github.blog/changelog/2026-07-01-new-c-language-server-config-skill-for-copilot-cli)
*Jul 1, 2026*

The Microsoft C++ Language Server is now available as a plugin on the Copilot Plugins marketplace. It includes a new built-in setup skill that helps automate project setup, making it easier to generate and maintain the compile_commands.json file the language server needs to understand your code.

### [GitHub Models is being fully retired on July 30, 2026](https://github.blog/changelog/2026-07-01-github-models-is-being-fully-retired-on-july-30-2026)
*Jul 1, 2026*

In June, we announced that we are retiring GitHub Models and closed it to new customers. We're now sharing the timeline for the next step: GitHub Models will be fully retired on July 30, 2026. After that date, GitHub Models—including the playground, model catalog, inference API, and bring your own key (BYOK)—will no longer be available to any customer.

### [Enterprises can default to auto model selection](https://github.blog/changelog/2026-07-01-enterprises-can-default-to-auto-model-selection)
*Jul 1, 2026*

Enterprise administrators can now set model to auto in the enterprise managed-settings.json to make Copilot auto model selection the default for new conversations. Add auto to .github-private/.github/copilot/managed-settings.json in your source organization for enterprise governance so new conversations start with Copilot auto model selection by default.

### [Copilot vision is generally available](https://github.blog/changelog/2026-07-01-copilot-vision-is-generally-available)
*Jul 1, 2026*

Copilot vision is now generally available. You can attach images and PDFs directly to your chat prompts so Copilot can reason about what it sees alongside your code.

### [GitHub Copilot Agent is now available in JetBrains AI Assistant](https://www.youtube.com/watch?v=JsRhoZJAIF4)
*Jun 30, 2026*

JetBrains fans, you can now add GitHub Copilot natively via AI Assistant into your favorite IDE. Using the new agent client protocol support, integrating Copilot takes just a few clicks from the AI...

---

## Older Updates

See [CHANGELOG.md](CHANGELOG.md) for the full historical timeline.

---

_All dates are complete and sorted newest first. For a full list of updates, see [CHANGELOG.md](CHANGELOG.md)._
