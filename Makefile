test:
	python -m pytest tests

lint:
	python -m pylint --rcfile=.pylintrc main.py src
	python -m pylint --rcfile=.pylintrc_tests tests
	python -m pydocstyle --add-ignore=D105
	python -m mypy . --ignore-missing-imports
	python -m black --check .

run:
	python main.py solve

install:
	python -m pip install -r requirements.txt

pur:
	pur -r requirements.txt