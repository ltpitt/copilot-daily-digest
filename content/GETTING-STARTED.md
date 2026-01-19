# Getting Started with GitHub Copilot

> Your 5-minute guide to productive AI pair programming

**Last Updated**: 2026-01-19

---

## 🚀 Quick Setup

### 1. Install Copilot in Your IDE

**VS Code**:
```bash
# Install extension
code --install-extension GitHub.copilot
```

**JetBrains**: Install from Plugins marketplace  
**Visual Studio**: Version 17.14+ includes built-in support  
**Xcode/Eclipse**: Available for Pro/Pro+ subscribers

### 2. Try Your First Prompt

Open any file and type a comment:
```javascript
// Create a function that validates email addresses with regex
```

Press `Enter` - Copilot suggests the implementation.

### 3. Use Chat for Complex Tasks

Press `Ctrl+I` (Windows/Linux) or `Cmd+I` (Mac):
```
Explain this codebase structure and list any failing tests
```

### 4. Enable Agent Mode (Optional)

For autonomous multi-step tasks:
- VS Code: Settings → enable "Copilot > Agent Mode"
- Ask: "Add Redis caching to userSessionService with 30s TTL"
- Copilot determines files, makes changes, opens a PR

---

## 💡 Best Practices

### Write Context-Rich Prompts

❌ **Don't**: "Add caching"  
✅ **Do**: "Add Redis caching to userSessionService with 30s TTL to reduce DB hits >1000/min"

**Why it matters**: Specific prompts with context, constraints, and success criteria lead to better code suggestions.

### Start General, Then Get Specific

When asking Copilot Chat:
1. **First**: Describe the broad goal ("Write a function to validate user input")
2. **Then**: Add specific requirements ("Function should accept email string, return boolean, handle edge cases for plus addressing and international domains")

→ Source: [Prompt Engineering for GitHub Copilot](https://docs.github.com/copilot/using-github-copilot/prompt-engineering-for-github-copilot)

### Give Examples for Complex Logic

Help Copilot understand by providing sample inputs and outputs:

```
Create a Go function that finds dates in strings.

Formats: 05/02/24, 05-02-2024, 5/2/24
Example: findDates("Meeting on 11/14/2023 and 12-1-23")
Returns: ["11/14/2023", "12-1-23"]
```

### Break Down Complex Tasks

Instead of: "Build a word search puzzle generator"

Try:
1. "Generate a 10x10 grid of random letters"
2. "Find all valid words in a letter grid"
3. "Combine functions to create a puzzle with 10+ words"

### Review Before Accepting

✅ **Always**:
- Understand suggested code before implementing
- Check for security issues and edge cases
- Use linters and automated tests
- Ask Copilot to explain if unclear

### Keep Context Relevant

- **IDE**: Open relevant files, close unrelated files
- **Chat**: Delete old requests that no longer apply
- **Keywords**: Use `@workspace`, `#file`, `#selection` to focus Copilot

---

## 🎯 What Copilot Does Best

Copilot excels at:
- ✅ Writing tests and repetitive code
- ✅ Debugging and fixing syntax errors
- ✅ Explaining and commenting code
- ✅ Generating regular expressions
- ✅ Answering coding questions in natural language

Copilot is **not** designed to:
- ❌ Replace your expertise and judgment
- ❌ Respond to non-coding questions

---

## 🎯 Next Steps

- **[Watch tutorials](VIDEOS.md)** - Learn from video demos
- **[Take courses](TRAININGS.md)** - Official GitHub Skills courses
- **[Explore updates](WHATS-NEW.md)** - See latest features
- **[Deep dive](STARTER-KIT.md)** - Master Copilot workflow

---

*For complete command reference, see [COMMANDS.md](COMMANDS.md)*
