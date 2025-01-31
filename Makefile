# Makefile pour configurer l'environnement dbt_unit_testing

# Variables
VENV_NAME = dbt-unit-testing

# Commandes
install_uv:
	curl -LsSf https://astral.sh/uv/install.sh | sh

install_dependencies:
	uv sync

build_database:
	uv run python duckdb/main.py

