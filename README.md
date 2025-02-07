# dbt_unit_testing

Ce projet a pour objectif de tester l'approche **Test-Driven Development (TDD)** avec **dbt** via des tests unitaires. Il permet d'appliquer des tests unitaires sur les modèles SQL pour garantir la qualité et la stabilité de votre code tout au long du développement.

## Installation

Pour installer ce projet et ses dépendances, suivez les étapes ci-dessous :

1. **Installer `uv`** :
   
   Exécutez la commande suivante pour installer `uv` :

    ```bash
    curl -LsSf https://astral.sh/uv/install.sh | sh
    ```

2. **Créer et activer un environnement virtuel** :

- Créez un environnement virtuel pour ce projet

  ```bash
      uv venv dbt-unit-testing-venv
      source dbt-unit-testing-venv/bin/activate
  ```

- Installez les dépendances du projet 

    ```bash
    uv sync
    ```

- Construire la base de donnée locale avec les données source du kata 
    ```bash
    make build_database
    ```

  *Correspond à l'exécution du script `duckdb/main.py`*


3. **Setup `dbt`**

- Editer le dbt `profiles.yml`

  ```bash
  code ~/.dbt/profiles.yml
  ```

  Ajustez votre profile dbt pour qu'il pointer sur la database duck_db que vous avez construite! 

    ```yml
      dbt_unit_testing:
      target: dev
      outputs:
        dev:
          type: duckdb
          threads: 1
          path: <PATH_TO_PROJECT>/dbt_unit_testing/kata.duckdb
    ```

## Utilisation du repertoire dbt

### 0 - Ajout des extensions 

L'expérience développeur dbt est facilitée par l'ajout de l'extention *Power User for dbt*! 
Pour ce kata, il vous est fortement recommandé d'installer l'extension.

### 1 - Première exécution 

Lancement de l'exécution des premiers modèles de donnée `src_personnes` et `src_voitures`.
```bash
dbt run --select <nom_du_modele>
```

### 2 - Lancement des tests 

##### 2.1 Test unitaire  

L'ensemble des tests unitaires sont définit dans `/tests/unit` et sont lancés via la commande 
```bash
dbt test --select "test_type:unit"
```


##### 2.2 Data test

Les tests data des modèles sont spécifiés dans chaque fichier de configuration associé à un modèle de donnée. Ils se lancent pour un modèle, un dossier ou pour l'ensemble des modèles. 

```bash
dbt test --select <nom_du_modele>
```

**Exemple**:
  Pour le modèle `dim_voitures_toyota`, le calcul du modèle est spécifié dans le fichier `dim_voitures_toyota.sql` et l'ensemble de la documentation et des tests de ce modèle sont spécifiés dans `dim_voitures_toyota.yml`. 

## Documentations 
### 1 Les documentations utiles pour le kata 
- Unit test avec dbt https://docs.getdbt.com/docs/build/unit-tests
- Data test avec dbt https://docs.getdbt.com/docs/build/data-tests
- Le TDD (Ressource notion theodo) https://www.notion.so/m33/ETQDev-je-pratique-le-TDD-16c8f3776f4f80bea77ff57b3376cae4