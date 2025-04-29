import cv2 as cv
import os
import matplotlib.pyplot as plt
import numpy as np

def pureColors():
    zeros =  np.zeros((100,100))
    ones =  np.ones((100,100))
    bImg = cv.merge((zeros, zeros, 255*ones)) 
    gImg = cv.merge((zeros, 255*ones, zeros)) 
    rImg = cv.merge((255*ones, zeros, zeros)) 

    plt.figure()
    plt.subplot(231)
    plt.imshow(bImg)
    plt.title('Blue')

    plt.subplot(232)
    plt.imshow(gImg)
    plt.title('Green')

    plt.subplot(233)
    plt.imshow(rImg)
    plt.title('Red')

    plt.show()

def bgrGrayGrayscale():
    root = os.getcwd()
    imgPath = os.path.join(root, "data\\pexels-malme.jpg")
    img = cv.imread(imgPath)
    b,g,r = cv.split(img)
     
    plt.figure()
    plt.subplot(131)
    plt.imshow(b, cmap="gray")
    plt.title('b')
    plt.subplot(132)
    plt.imshow(g)
    plt.title('g')
    plt.subplot(133)
    plt.imshow(r)
    plt.title('r')
    plt.show()

def bgrChannelColor():
    root = os.getcwd()
    imgPath = os.path.join(root, "data\\pexels-malme.jpg")
    img = cv.imread(imgPath)
    b,g,r = cv.split(img)
    zeros =  np.zeros_like(b)
    bimg = cv.merge((b, zeros, zeros))
    gimg = cv.merge((zeros, g, zeros))
    rimg = cv.merge((zeros, zeros, r))

    plt.figure()
    plt.subplot(131)
    plt.imshow(bimg)
    
    plt.subplot(132)
    plt.imshow(gimg)
     
    plt.subplot(133)
    plt.imshow(rimg)
   
    plt.show()

if __name__ == "__main__":
    # pureColors()
    # bgrGrayGrayscale()
    bgrChannelColor()