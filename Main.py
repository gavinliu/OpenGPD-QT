import os
import re
import sys
import socket

from PyQt5 import QtCore
from PyQt5.QtCore import Qt, QStringListModel, QModelIndex
from PyQt5.QtWidgets import QApplication, QMainWindow
from Main_UI import Ui_MainWindow

import Utils
import Constant
from Entity import TouchEvent
from Config import Config


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.setWindowTitle("OpenGamePad")

    def center(self):
        self.setFixedSize(640, 480)
        desktop = QApplication.desktop()
        MainWindow.move((desktop.width() - self.width()) / 2, (desktop.height() - self.height()) / 2)

    @QtCore.pyqtSlot()
    def on_pushButton_clicked(self):
        print("on_pushButton_clicked ", config.selectedDevice)

    @QtCore.pyqtSlot(QModelIndex)
    def on_listView_clicked(self, index):
        config.selectedDevice = config.devices[index.row()]
        print("on_listView_clicked: ", config.selectedDevice)

    @QtCore.pyqtSlot(bool)
    def on_actionConnection_triggered(self, triggered):
        print("on_actionConnection_triggered: ", triggered)


if __name__ == '__main__':
    config = Config()

    output = os.popen('adb devices')
    shell_devices = output.read()
    shell_devices = shell_devices.replace("\tdevice", "").replace("List of devices attached\n", "")
    shell_devices = re.compile(r'(\n){2,}').sub("", shell_devices)
    config.devices = shell_devices.split("\n")

    app = QApplication(sys.argv)

    MainWindow = MainWindow()
    MainWindow.listView.setModel(QStringListModel(config.devices))

    MainWindow.actionDisconnection.setEnabled(False)
    MainWindow.actionGetRules.setEnabled(False)
    MainWindow.groupBox.setEnabled(False)

    MainWindow.center()
    MainWindow.show()
    sys.exit(app.exec_())
