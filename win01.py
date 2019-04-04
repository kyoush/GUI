# -*- coding: utf-8 -*-

import sys
import time
from PyQt5.QtWidgets import *

#ウィンドウのリサイズを禁止するクラス
class SampleWindow(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle("Sample Window")
        self.setGeometry(300,300,200,150)
        self.setMinimumHeight(100)
        self.setMinimumWidth(250)
        self.setMaximumHeight(100)
        self.setMaximumWidth(250)

def main():
    app = QApplication(sys.argv)
    w = QWidget()
    w.resize(250, 150)
    w.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    myApp = QApplication(sys.argv)
    myWindow = SampleWindow()
    myWindow.show()
    myApp.exec_()
    sys.exit(0)

'''
import sys
from PyQt5 import QtWidgets

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    window = QtWidgets.QWidget()
    window.setWindowTitle('テスト')
    window.show()

    sys.exit(app.exec_())

'''
