# Makefile for ace-tools-lite

# Default target
.PHONY: help
help:
	@echo "Makefile commands:"
	@echo "  install       Install dependencies (incl. dev)"
	@echo "  format        Run black formatter"
	@echo "  build         Build the package"
	@echo "  publish       Publish to PyPI"
	@echo "  test-publish  Publish to TestPyPI"
	@echo "  clean         Remove build artifacts"

install:
	poetry install --with dev --no-root

format:
	poetry run black ace_tools

build:
	poetry build

publish: build
	poetry publish --username __token__ --password $(PYPI_TOKEN)

test-publish: build
	poetry publish --repository testpypi --username __token__ --password $(TEST_PYPI_TOKEN)

clean:
	rm -rf dist/ build/ *.egg-info
