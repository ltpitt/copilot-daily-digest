# GitHub Copilot Commands & Shortcuts

> Quick reference for slash commands, keyboard shortcuts, and chat features

---

## Slash Commands

Slash commands help you accomplish common tasks quickly. Type `/` in Copilot Chat to see all available commands.

| Command | Description | Example |
|---------|-------------|---------|
| `/explain` | Explain selected code or concepts | `/explain What does this regex do?` |
| `/fix` | Suggest fixes for problems in code | `/fix Why is this function throwing errors?` |
| `/tests` | Generate unit tests for selected code | `/tests Generate tests with edge cases` |
| `/doc` | Add documentation comments | `/doc Add JSDoc comments to this function` |
| `/clear` | Clear the chat conversation | `/clear` |
| `/help` | Get help with Copilot features | `/help` |

### Using Slash Commands

**VS Code / JetBrains**: Type `/` in the chat prompt box, then select from the dropdown or continue typing.

**Example Workflow**:
1. Select a function
2. Open Copilot Chat (`Ctrl+I` or `Cmd+I`)
3. Type `/tests` and press Enter
4. Copilot generates comprehensive unit tests

---

## Chat Participants

Chat participants scope your prompt to specific domains. Type `@` in chat to see available participants.

| Participant | Purpose | Example |
|-------------|---------|---------|
| `@workspace` | Ask about your entire codebase | `@workspace Where is user authentication handled?` |
| `@terminal` | Get help with shell commands | `@terminal How do I recursively delete .log files?` |
| `@vscode` | VS Code settings and features | `@vscode How do I enable auto-save?` |

**Note**: Copilot can often infer the right participant automatically from your natural language prompt.

---

## Chat Variables

Chat variables include specific context in your prompts. Type `#` in chat to see available variables.

| Variable | Description | Example |
|----------|-------------|---------|
| `#file` | Reference a specific file | `#file:database.js How does connection pooling work?` |
| `#selection` | Reference selected code | `Refactor #selection to use async/await` |
| `#codebase` | Include entire codebase context | `#codebase What is the main architecture pattern?` |
| `#editor` | Reference current editor content | `Add error handling to #editor` |

---

## Keyboard Shortcuts

### VS Code

| Action | Windows/Linux | macOS |
|--------|---------------|-------|
| Open Copilot Chat | `Ctrl+I` | `Cmd+I` |
| Accept suggestion | `Tab` | `Tab` |
| Reject suggestion | `Esc` | `Esc` |
| Next suggestion | `Alt+]` | `Option+]` |
| Previous suggestion | `Alt+[` | `Option+[` |
| Trigger inline suggestion | `Alt+\` | `Option+\` |
| Open chat view | `Ctrl+Alt+I` | `Cmd+Option+I` |

### JetBrains IDEs

| Action | Windows/Linux | macOS |
|--------|---------------|-------|
| Open Copilot Chat | `Alt+C` | `Option+C` |
| Accept suggestion | `Tab` | `Tab` |
| Reject suggestion | `Esc` | `Esc` |
| Next suggestion | `Alt+]` | `Option+]` |
| Previous suggestion | `Alt+[` | `Option+[` |

### Visual Studio

| Action | Windows |
|--------|---------|
| Open Copilot Chat | `Alt+/` |
| Accept suggestion | `Tab` or `Enter` |
| Reject suggestion | `Esc` |

---

## Copilot Chat Modes

Switch between modes using the dropdown at the bottom of the chat view.

| Mode | Purpose | Best For |
|------|---------|----------|
| **Ask** | Get answers and code suggestions | Questions, explanations, small code snippets |
| **Edit** | Controlled multi-file edits | Specific updates to a defined set of files |
| **Agent** | Autonomous task completion | Complex multi-step tasks with iterations |
| **Plan** | Create implementation plans | Large features requiring detailed planning |

### Mode Selection Guide

**Use Ask Mode when**:
- Learning how something works
- Getting quick code snippets
- Asking about best practices

**Use Edit Mode when**:
- Making specific changes to known files
- You want full control over LLM requests
- Iterating on defined edits

**Use Agent Mode when**:
- Task is complex and multi-step
- You want Copilot to determine necessary steps
- Integrating with external tools (MCP servers)

**Use Plan Mode when**:
- Starting a large feature
- Need to review requirements before coding
- Want a detailed implementation roadmap

---

## Common Prompt Patterns

### Code Generation
```
Create a REST API endpoint for user registration with:
- Email validation
- Password hashing (bcrypt)
- JWT token generation
- Error handling for duplicate emails
```

### Code Explanation
```
@workspace /explain
Explain the authentication flow from login to protected route access
```

### Refactoring
```
Refactor #selection to:
1. Use TypeScript interfaces
2. Add input validation
3. Implement error handling
4. Add comprehensive JSDoc comments
```

### Testing
```
/tests
Generate unit tests for the PaymentService class including:
- Successful payment processing
- Invalid card handling
- Network timeout scenarios
- Idempotency checks
```

### Debugging
```
/fix
This function throws "Cannot read property 'length' of undefined"
when the input array is empty. Fix it with proper null checks.
```

---

## Agent Mode Features

### Subagents

Delegate complex tasks to isolated agents with their own context.

**Enable**: Click tools icon → Enable `runSubagent` tool

**Usage**:
```
Use the testing subagent to write comprehensive tests
for the authentication module
```

**Automatic Delegation**: Copilot can automatically choose the right subagent based on your request.

---

## Model Context Protocol (MCP) Servers

Connect Copilot to external tools and data sources.

**Available in**: VS Code, JetBrains, Visual Studio, Eclipse

**Example Use Cases**:
- Database queries
- API integrations
- Custom tool integrations

→ [Learn more about MCP](https://docs.github.com/copilot/using-github-copilot/asking-github-copilot-questions-in-your-ide)

---

## AI Models

Choose different AI models based on your subscription:

| Model | Speed | Capability | Best For |
|-------|-------|------------|----------|
| GPT-4o | Fast | High | Most tasks, balanced performance |
| o1-preview | Medium | Highest | Complex reasoning, planning |
| o1-mini | Fast | High | Quick tasks, iterations |
| Claude 3.5 Sonnet | Fast | High | Code generation, analysis |

**How to switch**: Click model selector in Copilot Chat (Pro/Pro+ subscribers)

---

## Tips for Effective Commands

1. **Be Specific**: Include requirements, constraints, and expected output
2. **Use Examples**: Show input/output examples for clarity
3. **Iterate**: Refine prompts if first response isn't helpful
4. **Combine Tools**: Use slash commands + chat variables + participants together
5. **Review Output**: Always understand and test generated code

---

## 📚 Learn More

- [Copilot Chat in IDE](https://docs.github.com/copilot/using-github-copilot/asking-github-copilot-questions-in-your-ide)
- [Best Practices](GETTING-STARTED.md)
- [Prompt Engineering](https://docs.github.com/copilot/using-github-copilot/prompt-engineering-for-github-copilot)
- [Complete Documentation](REFERENCE.md)

---

*Command reference updated {last_updated[:10]}. Features vary by IDE and subscription level.*
