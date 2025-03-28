from flask import Flask, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)
model = joblib.load("domain_model.pkl")

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json
    features = np.array([[data["age"], data["https"], data["num_digits"]]])
    prediction = model.predict(features)[0]
    
    return jsonify({"prediction": int(prediction)})

if __name__ == "__main__":
    app.run(port=5000, debug=True)
