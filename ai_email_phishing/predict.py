# predict.py
import joblib
from preprocess import clean_text

# Load model and vectorizer
MODEL_PATH = "email_phishing_model.pkl"
VECTORIZER_PATH = "email_vectorizer.pkl"

model = joblib.load(MODEL_PATH)
vectorizer = joblib.load(VECTORIZER_PATH)

def predict_email(text):
    """Predict whether the email is phishing or not."""
    cleaned_text = clean_text(text)
    text_vectorized = vectorizer.transform([cleaned_text])
    prediction = model.predict(text_vectorized)[0]
    return "Phishing" if prediction == 1 else "Not Phishing"
