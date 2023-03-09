import cv2 #before importing install the library

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
img = cv2.imread('group.jpg') #read image for recognizing image from it
imS = cv2.resize(img, (960, 540)) #resize image and store it in the variable (width,height)
gray = cv2.cvtColor(imS, cv2.COLOR_BGR2GRAY) #inorder to process we want to convert our image to grayscale image
faces = face_cascade.detectMultiScale(gray, 1.1, 4)
for (x, y, w, h) in faces:
    cv2.rectangle(imS, (x, y), (x + w, y + h), (255, 0, 0), 2)

cv2.imshow('img', imS) 
cv2.waitKey()