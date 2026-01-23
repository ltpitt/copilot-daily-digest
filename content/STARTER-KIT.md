# GitHub AI Starter Kit

> Master GitHub Copilot: comprehensive onboarding for engineers

**Last Updated**: January 22, 2026

---

## Welcome & Mission

This starter kit helps you master GitHub Copilot, from understanding the AI landscape to building productive workflows. Whether you're new to AI-assisted coding or looking to optimize your usage, this guide provides the foundation you need.

---

## 1. Understand the Landscape

### Four Tools, One Mission

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

**GitHub Copilot CLI (terminal)** **NEW (Jan 2026)**
- AI assistance directly in your terminal
- Planning capabilities for complex tasks
- Slash commands for testing, fixing, and debugging
- Reasoning models for smarter command suggestions
- Install with: `gh copilot`

**GitHub Copilot SDK (build agents)** **NEW (Jan 2026 - Technical Preview)**
- Programmable layer for building AI agents into any application
- Enables planning, tool invocation, file editing, command execution
- Build custom agents tailored to your workflows
- Simple developer API for agentic AI capabilities
- Use cases: CLI tools, web apps, automation pipelines, custom integrations

**Key Differences**: 
- **Copilot** assists you in real-time as you code
- **Coding Agent** works autonomously on defined tasks
- **Copilot CLI** brings AI to your terminal workflows
- **Copilot SDK** lets you embed agent capabilities into your own applications

---

## 2. Best Practices

### The WRAP Methodology (Dec 2025)

GitHub engineers developed WRAP after using coding agent for over a year. This framework helps you maximize productivity:

**W - Write Effective Issues**
- Write issues as though for someone brand new to the codebase
- Craft descriptive titles explaining where work is being done
- Add examples of what you want (error-handling patterns, code snippets)

**R - Refine Your Instructions**
- **Repository instructions**: Coding standards specific to your repo
- **Organization instructions**: Requirements applying to all repos
- **Custom agents**: Specialized agents for repetitive development tasks

**A - Atomic Tasks**
- Break large problems into small, independent, well-defined tasks
- Example: Instead of "Rewrite 3M lines Java → Golang", break into: "Migrate auth module", "Convert validation utilities", "Rewrite user controllers"

**P - Pair with Coding Agent**
- Humans excel at: Understanding "why", navigating ambiguity, cross-system thinking
- Coding agent excels at: Tireless execution, repetitive tasks, exploring possibilities

→ **Source**: [WRAP up your backlog](https://github.blog/ai-and-ml/github-copilot/wrap-up-your-backlog-with-github-copilot-coding-agent/) (Dec 26, 2025)

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

## 4. Comparison: Copilot vs Coding Agent vs CLI

| Feature | Copilot (IDE) | Coding Agent | Copilot CLI |
|---------|--------------|--------------|-------------|
| **Location** | Your IDE | GitHub/IDE Agent Mode | Terminal |
| **Prompting** | Conversational, iterative | Structured task description | Commands & natural language |
| **Context** | Open files, editor state | Repository-wide | Terminal history, filesystem |
| **Validation** | Manual review | Can include automated tests | Manual review |
| **Scope** | Single function/file | Multi-file tasks | Terminal commands & scripts |
| **Workflow** | Interactive pair programming | Autonomous task execution | Terminal assistance |
| **Best For** | Real-time coding, learning | Scaffolding, automation | CLI workflows, debugging |
| **Key Feature** | Inline suggestions | Multi-step task planning | Planning before execution |

**When to use each**:
- **IDE Copilot**: Writing code, refactoring, learning new patterns
- **Coding Agent**: Complex multi-file tasks, scaffolding, automation
- **Copilot CLI**: Terminal workflows, debugging commands, script generation

---

## 5. Getting Started: Quick Actions

### Quick Action Checklist

✅ Install Copilot extension in your IDE  
✅ Install Copilot CLI with `gh copilot` (NEW!)  
✅ Try inline suggestions on a simple function  
✅ Ask Copilot Chat to explain unfamiliar code  
✅ Use `/tests` to generate test cases  
✅ Experiment with different AI models (GPT, Claude, Gemini)  
✅ Enable Auto Model Selection in VS Code  
✅ Try Agent Mode for a multi-file refactoring task  
✅ Use Copilot CLI for terminal tasks (NEW!)

### Your First Week with Copilot

**Day 1**: Installation and inline suggestions
- Install extension, authenticate
- Install Copilot CLI with `gh copilot`
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

**Day 4**: Copilot CLI workflows (NEW!)
- Try `gh copilot` in terminal
- Use planning mode for complex tasks
- Experiment with CLI slash commands
- [Review CLI cheat sheet](https://github.blog/ai-and-ml/github-copilot/a-cheat-sheet-to-slash-commands-in-github-copilot-cli/)

**Day 5**: Model selection
- Try different AI models
- Enable Auto Model Selection
- Compare results for different tasks

**Day 6**: Agent Mode
- Use Agent Mode for a small feature
- Review multi-file changes
- Refine your task descriptions

---

## 6. Workshop Area: Training & Learning

### Official GitHub Training

**Free Interactive Courses**:
- [Getting Started with GitHub Copilot](https://github.com/skills/getting-started-with-github-copilot) - Beginner, 1-2 hours
- [Expand Your Team with Copilot](https://github.com/skills/expand-your-team-with-copilot) - Intermediate

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
