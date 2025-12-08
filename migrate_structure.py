#!/usr/bin/env python3
"""
Repository Restructuring Migration Script
==========================================

This script migrates the copilot-daily-digest repository from its current
structure to the new organized directory layout.

Run this script from the repository root:
    python migrate_structure.py

What it does:
1. Creates new directory structure (data/, content/, templates/)
2. Moves raw_docs/ → data/docs/
3. Copies content files to content/ directory
4. Creates metadata.json
5. Updates .gitignore
"""

import os
import sys
import json
import shutil
from pathlib import Path
from datetime import datetime

class RepositoryMigration:
    def __init__(self, repo_root=None):
        """Initialize migration with repository root."""
        if repo_root is None:
            # Try to detect repository root
            current = Path.cwd()
            if (current / '.git').exists():
                repo_root = current
            else:
                print("Error: Could not find repository root (.git directory)")
                print("Please run this script from the repository root or provide path")
                sys.exit(1)
        
        self.repo_root = Path(repo_root)
        self.dry_run = False
        
    def log(self, message, level="INFO"):
        """Log a message with timestamp."""
        timestamp = datetime.now().strftime("%H:%M:%S")
        prefix = {
            "INFO": "ℹ️ ",
            "SUCCESS": "✓ ",
            "WARNING": "⚠️ ",
            "ERROR": "✗ ",
            "SKIP": "- "
        }.get(level, "  ")
        print(f"[{timestamp}] {prefix}{message}")
    
    def create_directories(self):
        """Create the new directory structure."""
        self.log("Creating new directory structure...", "INFO")
        
        directories = [
            "data",
            "data/docs",
            "data/blog", 
            "data/feeds",
            "data/videos",
            "data/changelogs",
            "content",
            "templates",
        ]
        
        for dir_path in directories:
            full_path = self.repo_root / dir_path
            if full_path.exists():
                self.log(f"Directory already exists: {dir_path}", "SKIP")
            else:
                if not self.dry_run:
                    full_path.mkdir(parents=True, exist_ok=True)
                    # Create .gitkeep to preserve in git
                    (full_path / ".gitkeep").touch()
                self.log(f"Created directory: {dir_path}", "SUCCESS")
    
    def create_metadata(self):
        """Create initial metadata.json file."""
        self.log("Creating metadata.json...", "INFO")
        
        metadata_path = self.repo_root / "data" / "metadata.json"
        
        if metadata_path.exists():
            self.log("metadata.json already exists", "SKIP")
            return
        
        metadata = {
            "last_updated": None,
            "content_hashes": {},
            "video_ids": [],
            "blog_urls": [],
            "doc_versions": {}
        }
        
        if not self.dry_run:
            with open(metadata_path, 'w') as f:
                json.dump(metadata, f, indent=2)
        
        self.log("Created data/metadata.json", "SUCCESS")
    
    def migrate_raw_docs(self):
        """Move raw_docs/ to data/docs/."""
        self.log("Migrating raw_docs/ to data/docs/...", "INFO")
        
        raw_docs = self.repo_root / "raw_docs"
        data_docs = self.repo_root / "data" / "docs"
        
        if not raw_docs.exists():
            self.log("No raw_docs/ directory found", "SKIP")
            return
        
        if not raw_docs.is_dir():
            self.log("raw_docs is not a directory", "WARNING")
            return
        
        moved_files = []
        for item in raw_docs.iterdir():
            if item.name in ['.gitkeep', '.DS_Store']:
                continue
                
            dest = data_docs / item.name
            if dest.exists():
                self.log(f"File already exists in destination: {item.name}", "SKIP")
                continue
            
            if not self.dry_run:
                shutil.move(str(item), str(dest))
            moved_files.append(item.name)
            self.log(f"Moved: {item.name}", "SUCCESS")
        
        if moved_files and not self.dry_run:
            # Remove raw_docs if empty
            try:
                remaining = list(raw_docs.iterdir())
                if not remaining or all(f.name in ['.gitkeep', '.DS_Store'] for f in remaining):
                    shutil.rmtree(raw_docs)
                    self.log("Removed empty raw_docs/ directory", "SUCCESS")
            except Exception as e:
                self.log(f"Could not remove raw_docs/: {e}", "WARNING")
    
    def migrate_content_files(self):
        """Copy content files to content/ directory."""
        self.log("Migrating content files to content/...", "INFO")
        
        content_files = ["README.md", "cheatsheet.md", "changelog.md"]
        
        for filename in content_files:
            src = self.repo_root / filename
            dest = self.repo_root / "content" / filename
            
            if not src.exists():
                self.log(f"File not found: {filename}", "SKIP")
                continue
            
            if dest.exists():
                self.log(f"File already exists in content/: {filename}", "SKIP")
                continue
            
            if not self.dry_run:
                shutil.copy2(src, dest)
            self.log(f"Copied to content/: {filename}", "SUCCESS")
    
    def update_gitignore(self):
        """Update .gitignore with data directory rules."""
        self.log("Updating .gitignore...", "INFO")
        
        gitignore_path = self.repo_root / ".gitignore"
        
        new_rules = """
# Raw data (keep metadata and structure)
data/docs/*.md
data/blog/*.json
data/videos/*.json
data/feeds/*.xml

# Keep metadata
!data/metadata.json

# Keep directory structure
!data/**/.gitkeep
"""
        
        if gitignore_path.exists():
            with open(gitignore_path, 'r') as f:
                current_content = f.read()
            
            if 'data/docs/' in current_content:
                self.log(".gitignore already contains data rules", "SKIP")
                return
            
            if not self.dry_run:
                with open(gitignore_path, 'a') as f:
                    f.write(new_rules)
            self.log("Added data rules to .gitignore", "SUCCESS")
        else:
            if not self.dry_run:
                with open(gitignore_path, 'w') as f:
                    f.write(new_rules)
            self.log("Created .gitignore with data rules", "SUCCESS")
    
    def run(self, dry_run=False):
        """Run the complete migration."""
        self.dry_run = dry_run
        
        print("=" * 70)
        print("Repository Restructuring Migration")
        print("=" * 70)
        print(f"Repository: {self.repo_root}")
        print(f"Mode: {'DRY RUN' if dry_run else 'LIVE'}")
        print("=" * 70)
        print()
        
        try:
            self.create_directories()
            print()
            
            self.create_metadata()
            print()
            
            self.migrate_raw_docs()
            print()
            
            self.migrate_content_files()
            print()
            
            self.update_gitignore()
            print()
            
            print("=" * 70)
            self.log("Migration completed successfully!", "SUCCESS")
            print("=" * 70)
            
            if not dry_run:
                print()
                print("Next steps:")
                print("1. Review changes: git status")
                print("2. Update file references in scripts and workflows")
                print("3. Run tests to verify nothing broke")
                print("4. Commit changes: git add . && git commit -m 'Restructure repository directories'")
            
        except Exception as e:
            print()
            print("=" * 70)
            self.log(f"Migration failed: {e}", "ERROR")
            print("=" * 70)
            import traceback
            traceback.print_exc()
            sys.exit(1)


def main():
    """Main entry point."""
    import argparse
    
    parser = argparse.ArgumentParser(
        description="Migrate repository structure for copilot-daily-digest"
    )
    parser.add_argument(
        '--dry-run',
        action='store_true',
        help='Preview changes without actually making them'
    )
    parser.add_argument(
        '--repo',
        default=None,
        help='Repository root path (default: current directory)'
    )
    
    args = parser.parse_args()
    
    migration = RepositoryMigration(repo_root=args.repo)
    migration.run(dry_run=args.dry_run)


if __name__ == "__main__":
    main()
