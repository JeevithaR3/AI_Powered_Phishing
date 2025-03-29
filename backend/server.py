from flask import Flask, request, jsonify
import pickle
from url_unshortening import unshorten_url
from domain_reputation import get_domain_reputation
from urllib.parse import urlparse

app = Flask(__name__)

# Load the pre-trained model
model = pickle.load(open('phishing_model.pkl', 'rb'))

def extract_features(url):
    # Unshorten the URL
    full_url = unshorten_url(url)
    
    # Extract domain from the URL
    domain = urlparse(full_url).netloc

    # Get domain reputation
    domain_reputation = get_domain_reputation(domain)
    
    # Return features (in this case, just domain reputation)
    return [1 if domain_reputation == 'good' else 0]

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    url = data['url']
    
    # Extract features and predict
    features = extract_features(url)
    prediction = model.predict([features])[0]
    
    return jsonify({'prediction': 'legitimate' if prediction == 0 else 'phishing', 'url': url})

if __name__ == '__main__':
    app.run(debug=True)