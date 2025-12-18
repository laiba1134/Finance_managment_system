# backend/app.py
from flask import Flask, request, jsonify
import joblib
from scipy.sparse import hstack
import pandas as pd

from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})



@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.json
    text = data.get("text", "")

    if not text:
        return jsonify({"error": "No text provided"}), 400

    # Transform the text using the TF-IDF vectorizer
    X_text = tfidf.transform([text])
    # If you have any metadata columns, you can handle them here (or pass dummy)
    import numpy as np
    X_meta = np.array([[0, 1, 0]])  # example placeholder if your model needs 3 meta features

    from scipy.sparse import hstack
    X_final = hstack([X_text, X_meta])

    # Predict
    prediction = model.predict(X_final)[0]
    probability = model.predict_proba(X_final)[0][1]  # probability of class 1 (fraudulent)

    return jsonify({
        "prediction": int(prediction),  # 1 = fraudulent, 0 = legitimate
        "confidence": float(probability)
    })


# Load model and TF-IDF vectorizer
model = joblib.load("models/job_fraud_model.pkl")  # adjust path if needed
tfidf = joblib.load("models/tfidf_vectorizer.pkl")


@app.route("/api/analyze", methods=["POST"])
def analyze_job():
    data = request.json
    text = data.get("text", "")
    meta = data.get("meta", {"telecommuting": 0, "has_company_logo": 0, "has_questions": 0})

    if not text:
        return jsonify({"error": "No text provided"}), 400

    # Vectorize text
    text_vector = tfidf.transform([text])

    # Convert meta features to DataFrame
    meta_df = pd.DataFrame([meta])

    # Combine text + meta
    X_input = hstack([text_vector, meta_df])

    # Predict
    prediction = model.predict(X_input)[0]
    confidence = model.predict_proba(X_input).max()

    return jsonify({
        "prediction": "Real" if prediction == 0 else "Fake",  # adjust based on your labeling
        "confidence": float(confidence)
    })

if __name__ == "__main__":
    app.run(debug=True)

