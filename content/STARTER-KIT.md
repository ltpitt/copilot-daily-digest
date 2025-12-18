# GitHub AI Starter Kit

## Welcome & Mission
Mastering GitHub Copilot Coding Agent is our journey.

The key for this journey is doing the right thing and doing this right thing right.

_For this reason this starter kit distills essential knowledge, common pitfalls, best practices, cheat sheets, how-tos, examples, and shortcuts to help us succeed._

---

## 1. Understand the Landscape
### 🔹 Two Modes, One Mission

**GitHub Copilot Agent Mode** (in your IDE)
- Your AI pair programmer
- Offers inline suggestions, code completions, and chat-based help
- Great for flow-state coding, refactoring, and exploration

**GitHub Copilot Coding Agent** (autonomous agent)
- Executes multi-step tasks using natural language instructions
- Operates on GitHub repos, reads `copilot-instructions.md`, and iterates
- Ideal for automation, scaffolding, and repetitive workflows

📖 [Less To-Do, More Done: The Difference Between Coding Agent and Agent Mode](https://github.blog/developer-skills/github/less-todo-more-done-the-difference-between-coding-agent-and-agent-mode-in-github-copilot)

---



## 2. Best Practices

- Write clear, scoped, testable instructions in `copilot-instructions.md` (or, for advanced multi-agent workflows, use `AGENTS.md`—see [changelog](https://github.blog/changelog/2025-08-28-copilot-coding-agent-now-supports-agents-md-custom-instructions/))
- **NEW (Dec 2025)**: Use Agent Skills to teach Copilot specialized, repeatable tasks ([learn more](https://docs.github.com/copilot/concepts/agents/about-agent-skills))
- Start with small tasks, then iterate
- Use the spec-drive development
- Use eval-driven development to validate outputs
- Use Copilot Chat for deeper context
- Keep context windows small: split files if needed
- Integrate Copilot Coding Agent into your workflow for automation, collaboration, and productivity—see [5 Ways to Integrate](https://github.blog/ai-and-ml/github-copilot/5-ways-to-integrate-github-copilot-coding-agent-into-your-workflow/)

📘 [Copilot Cheat Sheet](https://docs.github.com/en/copilot/reference/cheat-sheet)
📘 [Mastering GitHub Copilot for Paired Programming](https://github.com/microsoft/Mastering-GitHub-Copilot-for-Paired-Programming)
📘 [5 Ways to Integrate Copilot Coding Agent into Your Workflow](https://github.blog/ai-and-ml/github-copilot/5-ways-to-integrate-github-copilot-coding-agent-into-your-workflow/)
📘 [Spec-driven development toolkit](https://github.com/github/spec-kit)

---

## 2a. NEW: Agent Skills (December 2025)

**Copilot now supports Agent Skills - reusable, specialized task instructions!**

Agent Skills are folders containing instructions, scripts, and resources that Copilot automatically loads when relevant to your prompt.

**Key Features**:
- Create custom skills for your team's specific workflows
- Copilot automatically determines when to use each skill
- Works across Copilot coding agent, Copilot CLI, and agent mode in VS Code Insiders
- Compatible with Claude Code skills (`.claude/skills` directory)
- Share skills via repositories like [`anthropics/skills`](https://github.com/anthropics/skills) or [`github/awesome-copilot`](https://github.com/github/awesome-copilot)

**Example Use Cases**:
- Consistent code review standards across your team
- Specialized testing patterns for your domain
- Custom deployment workflows
- Domain-specific architectural patterns

📢 [Announcing Agent Skills (Dec 18, 2025)](https://github.blog/changelog/2025-12-18-github-copilot-now-supports-agent-skills)
📘 [Agent Skills Documentation](https://docs.github.com/copilot/concepts/agents/about-agent-skills)

---

## 2b. AGENTS.md Custom Instructions

**Copilot Coding Agent now supports custom instructions via `AGENTS.md`!**

- You can add an `AGENTS.md` file to your repository to provide advanced, multi-agent instructions and workflows.
- This enables more flexible, team-based, or role-based automation scenarios.
- For details and usage examples, see the official changelog:

📢 [Copilot Coding Agent now supports AGENTS.md custom instructions (2025-08-28)](https://github.blog/changelog/2025-08-28-copilot-coding-agent-now-supports-agents-md-custom-instructions/)

---

## 3. Onboarding Your AI Peer Programmer

📘 [Get the Best Results](https://docs.github.com/en/enterprise-cloud@latest/copilot/tutorials/coding-agent/get-the-best-results)
📘 [GitHub Copilot Documentation](https://docs.github.com/en/copilot)

---

## 4. Agent Mode vs Coding Agent

| Feature        | Agent Mode (IDE)         | Coding Agent (GitHub)         |
|---------------|--------------------------|-------------------------------|
| Prompting     | Be specific, iterative   | Use structured markdown       |
| Context       | Keep files focused       | Use repo-wide context         |
| Validation    | Manual review            | Automated evals/tests         |
| Scope         | One function or file     | One task or workflow          |
| Feedback Loop | Accept/reject suggestions| Refine instructions iteratively|

---


## 5. Getting Started: Quick Start in 5 Minutes

### Step 1: Choose Your Mode (1 min)

**GitHub Copilot Agent Mode** (in your IDE)
- Your AI pair programmer for inline suggestions and code completions
- Great for flow-state coding and real-time refactoring
- Works directly in your editor with context-aware suggestions

**GitHub Copilot Coding Agent** (autonomous agent)
- Executes multi-step tasks using natural language instructions
- Ideal for automation, scaffolding, and repetitive workflows
- Operates on GitHub repos with full project context

📖 [Understanding the Difference](https://github.blog/developer-skills/github/less-todo-more-done-the-difference-between-coding-agent-and-agent-mode-in-github-copilot)

### Step 2: Set Up Custom Instructions (2 min)

Create `copilot-instructions.md` in your repo root:

```markdown
# Project Context
This is a [your project type] built with [your stack].

# Code Style
- Use TypeScript with strict mode
- Follow functional programming patterns
- Write tests for all new features

# Preferences
- Prefer async/await over promises
- Use meaningful variable names
- Add JSDoc comments for public APIs
```

For advanced multi-agent workflows, use `AGENTS.md` instead.

📢 [AGENTS.md Custom Instructions](https://github.blog/changelog/2025-08-28-copilot-coding-agent-now-supports-agents-md-custom-instructions/)

### Step 3: Start Small, Then Iterate (2 min)

Begin with focused tasks:
- "Generate unit tests for the userService module"
- "Refactor authentication logic to use async/await"
- "Add TypeScript types to all API endpoints"

Avoid broad requests like "rewrite entire app" - small increments win.

### Quick Action Checklist

✅ Try Agent Mode in your IDE  
✅ Create a test repo with `copilot-instructions.md`  
✅ Run a small task with the Coding Agent  
✅ Share learnings and refine prompts  
✅ Track success with evals and feedback loops  

---

## 6. Workshop Area: First Steps & Actions

Jumpstart your Copilot Coding Agent journey with hands-on learning:

### Official GitHub Trainings

**GitHub Skills (Interactive)**
- 🛠️ [Expand Your Team with Copilot](https://github.com/skills/expand-your-team-with-copilot/) - Intermediate (2-3 hours)
  - Hands-on course covering code generation, testing, and collaboration
- 🛠️ [Code with GitHub Copilot](https://github.com/skills/copilot-codespaces-vscode) - Beginner (1-2 hours)
  - Get started with AI-assisted coding and best practices

**Microsoft Learn (Self-Paced)**
- 📘 [Introduction to GitHub Copilot](https://learn.microsoft.com/en-us/training/modules/introduction-to-github-copilot/) - Beginner (30 min)
  - Discover AI-powered code suggestions and workflow integration
- 📘 [GitHub Copilot Fundamentals](https://learn.microsoft.com/en-us/training/paths/copilot/) - Intermediate (2-3 hours)
  - Master prompts, chat features, testing, and documentation
- 📘 [Challenge: Build a Minigame with Copilot](https://learn.microsoft.com/en-us/training/modules/challenge-project-create-mini-game-with-copilot/) - Intermediate (1-2 hours)
  - Hands-on C# project to demonstrate Copilot proficiency

### Certifications

- 🏆 [GitHub Foundations Certification](https://resources.github.com/learn/certifications/) - Industry-recognized
  - Validates knowledge of GitHub fundamentals including Copilot usage
  - Preparation: 20-40 hours

### Third-Party Resources

**Community Courses (Check Corporate Access)**
- 🎥 Search platforms like Udemy, Coursera, Pluralsight for updated Copilot courses
  - Note: Many companies provide corporate accounts for free access
  - Always verify course recency (updated within last 6 months)

### Quick References

- 📋 [Commands & Shortcuts](COMMANDS.md) - Quick reference for commands and shortcuts
- 📰 [Complete Changelog](CHANGELOG.md) - Track all updates and new features
- 📘 [About Copilot Coding Agent (Official Docs)](https://docs.github.com/en/copilot/concepts/agents/coding-agent/about-coding-agent)

---

## 7. Daily Workflow

### 🔄 Automated Content Updates

The repository updates automatically via GitHub Actions:

**Schedule**: Daily at 1 PM UTC (configurable in `.github/workflows/daily-agent.yml`)

#### Workflow Steps

1. **📥 Fetch Content** 
   - GitHub Docs (official documentation)
   - GitHub Blog (RSS feed)
   - YouTube Videos (RSS with optional API enrichment)

2. **🔍 Detect Changes**
   - Compare with previous versions using metadata tracking
   - Identify new documentation, blog posts, and videos
   - Track what's changed in existing content
   - Generate comprehensive change summary

3. **📝 Generate Content** (only if changes detected)
   - Publisher Agent receives automated issue
   - Agent reads all data from `data/` directory
   - Agent generates or updates:
     - `content/README.md` - Main digest with highlights
     - `content/CHANGELOG.md` - Feature timeline
     - `content/COMMANDS.md` - Quick reference
     - `content/videos.md` - Video library
   - Agent creates PR with all updates

4. **✅ Review & Merge**
   - Review PR created by Publisher Agent
   - Verify changes and quality
   - Merge when ready
   - Updated content goes live

#### Quality Over Speed

The workflow prioritizes **content quality** over execution time. While most runs complete in a few minutes, complex updates may take longer—and that's perfectly fine! The focus is on delivering accurate, well-organized, and valuable content.

#### Manual Triggering

You can trigger the workflow manually:

```bash
# Using GitHub CLI
gh workflow run daily-agent.yml

# Monitor progress
gh run list --workflow=daily-agent.yml
gh run view
```

Or via GitHub UI: Actions → Daily Copilot Digest → Run workflow

#### Status & Monitoring

- **Workflow Badge**: Check the status badge at the top of README.md
- **Action Logs**: View detailed logs in the Actions tab
- **Change Summary**: Review `data/changes-summary.json` for latest changes
- **No Changes**: If no updates detected, workflow completes without creating an issue

---

## 8. Further Learning

📘 [Eval-Driven Development](https://vercel.com/blog/eval-driven-development-build-better-ai-faster)
📘 [Introduction to GitHub Copilot](https://learn.microsoft.com/en-us/training/modules/introduction-to-github-copilot/)
