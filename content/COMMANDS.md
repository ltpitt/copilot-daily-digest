# GitHub Copilot Commands & Shortcuts

> Quick reference for slash commands, keyboard shortcuts, and chat variables

**Last Updated**: January 25, 2026

---

## Table of Contents

- [Slash Commands](#slash-commands)
- [Copilot CLI](#copilot-cli)
- [Copilot SDK](#copilot-sdk)
- [Keyboard Shortcuts](#keyboard-shortcuts)
- [Chat Variables](#chat-variables)
- [Chat Participants](#chat-participants)

---

## Slash Commands

Type `/` in the chat prompt box to see all available commands.

| Command | Description | Example |
|---------|-------------|---------|
| `/clear` | Clear the chat history | `/clear` |
| `/explain` | Explain selected code or concept | `/explain how async/await works` |
| `/fix` | Suggest fixes for problems in code | `/fix this bug` |
| `/generate` | Generate code based on requirements | `/generate a REST API endpoint` |
| `/help` | Get help using Copilot Chat | `/help` |
| `/optimize` | Analyze and improve code performance | `/optimize this function` |
| `/tests` | Generate unit tests | `/tests for authentication module` |
| `/doc` | Generate documentation | `/doc this API` |
| `/new` | Scaffold new code or projects | `/new Express.js server with TypeScript` |
| `/newNotebook` | Create a new Jupyter notebook | `/newNotebook data analysis` |
| `/terminal` | Help with terminal commands | `/terminal find all .log files` |

**Usage Tips**:
- Combine slash commands with context: `/tests` with a function selected
- Chain slash commands in conversation: `/generate` → `/tests` → `/doc`
- Use `/explain` to understand Copilot's own suggestions

---

## Copilot CLI

**NEW (Jan 2026)**: GitHub Copilot CLI brings AI assistance directly to your terminal.

### Installation

```bash
# Install via GitHub CLI (recommended)
gh copilot

# The command will prompt you to install if not already installed
```

### CLI Slash Commands

Use these slash commands in GitHub Copilot CLI for terminal-based workflows:

| Command | Description | Use Case |
|---------|-------------|----------|
| `/test` | Run tests for the current context | Quickly execute test suites |
| `/fix` | Suggest fixes for errors or issues | Debug failing tests or code |
| `/explain` | Explain terminal output or commands | Understand error messages |
| `/suggest` | Suggest commands for a task | Get CLI recommendations |
| `/plan` | Plan multi-step tasks before executing | Complex workflows requiring thought |

**Key Features**:
- **Planning mode**: Think through tasks before execution
- **Reasoning models**: Advanced AI models for complex terminal tasks
- **Workflow steering**: Guide the AI as tasks progress
- **Context awareness**: Understands your project and terminal history

**Learn More**:
- [Copilot CLI cheat sheet](https://github.blog/ai-and-ml/github-copilot/a-cheat-sheet-to-slash-commands-in-github-copilot-cli/)
- [Installation guide](https://github.blog/changelog/2026-01-21-install-and-use-github-copilot-cli-directly-from-the-github-cli)
- [Planning workflows](https://github.blog/changelog/2026-01-21-github-copilot-cli-plan-before-you-build-steer-as-you-go)

---

## Copilot SDK

**NEW (Jan 2026)**: Build AI agents into any application with the GitHub Copilot SDK (Technical Preview).

### Core Capabilities

The SDK provides a programmable layer for integrating agentic AI into your applications:

| Capability | Description | Use Case |
|------------|-------------|----------|
| **Planning** | Autonomous task planning with reasoning | Multi-step workflows |
| **Tool Invocation** | Execute functions and API calls | Custom integrations |
| **File Editing** | Modify code across multiple files | Code generation tools |
| **Command Execution** | Run shell commands safely | Build/test automation |

### Quick Start

```javascript
// Example: Initialize Copilot SDK
import { CopilotSDK } from '@github/copilot-sdk';

const agent = new CopilotSDK({
  apiKey: process.env.COPILOT_API_KEY
});

// Plan and execute a task
const result = await agent.plan('Create a REST API endpoint for user authentication');
await agent.execute(result.plan);
```

### SDK Resources

- [SDK announcement](https://github.blog/news-insights/company-news/build-an-agent-into-any-app-with-the-github-copilot-sdk/)
- [Watch: SDK overview](https://www.youtube.com/watch?v=6yzGew8wA4A)
- [Watch: Integration guide](https://www.youtube.com/watch?v=hLzIAWIezBg)
- Documentation: Coming soon to docs.github.com

**Status**: Technical Preview (Jan 2026)

---

## Keyboard Shortcuts

### VS Code

| Action | Windows/Linux | Mac |
|--------|---------------|-----|
| Open chat view | `Ctrl+Alt+I` | `Cmd+Shift+I` |
| Quick chat | `Ctrl+Shift+Alt+L` | `Shift+Opt+Cmd+L` |
| Inline chat | `Ctrl+I` | `Cmd+I` |
| Accept suggestion | `Tab` | `Tab` |
| Dismiss suggestion | `Esc` | `Esc` |
| Show next suggestion | `Alt+]` | `Opt+]` |
| Show previous suggestion | `Alt+[` | `Opt+[` |
| Accept word | `Ctrl+→` | `Cmd+→` |
| Open Copilot Edits | `Ctrl+Shift+I` | `Cmd+Shift+I` |

### JetBrains IDEs

| Action | Windows/Linux | Mac |
|--------|---------------|-----|
| Open chat panel | `Alt+C` | `Opt+C` |
| Inline chat | `Ctrl+\` | `Cmd+\` |
| Accept suggestion | `Tab` | `Tab` |
| Dismiss suggestion | `Esc` | `Esc` |
| Show next suggestion | `Alt+]` | `Opt+]` |
| Show previous suggestion | `Alt+[` | `Opt+[` |

### Visual Studio

| Action | Shortcut |
|--------|----------|
| Open chat window | `Ctrl+/` or `Alt+/` |
| Inline chat | `Ctrl+/` (in editor) |
| Accept suggestion | `Tab` |
| Dismiss suggestion | `Esc` |
| Next suggestion | `Alt+]` |
| Previous suggestion | `Alt+[` |

### Eclipse

| Action | Shortcut |
|--------|----------|
| Open Copilot | `Alt+C` |
| Accept suggestion | `Tab` |
| Dismiss suggestion | `Esc` |

### Xcode

| Action | Shortcut |
|--------|----------|
| Open Copilot Chat | `Cmd+Shift+C` |
| Accept suggestion | `Tab` |
| Dismiss suggestion | `Esc` |

**Pro Tip**: Learn the shortcuts for your primary IDE to maximize flow state. Muscle memory with `Tab` (accept) and `Esc` (dismiss) is essential.

---

## Chat Variables

Type `#` in the chat prompt box to see available variables.

| Variable | Context | Example |
|----------|---------|---------|
| `#selection` | Currently selected code | `#selection explain this function` |
| `#file` | Current file | `#file add error handling` |
| `#editor` | Active editor content | `#editor refactor for readability` |
| `#web` | Web search results | `@github #web latest Python security best practices` |
| `#codebase` | Entire repository | `#codebase find all authentication logic` |
| `#terminalLastCommand` | Last terminal command | `#terminalLastCommand what went wrong?` |
| `#terminalSelection` | Selected terminal output | `#terminalSelection explain this error` |

**Usage Examples**:

**Explain selected code**:
```
Select code → #selection explain how this handles edge cases
```

**Add features to current file**:
```
#file add input validation with error messages
```

**Repository-wide refactoring**:
```
#codebase migrate all API calls from axios to fetch
```

**Debug terminal errors**:
```
#terminalLastCommand why did this fail?
```

---

## Chat Participants

Type `@` in the chat prompt box to see available participants.

| Participant | Expertise | When to Use |
|-------------|-----------|-------------|
| `@workspace` | Your codebase | Questions about project structure, dependencies, architecture |
| `@github` | GitHub features | Repository operations, issues, pull requests, web search |
| `@terminal` | Command line | Shell commands, CLI tools, environment setup |
| `@vscode` | VS Code | Editor features, settings, extensions (VS Code only) |

**Participant Examples**:

**@workspace - Codebase Questions**:
```
@workspace where is the user authentication logic?
@workspace explain the database schema
@workspace what are all the API endpoints?
```

**@github - GitHub Operations**:
```
@github create an issue for this bug
@github #web what's new in React 19?
@github find PRs related to authentication
```

**@terminal - Command Line Help**:
```
@terminal how do I find all files modified today?
@terminal convert this curl command to Python requests
@terminal explain what this bash script does
```

**@vscode - Editor Features**:
```
@vscode how do I set up debugging for Node.js?
@vscode configure prettier for this project
@vscode keyboard shortcut for multi-cursor editing
```

---

## Chat Modes

Switch between modes using the agents dropdown in chat view.

| Mode | Purpose | When to Use |
|------|---------|-------------|
| **Ask** | Answer questions | Understanding code, explanations, general help |
| **Edit** | Controlled multi-file edits | Specific updates to defined files |
| **Agent** | Autonomous task completion | Complex multi-step tasks, scaffolding |
| **Plan** | Create implementation plans | Large features requiring detailed planning |

**Mode Selection Tips**:
- Start with **Ask** for exploration and learning
- Use **Edit** when you know exactly which files to change
- Use **Agent** for complex tasks like "add Redis caching"
- Use **Plan** for large features to ensure all requirements are covered

---

## Advanced Features

### Model Context Protocol (MCP) Servers

Extend Copilot with external tools and services:
- Database connections for schema queries
- API documentation for external services
- Custom tooling for your tech stack

**Learn more**: [Using MCP servers](https://docs.github.com/en/copilot/how-tos/chat-with-copilot/chat-in-ide#using-model-context-protocol-mcp-servers)

### GitHub Skills

Use `@github` with natural language to invoke skills:
```
@github search the web for latest Next.js features
@github find issues labeled "bug" in this repo
@github what are the recent commits to main?
```

### Custom Instructions

Add repository-specific context with `.github/copilot-instructions.md`:
- Coding standards
- Architecture patterns
- Technology stack preferences
- Common pitfalls to avoid

**Learn more**: [Custom Instructions](https://docs.github.com/en/copilot/customizing-copilot/adding-custom-instructions-for-github-copilot)

---

## Quick Tips

### Maximize Inline Suggestions
1. Keep relevant files open
2. Write descriptive comments above code
3. Use consistent naming conventions
4. Press `Alt+]` / `Opt+]` to cycle through suggestions

### Effective Chat Usage
1. Be specific about requirements
2. Provide examples of inputs/outputs
3. Use slash commands for common tasks
4. Include relevant context with # variables

### Workflow Integration
1. Learn keyboard shortcuts for your IDE
2. Use chat participants for specific domains
3. Experiment with different AI models
4. Iterate on responses with follow-up questions

---

*For comprehensive documentation, see [REFERENCE.md](REFERENCE.md)*
