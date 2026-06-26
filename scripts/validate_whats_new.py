#!/usr/bin/env python3
"""
Validate WHATS-NEW.md for correct date formatting and chronological ordering.

This script checks:
1. All article dates are complete (Month Day, Year format)
2. No incomplete dates like "Dec 2025" without day
3. Articles are sorted in reverse chronological order (newest first)
4. Dates match the section they're in (This Week, This Month, Older)

Exit codes:
0 - All validations passed
1 - Validation errors found
"""

import re
import sys
from datetime import datetime, timedelta
from pathlib import Path
from typing import List, Tuple


# Configure paths
REPO_ROOT = Path(__file__).parent.parent
WHATS_NEW_FILE = REPO_ROOT / "content" / "WHATS-NEW.md"

# Regex patterns
COMPLETE_DATE_PATTERN = r"([A-Z][a-z]{2}) (\d{1,2}), (\d{4})"  # "Dec 8, 2025"
INCOMPLETE_DATE_PATTERN = r"([A-Z][a-z]{2}) (\d{4})"  # "Dec 2025" (no day)
LEGACY_HEADING_PATTERN = r"^###\s+(.+?)\s+\((.+?)\)\s*$"  # "### Title (Date)"
LINK_HEADING_PATTERN = r"^###\s+\[(.+?)\]\((.+?)\)\s*$"  # "### [Title](url)"
DATE_LINE_PATTERN = rf"^\*({COMPLETE_DATE_PATTERN})\*\s*$"  # "*Dec 8, 2025*"

# Date ranges
NOW = datetime.now()
SEVEN_DAYS_AGO = NOW - timedelta(days=7)
THIRTY_DAYS_AGO = NOW - timedelta(days=30)


def parse_date(date_str: str) -> datetime:
    """
    Parse date string in format "Month Day, Year" to datetime object.

    Args:
        date_str: Date string like "Dec 8, 2025"

    Returns:
        datetime object
    """
    # Handle both "Dec 8, 2025" and "Dec 08, 2025"
    date_str = date_str.strip()
    return datetime.strptime(date_str, "%b %d, %Y")


def extract_articles(content: str) -> List[Tuple[str, str, int]]:
    """
    Extract article headings with dates from WHATS-NEW.md.

    Args:
        content: File content

    Returns:
        List of (title, date_string, line_number) tuples
    """
    articles = []
    lines = content.split("\n")
    for i, line in enumerate(lines, start=1):
        legacy_match = re.match(LEGACY_HEADING_PATTERN, line)
        if legacy_match:
            articles.append((legacy_match.group(1), legacy_match.group(2), i))
            continue

        link_match = re.match(LINK_HEADING_PATTERN, line)
        if not link_match:
            continue

        title = link_match.group(1)
        for offset in range(1, 4):
            if i - 1 + offset >= len(lines):
                break
            next_line = lines[i - 1 + offset].strip()
            if not next_line:
                continue
            date_match = re.match(DATE_LINE_PATTERN, next_line)
            if date_match:
                articles.append((title, date_match.group(1), i))
            break
    return articles


def check_complete_dates(articles: List[Tuple[str, str, int]]) -> List[str]:
    """
    Check that all dates are complete (have day, month, and year).

    Args:
        articles: List of (title, date_string, line_number) tuples

    Returns:
        List of error messages
    """
    errors = []

    for title, date_str, line_num in articles:
        # Skip non-date entries
        if "Documentation Updates" in title:
            continue

        # Check if date is incomplete (month + year only)
        if re.match(INCOMPLETE_DATE_PATTERN + r"$", date_str):
            complete_match = re.match(COMPLETE_DATE_PATTERN, date_str)
            if not complete_match:
                errors.append(
                    f"Line {line_num}: Incomplete date '{date_str}' in '{title}'. "
                    f"Must include day (e.g., 'Dec 8, 2025')"
                )

    return errors


