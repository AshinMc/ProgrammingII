.PHONY: setup install test coverage lint format clean docs

install:
	python -m pip install --upgrade pip
	python -m pip install -r requirements.txt

test:
	pytest --verbose test_project.py

lint:
	pylint main.py || true
	pylint test_project.py || true 
	pylint dice.py || true

format:
	black main.py dice.py test_project.py

format-check:
	black --check main.py dice.py test_project.py

clean:
	rm -rf __pycache__
	rm -rf .pytest_cache
	rm -rf htmlcov
	rm -rf .coverage
	rm -rf .tox
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
