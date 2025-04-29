import cv2 as cv
print("OpenCV version:", cv.__version__)
import os
import matplotlib.pyplot as plt
import numpy as np

def videoFromWebcam():
    cap = cv.VideoCapture(1)

    if not cap.isOpened():
        exit()

    while True:
        ret, frame = cap.read()
        if ret:
            cv.imshow("Webcam", frame)

        if cv.waitKey(1) == ord("q"):
            break

    cap.release()
    cv.destroyAllWindows()

def videoFromFile():
    root = os.getcwd()
    vidPath = os.path.join(root, "data\\pexels-takeoff.mp4")
    cap = cv.VideoCapture(vidPath)

    while cap.isOpened():
        ret, frame = cap.read()
        
        cv.imshow("video", frame)
        delay = int(1000/60)

        if cv.waitKey(delay) == ord("q"):
            break

def writeVideoToFile():
    cap = cv.VideoCapture(0)
    # Define the codec and create VideoWriter object
    fourcc = cv.VideoWriter_fourcc(*'XVID')

    root = os.getcwd()
    outPath = os.path.join(root, "data\\webcam.avi")

    out = cv.VideoWriter(outPath, fourcc, 20.0, (640,  480))
    
    while cap.isOpened:
        ret, frame = cap.read()
        if ret:
            out.write(frame)
            cv.imshow("Webcam", frame)

        if cv.waitKey(1) == ord("q"):
            break
      
    # Release everything if job is finished
    cap.release()
    out.release()
    cv.destroyAllWindows()

if __name__ == "__main__":
    # videoFromWebcam()
    # videoFromFile()
    writeVideoToFile()
    
    
