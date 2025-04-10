import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
import joblib

df = pd.read_csv('Updated_Crop_Recommendation_with_Disease_Info.csv')

if df.isnull().sum().any():
    print("Dataset contains missing values. Filling with default values.")
    df = df.fillna("Unknown Disease")

X = df[['Nitrogen', 'Phosphorus', 'Potassium', 'Temperature', 'Humidity', 'pH_Value']]
y_crop = df['Recommended_Crop']
y_disease = df['Disease']

label_encoder_crop = LabelEncoder()
y_crop_encoded = label_encoder_crop.fit_transform(y_crop)

label_encoder_disease = LabelEncoder()
y_disease_encoded = label_encoder_disease.fit_transform(y_disease)

crop_model = RandomForestClassifier(random_state=42)
crop_model.fit(X, y_crop_encoded)

disease_model = RandomForestClassifier(random_state=42)
disease_model.fit(X, y_disease_encoded)

joblib.dump(crop_model, 'crop_model.pkl')
joblib.dump(disease_model, 'disease_model.pkl')
joblib.dump(label_encoder_crop, 'label_encoder_crop.pkl')
joblib.dump(label_encoder_disease, 'label_encoder_disease.pkl')

print("Models and LabelEncoders saved successfully.")
df['Recommended_Crop'] = df['Recommended_Crop'].str.split(',').str[0].str.strip()
