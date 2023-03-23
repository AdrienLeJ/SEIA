from PySide6.QtWidgets import QDialog


import cv2
import sys, psutil


class Function(QDialog):
    def __init__(self):
        super(Function,self).__init__()
        self.ONOFF.clicked.connect(self.onClicked)
    def onClicked(self):

        ### retour caméra ###
        cam = cv2.VideoCapture(1)
        while(cam.isOpened()):
            ret, frame = cam.read()
            if ret == True:
                self.displayimage(frame,1)
                cv2.waitKey()

         ### affichage orientation en ° d'après prédiction ###


        ### coloration des directions suivant la direction prise ###


        self.ONOFF.clicked.connect(self.offClicked)
    def offClicked(self):
        cv2.VideoCapture(0)
