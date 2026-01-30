#!/usr/bin/env python3
"""
Script to fetch and scrape GitHub Copilot documentation for the daily digest.
"""

import time

import requests
from bs4 import BeautifulSoup
from loguru import logger
from metadata import update_content_hash


def create_output_dir():
    """Create the top-level data/docs directory if it doesn't exist."""
    # Get the absolute path to the project root
    from pathlib import Path

    project_root = Path(__file__).resolve().parent.parent
    output_dir = project_root / "data" / "docs"
    if not output_dir.exists():
        output_dir.mkdir(parents=True)
        logger.info(f"Created output directory: {output_dir}")
    else:
        logger.debug(f"Output directory already exists: {output_dir}")
    return str(output_dir)


def fetch_url(url):
    """Fetch content from a URL with error handling."""
    try:
        headers = {"User-Agent": "Mozilla/5.0 (compatible; GitHub-Copilot-Daily-Digest/1.0)"}
        logger.info(f"Attempting to fetch URL: {url}")
        response = requests.get(url, headers=headers, timeout=30)
        response.raise_for_status()
        logger.success(f"Successfully fetched URL: {url}")
        return response.text
    except requests.RequestException as e:
        logger.error(f"Error fetching {url}: {e}")
        return None


def save_content(content, filename, output_dir):
    """Save content to a file in the output directory and track changes."""
    from pathlib import Path

    filepath = str(Path(output_dir) / filename)
    relative_path = f"docs/{filename}"

    # Read previous content if file exists
    previous_content = None
    if Path(filepath).exists():
        try:
            with open(filepath, encoding="utf-8") as f:
                previous_content = f.read()
        except Exception as e:
            logger.warning(f"Could not read previous content for {filename}: {e}")

    try:
        # Write new content
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        logger.success(f"Saved file: {filepath}")

        # Update metadata with diff tracking
        update_content_hash(relative_path, content, previous_content)
        logger.debug(f"Updated metadata for {relative_path}")
    except Exception as e:
        logger.error(f"Failed to save file {filepath}: {e}")


