# train_email_model.py
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_extraction.text import TfidfVectorizer
import joblib
from preprocess import clean_text

# Load dataset
df = pd.read_csv('phishing_dataset.csv')

# Clean the text data
df['message'] = df['message'].apply(clean_text)

# Vectorization
vectorizer = TfidfVectorizer(max_features=5000)
X = vectorizer.fit_transform(df['message'])
y = df['label']

# Train a model
model = RandomForestClassifier()
model.fit(X, y)

# Save model and vectorizer
joblib.dump(model, 'email_phishing_model.pkl')
joblib.dump(vectorizer, 'email_vectorizer.pkl')
