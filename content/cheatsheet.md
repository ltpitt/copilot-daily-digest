# GitHub Copilot Cheatsheet

> Quick reference for commands, shortcuts, and features

**Last Updated**: 2025-12-10

---

## 🎯 Quick Navigation

- [Slash Commands](#slash-commands)
- [Chat Variables](#chat-variables)
- [Keyboard Shortcuts](#keyboard-shortcuts)
- [Agent Mode Tips](#agent-mode-tips)
- [Coding Agent Workflows](#coding-agent-workflows)
- [Model Selection](#model-selection)
- [Custom Instructions](#custom-instructions)
- [Common Tasks](#common-tasks)
- [Troubleshooting](#troubleshooting)

---

## Slash Commands

Commands you can use in GitHub Copilot Chat:

| Command | Description | Example |
|---------|-------------|---------|
| `/explain` | Explain selected code or concept | `/explain` (with code selected) |
| `/fix` | Suggest fixes for problems in code | `/fix` (with problematic code selected) |
| `/tests` | Generate unit tests | `/tests` (with function selected) |
| `/help` | Get help with Copilot features | `/help` |
| `/clear` | Clear chat history | `/clear` |
| `/doc` | Generate documentation | `/doc` (with code selected) |

---

## Chat Variables

Reference context in your chat prompts:

| Variable | Description | Usage |
|----------|-------------|-------|
| `#file` | Reference a specific file | `#file:src/app.js explain the routing logic` |
| `#selection` | Reference current selection | `#selection refactor this to use async/await` |
| `#editor` | Reference active editor content | `#editor find performance issues` |
| `#terminal` | Reference terminal output | `#terminal explain this error` |
| `#codebase` | Reference entire codebase | `#codebase where is authentication handled?` |

**Pro Tip**: Copilot can auto-infer relevant participants (e.g., `@terminal` for CLI questions) in public preview.

---

## Keyboard Shortcuts

### Visual Studio Code

| Action | Windows/Linux | macOS |
|--------|--------------|--------|
| Open Chat | `Ctrl+I` | `Cmd+I` |
| Accept Suggestion | `Tab` | `Tab` |
| Dismiss Suggestion | `Esc` | `Esc` |
| Next Suggestion | `Alt+]` | `Option+]` |
| Previous Suggestion | `Alt+[` | `Option+[` |
| Open Copilot | `Ctrl+Shift+P` → "Copilot" | `Cmd+Shift+P` → "Copilot" |
| Inline Chat | `Ctrl+I` | `Cmd+I` |

### Visual Studio

| Action | Shortcut |
|--------|----------|
| Open Chat | `Alt+/` |
| Accept Suggestion | `Tab` |
| Dismiss Suggestion | `Esc` |
| Next Suggestion | `Alt+.` |
| Previous Suggestion | `Alt+,` |

### JetBrains IDEs

| Action | Shortcut |
|--------|----------|
| Open Chat | `Ctrl+Shift+A` → "Copilot Chat" |
| Accept Suggestion | `Tab` |
| Dismiss Suggestion | `Esc` |
| Next Suggestion | `Alt+]` |
| Previous Suggestion | `Alt+[` |

---

## Agent Mode Tips

### In Your IDE

**Quick Actions**:
- Select code + ask question = Context-aware response
- Comment + Tab = Generate code from comment
- Partial code + Tab = Complete the pattern
- Error message + `/fix` = Suggested fixes

**Best Practices**:
1. **Be Specific**: Instead of "make it better", try "refactor to use async/await pattern"
2. **Provide Context**: Reference files, functions, or error messages
3. **Iterate**: Accept partial suggestions and refine
4. **Review**: Always review generated code for correctness

**Example Prompts**:
```
✅ Good: "Add error handling to fetchUser function with try-catch"
❌ Bad: "Fix this"

✅ Good: "Refactor this function to be pure and testable"
❌ Bad: "Make it better"

✅ Good: "Generate unit tests for UserService with jest mocks"
❌ Bad: "Write tests"
```

---

## Coding Agent Workflows

### GitHub Copilot Coding Agent

**Common Tasks**:

| Task | Command Example |
|------|----------------|
| Generate tests | "Generate unit tests for all functions in src/services/" |
| Refactor code | "Refactor authentication logic to use JWT tokens" |
| Add features | "Add pagination to the user list API endpoint" |
| Fix bugs | "Fix the race condition in async data fetching" |
| Documentation | "Add JSDoc comments to all public APIs" |
| Setup | "Set up ESLint configuration for TypeScript project" |

**Workflow Pattern**:
1. Create clear task description
2. Reference specific files or modules
3. Include acceptance criteria
4. Let agent iterate
5. Review and test changes

---

## Model Selection

### Available Models (Pro/Pro+)

| Model | Best For | Context Window |
|-------|----------|---------------|
| **GPT-4** | General purpose, reliable | Large |
| **GPT-5.1 Codex Max** | Code generation, understanding | Very Large |
| **Claude Opus 4.5** | Complex reasoning, large codebases | Largest |
| **Claude Sonnet** | Fast, efficient responses | Large |

**Model Picker** (Dec 8, 2025):
- Pro and Pro+ subscribers can select model when starting tasks
- Choose based on workload type
- Available in coding agent interface

---

## Custom Instructions

### copilot-instructions.md

Create in your repository root:

```markdown
# Project Context
- Tech stack: [Your stack]
- Architecture: [Your architecture]
- Key patterns: [Your patterns]

# Code Style
- Use TypeScript with strict mode
- Prefer functional programming
- Follow [style guide name]

# Testing
- Write tests for all features
- Use [test framework]
- Aim for 80%+ coverage

# Documentation
- JSDoc for public APIs
- README for modules
- Inline comments for complex logic

# Preferences
- Async/await over callbacks
- Descriptive variable names
- Small, focused functions
```

### AGENTS.md (Advanced)

For multi-agent workflows:

```markdown
# Available Agents
- **backend-agent**: API and database changes
- **frontend-agent**: UI and component work
- **test-agent**: Test generation and validation
- **docs-agent**: Documentation updates

# Workflow Rules
- Backend changes require test coverage
- UI changes need component tests
- All PRs need documentation updates
```

📘 [Learn more about AGENTS.md](https://github.blog/ai-and-ml/github-copilot/how-to-write-a-great-agents-md-lessons-from-over-2500-repositories/)

---

## Common Tasks

### Code Generation

```
Task: Generate a REST API endpoint
Prompt: "Create a GET /api/users/:id endpoint with validation, 
         error handling, and response formatting"

Task: Create a React component
Prompt: "Generate a UserProfile component with props for name, 
         email, and avatar. Include TypeScript types and basic styling."
```

### Refactoring

```
Task: Modernize callback-based code
Prompt: "Refactor all callback functions in database.js to use 
         async/await pattern"

Task: Improve error handling
Prompt: "Add comprehensive error handling with custom error classes 
         to the API routes"
```

### Testing

```
Task: Generate unit tests
Prompt: "Generate Jest unit tests for UserService with mocks for 
         database calls. Cover all public methods."

Task: Generate integration tests
Prompt: "Create integration tests for authentication flow using 
         supertest and test database"
```

### Documentation

```
Task: Add code documentation
Prompt: "Add JSDoc comments to all functions in utils.js with 
         parameter types and return values"

Task: Generate README
Prompt: "Create a comprehensive README with setup instructions, 
         API documentation, and examples"
```

---

## Troubleshooting

### Common Issues

| Issue | Solution |
|-------|----------|
| Suggestions not appearing | Check internet connection, restart IDE |
| Incorrect suggestions | Provide more context, be more specific |
| Slow performance | Clear chat history, reduce file size |
| Authentication issues | Sign out and sign back in |
| Extension not working | Update to latest version |

### Getting Better Results

**Context is Key**:
- Select relevant code before asking
- Reference specific files or functions
- Include error messages in prompts
- Provide examples of desired output

**Iteration Strategy**:
1. Start with broad request
2. Refine based on results
3. Accept and modify incrementally
4. Test and validate changes

**Quality Checks**:
- ✅ Code compiles and runs
- ✅ Tests pass
- ✅ Follows project style guide
- ✅ Handles edge cases
- ✅ Includes error handling
- ✅ Has appropriate documentation

---

## CLI Usage

### GitHub Copilot CLI

```bash
# Install
npm install -g @githubnext/github-copilot-cli

# Setup
github-copilot-cli auth

# Usage
gh copilot suggest "find all large files"
gh copilot explain "git rebase origin/main"

# Shell integration
eval "$(github-copilot-cli alias -- "$0")"
```

📘 [Copilot CLI 101](https://github.blog/ai-and-ml/github-copilot-cli-101-how-to-use-github-copilot-from-the-command-line/)

---

## API Integration

### Assign Issues to Copilot

```bash
# Using GitHub CLI
gh api repos/OWNER/REPO/issues/123/assignees \
  -f assignees[]=@copilot

# Using REST API
POST /repos/{owner}/{repo}/issues/{issue_number}/assignees
{
  "assignees": ["@copilot"]
}
```

📘 [API Documentation](https://github.blog/changelog/2025-12-03-assign-issues-to-copilot-using-the-api)

---

## Metrics & Analytics

### Track Usage (Enterprise)

Available metrics:
- Code generation frequency
- Acceptance rates
- Productivity impact
- User adoption rates
- Team usage patterns

📊 [Dashboard Documentation](https://github.blog/changelog/2025-12-05-track-copilot-code-generation-metrics-in-a-dashboard)

---

## Quick Reference Links

### Documentation
- [Official Docs](https://docs.github.com/copilot)
- [Cheat Sheet](https://docs.github.com/en/copilot/reference/cheat-sheet)
- [Best Practices](https://docs.github.com/en/copilot/best-practices)

### Learning
- [GitHub Skills Course](https://github.com/skills/expand-your-team-with-copilot/)
- [Mastering Copilot](https://github.com/microsoft/Mastering-GitHub-Copilot-for-Paired-Programming)
- [Spec-driven Toolkit](https://github.com/github/spec-kit)

### Community
- [GitHub Blog - AI & ML](https://github.blog/ai-and-ml/)
- [Changelog](https://github.blog/changelog/)
- [Community Forums](https://github.community/)

---

## Pro Tips

1. **Start Small**: Begin with simple tasks, build complexity
2. **Clear Instructions**: Specific prompts get better results
3. **Iterate**: Accept partial solutions, refine incrementally
4. **Context Matters**: Reference files, functions, error messages
5. **Validate**: Always review and test generated code
6. **Learn Patterns**: Study successful prompts, refine your approach
7. **Use Custom Instructions**: Project-wide context improves consistency
8. **Track Metrics**: Monitor adoption and productivity gains
9. **Integrate Workflows**: Combine with CI/CD and testing
10. **Stay Updated**: Follow changelog for new features

---

*This cheatsheet is maintained by the GitHub Copilot Daily Digest system.*
