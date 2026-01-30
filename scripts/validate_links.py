#!/usr/bin/env python3
"""
Link Validation Script
Validates all links (internal and external) in markdown files.
"""

import json
import re
import sys
from pathlib import Path
from typing import Dict, List, Set, Tuple
from urllib.parse import urlparse

import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry


# Configuration
TIMEOUT = 10  # seconds
MAX_RETRIES = 3
BACKOFF_FACTOR = 0.5

# Patterns
MD_LINK_PATTERN = r"\[([^\]]*)\]\(([^\)]+)\)"
HTML_LINK_PATTERN = r'<a\s+(?:[^>]*?\s+)?href="([^"]*)"'

# Files and directories to check
MARKDOWN_DIRS = ["content", "docs", "scraper", "scripts", "tasks", ".github"]
MARKDOWN_FILES = ["README.md"]

# Links to skip (known to be problematic or not real URLs)
SKIP_LINKS = {
    "#",  # Internal anchor only
    "mailto:",  # Email links
    "tel:",  # Phone links
}


def create_http_session() -> requests.Session:
    """Create HTTP session with retry logic."""
    session = requests.Session()
    retry = Retry(
        total=MAX_RETRIES,
        read=MAX_RETRIES,
        connect=MAX_RETRIES,
        backoff_factor=BACKOFF_FACTOR,
        status_forcelist=[429, 500, 502, 503, 504],
    )
    adapter = HTTPAdapter(max_retries=retry)
    session.mount("http://", adapter)
    session.mount("https://", adapter)
    session.headers.update({"User-Agent": "Mozilla/5.0 (compatible; LinkValidator/1.0)"})
    return session


def find_markdown_files(base_path: Path) -> List[Path]:
    """Find all markdown files in specified directories."""
    md_files = []

    # Add root markdown files
    for filename in MARKDOWN_FILES:
        file_path = base_path / filename
        if file_path.exists():
            md_files.append(file_path)

    # Add markdown files from directories
    for directory in MARKDOWN_DIRS:
        dir_path = base_path / directory
        if dir_path.exists():
            md_files.extend(dir_path.rglob("*.md"))

    return sorted(md_files)


def extract_links(content: str, file_path: Path) -> List[Tuple[str, str, int]]:
    """
    Extract all links from markdown content.
    Returns list of (link_text, url, line_number) tuples.
    """
    links = []

    # Split content into lines for line number tracking
    lines = content.split("\n")

    for line_num, line in enumerate(lines, 1):
        # Extract markdown links [text](url)
        for match in re.finditer(MD_LINK_PATTERN, line):
            link_text = match.group(1)
            url = match.group(2)
            links.append((link_text, url, line_num))

        # Extract HTML links <a href="url">
        for match in re.finditer(HTML_LINK_PATTERN, line):
            url = match.group(1)
            links.append(("", url, line_num))

    return links


def should_skip_link(url: str) -> bool:
    """Check if link should be skipped."""
    url_lower = url.lower()

    # Skip certain prefixes
    for skip in SKIP_LINKS:
        if url_lower.startswith(skip):
            return True

    return False


def heading_to_anchor(heading_text: str) -> str:
    r"""
    Convert a markdown heading to its anchor ID.
    GitHub's markdown processor:
    1. Converts to lowercase
    2. Removes emojis and special characters (keeps word characters, spaces, hyphens)
    3. Replaces spaces with hyphens
    4. Strips leading/trailing hyphens

    Note: \w includes alphanumeric and underscores
    """
    # Convert to lowercase
    anchor = heading_text.lower()

    # Remove emojis and special characters, keep only word characters, spaces, hyphens
    anchor = re.sub(r"[^\w\s-]", "", anchor)

    # Replace spaces with hyphens
    anchor = re.sub(r"\s+", "-", anchor)

    # Strip leading/trailing hyphens
    anchor = anchor.strip("-")

    return anchor


def extract_headings(content: str) -> Set[str]:
    """
    Extract all heading anchors from markdown content.
    Returns set of anchor IDs.
    """
    anchors = set()

    # Match markdown headings: ## Heading Text
    for match in re.finditer(r"^#{1,6}\s+(.+)$", content, re.MULTILINE):
        heading_text = match.group(1).strip()
        anchor = heading_to_anchor(heading_text)
        anchors.add(anchor)

    return anchors


