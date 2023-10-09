build:
	poetry build

install:
	poetry install

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl
# Тут лучше инструкцию обозвать так же со словом package-...
# reinstall:
# 	pip install --user --force-reinstall dist/*.whl
reinstall:
	pip install --user --force-reinstall dist/*.whl

brain-games:
	poetry run brain-games

brain-even:
	poetry run brain-even

brain-calc:
	poetry run brain-calc

brain-gcd:
	poetry run brain-gcd

brain-progression:
	poetry run brain-progression

brain-prime:
	poetry run brain-prime

lint:
	poetry run flake8 brain_games
