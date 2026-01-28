# Archived Custom Agents

This directory contains custom agents that have been archived because their functionality is better handled by Python scripts.

## Archived Agents

### feed-fetcher.agent.md
**Reason**: Python scripts (`scraper/fetch_blog.py`, `scraper/fetch_youtube.py`) provide more reliable and deterministic RSS/Atom feed fetching.

**Why Python is better**:
- Faster execution (no LLM latency)
- Deterministic behavior
- Better error handling
- No LLM costs for data fetching
- Well-tested with `feedparser` library

**Status**: Archived - Keep as documentation reference

---

### change-detector.agent.md
**Reason**: Python script (`scraper/detect_changes.py`) handles change detection and metadata tracking deterministically.

**Why Python is better**:
- Reliable diff computation
- Consistent hash generation
- Fast metadata updates
- No risk of LLM hallucination
- Already proven and tested

**Status**: Archived - Keep as documentation reference

---

### youtube-specialist.agent.md
**Reason**: Python script (`scraper/fetch_youtube.py`) handles YouTube RSS feeds and API integration effectively.

**Why Python is better**:
- Efficient API quota management
- Reliable RSS parsing
- No LLM needed for data fetching
- Faster execution

**Status**: Archived - May be used for complex video analysis if needed (rarely)

---

## Active Agents

The following agents remain active in `.github/agents/`:

- **publisher.agent.md** - Editor-in-Chief, orchestrates content synthesis
- **content-generator.agent.md** - Generates markdown content (where LLMs excel)
- **link-validator.agent.md** - Validates links (quality gate)
- **infrastructure-architect.agent.md** - Project setup and infrastructure

---

## Workflow Design

**Data Collection** (Python scripts - automated):
- Fast, deterministic, reliable
- No LLM costs
- Proven tools (feedparser, requests, etc.)

**Content Synthesis** (Custom agents - triggered by issues):
- Creative content generation
- Complex formatting and categorization
- Quality validation

This hybrid approach optimizes for both reliability (Python) and creativity (agents).

---

**Last Updated**: January 28, 2026
