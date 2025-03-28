import os
import joblib
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report
from preprocess import preprocess_email_data

# Define file paths
MODEL_PATH = os.path.abspath("email_phishing_model.pkl")

# Preprocess data
X, y = preprocess_email_data()

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = MultinomialNB()
model.fit(X_train, y_train)

# Evaluate model
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

print(f"Model Accuracy: {accuracy:.4f}")
print("Classification Report:\n", classification_report(y_test, y_pred))

# Save trained model
joblib.dump(model, MODEL_PATH)
print(f"Model saved at: {MODEL_PATH}")
