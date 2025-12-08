#!/bin/bash
set -e

echo "🧪 Testing full workflow..."

# Step 1: Fetch all content
echo "📥 Step 1: Fetching content..."
python scraper/fetch_docs.py
python scraper/fetch_blog.py
python scraper/fetch_youtube.py

# Step 2: Detect changes
echo "🔍 Step 2: Detecting changes..."
python scraper/detect_changes.py

# Step 3: Check if changes detected
if grep -q '"has_changes": true' data/changes-summary.json; then
  echo "✅ Changes detected!"
  
  # Step 4: Generate content
  echo "📝 Step 3: Generating content..."
  python scraper/generate_videos.py
  # TODO: Add other content generators
  
  echo "✅ Workflow test complete!"
else
  echo "ℹ️  No changes detected. Skipping content generation."
fi
