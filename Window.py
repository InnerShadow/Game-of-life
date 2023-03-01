
from PyQt5 import QtGui, QtWidgets, QtCore
from PyQt5.QtGui import QPainter, QBrush, QPen
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, QTimer, QThread
import sys

import greed
import cell

class Window(QMainWindow):

    def __init__(self, _greed):
        super().__init__()
        self.greed = _greed
        self.title = "Game of live"
        self.top= 150
        self.left= 150
        self.width = 900
        self.height = 600
        self.InitWindow()

    def go(self):
        self.update()
        QApplication.processEvents()
        QThread.msleep(10)
        self.greed.doLive()

    def InitWindow(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width, self.height)
        self.setAttribute(QtCore.Qt.WA_StyledBackground, True)
        self.setStyleSheet('background-color: blue')
        self.show()

    def paintEvent(self, event):
        painter = QPainter()
        painter.begin(self)
        painter.setRenderHint(QPainter.Antialiasing)

        painter.setBrush(QBrush(Qt.yellow, Qt.SolidPattern))
        painter.setPen(QPen(Qt.black, 1, Qt.SolidLine))

        shape = self.greed.Matrix.shape
        for i in range(shape[0]):
            for j in range(shape[1]):
                if self.greed.Matrix[i, j].isAlive :
                    painter.drawRect(i * 10, j * 10, 10, 10)
        
        painter.setPen(QtCore.Qt.black)
        painter.setBrush(QtCore.Qt.white)
        for i in range(shape[1]):
            for i in range(shape[0]):
                painter.drawLine(i * 10, 0, i * 10, self.height)

        for i in range(shape[0]):
            for j in range(shape[1]):
                painter.drawLine(0, j * 10, self.width, j * 10)
        
        self.go()
        


