import pandas as pd
import re
import os
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer

# Define file paths
DATA_PATH = os.path.abspath("phishing_dataset.csv")
VECTORIZER_PATH = os.path.abspath("email_vectorizer.pkl")

def clean_text(text):
    """Remove special characters, URLs, and lowercase text."""
    if isinstance(text, str):
        text = re.sub(r"http\S+|www\S+|https\S+", '', text, flags=re.MULTILINE)
        text = re.sub(r'\W', ' ', text)
        return text.lower().strip()
    return ""

def preprocess_email_data():
    """Load, clean, and vectorize email phishing dataset."""
    df = pd.read_csv(DATA_PATH)

    # Ensure required columns exist
    if 'message' not in df.columns or 'label' not in df.columns:
        raise KeyError("Dataset must contain 'message' and 'label' columns")

    df['message'] = df['message'].apply(clean_text)
    
    vectorizer = TfidfVectorizer(max_features=5000)
    X = vectorizer.fit_transform(df['message'])

    joblib.dump(vectorizer, VECTORIZER_PATH)
    
    return X, df['label']
