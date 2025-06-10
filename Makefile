.PHONY: setup install test coverage lint format clean docs

PYTHON=python
PIP= $(PYTHON) -m pip
PYTEST = pytest
PYTEST_FLAGS = --verbose --color=yes
FORMAT_SOURCE = main.py test_project.py dice.py

install:
	$(PIP) install --upgrade pip
	$(PIP) install -r requirements.txt

test:
	$(PYTEST) $(PYTEST_FLAGS) test_project.py

coverage:
	$(PYTEST) $(PYTEST_FLAGS) $(COVERAGE_FLAGS) test_project.py

lint:
	pylint main.py || true
	pylint test_project.py || true 
	pylint dice.py || true

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