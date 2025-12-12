# GitHub Copilot Trainings Fetcher

## Overview

Fetches and curates high-quality training resources for GitHub Copilot Coding Agent and Agentic AI workflows.

## Data Sources

### 1. **GitHub Skills** (Official)
- Interactive, hands-on courses hosted on GitHub
- Free and self-paced
- Examples: "Expand Your Team with Copilot"
- URL pattern: `https://github.com/skills/*`

### 2. **Microsoft Learn** (Official)
- Structured learning modules and paths
- Free and self-paced
- Includes challenges and assessments
- URL pattern: `https://learn.microsoft.com/en-us/training/*`

### 3. **GitHub Certifications** (Official)
- Industry-recognized certifications
- Validates professional expertise
- Paid certification exams
- URL: `https://resources.github.com/learn/certifications/`

### 4. **Udemy** (Curated)
- Manually curated high-quality courses
- Criteria for inclusion:
  - Rating: 4.5+ stars
  - Students: 1000+ enrolled
  - Recent updates (within 6 months)
  - Focus on GitHub Copilot Coding Agent / Agentic AI
- Company Udemy account may provide access

## Quality Standards

Only include training that meets these criteria:

1. **Official Sources** (GitHub, Microsoft)
   - All official content is included automatically

2. **Third-Party Sources** (Udemy, etc.)
   - Rating: Minimum 4.5/5 stars
   - Popularity: 1000+ students or reviews
   - Recency: Updated within last 6 months
   - Relevance: GitHub Copilot Coding Agent / Agentic AI focus
   - Quality: Professional production, clear teaching

3. **Content Focus**
   - GitHub Copilot (Agent Mode or Coding Agent)
   - Agentic AI workflows
   - Best practices and patterns
   - Real-world applications

## Output Format

Each training is saved as a JSON file in `data/trainings/`:

```json
{
  "id": "github-skills-copilot-team",
  "title": "Expand Your Team with Copilot",
  "description": "Learn how to use GitHub Copilot...",
  "url": "https://github.com/skills/expand-your-team-with-copilot/",
  "provider": "GitHub Skills",
  "level": "Intermediate",
  "topics": ["GitHub Copilot", "AI Pair Programming"],
  "format": "Interactive",
  "is_free": true,
  "certification": false,
  "estimated_time": "2-3 hours",
  "rating": 4.8,
  "students": "10000+",
  "last_verified": "2025-12-12T00:00:00Z",
  "fetched_at": "2025-12-12T12:00:00Z"
}
```

## Usage

### Run Locally

```bash
# Using venv Python (recommended)
.venv/bin/python scraper/fetch_trainings.py

# Or with system Python
python3 scraper/fetch_trainings.py
```

### Output

```
[INFO] Starting GitHub Copilot trainings fetch...
[INFO] Fetching GitHub Skills courses...
[INFO] ✓ Found 2 GitHub Skills courses
[INFO] Fetching Microsoft Learn modules...
[INFO] ✓ Found 3 Microsoft Learn modules
[INFO] Loading curated Udemy courses...
[INFO] ✓ Found 1 curated Udemy courses
[INFO] Fetching GitHub certifications...
[INFO] ✓ Found 1 GitHub certifications
[INFO] Saving 7 training resources...
[INFO] ✓ Saved: Expand Your Team with Copilot
[INFO] ✓ Saved: Introduction to GitHub Copilot
...
[INFO] ✓ Fetch complete: 7/7 trainings saved
[INFO] Summary by provider:
[INFO]   - GitHub: 1
[INFO]   - GitHub Skills: 2
[INFO]   - Microsoft Learn: 3
[INFO]   - Udemy: 1
```

## Maintenance

### Adding New Trainings

1. **Official Sources**: Update the hardcoded lists in:
   - `fetch_github_skills()` - GitHub Skills courses
   - `fetch_microsoft_learn()` - Microsoft Learn modules
   - `fetch_github_certifications()` - GitHub certifications

2. **Third-Party Sources**: Add to `fetch_udemy_courses()`
   - Verify quality criteria
   - Include rating and student count
   - Add "note" field if special access required

### Verification Schedule

- **Monthly**: Verify all links still work
- **Quarterly**: Review third-party courses for quality
- **On-demand**: Add new courses as released

### Link Validation

Use the link validator to check all training URLs:

```bash
python3 scripts/validate_links.py
```

## Integration

This scraper integrates with:

1. **Change Detection** (`detect_changes.py`)
   - Tracks new/updated trainings
   - Generates change summaries

2. **Content Generation** (via agents)
   - Publisher agent reads `data/trainings/*.json`
   - Generates trainings section in content files

3. **Metadata Tracking** (`metadata.json`)
   - Stores training IDs for deduplication
   - Tracks last update time

## Future Enhancements

Potential improvements:

1. **Automated Udemy Scraping**
   - Use Udemy API (if available)
   - Auto-detect high-rated courses

2. **LinkedIn Learning Integration**
   - Add LinkedIn Learning courses
   - Require LinkedIn Learning API

3. **Coursera Integration**
   - Add Coursera specializations
   - Use Coursera API

4. **Rating Updates**
   - Periodic scraping of ratings/reviews
   - Track rating trends over time

5. **Completion Tracking**
   - Allow users to mark completed courses
   - Store in user preferences

## Notes

- All timestamps use UTC and ISO 8601 format
- Deduplication uses training ID (hashed URL or manual ID)
- Free courses are prioritized in content generation
- Certification programs are highlighted separately
