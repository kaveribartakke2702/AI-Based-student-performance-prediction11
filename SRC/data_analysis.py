import pandas as pd

# Load dataset
df = pd.read_csv("../data/student_raw_data.csv")

# Dataset information
print("Dataset Shape:")
print(df.shape)

print("\nColumns:")
print(df.columns)

print("\nDataset Summary:")
print(df.describe())

print("\nMissing Values:")
print(df.isnull().sum())
