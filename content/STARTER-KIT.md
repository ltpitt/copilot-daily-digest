# GitHub AI Starter Kit

> Master GitHub Copilot: comprehensive onboarding for engineers

**Last Updated**: December 22, 2025

---

## Welcome & Mission

This starter kit helps you master GitHub Copilot, from understanding the AI landscape to building productive workflows. Whether you're new to AI-assisted coding or looking to optimize your usage, this guide provides the foundation you need.

---

## 1. Understand the Landscape

### Two Modes, One Mission

**GitHub Copilot (in your IDE)**
- Your AI pair programmer
- Offers inline suggestions, code completions, and chat-based help
- Great for flow-state coding, refactoring, and exploration
- Available in VS Code, JetBrains, Visual Studio, Xcode, Eclipse

**GitHub Copilot Coding Agent (autonomous)**
- Executes multi-step tasks using natural language instructions
- Can read repository context, make changes across multiple files
- Ideal for scaffolding, automation, and repetitive workflows
- Operates on GitHub repositories or through IDE agent mode

**Key Difference**: Copilot assists you in real-time as you code. Coding Agent works autonomously on defined tasks.

---

## 2. Best Practices

### Understand Copilot's Strengths

Copilot excels at:
- Writing tests and repetitive code
- Debugging and correcting syntax
- Explaining and commenting code
- Generating regular expressions
- Translating natural language to code

Copilot is not designed to:
- Replace your expertise and judgment
- Respond to non-coding prompts
- Make architectural decisions without your guidance

### Choose the Right Tool

**Use inline suggestions for**:
- Completing code snippets as you type
- Generating repetitive code patterns
- Writing tests in test-driven development
- Auto-completing variable names and functions

**Use Copilot Chat for**:
- Answering questions about code
- Generating large sections of code
- Using slash commands for common tasks (/explain, /fix, /tests)
- Working with specific chat participants (@workspace, @github)

**Use Agent Mode for**:
- Multi-file refactoring
- Scaffolding new features
- Automated code transformations
- Tasks requiring multiple coordinated steps

### Create Thoughtful Prompts

**Break down complex tasks**:
- Instead of "Build authentication system"
- Try: "Create user registration endpoint" → "Add JWT generation" → "Implement password reset flow"

**Be specific about requirements**:
- Include: expected inputs, desired outputs, constraints, error handling needs
- Example: "Create a rate limiter that allows 100 requests per minute per user, returning 429 status when exceeded"

**Provide examples**:
- Show sample input/output data
- Reference similar existing implementations
- Include edge cases to handle

**Follow good coding practices**:
- Ask for tests alongside code
- Request documentation for complex logic
- Specify security requirements (input validation, sanitization)

### Check Copilot's Work

**Understand before implementing**:
- Read suggested code thoroughly
- Ask Copilot to explain complex sections: `/explain`
- Verify the logic matches your requirements

**Review carefully**:
- Functionality: Does it do what you expect?
- Security: Any SQL injection, XSS, or other vulnerabilities?
- Maintainability: Is it readable and well-structured?
- Performance: Any obvious inefficiencies?

**Use automated testing**:
- Run existing tests after accepting suggestions
- Generate new tests: `/tests`
- Use linters and code scanners
- Enable Copilot Autofix for security issues

### Guide Copilot Towards Better Outputs

