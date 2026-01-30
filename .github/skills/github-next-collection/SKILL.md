---
name: github-next-collection
description: Collect experimental projects from GitHub Next. Use when fetching research/experimental content or when user asks about GitHub Next features. IMPORTANT - All GitHub Next content must be marked as experimental.
---

# GitHub Next Collection

Fetch experimental research projects from GitHub Next (githubnext.com).

## Prerequisites

Python environment is auto-configured via `.github/workflows/copilot-setup-steps.yml`.

## Usage

```bash
python3 scripts/fetch_github_next.py
```

## Output

Creates `data/github-next/*.json` files containing:
- Project name and description
- Status (Completed, WIP, Napkin sketch, etc.)
- Project URL
- `experimental: true` flag

## CRITICAL: Experimental Content Warning

**ALL GitHub Next content MUST be marked as experimental:**

```markdown
## 🔬 GitHub Next: Experimental Projects

> ⚠️ **Experimental** - These are research projects from GitHub Next.
> Many are discontinued. Not official roadmap or stable features.
```

### Language Requirements

- ✅ Use: "exploring", "experimenting with", "research prototype"
- ❌ Avoid: "will launch", "coming soon", "official feature"

### Content Handling

- Keep separate from official docs/blog content
- Use 🔬 emoji for GitHub Next sections
- Display project status clearly
- Include disclaimer on every reference

## Verification

```bash
# Check data collected
ls data/github-next/*.json | wc -l  # Should have project files

# Verify experimental flag
grep '"experimental": true' data/github-next/*.json
```

## Important Notes

- Script is deterministic
- All projects have `experimental: true` flag
- Status field indicates project maturity
- Many projects are discontinued research
