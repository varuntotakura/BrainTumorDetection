import cv2
import imutils
import time

for i in range(256):
    try:
        image = cv2.imread("C:\\Users\\VARUN\\Desktop\\BrainTumor\\Dataset\\brain-mri-images-for-brain-tumor-detection\\yes\\Y"+str(i)+".jpg")
        ##cv2.imshow("Image", image)
        copy = image.copy()
        grey = cv2.cvtColor(copy,cv2.COLOR_BGR2GRAY)
        ##cv2.imshow("Grey",grey)
        blur = cv2.GaussianBlur(copy,(11,11),0)
        ##cv2.imshow("Blur",blur)
        edge = cv2.Canny(grey,30,150)
        ##cv2.imshow("Edge",edge)
        thresh = cv2.threshold(grey, 225, 255, cv2.THRESH_BINARY_INV)[1]
        ##cv2.imshow("Thresh", thresh)
        mask = cv2.erode(thresh, None, iterations=10)
        ##cv2.imshow("Eroded", mask)
        mask = cv2.dilate(mask, None, iterations=5)
        ##cv2.imshow("Dilated", mask)        
        bit = cv2.bitwise_and(image, image, mask=mask)
        cv2.imshow("Output", bit)
        edge = cv2.Canny(bit,900,150)
        ##cv2.imshow("Edge1",edge)

        cnts = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        cnts = imutils.grab_contours(cnts)
        copy = bit.copy()
        for c in cnts:
            cv2.drawContours(copy, [c], -1, (240, 0, 159), 2)
            cv2.waitKey(1)
        cv2.imshow("Contours", copy)
        
        cv2.waitKey(1)
        time.sleep(1)
    except:
        pass
