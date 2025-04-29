import cv2 as cv
import os
import matplotlib.pyplot as plt
import numpy as np

def grayscale():
    root = os.getcwd()
    imgPath = os.path.join(root, "data\\pexels-saab-340.jpg")
    img = cv.imread(imgPath)
    imgGRAY = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    cv.imshow("gray", imgGRAY)
    cv.waitKey(0)

def readAsGray():
    root = os.getcwd()
    imgPath = os.path.join(root, "data\\pexels-saab-340.jpg")
    img = cv.imread(imgPath, cv.IMREAD_GRAYSCALE)
     

    cv.imshow("gray", img)
    cv.waitKey(0)

if __name__ == "__main__":
    # grayscale()
    readAsGray()
    