**Provide helpful context**:
- Open relevant files in your IDE
- Include configuration files if relevant
- Reference similar working code
- Use chat variables (#file, #selection, #codebase)

**Use keywords and chat participants**:
- `@workspace` for repository-wide context
- `@github` for GitHub-specific features
- `@terminal` for command-line help
- Slash commands: `/explain`, `/fix`, `/tests`, `/doc`

**Iterate on responses**:
- "Make this more efficient"
- "Add error handling for network failures"
- "Refactor to use modern async/await syntax"
- "Add TypeScript types"

---

## 3. Onboarding Your AI Peer Programmer

### Get Started in 5 Minutes

1. **Install Copilot** in your preferred IDE
2. **Authenticate** with your GitHub account
3. **Try inline suggestions** - Start typing and watch Copilot suggest completions
4. **Open chat** (`Ctrl+I` or `Cmd+I`) and ask a question
5. **Review and accept** suggestions that fit your needs

### Official Resources

- [GitHub Copilot Quickstart](https://docs.github.com/en/copilot/quickstart)
- [Guides on Using GitHub Copilot](https://docs.github.com/en/copilot/using-github-copilot/guides-on-using-github-copilot)
- [Best Practices Guide](https://docs.github.com/en/copilot/using-github-copilot/best-practices-for-using-github-copilot)

---

## 4. Agent Mode vs Coding Agent

| Feature | Copilot (IDE) | Coding Agent |
|---------|--------------|--------------|
| **Location** | Your IDE | GitHub/IDE Agent Mode |
| **Prompting** | Conversational, iterative | Structured task description |
| **Context** | Open files, editor state | Repository-wide |
| **Validation** | Manual review | Can include automated tests |
| **Scope** | Single function/file | Multi-file tasks |
| **Workflow** | Interactive pair programming | Autonomous task execution |
| **Best For** | Real-time coding, learning | Scaffolding, automation |

---

## 5. Getting Started: Quick Actions

### Quick Action Checklist

✅ Install Copilot extension in your IDE  
✅ Try inline suggestions on a simple function  
✅ Ask Copilot Chat to explain unfamiliar code  
✅ Use `/tests` to generate test cases  
✅ Experiment with different AI models (GPT, Claude, Gemini)  
✅ Enable Auto Model Selection in VS Code  
✅ Try Agent Mode for a multi-file refactoring task

### Your First Week with Copilot

**Day 1**: Installation and inline suggestions
- Install extension, authenticate
- Write simple functions with inline suggestions
- Practice accepting/rejecting suggestions

**Day 2**: Copilot Chat basics
- Learn keyboard shortcuts (`Ctrl+I`, `Ctrl+Shift+I`)
- Ask questions about your codebase
- Use `/explain` on complex code

**Day 3**: Slash commands and chat participants
- Try `/fix`, `/tests`, `/doc`
- Use `@workspace` for repo context
- Experiment with chat variables (#file, #selection)

**Day 4**: Model selection
- Try different AI models
- Enable Auto Model Selection
- Compare results for different tasks

**Day 5**: Agent Mode
- Use Agent Mode for a small feature
- Review multi-file changes
- Refine your task descriptions

---

## 6. Workshop Area: Training & Learning

### Official GitHub Training

**Free Interactive Courses**:
- [Introduction to GitHub Copilot](https://github.com/skills/copilot-intro) - Beginner, 1-2 hours
- [Using GitHub Copilot with Team Collaboration](https://github.com/skills/copilot-team) - Intermediate

**Microsoft Learn Modules**:
- [Introduction to GitHub Copilot](https://learn.microsoft.com/en-us/training/modules/introduction-to-github-copilot/) - 30 minutes
- [GitHub Copilot Fundamentals](https://learn.microsoft.com/en-us/training/paths/copilot/) - Self-paced learning path

### Certifications

**GitHub Foundations Certification**
- Includes Copilot usage, best practices, collaboration
- Preparation: 20-40 hours
- [Learn more](https://resources.github.com/learn/certifications/)

### More Resources

For complete training catalog, see **[TRAININGS.md](TRAININGS.md)**

---

## 7. Daily Workflow

### How This Repository Stays Updated

**Automated Content Pipeline**:
1. **Scrapers run daily** at 1 PM UTC
   - Fetch documentation from docs.github.com
   - Collect blog posts from github.blog
   - Track video content from GitHub YouTube
   - Monitor training courses

2. **Change detection** identifies what's new
   - Compare file hashes
   - Detect new blog posts
   - Track documentation updates

3. **Content generation** synthesizes updates
   - Publisher Agent creates modular content files
   - WHATS-NEW.md highlights recent changes
   - CHANGELOG.md maintains complete history

4. **Review and merge** via pull requests

### Manual Triggering

You can manually trigger updates by running:
```bash
pip install -r requirements.txt
python3 scraper/fetch_docs.py
python3 scraper/fetch_blog.py
python3 scraper/detect_changes.py
```

---

## 8. Further Learning

### Advanced Topics

- **Prompt Engineering**: [Prompt engineering for GitHub Copilot](https://docs.github.com/en/copilot/using-github-copilot/prompt-engineering-for-github-copilot)
- **Custom Instructions**: [Add custom instructions](https://docs.github.com/en/copilot/customizing-copilot/adding-custom-instructions-for-github-copilot)
- **Extensions**: [About Copilot Extensions](https://docs.github.com/en/copilot/using-github-copilot/using-extensions-to-integrate-external-tools-with-copilot-chat)
- **Responsible Use**: [Responsible use of GitHub Copilot](https://docs.github.com/en/copilot/responsible-use-of-github-copilot-features)

### Community & Support

- [GitHub Community Discussions](https://github.com/orgs/community/discussions/categories/copilot)
- [Copilot Changelog](https://github.blog/changelog/label/copilot/)
- [GitHub Blog - Copilot](https://github.blog/tag/github-copilot/)

---

*Ready to dive deeper? Explore [WHATS-NEW.md](WHATS-NEW.md) for the latest features and updates.*
