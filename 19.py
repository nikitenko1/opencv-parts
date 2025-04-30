import cv2 as cv
import os
import matplotlib.pyplot as plt
import numpy as np

def grayHistogram():
    root = os.getcwd()
    imgPath = os.path.join(root, "data\\pexels-malme.jpg")
    img = cv.imread(imgPath,cv.IMREAD_GRAYSCALE)

    plt.figure()
    plt.imshow(img, cmap="gray")
    hist = cv.calcHist([img], [0], None, [256], [0,256])

    plt.figure()
    plt.plot(hist)
    plt.xlabel("pixel intensity")
    plt.ylabel("# if pixels")
    plt.show()

def colorHistogram():
    root = os.getcwd()
    imgPath = os.path.join(root, "data\\pexels-malme.jpg")
    img = cv.imread(imgPath)
    imgRgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    
    plt.figure()
    plt.imshow(imgRgb)

    colors = ['b', 'g', 'r']

    plt.figure()
    for i in range(len(colors)):
        hist = cv.calcHist([imgRgb], [i], None, [256], [0,256])
        plt.plot(hist, colors[i])
    
    plt.xlabel("pixel intensity")
    plt.ylabel("# if pixels")
    plt.show()

def histogramRegion():
    root = os.getcwd()
    imgPath = os.path.join(root, "data\\pexels-malme.jpg")
    img = cv.imread(imgPath)
    imgRgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    imgRgb = imgRgb[675:825,600:800,:] 
    
    plt.figure()
    plt.imshow(imgRgb)

    colors = ['b', 'g', 'r']

    plt.figure()
    for i in range(len(colors)):
        hist = cv.calcHist([imgRgb], [i], None, [256], [0,256])
        plt.plot(hist, colors[i])
    
    plt.xlabel("pixel intensity")
    plt.ylabel("# if pixels")
    plt.show()

if __name__ == "__main__":
    # grayHistogram()
    # colorHistogram()
    histogramRegion()