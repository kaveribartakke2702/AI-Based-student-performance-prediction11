import pandas as pd

# Load raw dataset
data = pd.read_csv("../data/student_raw_data.csv")

# Display first 5 rows
print(data.head())

# Check missing values
print("Missing Values:")
print(data.isnull().sum())

# Remove duplicate records
data = data.drop_duplicates()

# Save cleaned dataset
data.to_csv("../data/processed/student_cleaned_data.csv", index=False)

print("Data cleaning completed successfully")
