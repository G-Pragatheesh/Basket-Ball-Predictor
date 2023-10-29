# initialization
import cv2
import cvzone
from cvzone.ColorModule import ColorFinder
import numpy as np
import math

# cap = cv2.VideoCapture('Videos/vid (4).mp4')
cap = cv2.VideoCapture('Videos/vid (4).mp4') # initializing the captured video

# Assigning the found colour of the ball
myColorFinder = ColorFinder(False)

hsvVals = {'hmin': 5, 'smin': 89, 'vmin': 112, 'hmax': 16, 'smax': 255, 'vmax': 255}

while True:
    success, img = cap.read()
    img = img[0:850, :]  # Cropping the image

    # Detect the colour of the ball
    imgColor, mask = myColorFinder.update(img, hsvVals)

    # Finding the location of the ball
    imgContour, contours = cvzone.findContours(img, mask, minArea=1000)

    imgContour = cv2.resize(imgContour, (0, 0), None, 0.6, 0.6)
    # cv2.imshow("Image", img)
    cv2.imshow("ImageColor", imgContour)
    cv2.waitKey(20)