def has_emoji(text: str) -> bool:
    """
    Check if text contains emoji characters.
    Uses Unicode ranges for emoji detection.
    """
    emoji_pattern = re.compile(
        "["
        "\U0001f1e0-\U0001f1ff"  # flags (iOS)
        "\U0001f300-\U0001f5ff"  # symbols & pictographs
        "\U0001f600-\U0001f64f"  # emoticons
        "\U0001f680-\U0001f6ff"  # transport & map symbols
        "\U0001f700-\U0001f77f"  # alchemical symbols
        "\U0001f780-\U0001f7ff"  # Geometric Shapes Extended
        "\U0001f800-\U0001f8ff"  # Supplemental Arrows-C
        "\U0001f900-\U0001f9ff"  # Supplemental Symbols and Pictographs
        "\U0001fa00-\U0001fa6f"  # Chess Symbols
        "\U0001fa70-\U0001faff"  # Symbols and Pictographs Extended-A
        "\U00002702-\U000027b0"  # Dingbats
        "\U000024c2-\U0001f251"
        "]+",
        flags=re.UNICODE,
    )
    return bool(emoji_pattern.search(text))


def check_emoji_in_linked_headings(content: str, links: List[Tuple[str, str, int]]) -> List[Dict]:
    """
    Check if any headings that are link targets contain emojis.
    Returns list of violations.
    """
    violations = []

    # Extract all anchor links from the content
    anchor_targets = set()
    for _, url, _ in links:
        if "#" in url:
            anchor = url.split("#", 1)[1]
            anchor_targets.add(anchor)

    # Check each heading to see if it's a link target and contains emojis
    for match in re.finditer(r"^(#{1,6})\s+(.+)$", content, re.MULTILINE):
        heading_level = match.group(1)
        heading_text = match.group(2).strip()
        anchor = heading_to_anchor(heading_text)
        line_num = content[: match.start()].count("\n") + 1

        # If this heading is linked to and contains emoji, it's a violation
        if anchor in anchor_targets and has_emoji(heading_text):
            violations.append(
                {
                    "line": line_num,
                    "heading": heading_text,
                    "anchor": anchor,
                    "message": f"Heading '{heading_text}' contains emoji but is a link target (#{anchor})",
                }
            )

    return violations


def resolve_file_path(file_part: str, source_file: Path, base_path: Path) -> Path:
    """
    Resolve a relative or absolute file path to an absolute Path object.
    """
    if file_part.startswith("/"):
        # Absolute path from repo root
        return base_path / file_part.lstrip("/")
    # Relative to current file
    return (source_file.parent / file_part).resolve()


def validate_internal_link(
    url: str, source_file: Path, base_path: Path, source_content: str = None
) -> Tuple[bool, str]:
    """
    Validate internal (relative) link or anchor.
    Returns (is_valid, error_message).
    """
    # Check if it's an anchor-only link
    if url.startswith("#"):
        anchor = url[1:]  # Remove leading #
        if source_content:
            # Extract headings from source file
            valid_anchors = extract_headings(source_content)
            if anchor not in valid_anchors:
                anchor_list = ", ".join(f"#{a}" for a in sorted(list(valid_anchors)[:5]))
                more_anchors = (
                    f" (and {len(valid_anchors) - 5} more)" if len(valid_anchors) > 5 else ""
                )
                return (
                    False,
                    f"Anchor not found: #{anchor}. Available anchors: {anchor_list}{more_anchors}",
                )
            return True, ""
        # Can't validate without content
        return True, ""

    # Handle links with anchors (file.md#anchor)
    if "#" in url:
        file_part, anchor_part = url.split("#", 1)
        anchor = anchor_part

        # If file_part is empty, it's same-file anchor
        if not file_part:
            if source_content:
                valid_anchors = extract_headings(source_content)
                if anchor not in valid_anchors:
                    return False, f"Anchor not found: #{anchor}"
                return True, ""
        else:
            # Resolve the file path
            target = resolve_file_path(file_part, source_file, base_path)

            if not target.exists():
                rel_target = (
                    target.relative_to(base_path) if target.is_relative_to(base_path) else target
                )
                return False, f"File not found: {rel_target}"

            # Check anchor in target file
            try:
                with open(target, encoding="utf-8") as f:
                    target_content = f.read()
                valid_anchors = extract_headings(target_content)
                if anchor not in valid_anchors:
                    return False, f"Anchor not found in {target.name}: #{anchor}"
                return True, ""
            except Exception as e:
                return False, f"Error reading target file: {str(e)}"

    # Regular file link (no anchor)
    target = resolve_file_path(url, source_file, base_path)

    if not target.exists():
        rel_target = target.relative_to(base_path) if target.is_relative_to(base_path) else target
        return False, f"File not found: {rel_target}"

    return True, ""


def validate_external_link(url: str, session: requests.Session) -> Tuple[bool, str]:
    """
    Validate external (HTTP/HTTPS) link.
    Returns (is_valid, error_message).
    """
    try:
        response = session.head(url, timeout=TIMEOUT, allow_redirects=True)

        # Some servers don't support HEAD, try GET
        if response.status_code == 405:
            response = session.get(url, timeout=TIMEOUT, allow_redirects=True, stream=True)

        if response.status_code >= 400:
            return False, f"HTTP {response.status_code}"

        return True, ""

    except requests.exceptions.Timeout:
        return False, "Timeout"
    except requests.exceptions.TooManyRedirects:
        return False, "Too many redirects"
    except requests.exceptions.RequestException as e:
        return False, str(e)
    except Exception as e:
        return False, f"Unexpected error: {str(e)}"


