import requests
import json

# Define variables for the data to send
city = "New York"
temperature = 25.0
humidity = 60.0
wind_speed = 10.0
general_diffuse_flows = 150.0
diffuse_flows = 50.0
hour = 12
day = 15
month = 7

# API endpoint URL
api_url = "https://5000-firebase-power-backend-1748073811913.cluster-zkm2jrwbnbd4awuedc2alqxrpk.cloudworkstations.dev/predict"

# Prepare the data payload
payload = {
    "Temperature": temperature,
    "Humidity": humidity,
    "Wind Speed": wind_speed,
    "general diffuse flows": general_diffuse_flows,
    "diffuse flows": diffuse_flows,
    "hour": hour,
    "day": day,
    "month": month
}

# Send the POST request
try:
    response = requests.post(api_url, json=payload)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        print("Request successful!")
        print("Response:", response.json())  # Print the JSON response
    else:
        print(f"Request failed with status code: {response.status_code}")
        print("Response:", response.text) # Print the error response

except requests.exceptions.RequestException as e:
    print(f"An error occurred during the request: {e}")