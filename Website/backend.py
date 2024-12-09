from flask import Flask, request, jsonify
app = Flask(__name__)

def predict_risk(features):
    #utilisation du modèle de steve à faire
    return "pas de risque"


@app.route("/predict", methods=["POST"])
def predictAction():    

    features = request.json['features']
    
    prediction = predict_risk(features)
    return jsonify({
        "prediction": prediction
    })
    
    
app.run(host="0.0.0.0")