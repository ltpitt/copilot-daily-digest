# Getting Started with GitHub Copilot

> Your 5-minute guide to productive AI pair programming

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

### Write Context-Rich Prompts

❌ **Don't**: "Add caching"  
✅ **Do**: "Add Redis caching to userSessionService with 30s TTL to reduce DB hits >1000/min"

**Why**: Specific prompts give Copilot the context it needs to generate accurate, production-ready code.

### Break Down Complex Tasks

❌ **Don't**: "Build a complete authentication system"  
✅ **Do**: 
1. "Create a user registration endpoint with email validation"
2. "Add password hashing using bcrypt"
3. "Implement JWT token generation for authenticated users"

**Why**: Smaller, focused tasks lead to better code quality and easier review.

### Choose the Right Model for the Task

Different AI models excel at different tasks:
- **GPT models**: Best for general code generation and explanations
- **Claude models**: Excellent for code review and refactoring
- **Gemini models**: Strong at understanding complex codebases

**How**: Use the model picker in VS Code (Chat view → Model dropdown) or enable Auto Model Selection.

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

### Iterate on Responses

If Copilot's first response isn't perfect:
- Ask follow-up questions: "Make this more efficient"
- Request specific changes: "Use async/await instead of promises"
- Provide more context: "This runs in a serverless environment"

## Next Steps

- **[Watch tutorials](VIDEOS.md)** - Learn from video demos
- **[Take courses](TRAININGS.md)** - Official GitHub Skills courses
- **[Explore updates](WHATS-NEW.md)** - See latest features
- **[Read best practices](https://docs.github.com/en/copilot/using-github-copilot/best-practices-for-using-github-copilot)** - Official documentation

---

*For complete command reference, see [COMMANDS.md](COMMANDS.md)*
