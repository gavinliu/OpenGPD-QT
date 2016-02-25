import os
import re
import sys

from PyQt5 import QtCore
from PyQt5.QtCore import Qt, QStringListModel, QModelIndex
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog
from Main_UI import Ui_MainWindow
from Main_UI_Dialog import Ui_Dialog

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
        MainDialog.show()

    @QtCore.pyqtSlot(QModelIndex)
    def on_listView_clicked(self, index):
        config.selectedDevice = config.devices[index.row()]
        print("on_listView_clicked: ", config.selectedDevice)

    @QtCore.pyqtSlot(QModelIndex)
    def on_listView_2_clicked(self, index):
        config.selectedRules = config.rules[index.row()]
        config.selectedButtons = config.selectedRules["faceButtons"]
        print("on_listView2_clicked: ", config.selectedRules)

    @QtCore.pyqtSlot(bool)
    def on_actionConnection_triggered(self, triggered):
        print("on_actionConnection_triggered: ", triggered)

    @QtCore.pyqtSlot(bool)
    def on_actionGetRules_triggered(self, triggered):
        print("on_actionGetRules_triggered: ", triggered)
        data = Utils.getRules()
        lists = Utils.jsonStrToObject(data)

        config.rules = lists

        list_get = []
        for rules in lists:
            faceButtons = rules["faceButtons"]
            text = ""
            for faceButton in faceButtons:
                if len(text):
                    text += " | "
                text += faceButton["key"] + "(" + str(faceButton["x"]) + "," + str(faceButton["y"]) + ")"
            list_get.append(text)
        self.listView_2.setModel(QStringListModel(list_get))

        MainWindow.groupBox.setEnabled(True)


class MainDialog(QDialog, Ui_Dialog):
    def __init__(self):
        QDialog.__init__(self)
        self.setupUi(self)
        self.setWindowFlags(Qt.WindowStaysOnTopHint)

    def keyPressEvent(self, QKeyEvent):
        if not QKeyEvent.isAutoRepeat():
            event = QKeyEvent.text()
            event = event.upper()

            for button in config.selectedButtons:
                if button["key"] == event:
                    touch = TouchEvent(button["x"], button["y"], Constant.ACTION_TOUCH_DOWN)
                    Utils.sendMSG(Utils.toJsonStr(touch))
                    print("点击：", event, button)

    def keyReleaseEvent(self, QKeyEvent):
        if not QKeyEvent.isAutoRepeat():
            event = QKeyEvent.text()
            event = event.upper()

            for button in config.selectedButtons:
                if button["key"] == event:
                    touch = TouchEvent(button["x"], button["y"], Constant.ACTION_TOUCH_UP)
                    Utils.sendMSG(Utils.toJsonStr(touch))
                    print("释放：", event, button)


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
    MainWindow.groupBox.setEnabled(False)

    MainWindow.center()
    MainWindow.show()

    MainDialog = MainDialog()

    sys.exit(app.exec_())
