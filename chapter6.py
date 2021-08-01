# Objective: Learn how to split in image in its 3 colors
import cv2 as cv
import numpy as np

# read the image on the disk
img = cv.imread('Data\\dog.jpg')

# display the image and give a name to the window
cv.imshow('Dog', img)

# create a blank image
blank = np.zeros(img.shape[:2], dtype='uint8')


b,g,r = cv.split(img)

# they will be displayed in grayscale, actually this is the intensity of that color
# lighter -->  bigger concentration
cv.imshow('Blue',b)
cv.imshow('Green',g)
cv.imshow('Red',r)

print(img.shape)
print(b.shape)
print(g.shape)
print(r.shape)

# merge
merged = cv.merge([b,g,r])
cv.imshow('Merge',merged)

# If we want to display the color with have to convert the image to a 3 channel image
# Display the colors
blue = cv.merge([b,blank,blank])
green = cv.merge([blank,g,blank])
red = cv.merge([blank,blank,r])

cv.imshow('Blue 2',blue)
cv.imshow('Green 2',green)
cv.imshow('Red 2',red)

cv.waitKey(0)