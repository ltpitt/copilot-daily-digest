# GitHub Copilot Commands & Shortcuts

> Quick reference for slash commands, keyboard shortcuts, and chat variables

**Last Updated**: 2026-01-19

---

## 📋 Table of Contents

- [Slash Commands](#slash-commands)
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
| `/new` | Scaffold new code or projects | `/new Express.js REST API` |
| `/review` | Review code for issues | `/review for security vulnerabilities` |

**Note**: Available commands may vary by IDE. Type `/` in your chat to see all options for your environment.

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
| Trigger inline suggestion | `Alt+\` | `Opt+\` |
| Open completions panel | `Ctrl+Enter` | `Cmd+Enter` |

### JetBrains IDEs

| Action | Windows/Linux | Mac |
|--------|---------------|-----|
| Open chat | `Alt+C` | `Opt+C` |
| Inline chat | `Ctrl+Shift+Alt+L` | `Cmd+Shift+Opt+L` |
| Accept suggestion | `Tab` | `Tab` |
| Dismiss suggestion | `Esc` | `Esc` |
| Next suggestion | `Alt+]` | `Opt+]` |
| Previous suggestion | `Alt+[` | `Opt+[` |

### Visual Studio

| Action | Windows |
|--------|---------|
| Open chat | `Alt+/` |
| Inline chat | `Ctrl+I` |
| Accept suggestion | `Tab` |
| Dismiss suggestion | `Esc` |
| Next suggestion | `Alt+.` |
| Previous suggestion | `Alt+,` |

**Tip**: Keyboard shortcuts can be customized in your IDE settings.

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
| `#terminalLastCommand` | Last terminal command | `#terminalLastCommand why did this fail?` |
| `#terminalSelection` | Selected terminal text | `#terminalSelection explain this error` |

**Context is key**: Variables help Copilot understand what code you're referring to without copy-pasting.

---

## Chat Participants

Type `@` in the chat prompt box to see available participants.

| Participant | Expertise | When to Use |
|-------------|-----------|-------------|
| `@workspace` | Your codebase | Questions about project structure, dependencies, or architecture |
| `@github` | GitHub features | Repository operations, issues, pull requests, web search |
| `@terminal` | Command line | Shell commands, CLI tools, environment setup |
| `@vscode` | VS Code | Editor features, settings, extensions (VS Code only) |

### Using Participants Effectively

**Example prompts**:
- `@workspace where is the user authentication implemented?`
- `@github search for similar issues in this repository`
- `@terminal how do I install Python 3.11 on Ubuntu?`
- `@vscode how do I configure auto-save?`

**Tips**:
- Copilot can automatically infer the right participant based on your question
- Explicitly using participants helps when context is ambiguous
- Combine participants with variables: `@workspace #file explain this code`

---

## Advanced Features

### Copilot Edits (VS Code)

Multi-file editing mode for coordinated changes:
- Edit multiple files simultaneously
- Copilot maintains context across files
- Review all changes before accepting

**Keyboard shortcut**: `Ctrl+Shift+I` (Windows/Linux) or `Cmd+Shift+I` (Mac)

### Agent Mode (Select IDEs)

Autonomous multi-step task execution:
- Describe a complex task in natural language
- Copilot plans and executes across multiple files
- Review the plan before execution

**When to use**: Refactoring, scaffolding, repetitive tasks

### Model Selection

Choose different AI models for different tasks:
- GPT-5.2 Codex: Best for code generation
- Claude Opus 4.5: Great for explanations
- Gemini 3 Flash: Fast responses

**How**: Click model picker in chat interface (availability varies by subscription)

---

## Quick Tips

1. **Start with slash commands** - They're shortcuts for common tasks
2. **Use variables** - Help Copilot understand context without copying code
3. **Try different models** - Some models excel at specific tasks
4. **Combine features** - Use participants + variables + commands together
5. **Iterate prompts** - If first response isn't perfect, refine and try again

---

*For comprehensive documentation, see [REFERENCE.md](REFERENCE.md)*
