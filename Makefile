test:
	py.test tests

lint:
	pylint main.py src tests
	pydocstyle
	pycodestyle --select E,W .

run:
	@python main.py

update:
	python -m pip install -U pip setuptools
	python -m pip install -r requirements.txt

requirements:
	pur -r requirements.txt
