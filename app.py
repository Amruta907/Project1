from flask import Flask, render_template, request, jsonify
from tensorflow.keras.models import load_model # type: ignore
from PIL import Image, ImageOps
import numpy as np
import re
import base64
import io

app = Flask(__name__)
model = load_model("model/digit_model.h5")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    img_data = re.sub('^data:image/.+;base64,', '', data['image'])
    img = Image.open(io.BytesIO(base64.b64decode(img_data)))
    
    # Image processing (resize to 28x28)
    img = img.convert('L')  # grayscale
    img = ImageOps.invert(img)  # background white, number black
    img = img.resize((28, 28))
    img_array = np.array(img) / 255.0
    img_array = img_array.reshape(1, 28, 28, 1)

    prediction = model.predict(img_array)
    predicted_digit = int(np.argmax(prediction))
    return jsonify({'prediction': predicted_digit})

if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, request, jsonify
from tensorflow.keras.models import load_model # type: ignore
from PIL import Image, ImageOps
import numpy as np
import re
import base64
import io

app = Flask(__name__)
model = load_model("model/digit_model.h5")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    img_data = re.sub('^data:image/.+;base64,', '', data['image'])
    img = Image.open(io.BytesIO(base64.b64decode(img_data)))
    
    # Image processing (resize to 28x28)
    img = img.convert('L')  # grayscale
    img = ImageOps.invert(img)  # background white, number black
    img = img.resize((28, 28))
    img_array = np.array(img) / 255.0
    img_array = img_array.reshape(1, 28, 28, 1)

    prediction = model.predict(img_array)
    predicted_digit = int(np.argmax(prediction))
    return jsonify({'prediction': predicted_digit})

if __name__ == '__main__':
    app.run(debug=True)
