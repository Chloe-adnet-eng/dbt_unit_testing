SELECT 
    identifiant_voiture AS id, 
    identifiant_personne, 
    nombre_kilometre AS kilometrage, 
    nombre_places AS capacite,
    date_mise_en_circulation, 
    LOWER(TRIM(couleur)) AS couleur, 
    LOWER(TRIM(marque,)) AS marque,
    LOWER(TRIM(modele)) AS modele
FROM {{ source('kata', 'voitures') }}