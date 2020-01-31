import numpy as np
import cv2
import time
import win32api as wapi
import os
import sys
from PIL import Image
from random import shuffle
import pandas as pd

file_name = '../Data/training_data.npy'

if os.path.isfile(file_name):
    print("File exists, loading previous data")
    training_data = list(np.load(file_name))
else:
    print("File does not exist, starting fresh")
    training_data = []

for i in list(range(3))[::-1]:
    print(i+1)
    time.sleep(1)
    
last_time = time.time()

npath = "../Dataset/brain-mri-images-for-brain-tumor-detection/no/"
ypath = "../Dataset/brain-mri-images-for-brain-tumor-detection/yes/"

no = [os.path.join(npath, f) for f in os.listdir(npath)]
yes = [os.path.join(ypath, f) for f in os.listdir(ypath)]

for file in no:
    try:
        img = cv2.imread(file)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        cv2.imshow('img',img)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        img = cv2.resize(img, (30,30))
        #img = cv2.imread('Images/'+file)
        output = 0
        training_data.append([img, output])
        print('Frame took {} seconds'.format(time.time()-last_time))
        last_time = time.time()
        if cv2.waitKey(30) & 0xff == 'q' == 27:
            break
    except:
        np.save(file_name, training_data)

for file in yes:
    try:
        img = cv2.imread(file)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        cv2.imshow('img',img)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        img = cv2.resize(img, (30,30))
        #img = cv2.imread('Images/'+file)
        output = 1
        training_data.append([img, output])
        print('Frame took {} seconds'.format(time.time()-last_time))
        last_time = time.time()
        if cv2.waitKey(30) & 0xff == 'q' == 27:
            break
    except:
        np.save(file_name, training_data)

np.save(file_name, training_data)
cv2.destroyAllWindows()

train_data = np.load('../Data/training_data.npy')

TOTAL = []

for img, ind in train_data:
    TOTAL.append([img, ind])
    if cv2.waitKey(30) & 0xff == 'q' == 27:
        break
cv2.destroyAllWindows()
shuffle(TOTAL)
np.save('../Data/training_data_cleaned.npy', TOTAL)
