import cv2
import imutils
import time
import os

npath = "../Dataset/brain-mri-images-for-brain-tumor-detection/no/"
ypath = "../Dataset/brain-mri-images-for-brain-tumor-detection/yes/"

no = [os.path.join(npath, f) for f in os.listdir(npath)]
yes = [os.path.join(ypath, f) for f in os.listdir(ypath)]

for i in range(256):
    try:
        image1 = cv2.imread(no[i])
        image2 = cv2.imread(yes[i])
        #cv2.imshow("Image1",image1)
        #cv2.imshow("Image2",image2)

        copy1 = image1.copy()
        edge1 = cv2.Canny(copy1,150,150)
        cv2.imshow("Edge1",edge1)

        copy2 = image2.copy()#(copy2,80,80)
        edge3 = cv2.Canny(copy2,150,150)
        cv2.imshow("Edge3",edge3)
        time.sleep(1)
        cv2.waitKey(1)
    except:
        pass