def scrape_copilot_docs():
    """Scrape GitHub Copilot documentation and save to data/docs."""
    logger.info("Starting GitHub Copilot documentation scrape...")
    output_dir = create_output_dir()

    # Key GitHub Copilot documentation URLs
    docs_urls = {
        # Core Copilot Documentation
        "copilot-overview.md": "https://docs.github.com/en/copilot/about-github-copilot/what-is-github-copilot",
        "copilot-getting-started.md": "https://docs.github.com/en/copilot/getting-started-with-github-copilot",
        "copilot-chat.md": "https://docs.github.com/en/copilot/github-copilot-chat/using-github-copilot-chat-in-your-ide",
        # Agent & Extensions Documentation
        "copilot-extensions-overview.md": "https://docs.github.com/en/copilot/building-copilot-extensions/about-building-copilot-extensions",
        "copilot-extensions-integration.md": "https://docs.github.com/en/copilot/using-github-copilot/using-extensions-to-integrate-external-tools-with-copilot-chat",
        # Customization & Best Practices
        "copilot-custom-instructions.md": "https://docs.github.com/en/copilot/customizing-copilot/adding-custom-instructions-for-github-copilot",
        "copilot-best-practices.md": "https://docs.github.com/en/copilot/using-github-copilot/best-practices-for-using-github-copilot",
        "copilot-prompt-engineering.md": "https://docs.github.com/en/copilot/using-github-copilot/prompt-engineering-for-github-copilot",
        # Agent Workflow & Usage
        "copilot-asking-questions.md": "https://docs.github.com/en/copilot/using-github-copilot/asking-github-copilot-questions-in-your-ide",
        "copilot-code-suggestions.md": "https://docs.github.com/en/copilot/using-github-copilot/using-github-copilot-code-suggestions-in-your-editor",
        # Management & Configuration
        "copilot-managing-organization.md": "https://docs.github.com/en/copilot/managing-copilot/managing-github-copilot-in-your-organization",
        "copilot-configuration.md": "https://docs.github.com/en/copilot/configuring-github-copilot/configuring-github-copilot-in-your-environment",
        "copilot-responsible-use.md": "https://docs.github.com/en/copilot/responsible-use-of-github-copilot-features",
        "copilot-troubleshooting.md": "https://docs.github.com/en/copilot/troubleshooting-github-copilot",
    }

    # Fallback content in case network access fails
    sample_content = {
        # Core Copilot Documentation
        "copilot-overview.md": "# GitHub Copilot Overview\n\nGitHub Copilot is an AI pair programmer that helps you write code faster.",
        "copilot-getting-started.md": "# Getting Started with GitHub Copilot\n\nStart using GitHub Copilot in your favorite IDE.",
        "copilot-chat.md": "# GitHub Copilot Chat\n\nInteract with Copilot using natural language chat.",
        # Agent & Extensions Documentation
        "copilot-extensions-overview.md": "# Building Copilot Extensions\n\nLearn how to build custom extensions and agents for GitHub Copilot.",
        "copilot-extensions-integration.md": "# Integrating External Tools with Copilot\n\nUse extensions to integrate external tools and services with Copilot Chat.",
        # Customization & Best Practices
        "copilot-custom-instructions.md": "# Custom Instructions for Copilot\n\nCustomize Copilot's behavior with custom instructions tailored to your workflow.",
        "copilot-best-practices.md": "# Best Practices for Using GitHub Copilot\n\nLearn best practices to get the most out of GitHub Copilot.",
        "copilot-prompt-engineering.md": "# Prompt Engineering for GitHub Copilot\n\nMaster the art of writing effective prompts for Copilot.",
        # Agent Workflow & Usage
        "copilot-asking-questions.md": "# Asking Copilot Questions in Your IDE\n\nLearn how to effectively ask questions and get answers from Copilot in your IDE.",
        "copilot-code-suggestions.md": "# Using Copilot Code Suggestions\n\nGet the most out of Copilot's code suggestions in your editor.",
        # Management & Configuration
        "copilot-managing-organization.md": "# Managing Copilot in Your Organization\n\nAdministrative guide for managing GitHub Copilot across your organization.",
        "copilot-configuration.md": "# Configuring GitHub Copilot\n\nConfigure Copilot to work best in your development environment.",
        "copilot-responsible-use.md": "# Responsible Use of GitHub Copilot\n\nGuidelines for responsible and ethical use of Copilot features.",
        "copilot-troubleshooting.md": "# Troubleshooting GitHub Copilot\n\nCommon issues and solutions for GitHub Copilot.",
    }

    successful_fetches = 0

    for filename, url in docs_urls.items():
        logger.info(f"Fetching documentation for: {filename} from {url}")
        content = fetch_url(url)
        if content:
            logger.debug(f"Parsing HTML content for {filename}")
            soup = BeautifulSoup(content, "html.parser")
            main_content = (
                soup.find("article")
                or soup.find("main")
                or soup.find("div", class_="markdown-body")
            )
            if main_content:
                text_content = main_content.get_text(separator="\n", strip=True)
                logger.success(f"Extracted main content for {filename}")
                save_content(text_content, filename, output_dir)
                successful_fetches += 1
            else:
                logger.warning(f"Main content not found for {filename}, saving raw HTML.")
                save_content(content, filename, output_dir)
                successful_fetches += 1
        else:
            logger.warning(f"Fetch failed for {filename}, using fallback content.")
            save_content(sample_content[filename], filename, output_dir)

        # Be respectful and don't overwhelm the server
        time.sleep(1)

    # Create a summary file with timestamp
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S UTC")
    summary = f"""# GitHub Copilot Documentation Scrape Summary\n\nLast updated: {timestamp}\nSuccessful fetches: {successful_fetches}/{len(docs_urls)}\n\n## Files scraped:\n"""
    from pathlib import Path

    for filename in docs_urls:
        if (Path(output_dir) / filename).exists():
            summary += f"- {filename}\n"

    save_content(summary, "scrape-summary.md", output_dir)
    logger.info(f"Scraping completed. Files saved to {output_dir}/")


if __name__ == "__main__":
    logger.add(
        "scraper.log",
        format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level: <8}</level> | <cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>",
        level="DEBUG",
        rotation="1 MB",
    )
    scrape_copilot_docs()
