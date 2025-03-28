import os
from train_email_model import *
from predict import predict_email

if __name__ == "__main__":
    print("AI-Powered Phishing Detection System")

    while True:
        print("\nOptions:")
        print("1. Train Model")
        print("2. Predict Email")
        print("3. Exit")
        
        choice = input("Enter your choice: ")

        if choice == "1":
            os.system("python train_email_model.py")
        elif choice == "2":
            email_text = input("Enter email text: ")
            result = predict_email(email_text)
            print("Prediction:", result)
        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")
