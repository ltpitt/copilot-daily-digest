#!/usr/bin/env python3
"""
Script to fetch and scrape GitHub Copilot documentation for the daily digest.
"""

import os
import requests
from bs4 import BeautifulSoup
import time
from urllib.parse import urljoin, urlparse
from loguru import logger

def create_output_dir():
    """Create the top-level raw_docs directory if it doesn't exist."""
    # Get the absolute path to the project root
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    output_dir = os.path.join(project_root, "raw_docs")
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        logger.info(f"Created output directory: {output_dir}")
    else:
        logger.debug(f"Output directory already exists: {output_dir}")
    return output_dir

def fetch_url(url):
    """Fetch content from a URL with error handling."""
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (compatible; GitHub-Copilot-Daily-Digest/1.0)'
        }
        logger.info(f"Attempting to fetch URL: {url}")
        response = requests.get(url, headers=headers, timeout=30)
        response.raise_for_status()
        logger.success(f"Successfully fetched URL: {url}")
        return response.text
    except requests.RequestException as e:
        logger.error(f"Error fetching {url}: {e}")
        return None

def save_content(content, filename, output_dir):
    """Save content to a file in the output directory."""
    filepath = os.path.join(output_dir, filename)
    try:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        logger.success(f"Saved file: {filepath}")
    except Exception as e:
        logger.error(f"Failed to save file {filepath}: {e}")


def scrape_copilot_docs():
    """Scrape GitHub Copilot documentation and save to raw_docs."""
    logger.info("Starting GitHub Copilot documentation scrape...")
    output_dir = create_output_dir()

    # Key GitHub Copilot documentation URLs
    docs_urls = {
        'copilot-overview.md': 'https://docs.github.com/en/copilot/about-github-copilot/what-is-github-copilot',
        'copilot-getting-started.md': 'https://docs.github.com/en/copilot/getting-started-with-github-copilot',
        'copilot-chat.md': 'https://docs.github.com/en/copilot/github-copilot-chat/using-github-copilot-chat-in-your-ide'
    }

    # Fallback content in case network access fails
    sample_content = {
        'copilot-overview.md': "# GitHub Copilot Overview\n\nGitHub Copilot is an AI pair programmer that helps you write code faster.",
        'copilot-getting-started.md': "# Getting Started with GitHub Copilot\n\nStart using GitHub Copilot in your favorite IDE.",
        'copilot-chat.md': "# GitHub Copilot Chat\n\nInteract with Copilot using natural language chat."
    }

    successful_fetches = 0

    for filename, url in docs_urls.items():
        logger.info(f"Fetching documentation for: {filename} from {url}")
        content = fetch_url(url)
        if content:
            logger.debug(f"Parsing HTML content for {filename}")
            soup = BeautifulSoup(content, 'html.parser')
            main_content = soup.find('article') or soup.find('main') or soup.find('div', class_='markdown-body')
            if main_content:
                text_content = main_content.get_text(separator='\n', strip=True)
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
    timestamp = time.strftime('%Y-%m-%d %H:%M:%S UTC')
    summary = f"""# GitHub Copilot Documentation Scrape Summary\n\nLast updated: {timestamp}\nSuccessful fetches: {successful_fetches}/{len(docs_urls)}\n\n## Files scraped:\n"""
    for filename in docs_urls.keys():
        if os.path.exists(os.path.join(output_dir, filename)):
            summary += f"- {filename}\n"

    save_content(summary, 'scrape-summary.md', output_dir)
    logger.info(f"Scraping completed. Files saved to {output_dir}/")

if __name__ == "__main__":
    logger.add("scraper.log", format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level: <8}</level> | <cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>", level="DEBUG", rotation="1 MB")
    scrape_copilot_docs()
