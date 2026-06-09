from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import os

app = Flask(__name__)
CORS(app)

# Load model safely
MODEL_PATH = "model.pkl"
VECTORIZER_PATH = "vectorizer.pkl"

if not os.path.exists(MODEL_PATH) or not os.path.exists(VECTORIZER_PATH):
    raise Exception("Model or Vectorizer file missing!")

model = joblib.load(MODEL_PATH)
vectorizer = joblib.load(VECTORIZER_PATH)

@app.route("/")
def home():
    return "Backend Running Successfully"

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json()
        text = data.get("message", "")

        if not text:
            return jsonify({"error": "No message provided"}), 400

        transformed_text = vectorizer.transform([text])
        prediction = model.predict(transformed_text)[0]

        return jsonify({
            "prediction": prediction
        })

    except Exception as e:
        return jsonify({
            "error": str(e)
        }), 500


# IMPORTANT: production-safe run
if __name__ == "__main__":
    import os

    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)