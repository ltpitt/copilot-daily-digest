# GitHub Copilot: Your Daily Companion

> Last updated: December 9, 2025 | 📰 14 documentation updates this week

## 🚀 Quick Start in 5 Minutes

### Step 1: Choose Your Mode (1 min)
**GitHub Copilot Agent Mode** (in your IDE)
- Your AI pair programmer for inline suggestions and code completions
- Great for flow-state coding and real-time refactoring

**GitHub Copilot Coding Agent** (autonomous agent)
- Executes multi-step tasks using natural language instructions
- Ideal for automation, scaffolding, and repetitive workflows

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

## 📰 What's New This Week

**Model Picker for Coding Agent** (December 8, 2025)
- Pro and Pro+ subscribers can now choose their preferred AI model when starting coding agent tasks
- Select from Claude Sonnet, GPT-4, and other premium models for specialized workloads
→ [Learn more](https://github.blog/changelog/2025-12-08-model-picker-for-copilot-coding-agent-for-copilot-pro-and-pro-subscribers)

**Enterprise Team Limits Increased 10x** (December 8, 2025)
- Team product limits now significantly higher for enterprise customers
- Enables larger-scale deployments and automation workflows
→ [Read announcement](https://github.blog/changelog/2025-12-08-enterprise-teams-product-limits-increased-by-over-10x)

**Track Code Generation Metrics** (December 5, 2025)
- New dashboard to monitor Copilot code generation metrics
- Measure adoption, productivity impact, and usage patterns across your organization
→ [View dashboard features](https://github.blog/changelog/2025-12-05-track-copilot-code-generation-metrics-in-a-dashboard)

**GPT-5.1 Codex Max in Public Preview** (December 4, 2025)
- OpenAI's latest model now available for GitHub Copilot users
- Enhanced code understanding and generation capabilities
→ [Try it now](https://github.blog/changelog/2025-12-04-openais-gpt-5-1-codex-max-is-now-in-public-preview-for-github-copilot)

**Claude Opus 4.5 Available** (December 3, 2025)
- Now accessible in Visual Studio, JetBrains IDEs, Xcode, and Eclipse
- Improved reasoning and context handling for complex codebases
→ [Get started](https://github.blog/changelog/2025-12-03-claude-opus-4-5-is-now-available-in-visual-studio-jetbrains-ides-xcode-and-eclipse)

## 💡 Best Practices

### Write Clear Instructions
**Good**: "Add Redis caching to userSessionService with 30s TTL for getUserById method"
**Bad**: "Make it faster"

Be specific about what, where, and how. Include constraints and acceptance criteria.

### Use Spec-Driven Development
1. Define the specification first (what success looks like)
2. Let Copilot implement based on specs
3. Validate outputs against specifications
4. Iterate based on results

📘 [Spec-driven development toolkit](https://github.com/github/spec-kit)

### Keep Context Focused
- Split large files into smaller, focused modules
- Use clear naming conventions
- Leverage `copilot-instructions.md` for project-wide context
- Reference specific files or code sections in your prompts

### Iterate in Small Steps
Break complex tasks into smaller increments:
1. Generate test cases first
2. Implement core logic
3. Add error handling
4. Optimize performance
5. Document changes

Each step should be reviewable and testable.

### Integrate Into Your Workflow
- Use Copilot Chat for exploratory questions
- Leverage Coding Agent for repetitive scaffolding
- Combine with CI/CD for automated testing
- Track metrics to measure productivity impact

📘 [5 Ways to Integrate Copilot into Your Workflow](https://github.blog/ai-and-ml/github-copilot/5-ways-to-integrate-github-copilot-coding-agent-into-your-workflow/)

### Validate with Evals
Set up automated evaluation workflows:
- Unit test coverage metrics
- Code quality checks (linting, type safety)
- Performance benchmarks
- Security scanning

📘 [Eval-Driven Development](https://vercel.com/blog/eval-driven-development-build-better-ai-faster)

## 🎥 Featured Videos

### GitHub Copilot Spaces: Debug Issues Faster
[![Debug with Copilot Spaces](https://img.youtube.com/vi/dlgYCpQI_lU/maxresdefault.jpg)](https://www.youtube.com/watch?v=dlgYCpQI_lU)

Learn how to use GitHub Copilot Spaces for faster debugging workflows.

[Watch on YouTube →](https://www.youtube.com/watch?v=dlgYCpQI_lU)

### Orchestrate Agents Using Mission Control
[![Mission Control Overview](https://img.youtube.com/vi/X9jbNK1006E/maxresdefault.jpg)](https://www.youtube.com/watch?v=X9jbNK1006E)

Master agent orchestration with GitHub Copilot's Mission Control features.

[Watch on YouTube →](https://www.youtube.com/watch?v=X9jbNK1006E)

### More Videos
- [Writing Great AGENTS.md Files](https://www.youtube.com/watch?v=boviC841YWs)
- [Copilot CLI 101](https://www.youtube.com/watch?v=8hyvYP5PCks)
- [Building GitHub Platform with Copilot](https://www.youtube.com/watch?v=dI4H5ZyYOx0)
- [Developer's Guide to Shipping Faster](https://www.youtube.com/watch?v=LwqUp4Dc1mQ)

## 📚 Quick Links

- [Complete Reference](REFERENCE.md) - Full documentation and changelog
- [Changelog](changelog.md) - Timeline of features and updates
- [Cheatsheet](cheatsheet.md) - Quick reference for commands and shortcuts
- [Official Docs](https://docs.github.com/copilot) - GitHub Copilot documentation
- [GitHub Skills Course](https://github.com/skills/expand-your-team-with-copilot/) - Hands-on learning
- [Mastering GitHub Copilot](https://github.com/microsoft/Mastering-GitHub-Copilot-for-Paired-Programming) - Comprehensive guide

---

**Need more?** Check out the [Changelog](changelog.md) for a detailed timeline, [Cheatsheet](cheatsheet.md) for quick commands, or [Complete Reference](REFERENCE.md) for comprehensive documentation.
