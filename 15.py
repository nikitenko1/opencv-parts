import cv2 as cv
import os
import matplotlib.pyplot as plt
 

def imageTranslate():
    root = os.getcwd()
    imgPath = os.path.join(root, "data\\pexels-saab-39.jpg")
    img = cv.imread(imgPath)

    # dividing height and width by 2 to get the center of the image
    height, width = img.shape[:2]
    # get the center coordinates of the image to create the 2D rotation matrix
    center = (width/2, height/2)
    
    # using cv2.getRotationMatrix2D() to get the rotation matrix
    rotate_matrix = cv.getRotationMatrix2D(center=center, angle=45, scale=1)
    
    # rotate the image using cv2.warpAffine
    rotated_image = cv.warpAffine(src=img, M=rotate_matrix, dsize=(width, height))
    
    cv.imshow('Original image', img)
    cv.imshow('Rotated image', rotated_image)
    # wait indefinitely, press any key on keyboard to exit
    cv.waitKey(0)

if __name__ == "__main__":
    imageTranslate()