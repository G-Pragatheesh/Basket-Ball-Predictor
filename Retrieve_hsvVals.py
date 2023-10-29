import cv2
import cvzone
from cvzone.ColorModule import ColorFinder

cap = cv2.VideoCapture('Videos/vid (8).mp4')
myColorFinder = ColorFinder(True)
hsvVals = 'red'
while True:
    # Assigning the Video/Image to be process
    success, img = cap.read()
    img = cv2.imread("Ball2.png")

    imgColor, mask = myColorFinder.update(img, hsvVals)

    img = img[0:, :]  # Cropping
    imgColor = imgColor[:, :]

    # Displaying the Final Output
    img = cv2.resize(img, (0, 0), None, 0.6, 0.6)  # Resizing
    imgColor = cv2.resize(imgColor, (0, 0), None, 0.4, 0.4)  # Resizing
    cv2.imshow("Image", img)
    cv2.imshow("ImageColour", imgColor)
    cv2.waitKey(100)
