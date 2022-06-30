.DEFAULT_GOAL := help

DOC_INDEX := file://$(abspath $(dir $(lastword $(MAKEFILE_LIST)))/docs/_build/html/index.html)

# From https://marmelab.com/blog/2016/02/29/auto-documented-makefile.html
.PHONY: help
help:
	@grep -E '^[a-zA-Z_-_.]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

.PHONY: dev.install
dev.install:  ## Install local code as the package
	pip install -e .

clean:  ## Clean the distro directory
	rm -rf dist/*

setup:  ## Setup the environment
	mkdir -p dist
	mkdir -p build