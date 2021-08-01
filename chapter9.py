# Objective: Learn how to apply thresholding to a greyscale image
import cv2 as cv

# read the image on the disk
img = cv.imread('Data\\dog.jpg')
cv.imshow('Dog', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)

# Simple Thresholding
# Here, the matter is straight-forward. For every pixel, the same threshold value is applied.
# If the pixel value is smaller than the threshold, it is set to 0, otherwise it is set to a maximum value.
# The function cv.threshold is used to apply the thresholding.
# The first argument is the source image, which should be a grayscale image.
# The second argument is the threshold value which is used to classify the pixel values.
# The third argument is the maximum value which is assigned to pixel values exceeding the threshold.
threshold, thresh = cv.threshold(gray, 150, 255, cv.THRESH_BINARY)
cv.imshow('Simple Thresholded', thresh)

# cv.THRESH_BINARY_INV do the inverse with respect to cv.THRESH_BINARY
threshold, thresh_inverse = cv.threshold(gray, 150, 255, cv.THRESH_BINARY_INV)
cv.imshow('Simple Thresholded Inverse', thresh_inverse)

# Adaptive Thresholding --> compute the optimal threshold value on the base of the mean
adaptive_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C,
                                       cv.THRESH_BINARY, 11, 3)
cv.imshow('Adaptive Thresholding', adaptive_thresh)



cv.waitKey(0)