# initialization
import cv2
import cvzone
from cvzone.ColorModule import ColorFinder
import numpy as np
import math

"""
# Libraries written for checking the parameters of the execution of the code
import Verifying
import Retrieve_hsvVals
import Access_WebCam
"""

cap = cv2.VideoCapture('Videos/vid (4).mp4')  # initializing the captured video

# Assigning the found colour of the ball
myColorFinder = ColorFinder(False)
hsvVals = {'hmin': 5, 'smin': 89, 'vmin': 112, 'hmax': 16, 'smax': 255, 'vmax': 255}

# Creating empty list to hold the positions of the ball in space time
posListX = []
posListY = []
Xlist = [item for item in range(0, 1300)]
prediction = False  # A variable to print the final prediction
while True:
    # setting up the video to be displayed
    success, img = cap.read()

    # img = cv2.imread('Ball.png')
    img = img[0:850, :]  # Cropping the image

    # Detect the colour of the ball
    imgColor, mask = myColorFinder.update(img, hsvVals)

    # Finding the location of the ball
    imgContour, contours = cvzone.findContours(img, mask, minArea=1000)

    if contours:
        posListX.append(contours[0]['center'][0])
        posListY.append(contours[0]['center'][1])

    if posListX:
        # finding the coefficients of the polynomial equation
        a, b, c = np.polyfit(posListX, posListY, 2)

        for i, (posX, posY) in enumerate(zip(posListX, posListY)):
            pos = (posX, posY)
            cv2.circle(imgContour, pos, 7, (0, 255, 0), cv2.FILLED)
            if i == 0:
                cv2.line(imgContour, pos, pos, (0, 255, 0), 6)
            else:
                cv2.line(imgContour, pos, (posListX[i - 1], posListY[i - 1]), (0, 255, 0), 6)

        # Prediction path
        for x in Xlist:
            y = int(a * x ** 2 + b * x + c)
            cv2.circle(imgContour, (x, y), 1, (255, 0, 255), cv2.FILLED)  # Drawing the predicted path
        if len(posListX) < 10:
            c = c - 596
            x = int((-b - math.sqrt((b ** 2) - (4 * a * c))) / (2 * a))
            prediction = 326 < x < 430

        # Final prediction
        if prediction:
            cvzone.putTextRect(imgContour, "Basket", (50, 100), scale=8, thickness=5, colorR=(0, 200, 0), offset=20)
        else:
            cvzone.putTextRect(imgContour, "No Basket", (50, 100), scale=8, thickness=5, colorR=(0, 0, 200), offset=20)

    # Display the Output

    # img = cv2.resize(img, (0,0), None,0.6,0.6)
    # imgColor = cv2.resize(imgColor, (0, 0), None, 0.6, 0.6)

    imgContour = cv2.resize(imgContour, (0, 0), None, 0.6, 0.6)
    # cv2.imshow("Image", img)
    cv2.imshow("ImageColor", imgContour)
    cv2.waitKey(70)