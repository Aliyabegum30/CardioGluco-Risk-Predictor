from flask import Flask, request, jsonify
import joblib
import numpy as np
import os

from utils.preprocess import prepare_input
from utils.recommendations import (
    heart_risk_factors,
    diabetes_risk_factors,
    generate_recommendations
)

app = Flask(__name__)

# -------------------------------
# CORS
# -------------------------------
@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
    response.headers.add('Access-Control-Allow-Methods', 'GET,POST')
    return response


# -------------------------------
# LOAD MODELS
# -------------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "model")

heart_model = joblib.load(os.path.join(MODEL_PATH, "heart_model.pkl"))
heart_scaler = joblib.load(os.path.join(MODEL_PATH, "heart_scaler.pkl"))
heart_features = joblib.load(os.path.join(MODEL_PATH, "heart_features.pkl"))

diabetes_model = joblib.load(os.path.join(MODEL_PATH, "diabetes_model.pkl"))
diabetes_scaler = joblib.load(os.path.join(MODEL_PATH, "diabetes_scaler.pkl"))
diabetes_features = joblib.load(os.path.join(MODEL_PATH, "diabetes_features.pkl"))


# -------------------------------
# HELPERS
# -------------------------------
def get_risk_label(prob):
    if prob >= 0.7:
        return "High"
    elif prob >= 0.4:
        return "Moderate"
    return "Low"


def validate_input(data, required_fields):
    missing = [f for f in required_fields if f not in data]
    if missing:
        return False, f"Missing fields: {missing}"
    return True, ""


# -------------------------------
# ROUTES
# -------------------------------
@app.route("/")
def home():
    return jsonify({"message": "CardioGluco Risk Predictor API Running"})


# -------------------------------
# HEART
# -------------------------------
@app.route("/predict/heart", methods=["POST"])
def predict_heart():
    try:
        data = request.get_json()

        valid, msg = validate_input(data, heart_features)
        if not valid:
            return jsonify({"error": msg}), 400

        features = prepare_input(data, heart_features)
        features_scaled = heart_scaler.transform(features)

        prob = heart_model.predict_proba(features_scaled)[0][1]
        risk = get_risk_label(prob)

        factors = heart_risk_factors(data)
        recs = generate_recommendations(factors)

        return jsonify({
            "risk": risk,
            "probability": round(float(prob), 3),
            "factors": factors,
            "recommendations": recs
        })

    except Exception as e:
        print("Heart Error:", e)
        return jsonify({"error": str(e)}), 500


# -------------------------------
# DIABETES
# -------------------------------
@app.route("/predict/diabetes", methods=["POST"])
def predict_diabetes():
    try:
        data = request.get_json()

        valid, msg = validate_input(data, diabetes_features)
        if not valid:
            return jsonify({"error": msg}), 400

        if "BMI" not in data:
            height = float(data.get("height", 1))
            weight = float(data.get("weight", 1))
            data["BMI"] = weight / (height ** 2) if height > 0 else 0

        features = prepare_input(data, diabetes_features)
        features_scaled = diabetes_scaler.transform(features)

        prob = diabetes_model.predict_proba(features_scaled)[0][1]
        risk = get_risk_label(prob)

        factors = diabetes_risk_factors(data)
        recs = generate_recommendations(factors)

        return jsonify({
            "risk": risk,
            "probability": round(float(prob), 3),
            "factors": factors,
            "recommendations": recs
        })

    except Exception as e:
        print("Diabetes Error:", e)
        return jsonify({"error": str(e)}), 500


# -------------------------------
# RUN
# -------------------------------
if __name__ == "__main__":
    app.run(debug=True)