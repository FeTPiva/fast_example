
runserver:
	uvicorn credit_score.main:app --host 0.0.0.0 --port 8000

build:
	docker-compose up -d --build

up:
	docker-compose up -d

down:
	docker-compose down

reload: down up

rebuild: down build


dist: clean ## builds source and wheel package
	python setup.py sdist
	ls -l dist


clean-build:
	rm -rf build/
	rm -rf dist/

clean-pyc: ## remove Python file artifacts
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.DS_Store' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +
	find . -name '*.ipynb*' -exec rm -r {} +
	find . -name '*.db' -exec rm {} +

clean-test: ## remove test and coverage artifacts
	rm -fr .tox/
	rm -f .coverage
	rm -fr htmlcov/
	rm -fr .pytest_cache

clean-all: ## remove test and coverage artifacts
	rm -fr .vscode
	rm -f MANIFEST
	rm -fr .pytest_cache

clean: clean-pyc clean-all clean-build

ssh: 
	ssh -i ../data-science-prod.pem ec2-user@172.24.13.215

