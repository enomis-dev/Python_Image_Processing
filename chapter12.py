# Objective: Learn how to generate histograms for an image
import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

# read the image on the disk
img = cv.imread('Data\\dog.jpg')
cv.imshow('Dog', img)

blank = np.zeros(img.shape[:2], dtype='uint8')

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)


# Grayscale histogram
# 0 in the number of channels
# None is the mask (we don't have a mask now)
gray_hist = cv.calcHist([gray], [0], None, [256], [0,256])

plt.figure()
plt.title('Grayscale Histogram')
plt.xlabel('Bins')
plt.ylabel('# of pixels')
plt.plot(gray_hist)
plt.xlim([0,256])
plt.grid(True)
plt.show()

# Calculate color histograms and apply a mask i.e. histograms will be calculated only on the not masked part of the image
mask = cv.circle(blank, (img.shape[1]//2, img.shape[0]//2), 100, 255, -1)
masked = cv.bitwise_and(gray,gray,mask=mask)
cv.imshow('Masked',masked)
gray_hist = cv.calcHist([gray], [0], mask, [256], [0,256])

plt.figure()
plt.title('Colour Histogram')
plt.xlabel('Bins')
plt.ylabel('# of pixels')


# Color Histogram
mask = cv.circle(blank, (img.shape[1]//2, img.shape[0]//2), 100, 255, -1)
masked = cv.bitwise_and(img,img,mask=mask)
colors = ('b','g','r')
print(masked.shape)
for i,col in enumerate(colors):
    hist = cv.calcHist([img],[i],mask,[256],[0,256])
    plt.plot(hist,color=col)
    plt.xlim([0,256])

plt.show()
cv.waitKey(0)