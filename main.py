import sys
import socket
import HelloWorld

from PyQt5 import QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QDesktopWidget
from Utils import JSONEncoder
from HelloWorld import Ui_MainWindow

ACTION_DOWN = 1
ACTION_UP = 2
ACTION_SWIPE = 3


class TouchEvent:
    def __init__(self, x, y, action):
        self.x = x
        self.y = y
        self.action = action

    def __repr__(self):
        return 'TouchEvent X : %s , Y : %d' % (self.x, self.y)


class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)

    def center(self):
        self.setFixedSize(640, 480)
        desktop = QApplication.desktop()
        MainWindow.move((desktop.width() - self.width()) / 2, (desktop.height() - self.height()) / 2)

    @QtCore.pyqtSlot()
    def on_pushButton_clicked(self):
        print("xx")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = MainWindow()
    MainWindow.center()
    MainWindow.show()
    sys.exit(app.exec_())
