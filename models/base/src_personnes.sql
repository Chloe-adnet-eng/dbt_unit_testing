SELECT 
    *
FROM {{ source('kata', 'personnes') }}