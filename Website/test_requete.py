import requests

# Exemple de payload correspondant aux caractéristiques attendues par le modèle
payload = {
    "features": [
        1,        # Sexe: Homme (1 pour homme, 0 pour femme)
        4,        # Age: Catégorie (ex: 35-39 ans)
        22.5,     # BMI (Indice de Masse Corporelle)
        1,        # Tension: Oui (1 pour oui, 0 pour non)
        0,        # Cholestérol: Non (1 pour oui, 0 pour non)
        1,        # AVC: Oui (1 pour oui, 0 pour non)
        0,        # Difficultés à marcher: Non (1 pour oui, 0 pour non)
        5,         # Éducation (années après le bac)
        2         # Income
    ]
}

# URL de l'endpoint Flask
url = "http://localhost:5000/predict"

# Envoyer les données via une requête POST
response = requests.post(url, json=payload)

# Afficher la réponse du serveur
print("Statut de la réponse:", response.status_code)
print("Contenu de la réponse:", response.json())

