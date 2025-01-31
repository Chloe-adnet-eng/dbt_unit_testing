SELECT 
    identifiant_personne AS id, 
    age, 
    LOWER(TRIM(nom)) AS nom, 
    LOWER(TRIM(prenom)) AS prenom, 
    LOWER(TRIM(email)) AS email, 
    date_de_naissance, 
    permis AS possede_le_permis, 
    metier AS fonction, 
    nombre_enfants, 
    regexp_extract(xp, '^\S+') AS xp
FROM {{ source('kata', 'personnes') }}