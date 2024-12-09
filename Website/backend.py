from flask import Flask, request, jsonify
import joblib
import numpy as np
from sklearn.preprocessing import StandardScaler

# Charger le modèle et initialiser le scaler
model = joblib.load("model.joblib")
scaler = joblib.load(scaler.pkl)

# Assurez-vous de définir les caractéristiques attendues par le scaler
# Exemple de valeurs pour ajuster le scaler (cela devrait correspondre aux données d'entraînement du modèle)
dummy_data = np.array([[1, 1, 1, 1, 1, 1, 1, 1]])
scaler.fit(dummy_data)

app = Flask(__name__)

def predict_risk(features):
    # Mise à l’échelle des données
    scaled_features = scaler.transform([features])
    # Prédiction avec le modèle
    prediction = model.predict(scaled_features)
    return prediction[0]

@app.route("/predict", methods=["POST"])
def predictAction():
    try:
        features = request.json['features']
        prediction = predict_risk(features)
        return jsonify({"prediction": prediction})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
