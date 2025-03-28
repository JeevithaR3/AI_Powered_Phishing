import pandas as pd

df = pd.read_csv("backend/processed_dataset.csv")
print(df["Result"].value_counts())
