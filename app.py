from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib

app = Flask(__name__)
CORS(app)

# Load models and label encoders
crop_model = joblib.load('crop_model.pkl')
disease_model = joblib.load('disease_model.pkl')
label_encoder_crop = joblib.load('label_encoder_crop.pkl')
label_encoder_disease = joblib.load('label_encoder_disease.pkl')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        required_fields = ['nitrogen', 'phosphorus', 'potassium', 'temperature', 'humidity', 'ph_value']
        
        # Validate input data
        for field in required_fields:
            if field not in data:
                return jsonify({'error': f'Missing required field: {field}'}), 400

        # Extract values
        nitrogen = float(data['nitrogen'])
        phosphorus = float(data['phosphorus'])
        potassium = float(data['potassium'])
        temperature = float(data['temperature'])
        humidity = float(data['humidity'])
        ph_value = float(data['ph_value'])

        # Prepare input for models
        features = [[nitrogen, phosphorus, potassium, temperature, humidity, ph_value]]

        # Make predictions
        crop_prediction_encoded = crop_model.predict(features)[0]
        disease_prediction_encoded = disease_model.predict(features)[0]

        # Decode predictions
        predicted_crop = label_encoder_crop.inverse_transform([crop_prediction_encoded])[0]
        predicted_disease = label_encoder_disease.inverse_transform([disease_prediction_encoded])[0]

        return jsonify({
            'prediction': {
                'crop': predicted_crop,
                'disease': predicted_disease
            }
        })

    except Exception as e:
        return jsonify({'error': f'An error occurred: {str(e)}'}), 500

if __name__ == '__main__':
    app.run(debug=True)
