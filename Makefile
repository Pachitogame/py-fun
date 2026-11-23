PYTHON ?= python
DOCS_BUILD ?= docs
.DEFAULT_GOAL := help
.PHONY: help install run tests docs dist package build clean clean-f

help:
	@echo "Targets: install, run, tests, docs, package, dist, build, clean, clean-f"

install:
	$(PYTHON) -m pip install -r requirements.txt

run:
	$(PYTHON) -m main

tests:
	$(PYTHON) -m pytest -v

docs:
	$(MAKE) -C docs docs DOCS_BUILD="$(abspath $(DOCS_BUILD))"

package: tests
	$(PYTHON) -m build --sdist --outdir dist

dist: package
	$(MAKE) docs DOCS_BUILD=dist

build: dist

clean:
	@echo "Generated directories: build/ dist/ py_fun.egg-info/ .pytest_cache/ docs/html/ docs/doctrees/"

clean-f:
	rm -rf build dist py_fun.egg-info .pytest_cache docs/html docs/doctrees
