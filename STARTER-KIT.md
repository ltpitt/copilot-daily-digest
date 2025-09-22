---
marp: true
---


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
- Use eval-driven development to validate outputs
- Use Copilot Chat for deeper context
- Keep context windows small: split files if needed
- Integrate Copilot Coding Agent into your workflow for automation, collaboration, and productivity—see [5 Ways to Integrate](https://github.blog/ai-and-ml/github-copilot/5-ways-to-integrate-github-copilot-coding-agent-into-your-workflow/)

📘 [Copilot Cheat Sheet](https://docs.github.com/en/copilot/reference/cheat-sheet)
📘 [Mastering GitHub Copilot for Paired Programming](https://github.com/microsoft/Mastering-GitHub-Copilot-for-Paired-Programming)
📘 [5 Ways to Integrate Copilot Coding Agent into Your Workflow](https://github.blog/ai-and-ml/github-copilot/5-ways-to-integrate-github-copilot-coding-agent-into-your-workflow/)

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


## 5. Getting Started

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

These resources are ideal for beginners and teams looking to quickly gain practical experience with Copilot agents.

---

## 7. Further Learning

📘 [Eval-Driven Development](https://vercel.com/blog/eval-driven-development-build-better-ai-faster)
📘 [GitHub Copilot Agent Training](https://learn.microsoft.com/en-us/training/modules/github-copilot-agent)
