import requests

# Payload contenant les données du formulaire (exemple fictif)
payload = {
    "features": [
        1,  # Sexe: Homme
        4,  # Age: Catégorie (ex: 35-39 ans)
        22.5,  # BMI
        1,  # Tension: Oui
        0,  # Cholestérol: Non
        1,  # AVC: Oui
        0,  # Difficultés à marcher: Non
        15  # Éducation (années après le bac)
    ]
}

# Envoyer les données au backend
response = requests.post("http://localhost:5000/predict", json=payload)

# Afficher la réponse
print(response.json())
