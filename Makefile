build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl --force-reinstall

setup: build publish package-install

lint:
	poetry run flake8 gendiff

install:
	poetry install

check: selfcheck test lint

test:
	poetry run pytest

test-coverage:
	poetry run pytest --cov=gendiff --cov-report xml