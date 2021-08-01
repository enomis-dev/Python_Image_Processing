# Objective: Learn how to convert to other color spaces
import cv2 as cv
import matplotlib.pyplot as plt

# read the image on the disk
img = cv.imread('Data\\dog.jpg')

# display the image and give a name to the window
cv.imshow('Dog', img)

# if we do this we will not display the image correctly because the image is BGR
# while matplotlib displays as RGB
plt.imshow(img)
plt.show()

# BGR to GrayScale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)

# BGR to HSV
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('HSV',hsv)

# BGR to L*a*b
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow('LAB',lab)

# BGR to RGB
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow('RGB',rgb)

# we can not convert directly from grayscale to hsv ecc,
# we have to pass always by BGR





plt.imshow(rgb)
plt.show()



cv.waitKey(0)