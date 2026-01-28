# Getting Started with GitHub Copilot

> Your 5-minute guide to productive AI pair programming

## 🚀 Quick Setup

### 1. Install Copilot in Your IDE

**VS Code**:
```bash
# Install extension
code --install-extension GitHub.copilot
```

**JetBrains**: Install from Plugins marketplace (Settings → Plugins → search "GitHub Copilot")
**Visual Studio**: Version 17.14+ includes built-in support
**Xcode/Eclipse**: Available for Pro/Pro+ subscribers

### 2. Sign Up for GitHub Copilot

Choose your plan:
- **Copilot Free** - Limited features to explore without subscribing
- **Copilot Pro** - Full features, advanced models, higher limits ($10/month)
- **Copilot Pro+** - All Pro features + priority access to newest models ($15/month)
- **Copilot Enterprise** - Organization-wide deployment with custom instructions

[Sign up at GitHub Copilot Plans](https://docs.github.com/copilot/about-github-copilot/subscription-plans-for-github-copilot)

### 3. Try Your First Inline Suggestion

Open any code file and type a comment:

```javascript
// Create a function that validates email addresses with regex
```

Press `Enter` - Copilot suggests the implementation. Press `Tab` to accept.

### 4. Use Chat for Complex Tasks

**Keyboard Shortcuts**:
- VS Code: `Ctrl+I` (Windows/Linux) or `Cmd+I` (Mac)
- JetBrains: `Alt+C` or `Option+C`

Try this prompt:
```
Explain the structure of this codebase and list the main components
```

### 5. Enable Agent Mode (Advanced)

For autonomous multi-step tasks:
1. Open Copilot Chat
2. Select **Agent** from the mode dropdown at the bottom
3. Ask: "Add Redis caching to userSessionService with 30s TTL"
4. Copilot determines files, makes changes, and iterates to complete the task

## 💡 Best Practices

### 1. Write Context-Rich Prompts

❌ **Don't**: "Add caching"
✅ **Do**: "Add Redis caching to userSessionService with 30s TTL to reduce DB load when handling >1000 requests/min"

**Why**: Specific requirements help Copilot generate production-ready code.

→ [Learn more: Prompt Engineering](https://docs.github.com/copilot/using-github-copilot/prompt-engineering-for-github-copilot)

### 2. Break Complex Tasks into Smaller Steps

❌ **Don't**: "Build a word search puzzle generator"
✅ **Do**:
1. "Write a function to generate a 10x10 grid of letters"
2. "Write a function to find all words in a grid given a word list"
3. "Combine functions to generate grids containing at least 10 words"

**Why**: Simpler prompts = more accurate suggestions. You can iterate on each piece.

→ [Source: Best Practices - Break Down Tasks](https://docs.github.com/copilot/using-github-copilot/best-practices-for-using-github-copilot)

### 3. Provide Examples in Your Prompts

❌ **Don't**: "Parse dates from strings"
✅ **Do**:
```
Write a function that finds all dates in a string. Dates can be:
* 05/02/24, 05/02/2024, 5/2/24, 5/2/2024
* 05-02-24, 05-02-2024, 5-2-24, 5-2-2024

Example:
findDates("Meeting on 11/14/2023 and 12-1-23")
Returns: ["11/14/2023", "12-1-23"]
```

**Why**: Examples clarify edge cases and expected formats.

→ [Source: Prompt Engineering - Give Examples](https://docs.github.com/copilot/using-github-copilot/prompt-engineering-for-github-copilot#give-examples)

### 4. Use Chat Participants & Slash Commands

**Chat Participants** (type `@` in chat):
- `@workspace` - Ask about your entire codebase
- `@terminal` - Get shell command help
- `@vscode` - VS Code settings and features

**Slash Commands** (type `/` in chat):
- `/explain` - Explain selected code
- `/fix` - Suggest fixes for errors
- `/tests` - Generate unit tests
- `/doc` - Add documentation comments

**Example**:
```
@workspace /tests
Generate unit tests for the authentication module with edge cases
```

→ [Source: Chat in IDE - Using Keywords](https://docs.github.com/copilot/using-github-copilot/asking-github-copilot-questions-in-your-ide)

### 5. Review Copilot's Suggestions Carefully

✅ **Always**:
- Understand code before accepting (use `/explain` if unclear)
- Test generated code thoroughly
- Use linting and security scanning tools
- Check for similarities to public code (if enabled)

❌ **Never**:
- Blindly accept suggestions without understanding
- Skip testing AI-generated code
- Assume Copilot suggestions are always secure

**Why**: Copilot is a tool—you're responsible for code quality and security.

→ [Source: Best Practices - Check Copilot's Work](https://docs.github.com/copilot/using-github-copilot/best-practices-for-using-github-copilot#check-copilots-work)

### 6. Provide Relevant Context

**Do This**:
- Open files related to your task
- Close unrelated files to reduce noise
- Use chat variables: `#file`, `#selection`, `#codebase`

**Example**:
```
Using #file:database.js as a reference, add similar error handling
to #selection in api-routes.js
```

**Why**: Copilot uses open files and references to understand your codebase context.

→ [Source: Best Practices - Provide Context](https://docs.github.com/copilot/using-github-copilot/best-practices-for-using-github-copilot#guide-copilot-towards-helpful-outputs)

### 7. Iterate and Refine Prompts

If Copilot's first response isn't helpful:
1. **Rephrase** your prompt with different words
2. **Add more details** about requirements or constraints
3. **Ask follow-up questions** to refine the output
4. **Start a new conversation** if context becomes unhelpful

**Example Iteration**:
- First: "Create an API endpoint"
- Refined: "Create a POST /api/users endpoint in Express that validates email/password, hashes password with bcrypt, saves to MongoDB, and returns JWT"

→ [Source: Best Practices - Guide Copilot](https://docs.github.com/copilot/using-github-copilot/best-practices-for-using-github-copilot#guide-copilot-towards-helpful-outputs)

## 🎯 Next Steps

1. **Master Prompts**: Read [Prompt Engineering Guide](https://docs.github.com/copilot/using-github-copilot/prompt-engineering-for-github-copilot)
2. **Deep Dive**: Explore the [Starter Kit](STARTER-KIT.md) for workflow integration
3. **Train**: Take [official courses](TRAININGS.md) for certifications
4. **Stay Updated**: Bookmark [What's New](WHATS-NEW.md) for latest features

## 📚 Official Resources

- [Copilot Documentation](https://docs.github.com/copilot)
- [Best Practices](https://docs.github.com/copilot/using-github-copilot/best-practices-for-using-github-copilot)
- [Prompt Engineering](https://docs.github.com/copilot/using-github-copilot/prompt-engineering-for-github-copilot)
- [Chat in IDE](https://docs.github.com/copilot/using-github-copilot/asking-github-copilot-questions-in-your-ide)
