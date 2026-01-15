import pandas as pd

df = pd.read_csv("dataset/titanic.csv")

print("First 5 rows:")
print(df.head())

print("\nLast 5 rows:")
print(df.tail())

print("\nDataset Info:")
print(df.info())

print("\nStatistical Summary:")
print(df.describe())

categorical_cols = df.select_dtypes(include=['object']).columns
for col in categorical_cols:
    print(f"\nUnique values in {col}:")
    print(df[col].unique())

print("\nMissing Values:")
print(df.isnull().sum())
