import keras
import pickle
import numpy as np
from PIL import Image
import tensorflow as tf
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.preprocessing.image import load_img

from model.Plant import Plant


class ModelCls:
    train_model = tf.keras.models.load_model('trained_model/Plant_Disease_Detection.model')
    def __init__(self):
        pass

    @classmethod
    def get_trainModel(cls):
        return cls.train_model

    def predict_disease(self,image_path):

        image = load_img(image_path, target_size=(224, 224))

        if image is not None:
            image = img_to_array(image)
            image_data = preprocess_input(image)

        predictions = self.get_trainModel().predict(np.expand_dims(image_data, axis=0))

        class_labels = ['Healthy','Powdery','Rust']

        predicted_class_label = class_labels[np.argmax(predictions)]

        p = Plant(predicted_class_label)

        return p.label, p.recommondation

