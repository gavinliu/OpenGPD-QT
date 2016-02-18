# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'HelloWorld.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 480)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(490, 420, 113, 32))
        self.pushButton.setObjectName("pushButton")
        self.listView = QtWidgets.QListView(self.centralwidget)
        self.listView.setGeometry(QtCore.QRect(10, 10, 271, 441))
        self.listView.setObjectName("listView")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 22))
        self.menubar.setObjectName("menubar")
        self.menuXx = QtWidgets.QMenu(self.menubar)
        self.menuXx.setObjectName("menuXx")
        MainWindow.setMenuBar(self.menubar)
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionXx = QtWidgets.QAction(MainWindow)
        self.actionXx.setObjectName("actionXx")
        self.actionXx_2 = QtWidgets.QAction(MainWindow)
        self.actionXx_2.setObjectName("actionXx_2")
        self.menuXx.addAction(self.actionXx)
        self.menuXx.addAction(self.actionXx_2)
        self.menubar.addAction(self.menuXx.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Start"))
        self.menuXx.setTitle(_translate("MainWindow", "xx"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionXx.setText(_translate("MainWindow", "xx"))
        self.actionXx_2.setText(_translate("MainWindow", "xx"))

