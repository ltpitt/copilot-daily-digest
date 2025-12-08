#!/usr/bin/env python3
"""
Test YouTube API access

This script tests YouTube Data API v3 connectivity.
Note: API key is OPTIONAL - the project works with RSS feeds by default.

Usage:
    # Set API key
    export YOUTUBE_API_KEY="your-api-key-here"
    
    # Run test
    python scripts/test_youtube_api.py

Expected output:
    ✅ YouTube API working!
    Test search returned 1 results
"""

import os
import sys

def test_youtube_api():
    """Test YouTube Data API v3 connectivity"""
    api_key = os.getenv("YOUTUBE_API_KEY")
    if not api_key:
        print("⚠️  YOUTUBE_API_KEY not found in environment")
        print("ℹ️  This is OPTIONAL - the project works with RSS feeds by default")
        print("ℹ️  API is only needed for enrichment (duration, view counts, etc)")
        return False
    
    try:
        from googleapiclient.discovery import build
        
        youtube = build("youtube", "v3", developerKey=api_key)
        
        # Test with a simple search on GitHub channel
        request = youtube.search().list(
            part="snippet",
            channelId="UC7c3Kb6jYCRj4JOHHZTxKsQ",  # GitHub channel
            maxResults=1,
            type="video"
        )
        response = request.execute()
        
        print("✅ YouTube API working!")
        count = len(response.get('items', []))
        result_text = "result" if count == 1 else "results"
        print(f"✅ Test search returned {count} {result_text}")
        
        if response.get('items'):
            video = response['items'][0]
            print(f"✅ Sample video: {video['snippet']['title']}")
        
        return True
    
    except ImportError:
        print("❌ google-api-python-client not installed")
        print("ℹ️  Install with: pip install google-api-python-client")
        return False
    
    except Exception as e:
        print(f"❌ YouTube API test failed: {e}")
        print("ℹ️  Check your API key and ensure YouTube Data API v3 is enabled")
        return False


if __name__ == "__main__":
    success = test_youtube_api()
    sys.exit(0 if success else 1)
