# Objective: Learn some operations
# - translation
# - rotation
# - resizing
# - flipping
# - cropping
import cv2 as cv
import numpy as np

# read the image on the disk
img = cv.imread('Data\\dog.jpg')
cv.imshow('dog',img)

# Translation
def translate(img,x,y):
    transMat = np.float32([[1,0,x],[0,1,y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat, dimensions)

# -x --> left
# -y --> Up
#  x --> Right
#  y --> Down

translated = translate(img, 100, 100)
cv.imshow('Translated', translated)

# Rotation
def rotate(img, angle, rotPoint=None):
    (height,width) = img.shape[:2]

    if rotPoint is None:
        rotPoint = (width//2, height//2)  # we rotate around the center

    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (width, height)

    return cv.warpAffine(img, rotMat, dimensions)

rotated = rotate(img, -45) # negative --> clockwise
cv.imshow('Rotated', rotated)

# if we rotate a rotated image we end up with black spaces
# to avoid this we have to rotate the original image

# Resizing
resized = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)
cv.imshow('Resized', resized)

# Flipping
flip = cv.flip(img, 0) # 0 flip vertically
                       # 1 horizontally
                       # -1 both
cv.imshow('Flip', flip)

# Cropping
cropped = img[200:400, 300:400]
cv.imshow('Cropped', cropped)



cv.waitKey(0)