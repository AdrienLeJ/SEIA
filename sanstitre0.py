# -*- coding: utf-8 -*-
"""
Auteurs: Louis Perrodo et Adrien Le Janne

Projet : Analyseur de sommeil pour les personnes âgées

Objectif : Caméra avec modèle Yolo
"""
import torch
import numpy as np
import cv2

#importation modèle yolov5
model = torch.hub.load('ultralytics/yolov5', 'custom', path='/yolov5/best.pt', force_reload=True)


#-active la webcam
cap = cv2.VideoCapture(0)

width = 1500
height = 1080
dim = (width, height)

while cap.isOpened():
    ret, frame = cap.read()
    frame = cv2.resize(frame, dim, interpolation=cv2.INTER_AREA)

    # detections 
    results = model(frame)
    #affichage des résultats
    cv2.imshow('YOLO', np.squeeze(results.render()))
    
    if cv2.waitKey(1) & 0xFF == 27:
        break
cap.release()
cv2.destroyAllWindows()


