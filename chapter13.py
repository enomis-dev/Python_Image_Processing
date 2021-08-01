# Objective: Learn how to do face detection using haar cascade model in open cv
# Before using this code you need to create a file with the xml model
# The file will be called haar_face.xml and its content can be taken from github repository of the open cv project
# To do that go to https://github.com/opencv/opencv/tree/master/data/haarcascades and copy the content of
# haarcascade_frontalface_default.xml to the xml file haar_face.xml
# Further information on this model can be found here: https://towardsdatascience.com/face-detection-with-haar-cascade-727f68dafd08

import cv2 as cv
import numpy as np

# read the image on the disk
img = cv.imread('Data\\lena.png')
cv.imshow('lena', img)

# the face detection algorithm we are using doesn't look the colors, we convert to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray person', gray)

# we read the classifier
haar_cascade = cv.CascadeClassifier('haar_face.xml')

faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3)

print(f'Number of face found = {len(faces_rect)}')

# Draw a rectangle for the face
for (x,y,w,h) in faces_rect:
    cv.rectangle(img, (x,y), (x+w,y+h), (0,255,0), thickness=2)

cv.imshow('Detected faces',img)

# the classifier is realLy sensitive to noise,
# we have to increase the value of minNeighbors
# to make it less sensitive




cv.waitKey(0)
