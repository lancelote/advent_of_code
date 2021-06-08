test:
	python -m pytest tests

lint:
	pre-commit run --all-files

run:
	python main.py solve

install:
	python -m pip install -r requirements-dev.txt

pur:
	pur -r requirements.txt
