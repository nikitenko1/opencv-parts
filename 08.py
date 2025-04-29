import cv2 as cv
import os
import matplotlib.pyplot as plt
import numpy as np

def hsvColorSegmentation():
    root = os.getcwd()
    imgPath = os.path.join(root, "data\\pexels-saab-340.jpg")
    img = cv.imread(imgPath )
    imgRGB = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)

    lower_bound = np.array([0, 0, 50])
    upper_bound = np.array([10, 120, 100])
    mask = cv.inRange(hsv, lower_bound, upper_bound)
    
    plt.figure()
    plt.imshow(imgRGB)
    plt.show()  
    
    
    cv.imshow('mask', mask)
    cv.waitKey(0)

if __name__ == "__main__":
    hsvColorSegmentation()
    