---
name: content-generation
description: Video categorization and experimental content guidelines for publisher agent
---

# Content Generation Guidelines

This skill provides categorization rules and formatting guidelines for auto-generated content sections.

## Video Categorization

When the @publisher agent generates VIDEOS.md, use these keyword-based categories:

### Category Keywords (Priority Order)

1. **Getting Started**
   - Keywords: "getting started", "intro", "introduction", "basics", "beginner", "first steps"
   
2. **Features & Updates**
   - Keywords: "feature", "new feature", "announcement", "release", "introducing", "update", "changelog", "what's new", "improvements", "version"

3. **Tutorials**
   - Keywords: "tutorial", "how to", "guide", "walkthrough", "demo", "learn"

4. **Agents**
   - Keywords: "agent", "coding agent", "workspace agent", "autonomous", "multi-file", "agentic"

5. **Extensions**
   - Keywords: "extension", "plugin", "integrate", "integration", "api", "vscode", "jetbrains"

6. **Other**
   - Catch-all for uncategorized videos

### Categorization Logic

```python
def categorize_video(title: str, description: str) -> str:
    """Categorize video based on title and description keywords."""
    content = f"{title.lower()} {description.lower()}"
    
    for category, keywords in CATEGORIES.items():
        if category == "Other":
            continue
        for keyword in keywords:
            if keyword in content:
                return category
    
    return "Other"  # Default if no match
```

## Experimental Content Guidelines

### GitHub Next Disclaimer Template

**Always include at top of EXPERIMENTAL.md:**

```markdown
> **About GitHub Next**: GitHub's research and development lab exploring the future of software development. These are experimental prototypes, not production features. Availability and functionality may change without notice.

**⚠️ Important**: Projects listed here are research experiments. Many have been discontinued or remain in early exploration. They do not represent GitHub's official product roadmap.
```

### Experimental Language Examples

✅ **Use these phrases:**
- "exploring the possibility of..."
- "experimenting with..."
- "research prototype investigating..."
- "early-stage exploration of..."
- "proof-of-concept for..."

❌ **Avoid these phrases:**
- "will be released"
- "coming soon to production"
- "official GitHub feature"
- "launching in Q2"
- "roadmap includes..."

## Quality Checks

### For VIDEOS.md:
- [ ] All videos categorized (no empty categories if videos match)
- [ ] Chronological order within categories (newest first)
- [ ] Recent uploads section (last 30 days) highlighted
- [ ] Statistics accurate
- [ ] YouTube embeds work

### For EXPERIMENTAL.md:
- [ ] Disclaimer present at top
- [ ] All projects marked with 🔬 or 🧪
- [ ] Status clearly indicated
- [ ] Experimental language throughout
- [ ] Active/Archived separation clear

## Reference

This skill replaced the deprecated `scripts/generate_videos.py` Python script.
All content generation is now handled by the @publisher agent for consistency.
