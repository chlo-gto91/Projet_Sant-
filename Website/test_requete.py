import requests 

payload = {
    "features": [1, 2, 3, 5] #just pour le test, viendra du frontend
}
response = requests.post("http://localhost:5000/predict", json=payload)

print(response.json())