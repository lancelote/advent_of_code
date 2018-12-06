test:
	python -m pytest tests

lint:
	python -m pylint main.py src tests
	python -m pydocstyle
	python -m pycodestyle --select E,W .
	python -m mypy . --ignore-missing-imports

run:
	python main.py