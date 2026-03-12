import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import joblib
import os

# Load dataset
data = pd.read_csv("Updated_Crop_Recommendation_with_Disease_Info.csv")

# Features
X = data[
    [
        "Nitrogen",
        "Phosphorus",
        "Potassium",
        "Temperature",
        "Humidity",
        "pH_Value",
    ]
]

# Target
y = data["Recommended_Crop"]

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Evaluate model
predictions = model.predict(X_test)
accuracy = accuracy_score(y_test, predictions)

print("Model Accuracy:", accuracy)

# Save model
os.makedirs("models", exist_ok=True)
joblib.dump(model, "models/crop_model.pkl")

# Save metrics
os.makedirs("reports", exist_ok=True)

with open("reports/metrics.txt", "w") as f:
    f.write(f"Accuracy: {accuracy}")

print("Training completed successfully")