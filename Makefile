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

test:
	poetry run gendiff ./tmp/file1.json ./tmp/file2.json
