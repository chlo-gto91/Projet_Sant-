from flask import Flask, request, jsonify, send_from_directory
import joblib
import numpy as np

# Charger le modèle et le scaler
model = joblib.load("models/ensemble_model_xgb2.joblib")
scaler = joblib.load("models/scaler.pkl")

app = Flask(__name__, static_folder='static')

# Route pour la page principale (blood_analysis.html)
@app.route("/blood_analysis")
def serve_html():
    return send_from_directory(app.static_folder, "blood_analysis.html")

# Route pour la page "About Us"
@app.route("/aboutUs")
def serve_about_us():
    return send_from_directory(app.static_folder, "aboutUs.html")

# Route pour la page d'accueil (home_page.html)
@app.route("/")
def serve_home_page():
    return send_from_directory(app.static_folder, "home_page.html")

# Fonction de prédiction
def predict_risk(features):
    # Mise à l’échelle des données
    scaled_features = scaler.transform([features])
    prediction = model.predict(scaled_features)
    return prediction[0]

# API pour la prédiction
@app.route("/predict", methods=["POST"])
def predictAction():
    data = request.json
    print(data)
    features = data["features"]
    prediction = predict_risk(features)
    risk_message = "Risques faibles de maladies cardiovasculaires" if prediction == 0 else " Risques de maladies cardiovasculaires"
    return jsonify({"prediction": prediction, "message": risk_message})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
