install: # установка зависимостей
	poetry install
build: # сборка пакета
	poetry build
package-install: # установка пакета из дистрибутива
	python3 -m pip install --user dist/*.whl
package-uninstall: # удаление пакета
	python3 -m pip uninstall dist/*.whl
lint:
	poetry run flake8 gen_diff
tcov:
	poetry run pytest --cov=gen_diff --cov-report xml tests/