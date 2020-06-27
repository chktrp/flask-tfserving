from flask import Flask, request
import base64
import requests
from tensorflow.keras.preprocessing import image
from io import BytesIO
import numpy as np

# We use 'tfs' instead of 'localhost' because of Docker
SERVER_URL = 'http://tfs:8501/v1/models/room:predict'

classes = ['clean', 'messy']

app = Flask(__name__)

@app.route('/')
def home():
    return "It's running!"

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        file = request.files["image"]

        img = image.img_to_array(image.load_img(BytesIO(file.read()),
                                          target_size=(224, 224))) / 255.

        payload = {
            "instances": [{'input_3': img.tolist()}]
        }
        
        response = requests.post(SERVER_URL,  json=payload)
        prediction = response.json()['predictions'][0]
        index = prediction.index(max(prediction))

        return classes[index]
    return 'none'
    
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)