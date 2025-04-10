import joblib
import numpy as np

# Load pre-trained models and label encoder
crop_model = joblib.load('model_crop.pkl')
disease_model = joblib.load('model_disease.pkl')
label_encoder_disease = joblib.load('label_encoder_disease.pkl')

def predict_crop(nitrogen, phosphorus, potassium, temperature, humidity, ph_value):
    X = np.array([[nitrogen, phosphorus, potassium, temperature, humidity, ph_value]])
    crop_prediction = crop_model.predict(X)
    return crop_prediction[0]

def predict_disease(nitrogen, phosphorus, potassium, temperature, humidity, ph_value):
    X = np.array([[nitrogen, phosphorus, potassium, temperature, humidity, ph_value]])
    disease_prediction = disease_model.predict(X)
    
    try:
        disease = label_encoder_disease.inverse_transform(disease_prediction)
        return disease[0]
    except ValueError as e:
        print(f"Error encountered: {e}")
        return 'Unknown Disease'

# Example prediction
nitrogen = 70
phosphorus = 60
potassium = 80
temperature = 25
humidity = 70
ph_value = 6.5

predicted_crop = predict_crop(nitrogen, phosphorus, potassium, temperature, humidity, ph_value)
predicted_disease = predict_disease(nitrogen, phosphorus, potassium, temperature, humidity, ph_value)

print(f"Predicted Crop: {predicted_crop}")
print(f"Predicted Disease: {predicted_disease}")
