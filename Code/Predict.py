'''
## Licence:

This repository contains a variety of content; some developed by VARUN, and some from third-parties.
The third-party content is distributed under the license provided by those parties.
The content developed by VARUN is distributed under the following license:
I am providing code and resources in this repository to you under an open source license.
Because this is my personal repository, the license you receive to my code and resources is from me.

More about Licence at [link](https://github.com/t-varun/Face-Recognition/blob/master/LICENSE).
'''

# Import the requirements
import os
import cv2
import time
import numpy as np
import tensorflow as tf

class_names = ['Benign', 'Malignant']

npath = "../Dataset/brain-mri-images-for-brain-tumor-detection/no/"
ypath = "../Dataset/brain-mri-images-for-brain-tumor-detection/yes/"

no = [os.path.join(npath, f) for f in os.listdir(npath)]
yes = [os.path.join(ypath, f) for f in os.listdir(ypath)]

model = tf.keras.models.load_model('../Model/BrainTumorDetection-Tensorflow.model')

for im in no:
    img = cv2.imread(im)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imshow('img',img)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img = cv2.resize(img, (30,30))
    img = np.asarray(img)
    img = img.reshape((-1, 30, 30, 1))
    img = img / 255.0
    prediction = model.predict([img])[0]
    predicted_label = class_names[np.argmax(prediction)]
    print(predicted_label)
    if cv2.waitKey(30) & 0xff == 'q' == 27:
        break
print('================================================')
for im in yes:
    img = cv2.imread(im)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imshow('img',img)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img = cv2.resize(img, (30,30))
    img = np.asarray(img)
    img = img.reshape((-1, 30, 30, 1))
    img = img / 255.0
    prediction = model.predict([img])[0]
    predicted_label = class_names[np.argmax(prediction)]
    print(predicted_label)
    if cv2.waitKey(30) & 0xff == 'q' == 27:
        break
cv2.destroyAllWindows()
