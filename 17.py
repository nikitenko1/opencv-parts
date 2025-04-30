import cv2 as cv
import os
import matplotlib.pyplot as plt
import numpy as np

def affineTransform():
    root = os.getcwd()
    imgPath = os.path.join(root, "data\\pexels-saab-39.jpg")
    img = cv.imread(imgPath)
    img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    
    height,width ,_ = img.shape
    
    p1 = np.array([[100,100], [900,100], [100,900]], dtype=np.float32)
    p2 = np.array([[50,150], [900,100], [150,800]], dtype=np.float32)
    T = cv.getAffineTransform(p1, p2)
    imgTr = cv.warpAffine(img, T, (width, height))
    plt.figure()
    plt.subplot(121)
    plt.imshow( imgTr)
    plt.subplot(122)
    plt.imshow( img)
    plt.show()

if __name__ == "__main__":
    affineTransform()