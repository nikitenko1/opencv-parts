import cv2 as cv
import os
import matplotlib.pyplot as plt
import numpy as np

def trackbarCallback():
    pass

def trackbar():
    root = os.getcwd()
    imgPath = os.path.join(root, "data\\pexels-saab-340.jpg")
    img = cv.imread(imgPath)

    windowName = 'trackbar'
    cv.namedWindow(windowName)
    cv.createTrackbar("B", windowName, 0, 255,trackbarCallback)
    cv.createTrackbar("G", windowName, 0, 255,trackbarCallback)
    cv.createTrackbar("R", windowName, 0, 255,trackbarCallback)

    while True:
        cv.imshow(windowName, img)
        if cv.waitKey(1) == ord("q"):
            break
        
        b = cv.getTrackbarPos("B", windowName)
        g = cv.getTrackbarPos("G", windowName)
        r = cv.getTrackbarPos("R", windowName)

        cv.circle(img, (496,325),10,(b,g,r),-1)
        cv.circle(img, (353,315),10,(b,g,r),-1)

    cv.destroyAllWindows()
            
     
if __name__ == "__main__":
    trackbar()