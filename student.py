import pandas as pd

df = pd.read_csv("dataset/Student_performance.csv")

df.head()
df.tail()
df.info()
df.describe()

categorical_cols = df.select_dtypes(include=['object']).columns
for col in categorical_cols:
    print(f"\nUnique values in {col}:")
    print(df[col].unique())

print("\nMissing Values:")
print(df.isnull().sum())
