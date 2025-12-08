# Testing Publisher Agent

## Manual Testing

### 1. Prepare test data

**Note**: As a test administrator, YOU run the scrapers to populate test data. The Publisher Agent itself never runs these scripts.

Run the scrapers to populate the `data/` directory:

```bash
# Run scrapers to populate data/ (you do this, not the agent)
python scraper/fetch_docs.py
python scraper/fetch_blog.py
python scraper/fetch_youtube.py
python scraper/detect_changes.py
```

### 2. Create test issue on GitHub

Create a new issue in the repository with the following content:

```markdown
Title: [TEST] Publisher Agent Test

Body:
@copilot Please generate content from data/ directory.

This is a test. Use data in data/ to generate:
- content/README.md
- content/changelog.md
- content/cheatsheet.md
- content/videos.md

Create a PR with results.
```

### 3. Verify agent response

Check that the agent:
- ✓ Reads data files from data/ directory
- ✓ Generates all required content files
- ✓ Creates a PR with the changes
- ✓ PR description is clear and comprehensive
- ✓ Content is accurate and well-formatted

## What to Check

### Data Reading
- [ ] Agent correctly reads JSON files from data/blog/
- [ ] Agent correctly reads JSON files from data/videos/
- [ ] Agent correctly reads Markdown files from data/docs/
- [ ] Agent correctly reads data/changes-summary.json
- [ ] Agent correctly reads data/metadata.json

### Content Generation
- [ ] Agent identifies "What's New" content accurately
- [ ] Agent generates engaging summaries
- [ ] Agent follows editorial guidelines
- [ ] Agent maintains consistent formatting
- [ ] Agent includes proper timestamps

### Delegation
- [ ] Agent uses runSubagent when appropriate
- [ ] Agent delegates videos.md to content-generator if needed
- [ ] Agent delegates video categorization to youtube-specialist if needed

### PR Quality
- [ ] PR includes all required files
- [ ] PR title follows format: "📰 Content Update - [date]"
- [ ] PR description includes summary of changes
- [ ] PR description lists what's new
- [ ] PR description includes checklist of updated files
- [ ] No formatting issues in generated content

### Content Accuracy
- [ ] README.md has correct structure and sections
- [ ] changelog.md is chronologically ordered
- [ ] cheatsheet.md is comprehensive and accurate
- [ ] videos.md is well-organized and categorized
- [ ] All dates are correctly formatted
- [ ] All links are properly formatted with correct URLs from source data
- [ ] Statistics are accurate

## No Data Fetching Verification

**Critical**: Verify that the agent does NOT attempt to:
- [ ] Scrape websites
- [ ] Fetch data from APIs
- [ ] Download files from external sources
- [ ] Run Python scraper scripts

The agent should ONLY:
- ✓ Read existing files from data/ directory
- ✓ Synthesize content from prepared data
- ✓ Generate user-facing documentation

## Testing Different Scenarios

### Scenario 1: Normal Update
- Fresh data available in all directories
- Expected: All content files generated with latest information

### Scenario 2: Missing Data
- Remove some JSON files from data/videos/
- Expected: Agent generates content with available data and notes missing data

### Scenario 3: Stale Data
- Modify data/metadata.json to have old last_updated timestamp
- Expected: Agent generates content but alerts about stale data

### Scenario 4: Large Dataset
- Populate data/ with 50+ blog posts and videos
- Expected: Agent prioritizes recent content and handles large dataset gracefully

## Success Metrics

The Publisher Agent test is successful when:

1. **Completeness**: All 4 content files are generated
2. **Accuracy**: Content matches source data
3. **Quality**: Writing is clear, professional, and engaging
4. **Consistency**: Formatting is consistent across all files
5. **Timeliness**: "What's New" section highlights recent content
6. **Navigation**: All links are properly formatted
7. **Metadata**: Timestamps and statistics are accurate
8. **PR Quality**: PR is well-documented and ready for review

## Common Issues and Solutions

### Issue: Agent attempts to fetch data
**Solution**: Review agent instructions to emphasize "no data fetching" role

### Issue: Generated content has formatting issues
**Solution**: Add markdown syntax validation to quality checks section

### Issue: Agent doesn't use runSubagent
**Solution**: Clarify when delegation is recommended vs required

### Issue: Content is too verbose
**Solution**: Emphasize "scannable" and "concise" in editorial guidelines

### Issue: Timestamps are inconsistent
**Solution**: Specify exact date format in instructions (ISO 8601)

## Continuous Testing

After initial validation:
1. Run tests weekly with fresh data
2. Monitor PR quality and content accuracy
3. Update agent instructions based on feedback
4. Track common issues and refine guidelines
5. Validate against new types of content as they emerge

## Feedback Loop

Document any issues found during testing:
1. Create GitHub issue for each problem
2. Tag with "publisher-agent" label
3. Include example input and expected vs actual output
4. Update agent instructions to prevent recurrence
5. Re-test to verify fix

## Manual Review Checklist

Before approving a Publisher Agent PR:

- [ ] All content files present and complete
- [ ] Headlines accurately reflect recent changes
- [ ] Documentation updates are summarized correctly
- [ ] Blog posts have correct titles, dates, and links
- [ ] Videos have properly formatted YouTube links and correct metadata
- [ ] Cheatsheet commands are accurate
- [ ] Changelog is chronologically correct
- [ ] Statistics match actual data counts
- [ ] Markdown renders properly (no syntax errors)
- [ ] Writing style matches editorial guidelines
- [ ] No typos or grammar errors
- [ ] All emojis are appropriate and not excessive
- [ ] Links to original sources are included
- [ ] "Last Updated" timestamp is current
