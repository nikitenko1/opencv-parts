import cv2 as cv
import os
import matplotlib.pyplot as plt
import numpy as np

def rotation():
    root = os.getcwd()
    imgPath = os.path.join(root, "data\\pexels-saab-39.jpg")
    img = cv.imread(imgPath)

    
    height,width ,_ = img.shape
    # center: Point2f,     angle: float,     scale: float
    T = cv.getRotationMatrix2D((width/2, height/2), 180, 1)
    imgR = cv.warpAffine(img, T, (width, height))
    cv.imshow("Img Rotate", imgR )
    # wait indefinitely, press any key on keyboard to exit
    cv.waitKey(0)

if __name__ == "__main__":
    rotation()