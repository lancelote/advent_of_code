lint:
	uv run ruff check

format:
	uv run ruff format

ci-format:
	uv run ruff format --check --diff

typecheck:
	uv run ty check

check: format lint typecheck

test:
	uv run pytest tests

install:
	uv sync --locked --all-extras --dev