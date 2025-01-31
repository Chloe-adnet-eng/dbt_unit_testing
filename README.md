# dbt_unit_testing

Ce projet a pour objectif de tester l'approche **Test-Driven Development (TDD)** avec **dbt** via des tests unitaires. Il vous permet d'appliquer des tests unitaires sur vos modèles SQL pour garantir la qualité et la stabilité de votre code tout au long du développement.

## Installation

Pour installer ce projet et ses dépendances, suivez les étapes ci-dessous :

1. **Installer `uv`** :
   
   Exécutez la commande suivante pour installer `uv` :

   ```bash
   curl -LsSf https://astral.sh/uv/install.sh | sh
   ```

2. **Créer et activer un environnement virtuel** :

Une fois uv installé, créez un environnement virtuel pour ce projet :

```bash
    uv venv dbt-unit-testing-venv
    source dbt-unit-testing-venv/bin/activate
```

3. **Installer dbt** :

Dans votre environnement virtuel activé, installez dbt et duckdb, pathlib avec les commandes suivantes :

```bash
uv pip install dbt
uv pip install duckdb
uv pip install pathlib
uv pip install dbt-core
uv pip install dbt-duckdb
```

4. **Construire la base de donnée locale**:

```bash 
python duckdb/main.py
```

5. **Editer votre dbt `profiles.yml`**
```bash
code ~/.dbt/profiles.yml
```
    Ajouter votre profile dbt doit pointer sur la database duck_db que vous avez construite! 
    dbt_unit_testing:
```yml
  target: dev
  outputs:
    dev:
      type: duckdb
      threads: 1
      path: <PATH_TO_PROJECT>/dbt_unit_testing/kata.duckdb
``````