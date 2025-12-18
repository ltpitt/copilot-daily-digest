# GitHub Copilot Commands & Shortcuts

> Quick reference for slash commands, keyboard shortcuts, and chat variables

**Last Updated**: December 18, 2025

---

## Table of Contents

- [Slash Commands](#slash-commands)
- [Keyboard Shortcuts](#keyboard-shortcuts)
- [Chat Variables](#chat-variables)
- [Chat Participants](#chat-participants)

---

## Slash Commands

Type `/` in the Copilot Chat prompt box to see all available commands.

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
| `/new` | Scaffold new projects or files | `/new React component` |
| `/newNotebook` | Create a new Jupyter notebook | `/newNotebook data analysis` |
| `/simplify` | Simplify complex code | `/simplify this regex` |

**Usage tips**:
- Slash commands work in Copilot Chat (not inline suggestions)
- Combine commands with specific context using `#file` or `#selection`
- Commands can be used with chat participants like `@workspace /tests`

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
| Trigger inline suggest | `Alt+\` | `Opt+\` |
| Accept word | `Ctrl+→` | `Cmd+→` |
| Open Copilot Edits | `Ctrl+Shift+I` | `Cmd+Shift+I` |

### JetBrains IDEs

| Action | Windows/Linux | Mac |
|--------|---------------|-----|
| Open Copilot Chat | `Ctrl+Shift+A` → "Copilot" | `Cmd+Shift+A` → "Copilot" |
| Accept suggestion | `Tab` | `Tab` |
| Dismiss suggestion | `Esc` | `Esc` |
| Show next suggestion | `Alt+]` | `Opt+]` |
| Show previous suggestion | `Alt+[` | `Opt+[` |
| Trigger inline suggest | `Alt+\` | `Opt+\` |

### Visual Studio

| Action | Windows |
|--------|---------|
| Open Copilot Chat | `Alt+/` |
| Accept suggestion | `Tab` |
| Dismiss suggestion | `Esc` |
| Show next suggestion | `Alt+.` |
| Show previous suggestion | `Alt+,` |
| Accept suggestion word | `Ctrl+→` |

**Pro tip**: You can customize keyboard shortcuts in your IDE settings. Search for "Copilot" in your IDE's keyboard shortcut preferences.

---

## Chat Variables

Type `#` in the Copilot Chat prompt box to see available variables.

| Variable | Context | Example |
|----------|---------|---------|
| `#selection` | Currently selected code | `#selection explain this function` |
| `#file` | Current file | `#file add error handling` |
| `#editor` | Active editor content | `#editor refactor for readability` |
| `#codebase` | Entire repository | `#codebase find all authentication logic` |
| `#web` | Web search results | `@github #web latest Python security best practices` |
| `#terminalLastCommand` | Last terminal command | `#terminalLastCommand explain this error` |
| `#terminalSelection` | Selected terminal output | `#terminalSelection what does this mean` |

**When to use variables**:
- `#selection` - When you want to reference specific highlighted code
- `#file` - When the question is about the entire current file
- `#codebase` - When you need context from multiple files
- `#web` - When you need up-to-date information from the internet
- `#terminalLastCommand` - For debugging command-line errors

---

## Chat Participants

Type `@` in the Copilot Chat prompt box to see available participants.

| Participant | Expertise | When to Use |
|-------------|-----------|-------------|
| `@workspace` | Your codebase | Questions about your project structure, dependencies, or architecture |
| `@github` | GitHub-specific features | Repository operations, issues, pull requests, web search |
| `@terminal` | Command line | Shell commands, CLI tools, environment setup |
| `@vscode` | VS Code | Editor features, settings, extensions (VS Code only) |

**Example usage**:

```
@workspace /explain how authentication works in this project

@github #web What is the latest LTS version of Node.js?

@terminal how do I list all Docker containers

@vscode how do I change my color theme
```

**Pro tip**: Copilot can automatically infer which participant to use based on your natural language prompt, so you don't always need to specify one explicitly.

---

## Common Workflows

### Code Explanation

```
# Select code, then:
/explain

# Or with context:
#selection /explain how this algorithm works
```

### Generating Tests

```
# With file context:
@workspace /tests for the UserService class

# With specific selection:
#selection /tests with edge cases
```

### Fixing Bugs

```
# For selected code:
#selection /fix this null pointer exception

# For terminal errors:
#terminalLastCommand /fix
```

### Documentation

```
# Document current file:
#file /doc with examples

# Document selection:
#selection /doc in JSDoc format
```

### Code Optimization

```
# Optimize selected code:
#selection /optimize for performance

# Refactor:
#selection /simplify and make more readable
```

---

## Advanced Tips

### Combining Multiple Features

```
# Use participant + variable + command:
@workspace #codebase /explain how the payment flow works

# Chain context:
#file #selection /tests including integration tests
```

### Custom Instructions

- Create `.github/copilot-instructions.md` in your repository
- Add project-specific guidelines and context
- Copilot automatically includes these in all prompts

### Model Selection

- Use the model picker to choose between GPT-5.2, Claude, Gemini, etc.
- Different models excel at different tasks
- Auto-selection available in VS Code

### Iterating on Responses

If you don't get the desired result:
1. Rephrase your prompt with more specific requirements
2. Add examples of expected input/output
3. Break complex requests into smaller steps
4. Use different variables to provide more context

---

*For comprehensive documentation, see [REFERENCE.md](REFERENCE.md)*
