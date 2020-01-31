###
# Copyright (2019). All Rights belongs to VARUN
# Use the code by mentioning the Sredits
# Credit: github.com/varuntotakura
# Developer:
#
#               T VARUN
#
###

# Import the required libraries
import numpy
import numpy as np
import tensorflow as tf
from tensorflow import keras
import matplotlib.pyplot as plt
import time

# Import th data
data_name = '../Data/training_data_cleaned.npy'
data = np.load(data_name)

# Declare the required arrays
img = []
label = []
test_imgs = []
test_labs = []

# Class names 
class_names = ['Benign', 'Malignant']

# Input to the arrays
for item, index in data:
    img.append(item)
    label.append(index)

# Train and Test data
train_images = img
train_labels = label

test_images = img[-100:]
test_labels = label[-100:]

train_images = np.asarray(train_images)
test_images = np.asarray(test_images)

train_images = train_images.reshape((-1, 30, 30, 1))
test_images = test_images.reshape((-1, 30, 30, 1))

# Image Processing
train_images = train_images / 255.0

test_images = test_images / 255.0


# Sequential Model
# Convolutional Neural Network
model = keras.Sequential([
    keras.layers.Conv2D(32, (2, 2), activation='relu', input_shape=(30, 30, 1)),
    keras.layers.MaxPooling2D((2, 2)),
    keras.layers.Conv2D(64, (3, 3), activation='relu'),
    keras.layers.MaxPooling2D((2, 2)),
    keras.layers.Conv2D(64, (3, 3), activation='relu'),
    keras.layers.Dropout(0.25),
    keras.layers.Flatten(),
    keras.layers.Dense(512, activation=tf.nn.relu),
    keras.layers.Dense(128, activation=tf.nn.relu),
    keras.layers.Dense(128, activation=tf.nn.relu),
    keras.layers.Dense(len(class_names), activation=tf.nn.softmax)
])

# Compile the model
model.compile(optimizer=tf.train.AdamOptimizer(), 
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# Train the Model
history = model.fit(train_images, train_labels, epochs = 15)

# Save Model
model.save('../Model/BrainTumorDetection-Tensorflow.model')

# Print the Summary
model.summary()

# Accuracy of the Model
test_loss, test_acc = model.evaluate(test_images, test_labels)

# Print Test accuracy
print('Test accuracy:', test_acc*100)

# Make Predictions
predictions = model.predict([test_images])[0] 
predicted_label = class_names[np.argmax(predictions)]               

# Compare the predictions
print("Predictions : ",predicted_label)
print("Actual : ", class_names[test_labels[0]])

##print(history.history.keys())
# summarize history for accuracy
plt.plot(history.history['acc'])
plt.plot(history.history['loss'])
plt.title('Model')
plt.ylabel('Result')
plt.xlabel('Epochs')
plt.legend(['Accuracy', 'Loss'], loc='upper left')
plt.show()
