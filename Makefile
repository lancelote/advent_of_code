lint:
	uv run ruff check

format:
	uv run ruff format

ci-format:
	uv run ruff format --check --diff

typecheck:
	uv run basedpyright

check: lint format typecheck

test:
	uv run pytest tests

install:
	uv sync --locked --all-extras --dev