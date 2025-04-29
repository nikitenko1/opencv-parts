import cv2 as cv
import os
import matplotlib.pyplot as plt
import numpy as np

def readAndWriteSinglePixel():
    root = os.getcwd()
    imgPath = os.path.join(root, "data\\pexels-malme.jpg")
    img = cv.imread(imgPath)
    imgRGB = cv.cvtColor(img, cv.COLOR_BGR2RGB)

    plt.figure()
    plt.imshow(imgRGB)
    plt.show()
    # eyePixel = imgRGB[312,350]
    imgRGB[312,350] = (255,0,0)

    plt.figure()
    plt.imshow(imgRGB)
    plt.show()

def readAndWritePixelRegion():
    root = os.getcwd()
    imgPath = os.path.join(root, "data\\pexels-malme.jpg")
    img = cv.imread(imgPath)
    imgRGB = cv.cvtColor(img, cv.COLOR_BGR2RGB)

    plt.figure()
    plt.imshow(imgRGB)
    plt.show()
                             
    eyeRegion = imgRGB[480:650,0:220]

    dx = 650-480
    dy = 220-0

    startX = 480
    startY = 600
    imgRGB[startX:startX+dx, startY:startY+dy]=eyeRegion

    plt.figure()
    plt.imshow(imgRGB)
    plt.show()

    # debug = 1

if __name__ == "__main__":
    # readAndWriteSinglePixel()
    readAndWritePixelRegion()
    