import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib

data = pd.read_csv(r"D:\usecase\CROP-RECOMMENDATION--based-on-soil-metrics-with-DISEASE-DETECTION\Updated_Crop_Recommendation_with_Disease_Info.csv")

X = data.drop("label", axis=1)
y = data["label"]

model = RandomForestClassifier()

model.fit(X, y)

joblib.dump(model, "models/crop_model.pkl")

print("Crop model trained and saved successfully")