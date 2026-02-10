# Commands Reference

> Quick reference for GitHub Copilot slash commands, shortcuts, and variables

**Last Updated**: February 7, 2026

---

## Slash Commands

Use slash commands in Copilot Chat for specific tasks.

| Command | Description | Example |
|---------|-------------|---------|
| `/explain` | Explain selected code | Select code, then `/explain` |
| `/fix` | Suggest fixes for problems | `/fix this bug` |
| `/tests` | Generate unit tests | `/tests for this function` |
| `/doc` | Add documentation comments | `/doc for this class` |
| `/simplify` | Simplify complex code | `/simplify this logic` |
| `/review` | Review code for improvements | `/review security issues` |
| `/new` | Scaffold new code | `/new React component` |
| `/terminal` | Explain terminal commands | `/terminal git rebase` |

---

## Keyboard Shortcuts

### Visual Studio Code

| Action | Windows/Linux | macOS |
|--------|---------------|-------|
| Trigger inline suggestion | `Tab` | `Tab` |
| Dismiss inline suggestion | `Esc` | `Esc` |
| Next suggestion | `Alt+]` | `Option+]` |
| Previous suggestion | `Alt+[` | `Option+[` |
| Show all suggestions | `Ctrl+Enter` | `Cmd+Enter` |
| Open Copilot Chat | `Ctrl+Shift+I` | `Cmd+Shift+I` |
| Accept word | `Ctrl+→` | `Cmd+→` |
| Accept line | `Ctrl+End` | `Cmd+End` |

### Visual Studio

| Action | Shortcut |
|--------|----------|
| Trigger inline suggestion | `Tab` |
| Dismiss inline suggestion | `Esc` |
| Next suggestion | `Alt+.` |
| Previous suggestion | `Alt+,` |
| Show all suggestions | `Ctrl+Alt+Enter` |
| Open Copilot Chat | `Alt+/` |

### JetBrains IDEs

| Action | Shortcut |
|--------|----------|
| Trigger inline suggestion | `Tab` |
| Dismiss inline suggestion | `Esc` |
| Next suggestion | `Alt+]` |
| Previous suggestion | `Alt+[` |
| Open Copilot panel | `Alt+Shift+O` |

---

## Chat Variables

Use variables in Copilot Chat to reference specific context.

| Variable | Description | Example |
|----------|-------------|---------|
| `#file` | Reference a specific file | `#file:package.json explain dependencies` |
| `#selection` | Reference selected code | `#selection fix this error` |
| `#terminalLastCommand` | Reference last terminal command | `#terminalLastCommand what went wrong?` |
| `#terminalSelection` | Reference selected terminal output | `#terminalSelection explain this error` |
| `#codebase` | Reference entire codebase | `#codebase where is authentication handled?` |
| `#git` | Reference git context | `#git summarize recent changes` |

---

## Chat Participants

Use participants to route requests to specialized agents.

| Participant | Purpose | Example |
|-------------|---------|---------|
| `@workspace` | Workspace-aware questions | `@workspace how do I add a new API route?` |
| `@vscode` | VS Code questions | `@vscode how do I change the theme?` |
| `@terminal` | Terminal and shell help | `@terminal how do I find large files?` |
| `@github` | GitHub-specific questions | `@github create a pull request` |

---

## CLI Commands

GitHub Copilot CLI provides terminal assistance.

### Installation

```bash
# Install via GitHub CLI
gh extension install github/gh-copilot

# Or install directly
npm install -g @githubnext/github-copilot-cli
```

### Usage

```bash
# Get help with commands
gh copilot suggest "find all large files"

# Explain commands
gh copilot explain "git rebase -i HEAD~3"

# Interactive mode
gh copilot
```

### Common Patterns

```bash
# Git operations
gh copilot suggest "undo last commit"
gh copilot suggest "list all branches"

# File operations
gh copilot suggest "find files modified in last week"
gh copilot suggest "delete node_modules recursively"

# System operations
gh copilot suggest "check disk space"
gh copilot suggest "find process using port 3000"
```

---

## Model Selection

Choose different AI models for different tasks.

| Model | Best For | When to Use |
|-------|----------|-------------|
| **GPT-5.2** | General coding | Default for most tasks |
| **GPT-5.1 Codex Max** | Large refactoring | Complex multi-file changes |
| **Claude Opus 4.6** | Agentic workflows | Planning and tool-heavy tasks |
| **Gemini 3 Pro** | Performance | Speed-critical operations |

Access model picker:
- VS Code: Click model name in Copilot Chat
- Visual Studio: Settings → Copilot → Models
- GitHub.com: Chat settings

---

## Tips & Tricks

### Be Specific
```
❌ "make it better"
✅ "refactor this function to use async/await and add error handling"
```

### Provide Context
```
❌ "create a form"
✅ "create a React form component with validation using React Hook Form"
```

### Use Examples
```
"Create a function like getUserById() but for posts, called getPostById()"
```

### Iterate
```
1. "create a login form"
2. "add email validation"
3. "add password strength indicator"
4. "add remember me checkbox"
```

---

## Additional Resources

- [Copilot Documentation](https://docs.github.com/copilot)
- [Keyboard Shortcuts Guide](https://code.visualstudio.com/docs/copilot/copilot-vscode-features#_keyboard-shortcuts)
- [Chat Reference](https://docs.github.com/copilot/using-github-copilot/asking-github-copilot-questions-in-your-ide)
- [CLI Documentation](https://docs.github.com/copilot/github-copilot-in-the-cli)

---

_Commands and shortcuts are updated regularly. Check your IDE's Copilot documentation for the latest._
