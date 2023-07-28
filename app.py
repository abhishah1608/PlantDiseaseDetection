import os
from flask import Flask, request, jsonify, render_template
from werkzeug.utils import secure_filename

from model_logic.loadModel import ModelCls

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')


UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/upload', methods=['POST'])
def upload_image():
    if 'image' not in request.files:
        return jsonify({"message": "No file part in the request"}), 400

    file = request.files['image']


    if file.filename == '':
        return jsonify({"message": "No selected file"}), 400

    if file:
        # Save the file to the specified folder
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        # Now  here load model for the first time or else predict based on the trained model.
        model = ModelCls()
        disease, recommendation = model.predict_disease(filepath)
        return jsonify({"disease": disease, "recommendation" : recommendation}), 200



if __name__ == '__main__':
    app.run()
