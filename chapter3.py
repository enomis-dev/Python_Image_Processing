# How to process a video
import cv2 as cv

# this  function is used to rescale a frame (work for images and videos and live videos)
def rescaleFrame(frame, scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions =( width,height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

# this work for live videos
def changeRes(width,height):
    # Live videos
    capture.set(3,width)
    capture.set(4,width)


# reading videos
capture = cv.VideoCapture('Data\\kite.mkv')

# we read the video frame by frame
while True:
    isTrue, frame = capture.read()

    frame_resized = rescaleFrame(frame, 0.2)

    # cv.imshow('Video', frame)  to see the full size frame
    cv.imshow('Video Resized', frame_resized)

    # to stop the video from playing indefinitly press d
    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()

# wait an infinite amount of time
cv.waitKey(0)