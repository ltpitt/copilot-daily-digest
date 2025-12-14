# GitHub Copilot Commands & Shortcuts

> Quick reference for slash commands, keyboard shortcuts, and chat variables

**Last Updated**: 2025-12-14

---

## 📋 Table of Contents

- [Slash Commands](#slash-commands)
- [Keyboard Shortcuts](#keyboard-shortcuts)
- [Chat Variables](#chat-variables)
- [Chat Participants](#chat-participants)
- [Agent Mode](#agent-mode)

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
| `/new` | Scaffold a new project or file | `/new Express API with TypeScript` |
| `/newNotebook` | Create a new Jupyter notebook | `/newNotebook for data analysis` |
| `/simplify` | Simplify complex code | `/simplify this nested loop` |

**Usage**:
```
/explain the authentication flow in this file
```

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
| Trigger suggestions | `Alt+\` | `Opt+\` |
| Open Copilot | `Ctrl+Shift+P` → "Copilot" | `Cmd+Shift+P` → "Copilot" |

### JetBrains IDEs

| Action | Windows/Linux | Mac |
|--------|---------------|-----|
| Open Copilot Chat | `Alt+C` | `Cmd+Shift+A` → "Copilot Chat" |
| Accept suggestion | `Tab` | `Tab` |
| Dismiss suggestion | `Esc` | `Esc` |
| Show next suggestion | `Alt+]` | `Opt+]` |
| Show previous suggestion | `Alt+[` | `Opt+[` |
| Trigger suggestions | `Alt+\` | `Opt+\` |

### Visual Studio

| Action | Windows |
|--------|---------|
| Open Copilot Chat | `Alt+/` or View → GitHub Copilot Chat |
| Accept suggestion | `Tab` |
| Dismiss suggestion | `Esc` |
| Show next suggestion | `Alt+.` |
| Show previous suggestion | `Alt+,` |

### Eclipse

| Action | Windows/Linux | Mac |
|--------|---------------|-----|
| Open Copilot Chat | `Ctrl+Shift+C` | `Cmd+Shift+C` |
| Accept suggestion | `Tab` | `Tab` |
| Dismiss suggestion | `Esc` | `Esc` |

### Xcode

| Action | Mac |
|--------|-----|
| Open Copilot | Window → GitHub Copilot |
| Accept suggestion | `Tab` |
| Dismiss suggestion | `Esc` |

---

## Chat Variables

Type `#` in the chat prompt box to see available variables.

| Variable | Context | Example |
|----------|---------|---------|
| `#selection` | Currently selected code | `#selection explain this function` |
| `#file` | Current file | `#file add error handling` |
| `#editor` | Active editor content | `#editor refactor for readability` |
| `#web` | Web search results (with @github) | `@github #web latest Python security best practices` |
| `#codebase` | Entire repository | `#codebase find all authentication logic` |
| `#terminalLastCommand` | Last terminal command output | `#terminalLastCommand explain this error` |
| `#terminalSelection` | Selected terminal output | `#terminalSelection why did this fail` |

**Usage**:
```
#selection optimize this function for large datasets
```

```
@workspace #codebase where is the database connection configured?
```

---

## Chat Participants

Type `@` in the chat prompt box to see available participants.

| Participant | Expertise | When to Use |
|-------------|-----------|-------------|
| `@workspace` | Your codebase | Questions about your project structure, dependencies, or architecture |
| `@github` | GitHub-specific features | Repository operations, issues, pull requests, web search |
| `@terminal` | Command line | Shell commands, CLI tools, environment setup |
| `@vscode` | VS Code | Editor features, settings, extensions |

**Usage**:
```
@workspace Where is the authentication logic located?
```

```
@github #web What are the latest best practices for React hooks?
```

```
@terminal How do I list all files modified in the last 7 days?
```

---

## Agent Mode

Agent Mode enables Copilot to autonomously edit your code for multi-step tasks.

### Enabling Agent Mode

**VS Code**:
1. Open Settings (`Ctrl+,` or `Cmd+,`)
2. Search for "Copilot Agent"
3. Enable "Agent Mode"

**JetBrains**:
1. Settings → Tools → GitHub Copilot
2. Enable "Coding Agent"

### Using Agent Mode

**Activate**: Type your task in Copilot Chat:
```
Add Redis caching to userSessionService with 30s TTL
```

**What Copilot Does**:
1. Determines which files to modify
2. Proposes code changes
3. Suggests terminal commands if needed
4. Iterates to fix issues
5. Can open a PR when complete

**Review & Approve**:
- Review proposed changes in the diff view
- Approve or reject terminal commands
- Copilot iterates based on your feedback

### Agent Mode Commands

| Command | Description |
|---------|-------------|
| `/agent` | Start agent mode with a task |
| `/stop` | Stop current agent task |
| `/review` | Review agent's proposed changes |

---

## Plan Mode

Plan Mode helps Copilot understand large, complex tasks before execution.

**Usage**:
```
@workspace /plan Add user authentication with JWT tokens
```

**What It Does**:
- Breaks down complex tasks into steps
- Identifies files that need changes
- Proposes an implementation plan
- You can approve or modify the plan before execution

---

## Copilot Edits

Multi-file editing with iterative refinement.

**Open Copilot Edits**:
- VS Code: `Ctrl+Shift+I` (Windows/Linux) or `Cmd+Shift+I` (Mac)
- Or use Command Palette: "Copilot: Open Edits"

**Usage**:
1. Select files to edit (or let Copilot choose)
2. Describe your changes
3. Copilot proposes edits across multiple files
4. Review and refine iteratively

**Example**:
```
Refactor the authentication module to use async/await instead of promises
```

---

## Model Context Protocol (MCP)

MCP servers extend Copilot's capabilities with external tools.

**Using MCP Servers**:
```
@mcp-server-name perform task
```

**Example with GitHub MCP**:
```
@github-mcp list all open issues assigned to me
```

**Configuration**:
- MCP servers are configured per-IDE
- See IDE-specific documentation for setup

---

## Tips & Tricks

### Combining Features

**Use variables + participants + commands**:
```
@workspace #selection /optimize for better performance
```

**Chain requests**:
```
/tests for the userService module
```
Then:
```
@workspace #file update the tests to use async/await
```

### Best Practices

1. **Be specific**: Instead of `/fix`, try `/fix the null pointer error on line 42`
2. **Provide context**: Use `#file`, `#selection`, or `@workspace` to give Copilot context
3. **Iterate**: Start with a broad request, then refine with follow-ups
4. **Use examples**: Show Copilot what you want with example inputs/outputs

---

## Quick Reference Card

```
CHAT COMMANDS          SHORTCUTS (VS Code)     VARIABLES
/explain               Ctrl+I  - Inline chat   #selection
/fix                   Ctrl+Alt+I - Chat view  #file
/tests                 Tab - Accept            #editor
/doc                   Esc - Dismiss           #codebase
/optimize              Alt+] - Next            #web
                       Alt+[ - Previous        

PARTICIPANTS
@workspace - Your code
@github - GitHub features
@terminal - Command line
@vscode - VS Code help
```

---

*For comprehensive documentation, see [REFERENCE.md](REFERENCE.md)*
