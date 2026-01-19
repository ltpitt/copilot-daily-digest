# GitHub AI Starter Kit

> Master GitHub Copilot: From fundamentals to advanced workflows

**Last Updated**: 2026-01-19

---

## Welcome & Mission

This starter kit helps you **master GitHub Copilot** as your AI pair programmer. Whether you're writing your first line of AI-assisted code or optimizing an enterprise workflow, you'll find actionable guidance here.

**What you'll learn**:
- The Copilot landscape: Agent Mode vs Coding Agent
- Battle-tested best practices from docs and blog posts
- Onboarding your AI peer programmer effectively
- Daily workflows that keep you productive

---

## 1. Understand the Landscape

### Two Modes, One Mission

**GitHub Copilot Agent Mode** (in your IDE)
- Your AI pair programmer that offers inline suggestions and chat-based help
- Great for flow-state coding, refactoring, and exploration
- Works in VS Code, JetBrains, Visual Studio, Xcode, Eclipse

**GitHub Copilot Coding Agent** (autonomous agent)
- Executes multi-step tasks using natural language instructions
- Reads `copilot-instructions.md` from your repo for context
- Ideal for automation, scaffolding, and repetitive workflows
- Can make changes across multiple files and open PRs

### When to Use Each

| Use Case | Agent Mode (IDE) | Coding Agent |
|----------|------------------|--------------|
| Writing a function | ✅ Perfect fit | Overkill |
| Refactoring 10 files | ⚠️ Manual work | ✅ Automate it |
| Learning new API | ✅ Ask questions | ❌ Not designed for learning |
| Setting up CI/CD | ⚠️ Tedious | ✅ Describe workflow |

---

## 2. Best Practices

### Write Clear, Scoped Instructions

**For Agent Mode**:
- Be specific and iterative
- Reference open files explicitly
- Use `#file`, `#selection`, `@workspace` keywords

**For Coding Agent**:
- Use structured markdown with clear sections
- Include acceptance criteria
- Specify file paths and constraints

### Start Small, Then Iterate

❌ **Don't**: "Build a complete e-commerce platform"  
✅ **Do**: "Create a product catalog page with search and filtering. Use React and TypeScript."

Then iterate:
- "Add pagination to product catalog"
- "Implement shopping cart with local storage"
- "Add checkout flow with validation"

### Use Spec-Driven Development

Write specifications before code:
1. Create `SPEC.md` with requirements, constraints, examples
2. Ask Copilot to implement according to spec
3. Iterate on spec, not scattered chat messages

**Example spec structure**:
```markdown
## Feature: User Authentication

### Requirements
- JWT-based auth with 24h expiry
- Password hashing with bcrypt (10 rounds)
- Email verification required

### API Endpoints
POST /auth/register - Create account
POST /auth/login - Get JWT token
POST /auth/verify - Confirm email

### Error Handling
- Return 400 for validation errors
- Return 401 for auth failures
- Log all errors to CloudWatch
```

### Use Eval-Driven Development

Create automated evaluations to validate Copilot's output:
1. Write test cases or validation scripts
2. Run them against Copilot's code
3. Share failed tests with Copilot for fixes

### Keep Context Windows Small

- Focus on one task per conversation
- Split large files into modules
- Use clear file/function names
- Delete irrelevant chat history

---

## 3. Onboarding Your AI Peer Programmer

### Essential Resources

