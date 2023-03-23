from PySide6.QtWidgets import QDialog


import cv2


class Function(QDialog):
    def __init__(self):
        super(Function,self).__init__()
        self.ONOFF.clicked.connect(self.onClicked)
    def onClicked(self):
        cv2.VideoCapture(1)
        self.ONOFF.clicked.connect(self.offClicked)
    def offClicked(self):
        cv2.VideoCapture(0)

