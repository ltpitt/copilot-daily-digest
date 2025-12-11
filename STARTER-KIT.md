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

## 2a. NEW: AGENTS.md Custom Instructions

**Copilot Coding Agent now supports custom instructions via `AGENTS.md`!**

- You can add an `AGENTS.md` file to your repository to provide advanced, multi-agent instructions and workflows.
- This enables more flexible, team-based, or role-based automation scenarios.
- For details and usage examples, see the official changelog:

📢 [Copilot Coding Agent now supports AGENTS.md custom instructions (2025-08-28)](https://github.blog/changelog/2025-08-28-copilot-coding-agent-now-supports-agents-md-custom-instructions/)

---

## 3. Onboarding Your AI Peer Programmer

📘 [Onboarding Your AI Peer Programmer](https://github.blog/ai-and-ml/github-copilot/onboarding-your-ai-peer-programmer-setting-up-github-to-integrate-github-copilot)
📘 [Get the Best Results](https://docs.github.com/en/enterprise-cloud@latest/copilot/tutorials/coding-agent/get-the-best-results)

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

- 📘 [About Copilot Coding Agent (Official Docs)](https://docs.github.com/en/copilot/concepts/agents/coding-agent/about-coding-agent)
- 🛠️ [Expand Your Team with Copilot (GitHub Skills Course)](https://github.com/skills/expand-your-team-with-copilot/)
- 📋 [GitHub Copilot Cheatsheet](content/cheatsheet.md) - Quick reference for commands and shortcuts
- 📰 [Complete Changelog](content/changelog.md) - Track all updates and new features

These resources are ideal for beginners and teams looking to quickly gain practical experience with Copilot agents.

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
     - `content/changelog.md` - Feature timeline
     - `content/cheatsheet.md` - Quick reference
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
📘 [GitHub Copilot Agent Training](https://learn.microsoft.com/en-us/training/modules/github-copilot-agent)
