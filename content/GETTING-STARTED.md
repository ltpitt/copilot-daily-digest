# Getting Started with GitHub Copilot

> Your 5-minute guide to productive AI pair programming

**Last Updated**: 2025-12-15

---

## Quick Setup

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

Press `Enter` - Copilot suggests the implementation. Press `Tab` to accept.

### 3. Use Chat for Complex Tasks

Press `Ctrl+I` (Windows/Linux) or `Cmd+I` (Mac) to open inline chat:
```
Explain this codebase structure and list any failing tests
```

### 4. Enable Advanced Features (Optional)

**Copilot Edits**: Multi-file editing capability  
**Agent Mode**: Autonomous multi-step task completion  
**Model Selection**: Choose different AI models for specific tasks

---

## Best Practices

### 1. Start General, Then Get Specific

❌ **Don't**: "Make a function"  
✅ **Do**: "Write a JavaScript function that tells me if a number is prime. The function should take an integer and return true if the integer is prime. The function should error if the input is not a positive integer."

**Why it matters**: Specific prompts help Copilot understand your exact requirements and generate more accurate code.

→ Source: [Prompt Engineering for GitHub Copilot](https://docs.github.com/en/copilot/using-github-copilot/prompt-engineering-for-github-copilot)

### 2. Provide Examples in Your Prompts

❌ **Don't**: "Parse dates from a string"  
✅ **Do**: 
```
Write a Go function that finds all dates in a string and returns them in an array. 
Dates can be formatted like:
* 05/02/24
* 05-02-2024
* 5/2/24

Example: findDates("appointment on 11/14/2023 and book club on 12-1-23")
Returns: ["11/14/2023", "12-1-23"]
```

**Why it matters**: Examples eliminate ambiguity and show Copilot exactly what output format you expect.

→ Source: [Prompt Engineering for GitHub Copilot](https://docs.github.com/en/copilot/using-github-copilot/prompt-engineering-for-github-copilot)

### 3. Break Complex Tasks into Simpler Steps

❌ **Don't**: "Build a word search puzzle game"  
✅ **Do**: 
1. Write a function to generate a 10 by 10 grid of letters
2. Write a function to find all words in a grid of letters, given a list of valid words
3. Update the previous function to print the grid and 10 random words

**Why it matters**: Copilot performs better with focused, single-purpose requests than complex multi-step tasks.

→ Source: [Prompt Engineering for GitHub Copilot](https://docs.github.com/en/copilot/using-github-copilot/prompt-engineering-for-github-copilot)

### 4. Use the Right Tool for the Job

**Inline Suggestions** work best for:
- Completing code snippets, variable names, and functions as you write
- Generating repetitive code
- Generating tests for test-driven development

**Copilot Chat** is best suited for:
- Answering questions about code in natural language
- Generating large sections of code, then iterating
- Accomplishing specific tasks with slash commands (`/tests`, `/fix`, `/explain`)
- Code reviews and explanations

→ Source: [Best Practices for Using GitHub Copilot](https://docs.github.com/en/copilot/using-github-copilot/best-practices-for-using-github-copilot)

### 5. Always Verify Copilot's Suggestions

**Critical checks**:
- ✅ Understand the code before implementing it (ask Copilot to explain if needed)
- ✅ Review for functionality, security, readability, and maintainability
- ✅ Use automated tests and linting to validate suggestions
- ✅ Check for similarities to existing public code (optional setting available)

**Why it matters**: Copilot is a powerful tool, but you are ultimately responsible for the code you write.

→ Source: [Best Practices for Using GitHub Copilot](https://docs.github.com/en/copilot/using-github-copilot/best-practices-for-using-github-copilot)

### 6. Provide Relevant Context

**In your IDE**:
- ✅ Open relevant files, close irrelevant ones
- ✅ Use descriptive names for variables and functions
- ✅ Add comments to explain complex logic
- ✅ Follow consistent code style and patterns

**In Copilot Chat**:
- ✅ Use `@workspace` to reference your codebase
- ✅ Use `#file` or `#selection` to reference specific code
- ✅ Delete old chat messages that are no longer relevant
- ✅ Start a new chat thread for unrelated tasks

**Why it matters**: Copilot uses surrounding context to generate better suggestions. Clean, well-structured code produces better results.

→ Source: [Prompt Engineering for GitHub Copilot](https://docs.github.com/en/copilot/using-github-copilot/prompt-engineering-for-github-copilot)

### 7. Iterate and Experiment

**If you don't get the result you want**:
- Rephrase your prompt with different wording
- Add more specific requirements or constraints
- Provide additional examples
- Break the request into smaller steps
- Use keyboard shortcuts to cycle through multiple suggestions (`Alt+]` / `Opt+]`)

**Why it matters**: Prompt engineering is an iterative process. Small changes to your prompt can yield significantly different results.

→ Source: [Prompt Engineering for GitHub Copilot](https://docs.github.com/en/copilot/using-github-copilot/prompt-engineering-for-github-copilot)

---

## Quick Reference: Slash Commands

Type `/` in Copilot Chat to access these commands:

| Command | Purpose | Example |
|---------|---------|---------|
| `/explain` | Explain code or concepts | `/explain how async/await works` |
| `/fix` | Suggest fixes for problems | `/fix this bug` |
| `/tests` | Generate unit tests | `/tests for authentication module` |
| `/doc` | Generate documentation | `/doc this API` |
| `/optimize` | Improve code performance | `/optimize this function` |

For complete command reference, see **[COMMANDS.md](COMMANDS.md)**

---

## Next Steps

- **[Watch tutorials](VIDEOS.md)** - Learn from video demos and walkthroughs
- **[Take courses](TRAININGS.md)** - Official GitHub Skills courses and certifications
- **[Explore updates](WHATS-NEW.md)** - See the latest features and improvements
- **[Read the full documentation](REFERENCE.md)** - Deep dive into all Copilot features

---

*For advanced techniques and deep integration, see [STARTER-KIT.md](STARTER-KIT.md)*
