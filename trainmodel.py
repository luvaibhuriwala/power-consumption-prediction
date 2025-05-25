import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
import joblib
from utils.preprocess import preprocess_data

# Load dataset
df = pd.read_csv('data/power_consumption.csv')

# Preprocess
X, y = preprocess_data(df)

# Train models
zones = ['Zone 1', 'Zone 2', 'Zone 3']

for i, zone in enumerate(zones, start=1):
    y_zone = y[zone]
    X_train, X_test, y_train, y_test = train_test_split(X, y_zone, test_size=0.2, random_state=42)

    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    joblib.dump(model, f'model/zone{i}_model.pkl')
    print(f"Trained and saved model for Zone {i}")
