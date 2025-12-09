# GitHub Copilot Cheatsheet

> Quick reference for commands, variables, and features

**Last Updated**: December 9, 2025

---

## 📋 Table of Contents

- [Slash Commands](#slash-commands)
- [Chat Variables](#chat-variables)
- [Keyboard Shortcuts](#keyboard-shortcuts)
- [Setup & Configuration](#setup--configuration)
- [Best Practices](#best-practices)
- [Troubleshooting](#troubleshooting)

---

## ⚡ Slash Commands

Slash commands help you quickly perform common tasks in the Copilot chat interface.

### Code Understanding

| Command | Description | Example Usage |
|---------|-------------|---------------|
| `/explain` | Explain how selected code works | Select code → `/explain` |
| `/doc` | Generate documentation | Select function → `/doc` |
| `/review` | Request code review | Select code → `/review` |

### Code Generation

| Command | Description | Example Usage |
|---------|-------------|---------------|
| `/new` | Create new code or files | `/new React component for user profile` |
| `/tests` | Generate unit tests | Select function → `/tests` |
| `/fix` | Fix bugs or errors | Select buggy code → `/fix` |

### Code Modification

| Command | Description | Example Usage |
|---------|-------------|---------------|
| `/optimize` | Improve code performance | Select code → `/optimize` |
| `/simplify` | Simplify complex code | Select code → `/simplify` |
| `/refactor` | Refactor code structure | Select code → `/refactor` |

### Terminal & Development

| Command | Description | Example Usage |
|---------|-------------|---------------|
| `/terminal` | Generate terminal commands | `/terminal deploy to production` |
| `/git` | Git command assistance | `/git revert last 3 commits` |

### Project Management

| Command | Description | Example Usage |
|---------|-------------|---------------|
| `/search` | Search codebase | `/search authentication logic` |
| `/workspace` | Workspace-wide operations | `/workspace analyze dependencies` |

---

## 🏷️ Chat Variables

Variables provide context to Copilot by referencing specific parts of your project.

### File & Code References

| Variable | Description | Example Usage |
|----------|-------------|---------------|
| `#file` | Reference a specific file | `#file:src/app.js what does this do?` |
| `#selection` | Reference selected code | `#selection explain this function` |
| `#editor` | Reference active editor content | `#editor review this code` |
| `#codebase` | Reference entire codebase | `#codebase find authentication code` |

### Context Variables

| Variable | Description | Example Usage |
|----------|-------------|---------------|
| `#terminal` | Reference terminal output | `#terminal what does this error mean?` |
| `#git` | Reference Git information | `#git summarize recent changes` |

### Symbol References

| Variable | Description | Example Usage |
|----------|-------------|---------------|
| `#sym` | Reference a symbol/function | `#sym:calculateTotal optimize this` |

### Advanced References

| Variable | Description | Example Usage |
|----------|-------------|---------------|
| `#@workspace` | Workspace-level context | `#@workspace find all API calls` |

---

## ⌨️ Keyboard Shortcuts

### VS Code

| Action | Windows/Linux | macOS |
|--------|---------------|-------|
| Open Copilot Chat | `Ctrl+Shift+I` | `Cmd+Shift+I` |
| Inline Chat | `Ctrl+I` | `Cmd+I` |
| Accept Suggestion | `Tab` | `Tab` |
| Reject Suggestion | `Esc` | `Esc` |
| Next Suggestion | `Alt+]` | `Opt+]` |
| Previous Suggestion | `Alt+[` | `Opt+[` |
| Trigger Suggestion | `Alt+\` | `Opt+\` |

### JetBrains IDEs

| Action | Windows/Linux | macOS |
|--------|---------------|-------|
| Open Copilot Chat | `Ctrl+Shift+Enter` | `Cmd+Shift+Enter` |
| Accept Suggestion | `Tab` | `Tab` |
| Reject Suggestion | `Esc` | `Esc` |
| Next Suggestion | `Alt+]` | `Opt+]` |

### Visual Studio

| Action | Shortcut |
|--------|----------|
| Open Copilot Chat | `Alt+/` |
| Accept Suggestion | `Tab` |
| Reject Suggestion | `Esc` |

---

## 🔧 Setup & Configuration

### Installation

#### VS Code
1. Open Extensions panel (`Ctrl+Shift+X` / `Cmd+Shift+X`)
2. Search for "GitHub Copilot"
3. Click "Install" on both:
   - GitHub Copilot
   - GitHub Copilot Chat
4. Sign in with GitHub account
5. Authorize the extension

#### JetBrains IDEs
1. Open Settings → Plugins
2. Search for "GitHub Copilot"
3. Install plugin
4. Restart IDE
5. Sign in with GitHub account

#### Visual Studio
1. Extensions → Manage Extensions
2. Search for "GitHub Copilot"
3. Download and install
4. Restart Visual Studio
5. Sign in with GitHub account

### Configuration Options

#### Enable/Disable Copilot

**VS Code Settings** (`settings.json`):
```json
{
  "github.copilot.enable": {
    "*": true,
    "yaml": false,
    "plaintext": false
  }
}
```

#### Suggestion Behavior

```json
{
  "github.copilot.editor.enableAutoCompletions": true,
  "editor.inlineSuggest.enabled": true
}
```

#### Custom Instructions

Create `.github/copilot-instructions.md` in your repository:

```markdown
# Copilot Instructions

## Code Style
- Use TypeScript for all new files
- Follow Airbnb ESLint rules
- Prefer functional components in React

## Testing
- Generate Jest tests for all functions
- Aim for 80% code coverage
- Use React Testing Library for components

## Documentation
- Add JSDoc comments to all exported functions
- Include examples in documentation
```

---

## 💡 Best Practices

### Writing Effective Prompts

**✅ DO:**
- Be specific and descriptive
- Provide context with variables
- Break complex tasks into steps
- Include examples when possible

**❌ DON'T:**
- Use vague or ambiguous language
- Ask for too much at once
- Skip providing necessary context
- Forget to specify constraints

### Examples

**Good Prompt:**
```
Create a React functional component called UserProfile that:
- Accepts userId as a prop
- Fetches user data from /api/users/{userId}
- Displays name, email, and avatar
- Shows loading state while fetching
- Handles errors gracefully
```

**Better Prompt:**
```
#file:src/types/User.ts Create a React functional component using our 
existing User type that fetches and displays user data. Follow our 
component patterns from #file:src/components/ProductCard.tsx
```

### Iterative Refinement

1. Start with a basic request
2. Review the generated code
3. Ask for specific improvements
4. Iterate until satisfied

**Example Flow:**
```
User: "Create a function to validate email addresses"
[Review code]
User: "Add support for international domains"
[Review code]
User: "Add JSDoc comments and unit tests"
```

### Context Management

**For Single Files:**
```
#file:src/utils.js optimize the parseDate function
```

**For Related Files:**
```
#file:src/models/User.js #file:src/controllers/UserController.js 
add a method to update user preferences
```

**For Project-Wide Changes:**
```
#codebase update all API calls to use the new baseURL constant
```

---

## 🔍 Troubleshooting

### Common Issues

#### Copilot Not Working

**Check:**
1. ✅ GitHub Copilot subscription is active
2. ✅ Signed in to correct GitHub account
3. ✅ Extension is enabled in IDE
4. ✅ Internet connection is active
5. ✅ File type is supported

**Fix:**
- Reload IDE window
- Sign out and sign in again
- Check GitHub Copilot status page
- Verify firewall/proxy settings

#### No Suggestions Appearing

**Common Causes:**
- File type not supported (`.txt`, `.md` may have limited support)
- Code context is insufficient
- Copilot is disabled for current language
- Editor settings blocking inline suggestions

**Solutions:**
```json
// VS Code settings.json
{
  "editor.inlineSuggest.enabled": true,
  "github.copilot.enable": {
    "*": true
  }
}
```

#### Chat Not Responding

**Troubleshooting Steps:**
1. Check network connectivity
2. Clear chat history
3. Restart IDE
4. Check GitHub API status
5. Verify authentication token

#### Suggestions Are Irrelevant

**Improvements:**
- Provide more context with comments
- Use descriptive variable/function names
- Reference related files with `#file`
- Add custom instructions to repository
- Be more specific in chat prompts

---

## 🚀 Advanced Tips

### Multi-File Edits

Use the coding agent for changes across multiple files:
```
@workspace update all components to use the new theme system
```

### Code Review Workflow

1. Open PR in GitHub
2. Click "Copilot Code Review" button
3. Review AI-generated feedback
4. Address suggestions
5. Request human review

### Custom Agents

Create `.github/copilot/agents.md`:
```markdown
# Custom Agents

## @data-validator
Validates all data inputs and adds appropriate error handling.

## @security-checker  
Reviews code for security vulnerabilities and suggests fixes.

## @perf-optimizer
Analyzes code performance and suggests optimizations.
```

### Extension Integration

Connect Copilot to external tools:
- **Sentry**: Error tracking and debugging
- **DataDog**: Performance monitoring
- **Linear**: Issue tracking
- **Jira**: Project management

---

## 📊 Productivity Metrics

Track your Copilot usage:
- Acceptance rate of suggestions
- Time saved on repetitive tasks
- Code quality improvements
- Test coverage increases

**View Metrics:**
- Organization dashboard (Enterprise)
- VS Code Copilot status bar
- GitHub Insights page

---

## 🔗 Additional Resources

- [Official Documentation](https://docs.github.com/en/copilot)
- [Changelog](./changelog.md) - Recent updates
- [Video Library](./videos.md) - Tutorials
- [GitHub Blog](https://github.blog/tag/github-copilot/)
- [Back to Digest](./README.md)

---

## 🆘 Need Help?

- [GitHub Support](https://support.github.com)
- [Community Discussions](https://github.com/orgs/community/discussions/categories/copilot)
- [VS Code Issues](https://github.com/microsoft/vscode-copilot/issues)
- [Stack Overflow](https://stackoverflow.com/questions/tagged/github-copilot)

---

*This cheatsheet is updated regularly with the latest commands and features.*

*Last updated: December 9, 2025 at 10:22 UTC*
