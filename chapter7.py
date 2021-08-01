# Objective: Blurring an image

import cv2 as cv
import numpy as np

# read the image on the disk
img = cv.imread('Data\\dog.jpg')

# display the image and give a name to the window
cv.imshow('Dog', img)

# Averaging blur (we define a kernel size and we blur the image)
average = cv.blur(img, (7,7))
cv.imshow('Average Blur', average)

# Gaussian blur, it is more natural as compared to the gaussian one
gauss = cv.GaussianBlur(img,(7,7),0)
cv.imshow('Gaussian Blur', gauss)

# Median Blur, is like average
# but it take the median

median = cv.medianBlur(img,7)
cv.imshow('Median Blur', median)

# Bilateral blurring
# it is the most effective, traditional blurring methods
# don't care about edges. Bilateral takes care
bilateral = cv.bilateralFilter(img, 5, 15, 15)
cv.imshow('Bilateral', bilateral)


cv.waitKey(0)