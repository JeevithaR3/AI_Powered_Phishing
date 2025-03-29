#!/usr/bin/python

import time
import numpy as np
import pandas as pd
import joblib  # For saving/loading models
from sklearn.model_selection import train_test_split  # Fix for cross_validation issue
from sklearn.metrics import accuracy_score, confusion_matrix, f1_score
from sklearn.neural_network import MLPClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC

def calculate_metrics(y_test, Y_predicted):
    """Calculate and print evaluation metrics."""
    accuracy = accuracy_score(y_test, Y_predicted)
    print("accuracy = {:.2f}%".format(accuracy * 100))

    confusion_mat = confusion_matrix(y_test, Y_predicted)
    print("Confusion Matrix:\n", confusion_mat)

    print("TP\tFP\tFN\tTN\tSensitivity\tSpecificity")
    for i in range(confusion_mat.shape[0]):
        TP = round(float(confusion_mat[i, i]), 2)  # Correctly labeled as i
        FP = round(float(confusion_mat[:, i].sum()), 2) - TP  # Incorrectly labeled as i
        FN = round(float(confusion_mat[i, :].sum()), 2) - TP  # Incorrectly labeled as non-i
        TN = round(float(confusion_mat.sum().sum()), 2) - TP - FP - FN
        sensitivity = round(TP / (TP + FN), 2) if (TP + FN) != 0 else 0
        specificity = round(TN / (TN + FP), 2) if (TN + FP) != 0 else 0
        print(f"{TP}\t{FP}\t{FN}\t{TN}\t{sensitivity}\t\t{specificity}")

    f_score = f1_score(y_test, Y_predicted, average="weighted")
    print("F1 Score:", f_score)

def neural_network(dataset, class_labels, test_size):
    """Train and evaluate a Neural Network model."""
    X = pd.read_csv(dataset)
    Y = pd.read_csv(class_labels).squeeze()  # Ensure Y is a Series

    X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=test_size, random_state=42)

    model = MLPClassifier(hidden_layer_sizes=(100), activation='logistic', random_state=42)
    model.fit(X_train, y_train)
    Y_predicted = model.predict(X_test)

    return y_test, Y_predicted

def random_forests(dataset, class_labels, test_size):
    """Train and evaluate a Random Forest model."""
    X = pd.read_csv(dataset)
    Y = pd.read_csv(class_labels).squeeze()

    X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=test_size, random_state=42)

    model = RandomForestClassifier(n_estimators=5, criterion='entropy', random_state=42)
    model.fit(X_train, y_train)
    Y_predicted = model.predict(X_test)

    return y_test, Y_predicted

def support_vector_machines(dataset, class_labels, test_size):
    """Train and evaluate an SVM model, and save it as 'svm_model.pkl'."""
    X = pd.read_csv(dataset)
    Y = pd.read_csv(class_labels).squeeze()

    X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=test_size, random_state=42)

    model = SVC(kernel='rbf', C=2.0)
    model.fit(X_train, y_train)
    Y_predicted = model.predict(X_test)

    # ✅ Save the trained model
    joblib.dump(model, "svm_model.pkl")
    print("✅ SVM Model saved as svm_model.pkl")

    return y_test, Y_predicted

def main():
    """Main function to run all models and measure runtime."""
    dataset = "Dataset.csv"
    class_labels = "Target_Labels.csv"
    test_size = 0.3

    print("\n🔹 Running Neural Network...")
    start_time = time.time()
    y_test, Y_predicted = neural_network(dataset, class_labels, test_size)
    calculate_metrics(y_test, Y_predicted)
    print("Runtime:", round(time.time() - start_time, 2), "seconds")

    print("\n🔹 Running Random Forest...")
    start_time = time.time()
    y_test, Y_predicted = random_forests(dataset, class_labels, test_size)
    calculate_metrics(y_test, Y_predicted)
    print("Runtime:", round(time.time() - start_time, 2), "seconds")

    print("\n🔹 Running Support Vector Machine...")
    start_time = time.time()
    y_test, Y_predicted = support_vector_machines(dataset, class_labels, test_size)
    calculate_metrics(y_test, Y_predicted)
    print("Runtime:", round(time.time() - start_time, 2), "seconds")

if __name__ == "__main__":
    start_time = time.time()
    main()
    print("\nTotal Runtime:", round(time.time() - start_time, 2), "seconds")