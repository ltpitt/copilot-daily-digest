# GitHub Next Project Scraper

Fetches experimental projects from GitHub Next (https://githubnext.com/) research team.

## ⚠️ Important: Experimental Content

**GitHub Next projects are experimental and require special handling:**

- Projects are research explorations that may or may not become official features
- Many experiments are discontinued
- Content should **never** be presented as official roadmap or stable features
- All scraped data includes `"experimental": true` flag
- Projects have statuses: "Completed", "WIP", "Napkin sketch", "Research prototype", "Open sourced"
- **"Completed" status ≠ production ready** - still experimental

## Usage

```bash
python3 scraper/fetch_github_next.py
```

## What It Does

1. Fetches the GitHub Next homepage (https://githubnext.com/)
2. Parses HTML to extract project cards
3. Extracts for each project:
   - Title
   - URL (e.g., https://githubnext.com/projects/copilot-workspace/)
   - Date (when announced)
   - Status (Completed, WIP, etc.)
   - Description
   - Source marker: "github-next"
   - Experimental flag: `true`
4. Saves each project as JSON in `data/github-next/`
5. Tracks URLs in metadata to prevent duplicates

## Output Format

Each project is saved as `data/github-next/{project-slug}.json`:

```json
{
  "title": "Copilot Workspace",
  "url": "https://githubnext.com/projects/copilot-workspace/",
  "date": "2024-04-29T00:00:00Z",
  "status": "Completed",
  "description": "An agentic dev environment, designed for everyday tasks.",
  "source": "github-next",
  "experimental": true,
  "scraped_at": "2025-12-11T08:37:25.943187Z"
}
```

## Metadata Tracking

URLs are tracked in `data/metadata.json` under `github_next_urls` array to prevent duplicate scraping.

## Dependencies

- `requests` - HTTP client
- `beautifulsoup4` - HTML parsing
- `lxml` - Parser for BeautifulSoup
- `certifi` - SSL certificate verification
- `loguru` - Logging

## Integration

The scraper integrates with:
- `metadata.py` - Tracks GitHub Next URLs
- `detect_changes.py` - Detects new projects in `detect_github_next_changes()`
- Custom agents - All agents are aware of experimental nature and add disclaimers

## Content Generation Rules

When GitHub Next content appears in generated content files:

1. **Always use 🔬 emoji** to mark experimental content
2. **Add disclaimer**: "⚠️ Experimental - May not become official features"
3. **Separate section** from official docs/blog posts
4. **Include status** in every mention
5. **Use cautious language**: "exploring", "researching", "experimenting with"

See `.github/copilot-instructions.md` for full content generation guidelines.

## Example Integration in Content

```markdown
## 🔬 GitHub Next: Experimental Projects

> ⚠️ **Experimental** - These are research projects from GitHub Next.
> Many are discontinued. Not official roadmap or stable features.

**Copilot Workspace** (Status: Completed)
GitHub Next built an agentic dev environment designed for everyday tasks.
This is an experimental prototype - not a confirmed production feature.

→ [Explore project](https://githubnext.com/projects/copilot-workspace/)
```

## Error Handling

- Network failures: Logged and script continues
- Parse errors: Individual projects skipped, others processed
- Missing fields: Uses empty string defaults
- Duplicate URLs: Skipped automatically

## Logging

Uses `loguru` for structured logging:
- INFO: Scraping progress and successful operations
- WARNING: Missing data, parsing issues
- ERROR: Network failures, file I/O errors

## Notes

- **No RSS feed available** - Must scrape HTML (unlike blog/YouTube sources)
- Project list changes infrequently (new projects added monthly/quarterly)
- Scraper is idempotent - safe to run multiple times
- Respects SSL certificates via `certifi`
