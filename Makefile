# Makefile for copilot-daily-digest

.PHONY: help lint format validate clean setup ensure-venv ensure-ruff

help:
	@echo "Available targets:"
	@echo "  lint      - Run ruff linter on the codebase"
	@echo "  format    - Run ruff format on the codebase"
	@echo "  validate  - Run all validation scripts (links, what's new)"
	@echo "  clean     - Remove Python cache files"
	@echo "  setup     - Create venv and install requirements"
	@echo "  ensure-venv - Ensure .venv exists and requirements are installed"
	@echo "  ensure-ruff - Ensure ruff is installed in .venv"



lint: ensure-venv ensure-ruff
	. .venv/bin/activate && ruff check scripts/



format: ensure-venv ensure-ruff
	. .venv/bin/activate && ruff format scripts/


validate: ensure-venv
	. .venv/bin/activate && python scripts/validate_links.py
	. .venv/bin/activate && python scripts/validate_whats_new.py

clean:
	find . -type d -name '__pycache__' -exec rm -rf {} +
	find . -type f -name '*.pyc' -delete


setup:
	python3 -m venv .venv
	. .venv/bin/activate && pip install --upgrade pip && pip install -r requirements.txt
	@echo "Virtual environment created in .venv. To activate, run:"
	@echo "  source .venv/bin/activate"

ensure-venv:
	@if [ ! -d ".venv" ]; then \
		python3 -m venv .venv; \
		. .venv/bin/activate && pip install --upgrade pip && pip install -r requirements.txt; \
	fi

ensure-ruff: ensure-venv
	. .venv/bin/activate && pip show ruff > /dev/null 2>&1 || pip install ruff
