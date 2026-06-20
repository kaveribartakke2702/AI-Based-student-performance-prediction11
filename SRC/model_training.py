import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score


# Load cleaned dataset
df = pd.read_csv("../data/processed/student_cleaned_data.csv")


# Convert grade into numerical values
encoder = LabelEncoder()

df["grade"] = encoder.fit_transform(df["grade"])


# Input features
X = df[
    [
        "weekly_self_study_hours",
        "attendance_percentage",
        "class_participation",
        "total_score"
    ]
]


# Target variable
y = df["grade"]


# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)


# Train AI model
model = RandomForestClassifier()

model.fit(
    X_train,
    y_train
)


# Prediction
prediction = model.predict(X_test)


# Accuracy
accuracy = accuracy_score(
    y_test,
    prediction
)


print("Model Accuracy:", accuracy)
