# -*- coding: utf-8 -*-
"""
Created on Wed Mar 22 14:26:36 2023

@author: alexa
"""
import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from IHMv2 import Ui_MainWindow
from listenning_function import Function


class MainWindow(QMainWindow):
    def __init__(self):
        super (MainWindow, self).__init__()
        self.ui = Ui_MainWindow()


        self.inner_function = Function()

if __name__== '__main__':
    app = QApplication(sys.argv)

    window = MainWindow()
    window. show()

    sys. exit(app.exec_())


