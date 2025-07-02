import requests

# Path to the test image
file_path = "output_dataset/test/apple_pie/64846.jpg"

# Make a request to the predict endpoint
with open(file_path, 'rb') as file:
    response = requests.post("http://127.0.0.1:5000/predict", files={'file': file})

# Check the response
if response.status_code == 200:
    prediction = response.json()
    print("Prediction:", prediction)
else:
    print("Error:", response.status_code, response.text)
