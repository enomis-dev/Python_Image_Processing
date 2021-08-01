# Objective: Learn how to train the haar cascade model for face recognition
# The trained model is saved in a .yml file and used in the next chapter exercise to recognize an unseen photo
import os
import cv2 as cv
import numpy as np

# create a list with names
people = []
DIR = r'Data\faces\train'
for i in os.listdir(DIR):
    people.append(i)

features = []
labels = []

# we read the classifier model
haar_cascade = cv.CascadeClassifier('haar_face.xml')

def create_train():
    for person in people:
        path = os.path.join(DIR, person)
        label = people.index(person)

        for img in os.listdir(path):
            img_path = os.path.join(path, img)

            img_array = cv.imread(img_path)
            gray = cv.cvtColor(img_array, cv.COLOR_BGR2GRAY)

            faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1,
                                                       minNeighbors=4)

            for (x,y,w,h) in faces_rect:
                faces_roi = gray[y:y+h, x:x+w]
                features.append(faces_roi)
                labels.append(label)

create_train()

print(f'Length of the features = {len(features)}')
print(f'Length of the labels = {len(labels)}')
print('Training done---------')

features = np.array(features, dtype='object')
labels = np.array(labels)


# Create a face recognizer object
face_recognizer = cv.face.LBPHFaceRecognizer_create()

# Train the Recognizer on the features list and labels list
face_recognizer.train(features, labels)

# we save the recognizer to a yml file
face_recognizer.save('face_trained.yml')
np.save('features.npy', features)
np.save('labels.npy', labels)



