# Objective: learn how to add figures or text to blank images
import cv2 as cv
import numpy as np

# create a blank image
blank = np.zeros((500,500,3), dtype='uint8')
cv.imshow('Blank',blank)

# 1. Point the image a certain colour
#blank[200:300, 300:400] = 0,0,255
#cv.imshow('Green',blank)

# 2. Draw a Rectangle
cv.rectangle(blank, (0,0), (250,250), (0,255,0), thickness=cv.FILLED) # cv.Filled to add a full color
cv.imshow('Rectangle', blank)

# 3. Draw a circle
# we are giving the coordinates of the image center
cv.circle(blank, (blank.shape[1]//2,blank.shape[0]//2), 40, (0,0,255), thickness=-1)
cv.imshow('circle',blank)

# 4. Draw a line
cv.line(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), (255,255,255), thickness=3)
cv.imshow('Line', blank)

# 5. Write text
cv.putText(blank, 'Hello', (225,225), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0,255,0), thickness=2)
cv.imshow('Line', blank)

# it is important if we want to maintain the image window open
cv.waitKey(0)