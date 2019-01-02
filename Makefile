test:
	python -m pytest tests

lint:
	python -m pylint --rcfile=.pylintrc main.py src
	python -m pylint --rcfile=.pylintrc_tests tests
	python -m pydocstyle --add-ignore=D105
	python -m pycodestyle --select E,W .
	python -m mypy . --ignore-missing-imports

run:
	python main.py

update:
	python -m pip install -r requirements.txt

deps:
	pur -r requirements.txt