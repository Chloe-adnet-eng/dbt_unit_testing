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
    uv venv dbt-unit-testing-venv --python 3.11
    source dbt-unit-testing-venv/bin/activate
```

3. **Installer dbt** :

Dans votre environnement virtuel activé, installez dbt avec la commande suivante :

```bash
uv pip install dbt
```