# Guide: Focusing on AI/Copilot Videos

## Current Situation

The YouTube scraper is currently configured to fetch **ALL videos** from the GitHub channel (last 30 days), without keyword filtering. This is the default behavior (`require_keywords: false`).

### Analysis of Current Videos (December 2025)

When testing the scraper with the GitHub channel, we found:
- **15 videos** in the last 30 days
- **15 videos** match AI/Copilot keywords (100% match rate!)

**All current videos mention:** copilot, AI, agents, MCP, or coding

**Sample videos:**
- "The latest in managing and auditing GitHub Copilot agents"
- "How to close pull requests faster with Copilot code review"
- "Assign Linear issues to Copilot coding agent"
- "Extending AI Agents: A live demo of the GitHub MCP Server"
- "Rubber Duck Thursdays - Let's build with custom agents"

**Conclusion:** The GitHub channel is already heavily focused on AI/Copilot content, so keyword filtering may not be necessary in practice. However, the filtering capability is available if needed.

---

## How to Enable AI/Copilot Filtering

You have **three options** to focus on AI/Copilot videos:

### Option 1: CLI Flag (Temporary, Per-Run)

Use the `--require-keywords` flag to enable filtering for a single run:

```bash
# Enable keyword filtering for this run only
python scripts/fetch_youtube.py --require-keywords

# Combine with other flags
python scripts/fetch_youtube.py --require-keywords --max-age-days 7
```

**Pros:**
- Easy to test
- Doesn't change default behavior
- Can be used selectively

**Cons:**
- Must remember to use flag each time
- Not suitable for automated/scheduled runs

---

### Option 2: Configuration Change (Permanent)

Edit `config/youtube.yml` and change the `require_keywords` setting:

**Before:**
```yaml
filters:
  require_keywords: false  # Returns all videos
```

**After:**
```yaml
filters:
  require_keywords: true   # Returns only AI/Copilot videos
```

**Pros:**
- Permanent change - applies to all runs
- Works in automated/scheduled runs
- Clear default behavior

**Cons:**
- Affects all future runs
- Requires editing config file

---

### Option 3: Workflow/CI Configuration

For GitHub Actions or scheduled runs, you can set the flag in the workflow:

**`.github/workflows/daily-scraper.yml`** (example):
```yaml
- name: Fetch YouTube Videos
  run: python scripts/fetch_youtube.py --require-keywords
```

**Pros:**
- Automated runs use filtering
- Keeps config flexible for manual runs
- Easy to change in workflow file

**Cons:**
- Only affects automated runs
- Requires workflow file access

---

## Keyword Configuration

The scraper filters videos based on keywords in the title and description. The current keywords are configured in `config/youtube.yml`:

```yaml
filters:
  keywords:
    - "copilot"
    - "github copilot"
    - "ai"
    - "agent"
    - "coding agent"
    - "workspace"
    - "extensions"
```

### Customizing Keywords

You can modify the keyword list to be more or less restrictive:

**More restrictive (Copilot-only):**
```yaml
filters:
  keywords:
    - "copilot"
    - "github copilot"
```

**Less restrictive (broader AI topics):**
```yaml
filters:
  keywords:
    - "copilot"
    - "ai"
    - "machine learning"
    - "llm"
    - "agent"
    - "automation"
```

**Note:** Keywords are case-insensitive and match anywhere in title or description.

---

## Testing the Filter

To see what difference the keyword filter makes:

### 1. Preview with Dry-Run

```bash
# Without keyword filter (current default)
python scripts/fetch_youtube.py --dry-run

# With keyword filter
python scripts/fetch_youtube.py --require-keywords --dry-run
```

### 2. Compare Results

```bash
# Run without filter and count
python scripts/fetch_youtube.py --dry-run 2>&1 | grep "Would save"

# Run with filter and count
python scripts/fetch_youtube.py --require-keywords --dry-run 2>&1 | grep "Would save"
```

### 3. Check Filter Statistics

The scraper logs show filtering statistics:

```
[INFO] Total videos fetched: 15
[INFO] Filtered by age (30 days): 15 videos from 15 total
[INFO] Filtered to 12 Copilot-related videos from 15 total  ← Filter result
```

---

## Recommendation

Based on current analysis (December 2025):

### ✅ **Current Setup is Good**

The GitHub channel content is already **100% AI/Copilot focused**, so keyword filtering is not necessary right now. The default configuration (`require_keywords: false`) works well because:

1. **All videos are relevant** - Every video mentions Copilot, AI, or agents
2. **No false positives** - You're not getting unrelated content
3. **Complete coverage** - You're capturing all the AI/Copilot news

### 🔄 **When to Enable Filtering**

You should enable keyword filtering (`require_keywords: true`) if:

1. **Channel diversifies** - GitHub starts posting more non-Copilot content
2. **Stricter focus needed** - You only want "Copilot" mentions, not general "AI" topics
3. **Multiple channels** - You enable other channels that have mixed content

### 🎯 **Suggested Action**

**For now: Keep current configuration** (`require_keywords: false`)

**Monitor regularly:** Check if non-Copilot videos appear:
```bash
python scripts/fetch_youtube.py --dry-run | grep -i "title"
```

**Enable filtering later** if needed:
```bash
# Quick test
python scripts/fetch_youtube.py --require-keywords

# Or edit config/youtube.yml to make it permanent
```

---

## Example Scenarios

### Scenario 1: Daily Automated Scraping (Current)

**Configuration:** `require_keywords: false`
**Result:** Captures all 15 GitHub videos from last 30 days
**Use case:** "Give me everything from GitHub's channel"

### Scenario 2: Copilot-Only Focus

**Configuration:** `require_keywords: true` + keywords: ["copilot", "github copilot"]
**Result:** Would capture ~10-12 videos (only those specifically mentioning Copilot)
**Use case:** "I only want Copilot-specific content, not general AI news"

### Scenario 3: Multi-Channel with Filtering

**Configuration:** 
- Enable VS Code and Microsoft Reactor channels
- Set `require_keywords: true`

**Result:** Gets AI/Copilot videos from all three channels
**Use case:** "Aggregate Copilot content from multiple Microsoft channels"

---

## Quick Reference Commands

```bash
# Current default (all videos)
python scripts/fetch_youtube.py

# Enable keyword filtering (one time)
python scripts/fetch_youtube.py --require-keywords

# Test without saving files
python scripts/fetch_youtube.py --require-keywords --dry-run

# Stricter age + keyword filter
python scripts/fetch_youtube.py --require-keywords --max-age-days 7

# View current config
cat config/youtube.yml | grep -A 10 filters
```

---

## Summary

✅ **Current situation:** GitHub channel is 100% AI/Copilot focused (15/15 videos match)  
✅ **Current config works well:** No filtering needed right now  
✅ **Filtering ready:** Available via `--require-keywords` flag or config change  
✅ **Flexible:** Easy to enable/customize if channel content changes  

**Bottom line:** The scraper is already capturing the "wealth" of AI/Copilot content. Filtering is available but not currently necessary since the channel is fully focused on these topics.
