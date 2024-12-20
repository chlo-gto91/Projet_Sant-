from flask import Flask, request, jsonify, send_from_directory
import joblib
import numpy as np

# Charger le modèle et appeler le scaler
model = joblib.load("models/ensemble_model_xgb2.joblib")
scaler = joblib.load("models/scaler.pkl")

app = Flask(__name__, static_folder='static')

# Route pour servir la page HTML
@app.route("/")
def serve_html():
    return send_from_directory(app.static_folder, "blood_analysis.html")

def predict_risk(features):
    # Mise à l’échelle des données
    scaled_features = scaler.transform([features])
    prediction = model.predict(scaled_features)
    return prediction[0]

@app.route("/predict", methods=["POST"])
def predictAction():
    data = request.json
    print(data)
    features = data["features"]
    prediction = predict_risk(features)
    return jsonify({"prediction": prediction})
        
    

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000,debug=True)
