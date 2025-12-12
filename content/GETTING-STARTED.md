# Getting Started with GitHub Copilot

> Your 5-minute guide to productive AI pair programming

## 🚀 Quick Setup

### 1. Install Copilot in Your IDE

**VS Code**:
```bash
# Install extension from marketplace
code --install-extension GitHub.copilot
```
Or search for "GitHub Copilot" in the Extensions panel (`Ctrl+Shift+X`).

**JetBrains IDEs**: Install from Plugins marketplace (Settings → Plugins → Search "GitHub Copilot")

**Visual Studio**: Version 17.14+ includes built-in support (View → GitHub Copilot Chat)

**Xcode/Eclipse**: Available for Pro/Pro+ subscribers via extension marketplace

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

Or open the chat view and ask questions:
```
How do I add error handling to the authentication flow?
```

### 4. Enable Agent Mode (Optional)

For autonomous multi-step tasks:
- **VS Code**: Settings → search "Copilot" → enable "Agent Mode"
- **JetBrains**: Settings → Tools → GitHub Copilot → Enable Coding Agent

Ask: "Add Redis caching to userSessionService with 30s TTL"

Copilot determines files, makes changes, and can open a PR.

---

## 💡 Best Practices

### 1. Write Context-Rich Prompts

**❌ Don't**: "Add caching"

**✅ Do**: "Add Redis caching to userSessionService with 30s TTL for getUserById method to reduce DB hits >1000/min"

**Why**: Specific requirements help Copilot generate production-ready code.

→ Source: [Prompt Engineering for GitHub Copilot Chat](https://docs.github.com/copilot)

---

### 2. Start General, Then Get Specific

Break down your request:
```
Write a JavaScript function that tells me if a number is prime

The function should take an integer and return true if the integer is prime

The function should error if the input is not a positive integer
```

**Why**: Broad context first, then requirements ensures Copilot understands the goal.

→ Source: [Prompt Engineering for GitHub Copilot Chat](https://docs.github.com/copilot)

---

### 3. Give Examples

Provide sample inputs and outputs:
```
Write a Go function that finds all dates in a string and returns them in an array. 
Dates can be formatted like:
* 05/02/24
* 05-02-2024

Example:
findDates("I have a dentist appointment on 11/14/2023 and book club on 12-1-23")
Returns: ["11/14/2023", "12-1-23"]
```

**Why**: Examples clarify edge cases and expected behavior.

→ Source: [Prompt Engineering for GitHub Copilot Chat](https://docs.github.com/copilot)

---

### 4. Break Complex Tasks into Smaller Tasks

**❌ Don't**: "Generate a word search puzzle"

**✅ Do**:
1. "Write a function to generate a 10 by 10 grid of letters"
2. "Write a function to find all words in a grid of letters, given a list of valid words"
3. "Write a function that uses the previous functions to generate a 10 by 10 grid"
4. "Update the previous function to print the grid and 10 random words"

**Why**: Small, incremental steps produce better results.

→ Source: [Prompt Engineering for GitHub Copilot Chat](https://docs.github.com/copilot)

---

### 5. Choose the Right Tool

**Inline Suggestions** work best for:
- Completing code snippets, variable names, and functions
- Generating repetitive code
- Generating code from inline comments

**Copilot Chat** is best suited for:
- Answering questions about code
- Generating large sections of code
- Using keywords and skills like `@workspace`, `/explain`, `/tests`
- Complex multi-step tasks

→ Source: [Best Practices for Using GitHub Copilot](https://docs.github.com/copilot)

---

### 6. Validate Copilot's Work

**Always review** suggested code:
- Understand the code before implementing it
- Ask Copilot Chat to explain: `/explain this function`
- Check for security issues, performance, and readability
- Use automated tests and linting tools

**Tip**: You can ask Copilot to generate tests first:
```
/tests for the authentication module
```

→ Source: [Best Practices for Using GitHub Copilot](https://docs.github.com/copilot)

---

### 7. Provide Relevant Context

**In your IDE**:
- Open relevant files, close irrelevant files
- Use keywords: `@workspace` (VS Code) or `@project` (JetBrains)
- Reference specific code: highlight it before asking

**Example**:
```
@workspace Where is the authentication logic located?
```

**Why**: Copilot uses open files and workspace context to understand your request.

→ Source: [Asking GitHub Copilot Questions in Your IDE](https://docs.github.com/copilot)

---

## 🎯 Next Steps

- **[Watch tutorials](videos.md)** - Learn from video demos
- **[Take courses](TRAININGS.md)** - Official GitHub Skills courses
- **[Explore updates](WHATS-NEW.md)** - See latest features
- **[Read best practices guide](https://docs.github.com/en/copilot/using-github-copilot/best-practices-for-using-github-copilot)** - Complete best practices

---

## 🔍 Common Use Cases

### Generate Unit Tests
```
/tests for the userService.validateEmail function
```

### Explain Code
```
/explain the authentication flow in this file
```

### Fix Issues
```
/fix the error on line 42
```

### Optimize Performance
```
/optimize this database query for large datasets
```

### Generate Documentation
```
/doc this API with JSDoc comments
```

---

## 💻 Keyboard Shortcuts

| Action | Windows/Linux | Mac |
|--------|---------------|-----|
| Open chat | `Ctrl+Alt+I` | `Cmd+Shift+I` |
| Inline chat | `Ctrl+I` | `Cmd+I` |
| Accept suggestion | `Tab` | `Tab` |
| Reject suggestion | `Esc` | `Esc` |
| Next suggestion | `Alt+]` | `Opt+]` |
| Previous suggestion | `Alt+[` | `Opt+[` |

---

*For complete command reference, see [COMMANDS.md](COMMANDS.md)*
