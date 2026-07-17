import pandas as pd

# Load Dataset
df = pd.read_csv("dataset/HDI.csv")

print("First 5 Rows")
print(df.head())

print("\nDataset Information")
print(df.info())

print("\nMissing Values")
print(df.isnull().sum())

print("\nColumns")
print(df.columns)