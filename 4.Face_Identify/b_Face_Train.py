# -*- coding: utf-8 -*-
"""
Created on Tue May  9 22:54:53 2023

@author: Wantzu
"""

import cv2
import numpy as np

images = []
labels = []
for index in range(100):
    filename = 'images/h0/{:02d}.jpg'.format(index)
    print('read' + filename)
    img = cv2.imread(filename, cv2.COLOR_BGR2GRAY)
    images.append(img)
    labels.append(0)
    
print('training...')
model = cv2.face.LBPHFaceRecognizer_create()
model.train(np.asarray(images), np.asarray(labels))
model.save('faces.data')
print('training done')
    