- **[Copilot Overview](https://docs.github.com/copilot/about-github-copilot/what-is-github-copilot)** - What Copilot can do
- **[Best Practices Guide](https://docs.github.com/copilot/using-github-copilot/best-practices-for-using-github-copilot)** - Official recommendations
- **[Prompt Engineering](https://docs.github.com/copilot/using-github-copilot/prompt-engineering-for-github-copilot)** - Crafting effective prompts

### Quick Setup Checklist

✅ Install Copilot extension in your IDE  
✅ Sign in with GitHub account  
✅ Try inline suggestions on a test file  
✅ Ask Copilot Chat a simple question  
✅ Review keyboard shortcuts for your IDE  
✅ Create `copilot-instructions.md` for your repo (optional)

---

## 4. Agent Mode vs Coding Agent

| Feature | Agent Mode (IDE) | Coding Agent (GitHub) |
|---------|-----------------|----------------------|
| **Prompting** | Be specific, iterative | Use structured markdown |
| **Context** | Keep files focused | Use repo-wide context |
| **Validation** | Manual review | Automated evals/tests |
| **Scope** | One function or file | One task or workflow |
| **Feedback Loop** | Accept/reject suggestions | Refine instructions iteratively |
| **Best For** | Learning, exploration | Automation, repetitive tasks |

---

## 5. Getting Started: Quick Actions

### Step 1: Choose Your Mode (1 min)

- **New to Copilot?** Start with Agent Mode in your IDE
- **Automating workflows?** Try Coding Agent with a test repo

### Step 2: Set Up Custom Instructions (2 min)

Create `.github/copilot-instructions.md` in your repo:

```markdown
# Project Context

This is a TypeScript microservice using Express and PostgreSQL.

## Code Style
- Use async/await (not callbacks)
- Prefer functional patterns
- All functions must have JSDoc comments

## Testing
- Write tests in `__tests__/` directories
- Use Jest for unit tests
- Aim for 80%+ coverage
```

### Step 3: Start Small, Then Iterate (2 min)

**Try these prompts**:
1. "Explain the authentication flow in this codebase"
2. "Generate unit tests for the userService module"
3. "Refactor this function to use async/await"

### Quick Action Checklist

✅ Try Agent Mode in your IDE  
✅ Create a test repo with `copilot-instructions.md`  
✅ Run a small task with the Coding Agent  
✅ Share learnings with your team  
✅ Track success with evals and feedback loops

---

## 6. Workshop Area: First Steps & Training

### Official GitHub Training

**For Beginners**:
- [Introduction to GitHub Copilot](https://skills.github.com/) - Interactive, 1-2 hours, FREE
- [Code with GitHub Copilot](https://skills.github.com/) - Team collaboration, FREE

**For Advanced Users**:
- [Microsoft Learn: Copilot Fundamentals](https://learn.microsoft.com/training/paths/copilot/) - Self-paced modules
- [GitHub Copilot Certification](https://examregistration.github.com/) - Professional credential, $99

→ See complete catalog: **[TRAININGS.md](TRAININGS.md)**

### Quick References

- **[Commands & Shortcuts](COMMANDS.md)** - Slash commands, keyboard shortcuts
- **[Complete Changelog](CHANGELOG.md)** - Historical timeline
- **[Official Docs Index](REFERENCE.md)** - All documentation links

---

## 7. Daily Workflow

### How This Repository Stays Fresh

**Automated Updates**: Every day at 1 PM UTC, scrapers fetch the latest content:
1. **Fetch Content** - Documentation, blog posts, videos, trainings
2. **Detect Changes** - Compare with previous versions
3. **Generate Content** - Publisher Agent synthesizes updates
4. **Review & Merge** - PR created for human review

**Manual Triggering**:
```bash
# Run scrapers manually
python3 scraper/fetch_docs.py
python3 scraper/fetch_blog.py
python3 scraper/detect_changes.py

# Generate content files
python3 scraper/generate_videos.py
```

---

## 8. Further Learning

### Advanced Topics
- **Eval-Driven Development** - Automated validation of AI output
- **Spec-Driven Development** - Write specs, let AI implement
- **Prompt Engineering** - Craft prompts that get results
- **Custom Instructions** - Tailor Copilot to your codebase

### Community Resources
- [GitHub Community Discussions](https://github.com/orgs/community/discussions/categories/copilot)
- [GitHub Blog - Copilot Tag](https://github.blog/tag/github-copilot/)
- [Copilot Trust Center](https://resources.github.com/copilot-trust-center/)

---

*Ready to dive deeper? Explore [WHATS-NEW.md](WHATS-NEW.md) for the latest features.*
