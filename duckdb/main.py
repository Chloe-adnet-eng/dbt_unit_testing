import duckdb
from pathlib import Path

INPUT_PATH = Path(__name__).parent / 'duckdb' / 'inputs' 
PERSONNES_INPUT = INPUT_PATH / 'personnes.csv'
VOITURES_INPUT = INPUT_PATH / 'voitures.csv'


# Connexion à la base de données kata.duckdb
conn = duckdb.connect('kata.duckdb')

conn.execute("CREATE SCHEMA IF NOT EXISTS kata.bronze")

tables = conn.execute("SHOW ALL TABLES").fetchall()
personnes_exists = any(table[0] == 'kata' and table[1] == 'bronze' and table[2] =='personnes' for table in tables)


print("⏳ Ajout de la table PERSONNES")
if not personnes_exists:
    conn.execute("""
    CREATE TABLE bronze.personnes (
        identifiant_personne BIGINT PRIMARY KEY,
        age BIGINT,
        nom TEXT,
        prenom TEXT,
        identifiant TEXT,
        email TEXT,
        date_de_naissance DATE,
        permis BOOLEAN,
        metier TEXT,
        nombre_enfants BIGINT,
        xp TEXT
    );
    """)
    print("1️⃣ Table construite!")

    # Alimentation de la table personnes
    conn.execute(f"""
    COPY bronze.personnes FROM '{PERSONNES_INPUT}' (FORMAT CSV, HEADER TRUE, DELIMITER ',', QUOTE '"');
    """)
    print("2️⃣ Table personnes alimentée!")

else:
    print("Table personnes existe déjà, pas de modification.")

print("⏳ Ajout de la table VOITURES")
voitures_exists = any(table[0] == 'kata' and table[1] == 'bronze' and table[2] =='voitures' for table in tables)

if not voitures_exists:
    conn.execute("""
    CREATE TABLE bronze.voitures (
        identifiant_voiture BIGINT PRIMARY KEY,
        identifiant_personne BIGINT,  
        nombre_kilometre BIGINT,
        nombre_places BIGINT,
        date_mise_en_circulation DATE,
        couleur TEXT,
        marque TEXT,
        modele TEXT
    );
    """)
    print("1️⃣ Table voitures construite!")

    conn.execute(f"""
    COPY bronze.voitures FROM '{VOITURES_INPUT}' (FORMAT CSV, HEADER TRUE, DELIMITER ',', QUOTE '"');
    """)
    print("2️⃣ Table voitures alimentée!")

else:
    print("Table voitures existe déjà, pas de modification.")

conn.close()

