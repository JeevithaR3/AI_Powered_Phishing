# app.py

from flask import Flask, request, jsonify
from predict import predict_email

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        email_text = request.json.get('email_text')
        if not email_text:
            return jsonify({'error': 'No email text provided'}), 400

        result = predict_email(email_text)
        return jsonify({'prediction': result})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
