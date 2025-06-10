.PHONY: setup install test coverage lint format clean docs help

# Variables
PYTHON = python
PIP = $(PYTHON) -m pip
PYTEST = pytest
PYTEST_FLAGS = --verbose --color=yes
COVERAGE_FLAGS = --cov=. --cov-report=term --cov-report=html
LINT_FLAGS = --disable=C0111,R0903
FORMAT_SOURCE = main.py test_project.py

help:
    @echo "Available commands"
    @echo "  make setup      - Create virtual environment"
    @echo "  make install    - Install dependencies"
    @echo "  make test       - Run tests"
    @echo "  make coverage   - Run tests with coverage"
    @echo "  make lint       - Check code with pylint"
    @echo "  make format     - Format code with black"
    @echo "  make clean      - Remove temporary files"
    @echo "  make docs       - Generate documentation"
    
    setup:
    $(PYTHON) -m venv venv
    @echo "Virtual environment created. Activate with: source venv/bin/activate (Linux/Mac) or venv\\Scripts\\activate (Windows)"

install:
    $(PIP) install --upgrade pip
    $(PIP) install -r requirements.txt

test:
    $(PYTEST) $(PYTEST_FLAGS) test_project.py

coverage:
    $(PYTEST) $(PYTEST_FLAGS) $(COVERAGE_FLAGS) test_project.py

lint:
    pylint $(LINT_FLAGS) main.py test_project.py

format:
    black $(FORMAT_SOURCE)

format-check:
    black --check $(FORMAT_SOURCE)

clean:
    rm -rf __pycache__
    rm -rf .pytest_cache
    rm -rf htmlcov
    rm -rf .coverage
    rm -rf .tox
    find . -type d -name __pycache__ -exec rm -rf {} +
    find . -type f -name "*.pyc" -delete

docs:
    mkdir -p docs
    pdoc --html --output-dir docs main.py