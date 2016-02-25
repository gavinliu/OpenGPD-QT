# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Main_UI.ui'
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
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 140, 621, 231))
        self.groupBox.setObjectName("groupBox")
        self.listView_2 = QtWidgets.QListView(self.groupBox)
        self.listView_2.setGeometry(QtCore.QRect(0, 20, 621, 211))
        self.listView_2.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.listView_2.setObjectName("listView_2")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 10, 621, 121))
        self.groupBox_2.setObjectName("groupBox_2")
        self.listView = QtWidgets.QListView(self.groupBox_2)
        self.listView.setGeometry(QtCore.QRect(0, 20, 621, 91))
        self.listView.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.listView.setObjectName("listView")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(10, 130, 621, 3))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 380, 621, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 24))
        self.menubar.setObjectName("menubar")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        self.menuAout = QtWidgets.QMenu(self.menubar)
        self.menuAout.setObjectName("menuAout")
        MainWindow.setMenuBar(self.menubar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setMovable(False)
        self.toolBar.setAllowedAreas(QtCore.Qt.TopToolBarArea)
        self.toolBar.setToolButtonStyle(QtCore.Qt.ToolButtonTextOnly)
        self.toolBar.setFloatable(True)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionHelp = QtWidgets.QAction(MainWindow)
        self.actionHelp.setObjectName("actionHelp")
        self.actionConnection = QtWidgets.QAction(MainWindow)
        self.actionConnection.setObjectName("actionConnection")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionDisconnection = QtWidgets.QAction(MainWindow)
        self.actionDisconnection.setObjectName("actionDisconnection")
        self.actionGetDevice = QtWidgets.QAction(MainWindow)
        self.actionGetDevice.setObjectName("actionGetDevice")
        self.actionGetRules = QtWidgets.QAction(MainWindow)
        self.actionGetRules.setObjectName("actionGetRules")
        self.actionAbout_Author = QtWidgets.QAction(MainWindow)
        self.actionAbout_Author.setObjectName("actionAbout_Author")
        self.actionAoub_OpenGpad = QtWidgets.QAction(MainWindow)
        self.actionAoub_OpenGpad.setObjectName("actionAoub_OpenGpad")
        self.menuHelp.addAction(self.actionHelp)
        self.menuAout.addAction(self.actionAbout_Author)
        self.menuAout.addAction(self.actionAoub_OpenGpad)
        self.menubar.addAction(self.menuAout.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.toolBar.addAction(self.actionConnection)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionDisconnection)
        self.toolBar.addAction(self.actionGetRules)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "Rules"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Device List"))
        self.pushButton.setText(_translate("MainWindow", "Start"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.menuAout.setTitle(_translate("MainWindow", "Aout"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.actionHelp.setText(_translate("MainWindow", "Help ?"))
        self.actionConnection.setText(_translate("MainWindow", "Connection"))
        self.actionConnection.setToolTip(_translate("MainWindow", "Connection"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
        self.actionDisconnection.setText(_translate("MainWindow", "Disconnection"))
        self.actionDisconnection.setToolTip(_translate("MainWindow", "Disconnection"))
        self.actionGetDevice.setText(_translate("MainWindow", "GetDevice"))
        self.actionGetDevice.setToolTip(_translate("MainWindow", "GetDevice"))
        self.actionGetRules.setText(_translate("MainWindow", "GetRules"))
        self.actionAbout_Author.setText(_translate("MainWindow", "About Author"))
        self.actionAoub_OpenGpad.setText(_translate("MainWindow", "About OpenGpad"))

