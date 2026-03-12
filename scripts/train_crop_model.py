import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib
import os

data = pd.read_csv(r"D:\usecase\CROP-RECOMMENDATION--based-on-soil-metrics-with-DISEASE-DETECTION\Updated_Crop_Recommendation_with_Disease_Info.csv")

print("Dataset columns:", data.columns)

# Features
X = data[[
    "Nitrogen",
    "Phosphorus",
    "Potassium",
    "Temperature",
    "Humidity",
    "pH_Value"
]]

# Target
y = data["Recommended_Crop"]

# Train model
model = RandomForestClassifier()
model.fit(X, y)

# Ensure models folder exists
os.makedirs("models", exist_ok=True)

# Save model
joblib.dump(model, "models/crop_model.pkl")

print("Crop model trained successfully")