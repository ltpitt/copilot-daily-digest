#!/usr/bin/env python3
"""
Script to fetch and scrape GitHub Copilot documentation for the daily digest.
"""

import os
import requests
from bs4 import BeautifulSoup
import time
from urllib.parse import urljoin, urlparse

def create_output_dir():
    """Create the raw_docs directory if it doesn't exist."""
    output_dir = "raw_docs"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    return output_dir

def fetch_url(url):
    """Fetch content from a URL with error handling."""
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (compatible; GitHub-Copilot-Daily-Digest/1.0)'
        }
        response = requests.get(url, headers=headers, timeout=30)
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return None

def save_content(content, filename, output_dir):
    """Save content to a file in the output directory."""
    filepath = os.path.join(output_dir, filename)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Saved: {filepath}")

def scrape_copilot_docs():
    """Scrape GitHub Copilot documentation and save to raw_docs."""
    output_dir = create_output_dir()
    
    # Key GitHub Copilot documentation URLs
    docs_urls = {
        'copilot-overview.md': 'https://docs.github.com/en/copilot/about-github-copilot/what-is-github-copilot',
        'copilot-getting-started.md': 'https://docs.github.com/en/copilot/getting-started-with-github-copilot',
        'copilot-using-in-ide.md': 'https://docs.github.com/en/copilot/using-github-copilot/getting-started-with-github-copilot-in-your-ide',
        'copilot-chat.md': 'https://docs.github.com/en/copilot/github-copilot-chat/using-github-copilot-chat-in-your-ide',
        'copilot-extensions.md': 'https://docs.github.com/en/copilot/using-github-copilot/using-github-copilot-extensions',
    }
    
    # Fallback content in case network access fails
    sample_content = {
        'copilot-overview.md': "# GitHub Copilot Overview\n\nGitHub Copilot is an AI pair programmer that helps you write code faster.",
        'copilot-getting-started.md': "# Getting Started with GitHub Copilot\n\nStart using GitHub Copilot in your favorite IDE.",
        'copilot-using-in-ide.md': "# Using GitHub Copilot in Your IDE\n\nLearn how to use Copilot features in various IDEs.",
        'copilot-chat.md': "# GitHub Copilot Chat\n\nInteract with Copilot using natural language chat.",
        'copilot-extensions.md': "# GitHub Copilot Extensions\n\nExtend Copilot functionality with third-party integrations."
    }
    
    successful_fetches = 0
    
    for filename, url in docs_urls.items():
        print(f"Fetching: {url}")
        content = fetch_url(url)
        if content:
            # Parse the HTML and extract main content
            soup = BeautifulSoup(content, 'html.parser')
            
            # Extract the main article content
            main_content = soup.find('article') or soup.find('main') or soup.find('div', class_='markdown-body')
            
            if main_content:
                # Convert to markdown-like format
                text_content = main_content.get_text(separator='\n', strip=True)
                save_content(text_content, filename, output_dir)
                successful_fetches += 1
            else:
                # Fallback: save raw content
                save_content(content, filename, output_dir)
                successful_fetches += 1
        else:
            # Use sample content if fetch fails
            print(f"Using fallback content for {filename}")
            save_content(sample_content[filename], filename, output_dir)
        
        # Be respectful and don't overwhelm the server
        time.sleep(1)
    
    # Create a summary file with timestamp
    timestamp = time.strftime('%Y-%m-%d %H:%M:%S UTC')
    summary = f"""# GitHub Copilot Documentation Scrape Summary

Last updated: {timestamp}
Successful fetches: {successful_fetches}/{len(docs_urls)}

## Files scraped:
"""
    for filename in docs_urls.keys():
        if os.path.exists(os.path.join(output_dir, filename)):
            summary += f"- {filename}\n"
    
    save_content(summary, 'scrape-summary.md', output_dir)
    print(f"Scraping completed. Files saved to {output_dir}/")

if __name__ == "__main__":
    scrape_copilot_docs()