def validate_links(base_path: Path) -> Dict:
    """
    Validate all links in markdown files.
    Returns report dictionary.
    """
    session = create_http_session()
    report = {
        "total_files": 0,
        "total_links": 0,
        "internal_links": 0,
        "external_links": 0,
        "valid_links": 0,
        "broken_links": [],
        "emoji_violations": [],
        "skipped_links": 0,
    }

    md_files = find_markdown_files(base_path)
    report["total_files"] = len(md_files)

    print(f"Found {len(md_files)} markdown files to check\n")

    for md_file in md_files:
        rel_path = md_file.relative_to(base_path)
        print(f"Checking: {rel_path}")

        with open(md_file, encoding="utf-8") as f:
            content = f.read()

        links = extract_links(content, md_file)

        # Check for emoji violations in linked headings
        emoji_violations = check_emoji_in_linked_headings(content, links)
        if emoji_violations:
            for violation in emoji_violations:
                report["emoji_violations"].append({"file": str(rel_path), **violation})
                print(
                    f"  ⚠️  Line {violation['line']}: EMOJI IN LINKED HEADING - {violation['message']}"
                )

        for link_text, url, line_num in links:
            report["total_links"] += 1

            # Skip certain links
            if should_skip_link(url):
                report["skipped_links"] += 1
                continue

            # Determine if internal or external
            parsed = urlparse(url)
            is_external = parsed.scheme in ("http", "https")

            if is_external:
                report["external_links"] += 1
                is_valid, error = validate_external_link(url, session)
            else:
                report["internal_links"] += 1
                is_valid, error = validate_internal_link(url, md_file, base_path, content)

            if is_valid:
                report["valid_links"] += 1
                print(f"  ✓ Line {line_num}: {url[:60]}")
            else:
                report["broken_links"].append(
                    {
                        "file": str(rel_path),
                        "line": line_num,
                        "url": url,
                        "text": link_text,
                        "error": error,
                        "type": "external" if is_external else "internal",
                    }
                )
                print(f"  ✗ Line {line_num}: {url[:60]} - {error}")

        print()

    return report


def print_report(report: Dict):
    """Print summary report."""
    print("=" * 70)
    print("LINK VALIDATION REPORT")
    print("=" * 70)
    print(f"Files checked:        {report['total_files']}")
    print(f"Total links:          {report['total_links']}")
    print(f"Internal links:       {report['internal_links']}")
    print(f"External links:       {report['external_links']}")
    print(f"Valid links:          {report['valid_links']}")
    print(f"Broken links:         {len(report['broken_links'])}")
    print(f"Emoji violations:     {len(report['emoji_violations'])}")
    print(f"Skipped links:        {report['skipped_links']}")
    print()

    has_issues = False

    if report["emoji_violations"]:
        has_issues = True
        print("EMOJI VIOLATIONS (Emojis in headings that are link targets):")
        print("-" * 70)
        print("⚠️  CRITICAL: Headings that are link targets must NOT contain emojis.")
        print("    GitHub strips emojis from anchor IDs, breaking the links.\n")

        for violation in report["emoji_violations"]:
            print(f"\nFile: {violation['file']}:{violation['line']}")
            print(f"Heading: {violation['heading']}")
            print(f"Anchor: #{violation['anchor']}")
            print("Fix: Remove emoji from heading")

        print()
        print("-" * 70)
        print()

    if report["broken_links"]:
        has_issues = True
        print("BROKEN LINKS:")
        print("-" * 70)

        for broken in report["broken_links"]:
            print(f"\nFile: {broken['file']}:{broken['line']}")
            print(f"Type: {broken['type']}")
            print(f"URL:  {broken['url']}")
            if broken["text"]:
                print(f"Text: {broken['text']}")
            print(f"Error: {broken['error']}")

        print()
        print("=" * 70)

    if not has_issues:
        print("✓ All links are valid and no emoji violations found!")
        print("=" * 70)
        return True
    print("=" * 70)
    return False


def save_report(report: Dict, output_file: Path):
    """Save report to JSON file."""
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(report, f, indent=2)
    print(f"\nReport saved to: {output_file}")


def main():
    """Main entry point."""
    base_path = Path(__file__).parent.parent

    print("Link Validation Script")
    print("=" * 70)
    print(f"Base path: {base_path}\n")

    # Validate links
    report = validate_links(base_path)

    # Save report
    output_file = base_path / "link-validation-report.json"
    save_report(report, output_file)

    # Print summary
    all_valid = print_report(report)

    # Exit with appropriate code
    sys.exit(0 if all_valid else 1)


if __name__ == "__main__":
    main()
