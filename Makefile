# Makefile pour configurer l'environnement dbt_unit_testing

# Variables
VENV_NAME = dbt-unit-testing

# Commandes
install_uv:
	curl -LsSf https://astral.sh/uv/install.sh | sh

create_venv:
	uv venv $(VENV_NAME)

activate_venv:
	source $(VENV_NAME)/bin/activate

install_dependencies:
	uv pip install dbt
	uv pip install duckdb
	uv pip install pathlib
	uv pip install dbt-core
	uv pip install dbt-duckdb

build_database:
	uv run python duckdb/main.py