def check_chronological_order(articles: List[Tuple[str, str, int]]) -> List[str]:
    """
    Check that articles are sorted in reverse chronological order.

    Args:
        articles: List of (title, date_string, line_number) tuples

    Returns:
        List of error messages
    """
    errors = []

    # Parse dates
    dated_articles = []
    for title, date_str, line_num in articles:
        try:
            date_obj = parse_date(date_str)
            dated_articles.append((title, date_obj, line_num))
        except ValueError:
            # Skip unparseable dates (they'll be caught by complete_dates check)
            continue

    # Check order
    for i in range(len(dated_articles) - 1):
        current_title, current_date, current_line = dated_articles[i]
        next_title, next_date, next_line = dated_articles[i + 1]

        if current_date < next_date:
            errors.append(
                f"Lines {current_line}-{next_line}: Incorrect order. "
                f"'{current_title}' ({current_date.strftime('%b %d, %Y')}) "
                f"should come AFTER '{next_title}' ({next_date.strftime('%b %d, %Y')}). "
                f"Articles must be sorted newest first."
            )

    return errors


def check_section_dates(content: str) -> List[str]:
    """
    Check that articles are in the correct section based on their dates.

    Args:
        content: File content

    Returns:
        List of error messages
    """
    errors = []

    # Split content into sections
    sections = {"This Week": [], "Last 30 Days": [], "Older Updates": []}

    current_section = None
    articles_by_line = {line_num: (title, date_str) for title, date_str, line_num in extract_articles(content)}

    for line_num, line in enumerate(content.split("\n"), start=1):
        if "## This Week" in line:
            current_section = "This Week"
        elif "## This Month" in line or "## Last 30 Days" in line:
            current_section = "Last 30 Days"
        elif "## Older Updates" in line:
            current_section = "Older Updates"
        elif current_section and line_num in articles_by_line:
            sections[current_section].append(articles_by_line[line_num])

    # Validate dates in each section
    for section, articles in sections.items():
        for title, date_str in articles:
            try:
                date_obj = parse_date(date_str)

                if section == "This Week":
                    if date_obj < SEVEN_DAYS_AGO:
                        errors.append(
                            f"Section '{section}': '{title}' dated {date_str} is older "
                            f"than 7 days and should be in 'This Month' or 'Older Updates'"
                        )
                elif section == "Last 30 Days":
                    if date_obj < THIRTY_DAYS_AGO:
                        errors.append(
                            f"Section '{section}': '{title}' dated {date_str} is older "
                            f"than 30 days and should be in 'Older Updates'"
                        )
                elif section == "Older Updates" and date_obj >= THIRTY_DAYS_AGO:
                    errors.append(
                        f"Section '{section}': '{title}' dated {date_str} is within "
                        f"last 30 days and should be in 'This Week' or 'This Month'"
                    )
            except ValueError:
                # Skip unparseable dates
                continue

    return errors


def main():
    """Main validation function."""
    if not WHATS_NEW_FILE.exists():
        print(f"❌ ERROR: {WHATS_NEW_FILE} not found")
        return 1

    print(f"📋 Validating {WHATS_NEW_FILE.relative_to(REPO_ROOT)}")
    print()

    # Read file
    content = WHATS_NEW_FILE.read_text()

    # Extract articles
    articles = extract_articles(content)
    print(f"✓ Found {len(articles)} articles")

    if not articles:
        print("❌ VALIDATION FAILED: no WHATS-NEW articles were found")
        return 1

    # Run validations
    all_errors = []

    # Check 1: Complete dates
    print("Checking for complete dates...")
    errors = check_complete_dates(articles)
    if errors:
        all_errors.extend(errors)
        print(f"  ❌ {len(errors)} incomplete date(s) found")
    else:
        print("  ✓ All dates are complete")

    # Check 2: Chronological order
    print("Checking chronological order...")
    errors = check_chronological_order(articles)
    if errors:
        all_errors.extend(errors)
        print(f"  ❌ {len(errors)} ordering issue(s) found")
    else:
        print("  ✓ Articles are correctly ordered (newest first)")

    # Check 3: Section dates
    print("Checking section date ranges...")
    errors = check_section_dates(content)
    if errors:
        all_errors.extend(errors)
        print(f"  ❌ {len(errors)} section placement issue(s) found")
    else:
        print("  ✓ All articles are in correct sections")

    # Report results
    print()
    if all_errors:
        print(f"❌ VALIDATION FAILED: {len(all_errors)} error(s) found")
        print()
        for error in all_errors:
            print(f"  • {error}")
        return 1
    print("✅ ALL VALIDATIONS PASSED")
    return 0


if __name__ == "__main__":
    sys.exit(main())
