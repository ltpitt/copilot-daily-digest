.PHONY: help install setup fetch-all fetch-blog fetch-docs fetch-videos fetch-trainings fetch-next detect-changes enrich-dates validate validate-links validate-whats-new lint clean

# Variables
PYTHON := python3
PIP := pip3
VENV_DIR := venv
SCRIPTS_DIR := scripts

# Default target - show help
help:
	@echo "📰 GitHub Copilot Daily Digest - Makefile Commands"
	@echo ""
	@echo "Setup & Installation:"
	@echo "  make help              Show this help message"
	@echo "  make install           Install Python dependencies from requirements.txt"
	@echo "  make setup             Full setup (install + fetch all data)"
	@echo ""
	@echo "Data Fetching:"
	@echo "  make fetch-all         Fetch all data sources (blog, docs, videos, trainings, github-next)"
	@echo "  make fetch-blog        Fetch blog posts from GitHub blog"
	@echo "  make fetch-docs        Fetch official Copilot documentation"
	@echo "  make fetch-videos      Fetch YouTube videos"
	@echo "  make fetch-trainings   Fetch training courses"
	@echo "  make fetch-next        Fetch GitHub Next experimental projects"
	@echo ""
	@echo "Data Processing:"
	@echo "  make detect-changes    Detect what changed since last run"
	@echo "  make enrich-dates      Enrich blog post dates from URLs"
	@echo ""
	@echo "Validation & Quality:"
	@echo "  make validate          Run all validations (links + whats-new)"
	@echo "  make validate-links    Validate all markdown links"
	@echo "  make validate-whats-new Validate WHATS-NEW.md dates and ordering"
	@echo "  make lint              Lint Python code with ruff"
	@echo ""
	@echo "Maintenance:"
	@echo "  make clean             Remove generated files (cache, reports)"
	@echo ""
	@echo "Complete Workflow Example:"
	@echo "  make install && make fetch-all && make detect-changes && make validate"
	@echo ""

# Install Python dependencies
install:
	@echo "📦 Installing dependencies..."
	$(PIP) install -r requirements.txt

# Full setup - install dependencies and fetch initial data
setup: install
	@echo "🚀 Running initial setup..."
	$(MAKE) fetch-all
	$(MAKE) enrich-dates
	$(MAKE) detect-changes
	@echo "✅ Setup complete! Run 'make validate' to verify data quality."

# Fetch all data sources
fetch-all: fetch-blog fetch-docs fetch-videos fetch-trainings fetch-next
	@echo "✅ All data sources fetched successfully"

# Individual fetch targets
fetch-blog:
	@echo "📝 Fetching blog posts..."
	@$(PYTHON) $(SCRIPTS_DIR)/fetch_blog.py

fetch-docs:
	@echo "📚 Fetching documentation..."
	@$(PYTHON) $(SCRIPTS_DIR)/fetch_docs.py

fetch-videos:
	@echo "🎥 Fetching YouTube videos..."
	@$(PYTHON) $(SCRIPTS_DIR)/fetch_youtube.py

fetch-trainings:
	@echo "🎓 Fetching training courses..."
	@$(PYTHON) $(SCRIPTS_DIR)/fetch_trainings.py

fetch-next:
	@echo "🔬 Fetching GitHub Next experiments..."
	@$(PYTHON) $(SCRIPTS_DIR)/fetch_github_next.py

# Data processing targets
detect-changes:
	@echo "🔍 Detecting changes..."
	@$(PYTHON) $(SCRIPTS_DIR)/detect_changes.py

enrich-dates:
	@echo "📅 Enriching blog dates..."
	@$(PYTHON) $(SCRIPTS_DIR)/enrich_blog_dates.py

# Validation targets
validate: validate-links validate-whats-new
	@echo "✅ All validations passed!"

validate-links:
	@echo "🔗 Validating links..."
	@$(PYTHON) $(SCRIPTS_DIR)/validate_links.py

validate-whats-new:
	@echo "📋 Validating WHATS-NEW.md..."
	@$(PYTHON) $(SCRIPTS_DIR)/validate_whats_new.py

# Lint Python code
lint:
	@echo "🔍 Linting Python code with ruff..."
	@ruff check $(SCRIPTS_DIR)/

# Clean up generated files
clean:
	@echo "🧹 Cleaning up generated files..."
	@find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
	@find . -type f -name "*.pyc" -delete
	@rm -f link-validation-report.json
	@echo "✅ Cleanup complete"

# Print data directory info
info:
	@echo "📊 Project Information"
	@echo "Data sources:"
	@ls -lh data/ | tail -n +2 | awk '{print "  " $$9 " (" $$5 ")"}'
	@echo ""
	@echo "Content files:"
	@ls -lh content/*.md | awk '{print "  " $$9 " (" $$5 ")"}'
