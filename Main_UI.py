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
        self.listView_2.setGeometry(QtCore.QRect(10, 20, 601, 201))
        self.listView_2.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.listView_2.setObjectName("listView_2")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 10, 621, 121))
        self.groupBox_2.setObjectName("groupBox_2")
        self.listView = QtWidgets.QListView(self.groupBox_2)
        self.listView.setGeometry(QtCore.QRect(10, 20, 601, 91))
        self.listView.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.listView.setObjectName("listView")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(10, 130, 621, 3))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 370, 621, 41))
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
        self.menuADB_Tool = QtWidgets.QMenu(self.menubar)
        self.menuADB_Tool.setObjectName("menuADB_Tool")
        MainWindow.setMenuBar(self.menubar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setMovable(False)
        self.toolBar.setAllowedAreas(QtCore.Qt.TopToolBarArea)
        self.toolBar.setToolButtonStyle(QtCore.Qt.ToolButtonTextOnly)
        self.toolBar.setFloatable(True)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.actionHelp = QtWidgets.QAction(MainWindow)
        self.actionHelp.setObjectName("actionHelp")
        self.actionGetRules = QtWidgets.QAction(MainWindow)
        self.actionGetRules.setObjectName("actionGetRules")
        self.actionAbout_Author = QtWidgets.QAction(MainWindow)
        self.actionAbout_Author.setObjectName("actionAbout_Author")
        self.actionAoub_OpenGpad = QtWidgets.QAction(MainWindow)
        self.actionAoub_OpenGpad.setObjectName("actionAoub_OpenGpad")
        self.actionKill_Server = QtWidgets.QAction(MainWindow)
        self.actionKill_Server.setObjectName("actionKill_Server")
        self.actionGetDevices = QtWidgets.QAction(MainWindow)
        self.actionGetDevices.setObjectName("actionGetDevices")
        self.menuHelp.addAction(self.actionHelp)
        self.menuAout.addAction(self.actionAbout_Author)
        self.menuAout.addAction(self.actionAoub_OpenGpad)
        self.menuADB_Tool.addAction(self.actionKill_Server)
        self.menubar.addAction(self.menuADB_Tool.menuAction())
        self.menubar.addAction(self.menuAout.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.toolBar.addAction(self.actionGetDevices)
        self.toolBar.addAction(self.actionGetRules)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "映射列表"))
        self.groupBox_2.setTitle(_translate("MainWindow", "设备列表"))
        self.pushButton.setText(_translate("MainWindow", "开始"))
        self.menuHelp.setTitle(_translate("MainWindow", "帮助"))
        self.menuAout.setTitle(_translate("MainWindow", "关于"))
        self.menuADB_Tool.setTitle(_translate("MainWindow", "ADB 工具"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.actionHelp.setText(_translate("MainWindow", "帮助"))
        self.actionGetRules.setText(_translate("MainWindow", "获取映射列表"))
        self.actionAbout_Author.setText(_translate("MainWindow", "关于作者"))
        self.actionAoub_OpenGpad.setText(_translate("MainWindow", "开放源代码"))
        self.actionKill_Server.setText(_translate("MainWindow", "Kill-Server"))
        self.actionGetDevices.setText(_translate("MainWindow", "获取设备列表"))

