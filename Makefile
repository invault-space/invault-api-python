.PHONY: venv-deps test-deps build test test-all

TEST_PKGS = pytest pytest-timeout
PIP = ./.venv/bin/pip3
PYTHON = ./.venv/bin/python3
PYTEST = ./.venv/bin/pytest

venv-deps:
	@python3 -m venv .venv

build: venv-deps
	@$(PIP) install -q build
	@$(PYTHON) -m build

tox-deps: venv-deps
	@$(PIP) install tox

test-deps: venv-deps
	@$(PIP) install $(TEST_PKGS)
	@${PIP} install -r requirements.txt

test: test-deps
	$(PYTEST)

test-all: venv-deps tox-deps
	tox
