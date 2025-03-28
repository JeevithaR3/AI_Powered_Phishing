import os
import joblib
from preprocess import clean_text

# Define file paths
MODEL_PATH = os.path.abspath("email_phishing_model.pkl")
VECTORIZER_PATH = os.path.abspath("email_vectorizer.pkl")

# Load model and vectorizer
model = joblib.load(MODEL_PATH)
vectorizer = joblib.load(VECTORIZER_PATH)

def predict_email(text):
    """Predict whether an email is phishing or not."""
    cleaned_text = clean_text(text)
    text_vectorized = vectorizer.transform([cleaned_text])
    prediction = model.predict(text_vectorized)[0]
    return "Phishing" if prediction == 1 else "Not Phishing"

if __name__ == "__main__":
    email_text = input("Enter email text: ")
    result = predict_email(email_text)
    print("Prediction:", result)
