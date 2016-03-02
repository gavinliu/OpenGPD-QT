import sys

from PyQt5 import QtCore
from PyQt5.QtCore import Qt, QStringListModel, QModelIndex, QThread, QUrl
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QLabel
from PyQt5.QtGui import QDesktopServices

import ADB
import Constant
import Utils
from Config import Config
from Entity import TouchEvent
from Main_UI import Ui_MainWindow
from Main_UI_Dialog import Ui_Dialog


class TestRunner(QThread):
    def run(self):
        ADB.startTesting(config.selectedDevice)


class Checker(QThread):
    def run(self):
        MainWindow.info.setText("正在检测手机状态，请稍等...")
        ADB.checkAPK(config.selectedDevice, MainWindow.info)
        ADB.startHelperApp(config.selectedDevice, MainWindow.info)
        MainWindow.actionGetRules.setEnabled(True)


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.setWindowTitle("OpenGamePad")

        self.info = QLabel()
        self.info.setFixedSize(640, 20)
        self.statusBar.addWidget(self.info)

    def center(self):
        self.setFixedSize(640, 480)
        desktop = QApplication.desktop()
        MainWindow.move((desktop.width() - self.width()) / 2, (desktop.height() - self.height()) / 2)

    @QtCore.pyqtSlot()
    def on_pushButton_clicked(self):
        print("on_pushButton_clicked ", config.selectedDevice)
        testRunner.start()

        MainDialog.setWindowModality(Qt.ApplicationModal)
        MainDialog.exec()

    @QtCore.pyqtSlot(QModelIndex)
    def on_listView_clicked(self, index):
        MainWindow.actionGetRules.setEnabled(False)

        config.selectedDevice = config.devices[index.row()]

        ADB.startForward(config.selectedDevice, "8000", "9000")
        ADB.startForward(config.selectedDevice, "8001", "9001")

        print("on_listView_clicked: ", config.selectedDevice)
        checker.start()

    @QtCore.pyqtSlot(QModelIndex)
    def on_listView_2_clicked(self, index):
        config.selectedRules = config.rules[index.row()]
        config.selectedButtons = config.selectedRules["faceButtons"]
        print("on_listView2_clicked: ", config.selectedRules)
        MainWindow.pushButton.setEnabled(True)

    @QtCore.pyqtSlot(bool)
    def on_actionGetRules_triggered(self, triggered):
        print("on_actionGetRules_triggered: ", triggered)
        data = Utils.getRules()
        if not len(data):
            return

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

    @QtCore.pyqtSlot(bool)
    def on_actionKill_Server_triggered(self, triggered):
        ADB.killServer()
        pass

    @QtCore.pyqtSlot(bool)
    def on_actionStart_Server_triggered(self, triggered):
        ADB.startServer()
        pass

    @QtCore.pyqtSlot(bool)
    def on_actionHelp_triggered(self, triggered):
        QDesktopServices.openUrl(QUrl("https://github.com/gavinliu/OpenGpad"))
        pass

    @QtCore.pyqtSlot(bool)
    def on_actionAbout_Author_triggered(self, triggered):
        QDesktopServices.openUrl(QUrl("http://gavinliu.cn/about/"))
        pass

    @QtCore.pyqtSlot(bool)
    def on_actionAoub_OpenGpad_triggered(self, triggered):
        QDesktopServices.openUrl(QUrl("https://github.com/gavinliu/OpenGpad"))
        pass


class MainDialog(QDialog, Ui_Dialog):
    def __init__(self):
        QDialog.__init__(self)
        self.setupUi(self)
        self.setWindowTitle("请保持这个窗口，在焦点上。")
        self.setWindowFlags(Qt.WindowStaysOnTopHint)
        self.setFixedSize(320, 240)

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

    def closeEvent(self, QCloseEvent):
        Utils.sendMSG("CLOSE")


if __name__ == '__main__':
    config = Config()

    testRunner = TestRunner()
    checker = Checker()

    config.devices = ADB.getDevice()

    app = QApplication(sys.argv)

    MainWindow = MainWindow()
    MainWindow.listView.setModel(QStringListModel(config.devices))

    MainWindow.groupBox.setEnabled(False)
    MainWindow.pushButton.setEnabled(False)
    MainWindow.actionGetRules.setEnabled(False)

    MainWindow.info.setText("提示：先选择手机，然后获取映射规则")

    MainWindow.center()
    MainWindow.show()

    MainDialog = MainDialog()

    sys.exit(app.exec_())
