from flask import Flask, request, jsonify
import joblib
from utils.weather import get_weather
from flask_cors import CORS
import pandas as pd

app = Flask(__name__)

# Load models
zone1_model = joblib.load('model/zone1_model.pkl')
zone2_model = joblib.load('model/zone2_model.pkl')
zone3_model = joblib.load('model/zone3_model.pkl')

# Initialize CORS
CORS(app, resources={r"/*": {"origins": "*"}})

@app.route('/')
def index():
    return jsonify({'message': 'Welcome to the power consumption prediction API!'})

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()

        required_fields = [
            'Temperature', 'Humidity', 'Wind Speed',
            'general diffuse flows', 'diffuse flows',
            'hour', 'day', 'month'
        ]

        missing = [field for field in required_fields if field not in data]
        if missing:
            return jsonify({'error': f'Missing fields: {missing}'}), 400

        input_df = pd.DataFrame([{
            'Temperature': data['Temperature'],
            'Humidity': data['Humidity'],
            'Wind Speed': data['Wind Speed'],
            'general diffuse flows': data['general diffuse flows'],
            'diffuse flows': data['diffuse flows'],
            'hour': data['hour'],
            'day': data['day'],
            'month': data['month']
        }])

        z1 = zone1_model.predict(input_df)[0]
        z2 = zone2_model.predict(input_df)[0]
        z3 = zone3_model.predict(input_df)[0]

        return jsonify({
            'Zone 1 Power Consumption': round(z1, 2),
            'Zone 2 Power Consumption': round(z2, 2),
            'Zone 3 Power Consumption': round(z3, 2)
        })

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
