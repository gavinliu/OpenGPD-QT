import sys
import socket
import HelloWorld

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QDesktopWidget
from Utils import JSONEncoder

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


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        # self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 290, 150)
        self.setWindowTitle('Emit signal')
        self.show()

    def keyPressEvent(self, QKeyEvent):
        if not QKeyEvent.isAutoRepeat():
            print("keyPressEvent", QKeyEvent.text())
            if QKeyEvent.key() == Qt.Key_A:
                event = TouchEvent(190, 900, ACTION_DOWN)
                self.sendMSG(JSONEncoder().toJsonStr(event))
            if QKeyEvent.key() == Qt.Key_D:
                event = TouchEvent(480, 900, ACTION_DOWN)
                self.sendMSG(JSONEncoder().toJsonStr(event))
            if QKeyEvent.key() == Qt.Key_K:
                event = TouchEvent(1740, 900, ACTION_DOWN)
                self.sendMSG(JSONEncoder().toJsonStr(event))

            if QKeyEvent.key() == Qt.Key_J:
                event = TouchEvent(1500, 966, ACTION_DOWN)
                self.sendMSG(JSONEncoder().toJsonStr(event))
            if QKeyEvent.key() == Qt.Key_I:
                event = TouchEvent(1500, 800, ACTION_DOWN)
                self.sendMSG(JSONEncoder().toJsonStr(event))
            if QKeyEvent.key() == Qt.Key_O:
                event = TouchEvent(1650, 700, ACTION_DOWN)
                self.sendMSG(JSONEncoder().toJsonStr(event))
            if QKeyEvent.key() == Qt.Key_P:
                event = TouchEvent(1780, 680, ACTION_DOWN)
                self.sendMSG(JSONEncoder().toJsonStr(event))

    def keyReleaseEvent(self, QKeyEvent):
        if not QKeyEvent.isAutoRepeat():
            print("keyReleaseEvent", QKeyEvent.text())
            if QKeyEvent.key() == Qt.Key_A:
                event = TouchEvent(190, 900, ACTION_UP)
                self.sendMSG(JSONEncoder().toJsonStr(event))
            if QKeyEvent.key() == Qt.Key_D:
                event = TouchEvent(480, 900, ACTION_UP)
                self.sendMSG(JSONEncoder().toJsonStr(event))
            if QKeyEvent.key() == Qt.Key_K:
                event = TouchEvent(1740, 900, ACTION_UP)
                self.sendMSG(JSONEncoder().toJsonStr(event))

            if QKeyEvent.key() == Qt.Key_J:
                event = TouchEvent(1500, 966, ACTION_UP)
                self.sendMSG(JSONEncoder().toJsonStr(event))
            if QKeyEvent.key() == Qt.Key_I:
                event = TouchEvent(1500, 800, ACTION_UP)
                self.sendMSG(JSONEncoder().toJsonStr(event))
            if QKeyEvent.key() == Qt.Key_O:
                event = TouchEvent(1650, 700, ACTION_UP)
                self.sendMSG(JSONEncoder().toJsonStr(event))
            if QKeyEvent.key() == Qt.Key_P:
                event = TouchEvent(1780, 680, ACTION_UP)
                self.sendMSG(JSONEncoder().toJsonStr(event))

    def sendMSG(self, message):
        HOST = '127.0.0.1'
        PORT = 8000
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 定义socket类型，网络通信，TCP
        s.connect((HOST, PORT))  # 要连接的IP与端口
        s.sendall(message.encode(encoding="utf-8"))  # 把命令发送给对端
        # data = s.recv(1024)  # 把接收的数据定义为变量
        # print(type(data))
        # print(data.decode())  # 输出变量
        s.close()  # 关闭连接
        pass

    def center(self):
        self.setFixedSize(640, 480)
        desktop = QApplication.desktop()
        MainWindow.move((desktop.width() - self.width()) / 2, (desktop.height() - self.height()) / 2)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = Example()

    ui = HelloWorld.Ui_MainWindow()
    ui.setupUi(MainWindow)

    MainWindow.center()
    MainWindow.show()

    sys.exit(app.exec_())
