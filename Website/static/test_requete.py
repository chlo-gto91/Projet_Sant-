from selenium import webdriver
from selenium.webdriver.common.by import By
import requests

# Initialiser le navigateur
browser = webdriver.Firefox()

# Charger la page HTML locale
browser.get("C:/xampp/htdocs/Projet_Sant-/Website")

# Récupérer les données encodées affichées dans le div "encodedDataDisplay"
encoded_data_div = browser.find_element(By.ID, "encodedDataDisplay")
encoded_data_paragraphs = encoded_data_div.find_elements(By.TAG_NAME, "p")

# Extraire les données encodées dans un dictionnaire
encoded_data = {}
for paragraph in encoded_data_paragraphs:
    key_value = paragraph.text.split(":")
    if len(key_value) == 2:
        key, value = key_value[0].strip(), key_value[1].strip()
        encoded_data[key] = value

# Construire le payload pour la requête POST
payload = {
    "features": [
        int(encoded_data.get("sexe", 0)),
        int(encoded_data.get("age", 0)),
        float(encoded_data.get("bmi", 0.0)),
        int(encoded_data.get("tension", 0)),
        int(encoded_data.get("cholesterol", 0)),
        int(encoded_data.get("avc", 0)),
        int(encoded_data.get("diffWalk", 0)),
        int(encoded_data.get("education", 0))
    ]
}

# Fermer le navigateur
browser.quit()

# Envoyer les données au backend
response = requests.post("http://localhost:5000/predict", json=payload)

# Afficher la réponse
print(response.json())
