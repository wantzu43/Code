# -*- coding: utf-8 -*-
"""
Created on Tue May  9 22:15:33 2023

@author: Wantzu
"""
import cv2
ESC = 27
#畫面數量計數
n = 1
#存檔檔名用
index = 0
#人臉取樣總數
total = 100

def saveImage(face_image, index):
    filename = 'images/h0/{:02d}.jpg'.format(index)
    cv2.imwrite(filename, face_image)
    print(filename)
    
har_1 = r'C:\Users\Wantzu\anaconda3\Lib\site-packages\cv2\data\haarcascade_frontalface_default.xml'
face_cascade = cv2.CascadeClassifier(har_1)
cap = cv2.VideoCapture(0)
cv2.namedWindow('video', cv2.WINDOW_NORMAL)

while n > 0:
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 3)
    for (x, y, w, h) in faces:
        frame = cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 3)
        if n % 5 == 0:
            face_image = cv2.resize(gray[y:y+h, x:x+w], (400, 400))
            saveImage(face_image, index)
            index += 1
            if index >= total :
                print('get training data done')
                n = -1
                break
        n+=1
        
    cv2.imshow('video', frame)
    if cv2.waitKey(1) == 27:
        cv2.destroyAllWindows()
        break