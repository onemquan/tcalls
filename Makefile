check_dirs := src tests examples 
exclude_folders := docs

# Run code-style
style:
	isort $(check_dirs)
	ruff check $(check_dirs) --fix --exclude $(exclude_folders)
	ruff format $(check_dirs) --exclude $(exclude_folders)

# Run tests for the library
test:
	python -m pytest -n auto --dist=loadfile -s -v ./tests/
