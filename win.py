# -*- codig: utf-8 -*-

import sys
from PyQt5.QtCore import pyqtSignal, QObject
from PyQt5.QtWidgets import QMainWindow, QApplication

class Communicate(QObject):

    close App = pyqtSignal()

class Example(QMainWindow):

    def __init__(self):
        super().__init__()

        self.
