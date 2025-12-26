# Getting Started with GitHub Copilot

> Your 5-minute guide to productive AI pair programming

**Last Updated**: December 26, 2025

## Quick Setup

### 1. Install Copilot in Your IDE

**VS Code**:
```bash
# Install extension
code --install-extension GitHub.copilot
```

**JetBrains**: Install from Plugins marketplace (Settings → Plugins → Search "GitHub Copilot")  
**Visual Studio**: Built-in for Version 17.14+  
**Xcode/Eclipse**: Available for Pro/Pro+ subscribers

### 2. Try Your First Prompt

Open any file and type a comment:
```javascript
// Create a function that validates email addresses with regex
```

Press `Enter` - Copilot suggests the implementation. Press `Tab` to accept.

### 3. Use Chat for Complex Tasks

Press `Ctrl+I` (Windows/Linux) or `Cmd+I` (Mac) for inline chat:
```
Explain this codebase structure and list any failing tests
```

### 4. Enable Agent Mode (Optional)

For autonomous multi-step tasks:
- VS Code: Chat view → Select "Agent" from mode dropdown
- Ask: "Add Redis caching to userSessionService with 30s TTL"
- Copilot determines files, makes changes, and you review

## Best Practices

### Write Effective Issues (WRAP Methodology)

❌ **Don't**: "Update the entire repository to use async/await"  
✅ **Do**: "Update the authentication middleware to use the newer async/await pattern, as shown below. Add unit tests for verification."

```javascript
async function exampleFunction() {
  let result = await promise;
  console.log(result); // "done!"
}
```

**Why**: Write issues as though they're for someone brand new to the codebase. Include context and examples.

→ **Source**: [WRAP up your backlog with GitHub Copilot coding agent](https://github.blog/ai-and-ml/github-copilot/wrap-up-your-backlog-with-github-copilot-coding-agent/) (Dec 26, 2025)

### Use Atomic Tasks

❌ **Don't**: "Rewrite 3 million lines of code from Java to Golang"  
✅ **Do**: Break into smaller atomic tasks:
1. "Migrate the authentication module to Golang, ensuring all existing unit tests pass"
2. "Convert the data validation utilities package to Golang while maintaining the same API interface"
3. "Rewrite the user management controllers to Golang, preserving existing REST endpoints"

**Why**: Atomic tasks are easier to test, validate, and review. Coding agent excels at small, well-defined tasks.

→ **Source**: [WRAP up your backlog](https://github.blog/ai-and-ml/github-copilot/wrap-up-your-backlog-with-github-copilot-coding-agent/) (Dec 26, 2025)

### Refine Your Custom Instructions

Improve results by adding custom instructions at different levels:

**Repository instructions**: Add coding standards specific to your repository (e.g., "Use async/await for Go applications")

**Organization instructions**: Set requirements that apply to all repos (e.g., "All applications must have unit tests")

**Custom agents**: Create specialized agents for repetitive tasks (e.g., "Integration Agent" for product integrations)

→ **Source**: [WRAP up your backlog](https://github.blog/ai-and-ml/github-copilot/wrap-up-your-backlog-with-github-copilot-coding-agent/) (Dec 26, 2025)  
→ **Guide**: [Configure custom instructions](https://docs.github.com/en/copilot/how-tos/configure-custom-instructions/add-repository-instructions)

### Provide Examples

❌ **Don't**: "Create a data validation function"  
✅ **Do**: 
```
Create a data validation function. Example input:
{ name: "John", age: 25, email: "john@example.com" }
Expected output: { valid: true, errors: [] }
```

**Why**: Examples clarify your requirements and reduce ambiguity.

### Use Inline Suggestions for Repetitive Code

**Best for**:
- Completing similar functions
- Writing test cases
- Generating boilerplate

**How**: Start typing, wait for ghost text, press `Tab` to accept.

### Use Chat for Complex Reasoning

**Best for**:
- Debugging issues
- Understanding unfamiliar code
- Architecture decisions
- Code review

**How**: Press `Ctrl+Shift+I` (VS Code) to open chat view, then ask questions.

### Review and Test Copilot's Suggestions

✅ **Always**:
- Read suggested code before accepting
- Run tests to verify behavior
- Check for security issues (SQL injection, XSS, etc.)
- Validate that code follows your project's conventions

❌ **Never**:
- Blindly accept all suggestions
- Skip code review for AI-generated code
- Commit without testing

### Use Slash Commands for Common Tasks

Quick shortcuts in chat:
- `/explain` - Explain selected code
- `/fix` - Suggest fixes for problems
- `/tests` - Generate unit tests
- `/doc` - Add documentation

**Example**: Select a function → Open chat → Type `/tests` → Get comprehensive test cases.

### Keep Context Files Open

**Tip**: Open relevant files in tabs before asking Copilot questions. It uses open files as context.

**Example**: Before asking "Add error handling to API routes", open:
- Your API route files
- Error handler utilities
- Similar implemented routes

### Pair with Coding Agent

Understand what humans vs. AI do best:

**Humans excel at**:
- Understanding the "why" behind tasks
- Navigating ambiguity and making judgment calls
- Cross-system thinking and impact analysis

**Coding agent excels at**:
- Tireless execution (assign 10 tasks simultaneously)
- Repetitive tasks (updating naming conventions across many files)
- Exploring possibilities (test multiple approaches in parallel)

→ **Source**: [WRAP up your backlog](https://github.blog/ai-and-ml/github-copilot/wrap-up-your-backlog-with-github-copilot-coding-agent/) (Dec 26, 2025)

## Next Steps

- **[Watch tutorials](VIDEOS.md)** - Learn from video demos
- **[Take courses](TRAININGS.md)** - Official GitHub Skills courses
- **[Explore updates](WHATS-NEW.md)** - See latest features
- **[Read best practices](https://docs.github.com/en/copilot/using-github-copilot/best-practices-for-using-github-copilot)** - Official documentation

---

*For complete command reference, see [COMMANDS.md](COMMANDS.md)*
