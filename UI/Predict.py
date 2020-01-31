import os
import cv2
import time
import numpy as np
import tensorflow as tf

def predict():
    class_names = ['Benign', 'Malignant']
    path = "C:/Users/VARUN/Desktop/BrainTumor/Images/Uploads/Test.png"
    model = tf.keras.models.load_model('C:/Users/VARUN/Desktop/BrainTumor/Model/BrainTumorDetection-Tensorflow.model')
    img = cv2.imread(path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img = cv2.resize(img, (30,30))
    img = np.asarray(img)
    img = img.reshape((-1, 30, 30, 1))
    img = img / 255.0
    prediction = model.predict([img])[0]
    predicted_label = class_names[np.argmax(prediction)]
    cv2.waitKey(0)
    file = "C:/Users/VARUN/Desktop/BrainTumor/Images/Uploads/Class.txt"
    return predicted_label
