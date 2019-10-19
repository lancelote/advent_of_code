test:
	python -m pytest tests

lint:
	python -m pylint --rcfile=.pylintrc main.py src
	python -m pylint --rcfile=.pylintrc_tests tests
	python -m pydocstyle --add-ignore=D105
	python -m pycodestyle --select E,W .
	python -m mypy . --ignore-missing-imports

run:
	python main.py solve

install:
	python -m pip install -r requirements.txt

pur:
	pur -r requirements.txt