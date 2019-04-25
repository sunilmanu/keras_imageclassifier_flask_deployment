from __future__ import division, print_function
import sys
import os
import glob
import re
import numpy as np
import tensorflow as tf

from keras.applications.imagenet_utils import preprocess_input, decode_predictions
from keras.models import load_model
from keras.preprocessing import image

from flask import Flask, redirect, url_for, request, render_template
from werkzeug.utils import secure_filename
from gevent.pywsgi import WSGIServer

# Define a flask app
app = Flask(__name__)

# Model saved with Keras model.save()
MODEL_PATH = 'models/your_model.h5'

# Load your trained model
# model = load_model(MODEL_PATH)
# model._make_predict_function()          # Necessary
# print('Model loaded. Start serving...')

# You can also use pretrained model from Keras
# Check https://keras.io/applications/
from keras.applications.resnet50 import ResNet50
global model
model = ResNet50(weights="imagenet")
global graph
graph = tf.get_default_graph()


def model_predict(img_path, model):
    img = image.load_img(img_path, target_size=(224, 224))

    # Preprocessing the image
    x = image.img_to_array(img)
    # x = np.true_divide(x, 255)
    x = np.expand_dims(x, axis=0)

    # Be careful how your trained model deals with the input
    # otherwise, it won't make correct prediction!
    x = preprocess_input(x, mode='caffe')

    preds = model.predict(x)
    return preds


@app.route('/', methods=['GET'])
def index():
    # Main page
    return render_template('index.html')


@app.route('/predict', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        f = request.files['file']
        basepath = os.path.dirname(__file__)
        file_path = os.path.join(basepath, 'uploads', secure_filename(f.filename))
        f.save(file_path)
        with graph.as_default():
            preds = model_predict(file_path, model)          
            pred_class = decode_predictions(preds, top=1)   
            result = str(pred_class[0][0][1])               
            return result
    return None

@app.route('/satisfy', methods=['GET', 'POST'])	
def satisfy():
    if request.method == 'POST':
        f = request.files['file']
        basepath = os.path.dirname(__file__)
        file_path = os.path.join(basepath, 'satisfied', secure_filename(f.filename))
        f.save(file_path)
    return None	

	
@app.route('/notsatisfy', methods=['GET', 'POST'])	
def notsatisfy():
    if request.method == 'POST':
        f = request.files['file']
        basepath = os.path.dirname(__file__)
        file_path = os.path.join(basepath, 'unsatisfied', secure_filename(f.filename))
        f.save(file_path)
    return None	


if __name__ == '__main__':
	app.run(debug = True, threaded = False)

