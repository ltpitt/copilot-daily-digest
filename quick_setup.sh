#!/bin/bash
# Repository Restructuring - Quick Setup Script
# Run this from the repository root: bash quick_setup.sh

set -e  # Exit on error

echo "========================================="
echo "Repository Restructuring - Quick Setup"
echo "========================================="
echo ""

# Step 1: Create directory structure
echo "Step 1: Creating directory structure..."
mkdir -p data/docs
mkdir -p data/blog
mkdir -p data/feeds
mkdir -p data/videos
mkdir -p data/changelogs
mkdir -p content
mkdir -p templates
echo "✓ Directories created"
echo ""

# Step 2: Create .gitkeep files
echo "Step 2: Creating .gitkeep files..."
touch data/.gitkeep
touch data/docs/.gitkeep
touch data/blog/.gitkeep
touch data/feeds/.gitkeep
touch data/videos/.gitkeep
touch data/changelogs/.gitkeep
touch content/.gitkeep
touch templates/.gitkeep
echo "✓ .gitkeep files created"
echo ""

# Step 3: Create metadata.json
echo "Step 3: Creating metadata.json..."
cat > data/metadata.json << 'EOF'
{
  "last_updated": null,
  "content_hashes": {},
  "video_ids": [],
  "blog_urls": [],
  "doc_versions": {}
}
EOF
echo "✓ metadata.json created"
echo ""

# Step 4: Move raw_docs to data/docs
echo "Step 4: Moving raw_docs/ to data/docs/..."
if [ -d "raw_docs" ]; then
  if [ "$(ls -A raw_docs)" ]; then
    cp -r raw_docs/* data/docs/ 2>/dev/null || true
    echo "✓ Files moved from raw_docs/ to data/docs/"
    rm -rf raw_docs
    echo "✓ raw_docs/ directory removed"
  else
    echo "! raw_docs/ is empty, removing it"
    rmdir raw_docs
  fi
else
  echo "! raw_docs/ directory not found, skipping"
fi
echo ""

# Step 5: Copy content files
echo "Step 5: Copying content files to content/..."
for file in README.md cheatsheet.md changelog.md; do
  if [ -f "$file" ]; then
    cp "$file" "content/$file"
    echo "✓ Copied $file to content/"
  else
    echo "! $file not found, skipping"
  fi
done
echo ""

# Step 6: Update .gitignore
echo "Step 6: Updating .gitignore..."
if ! grep -q "data/docs/\*\.md" .gitignore 2>/dev/null; then
  cat >> .gitignore << 'EOF'

# Raw data (keep metadata and structure)
data/docs/*.md
data/docs/*.html
data/blog/*.json
data/videos/*.json
data/feeds/*.xml
data/feeds/*.json
data/changelogs/*.json

# Keep metadata and structure
!data/metadata.json
!data/**/.gitkeep
EOF
  echo "✓ .gitignore updated"
else
  echo "! .gitignore already contains data rules, skipping"
fi
echo ""

# Step 7: Update file references
echo "Step 7: Updating file references..."

# Update scraper/fetch_docs.py if it exists
if [ -f "scraper/fetch_docs.py" ]; then
  if grep -q "raw_docs" scraper/fetch_docs.py; then
    sed -i.bak 's/raw_docs/data\/docs/g' scraper/fetch_docs.py
    echo "✓ Updated scraper/fetch_docs.py"
  else
    echo "! No raw_docs references in scraper/fetch_docs.py"
  fi
else
  echo "! scraper/fetch_docs.py not found, skipping"
fi

# Note about workflow and instructions
echo "! Manual update required for .github/workflows/daily-agent.yml"
echo "! Manual update required for .github/copilot-instructions.md"
echo ""

# Step 8: Verification
echo "Step 8: Verification..."
echo "Directory structure:"
ls -la data/ 2>/dev/null || echo "! data/ not found"
ls -la content/ 2>/dev/null || echo "! content/ not found"
ls -la templates/ 2>/dev/null || echo "! templates/ not found"
echo ""

echo "metadata.json:"
cat data/metadata.json 2>/dev/null || echo "! metadata.json not found"
echo ""

echo "========================================="
echo "✓ Quick setup complete!"
echo "========================================="
echo ""
echo "Next steps:"
echo "1. Review changes: git status"
echo "2. Update .github/workflows/daily-agent.yml (see FILE_UPDATES.md)"
echo "3. Update .github/copilot-instructions.md (see FILE_UPDATES.md)"
echo "4. Search for remaining references: grep -r 'raw_docs' ."
echo "5. Test: python scraper/fetch_docs.py (if exists)"
echo "6. Commit: git add . && git commit -m 'Restructure repository directories'"
echo ""
