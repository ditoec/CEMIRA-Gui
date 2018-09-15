# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'control_panel.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(20, 20, 761, 551))
        self.tabWidget.setObjectName("tabWidget")
        self.tabMain = QtWidgets.QWidget()
        self.tabMain.setObjectName("tabMain")
        self.formLayoutWidget = QtWidgets.QWidget(self.tabMain)
        self.formLayoutWidget.setGeometry(QtCore.QRect(20, 20, 501, 111))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.formLayoutWidget)
        self.gridLayout.setObjectName("gridLayout")
        self.labelHead = QtWidgets.QLabel(self.formLayoutWidget)
        self.labelHead.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.labelHead.setObjectName("labelHead")
        self.gridLayout.addWidget(self.labelHead, 2, 1, 1, 1)
        self.pushHead = QtWidgets.QPushButton(self.formLayoutWidget)
        self.pushHead.setObjectName("pushHead")
        self.gridLayout.addWidget(self.pushHead, 2, 0, 1, 1)
        self.pushArm = QtWidgets.QPushButton(self.formLayoutWidget)
        self.pushArm.setObjectName("pushArm")
        self.gridLayout.addWidget(self.pushArm, 3, 0, 1, 1)
        self.labelArm = QtWidgets.QLabel(self.formLayoutWidget)
        self.labelArm.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.labelArm.setObjectName("labelArm")
        self.gridLayout.addWidget(self.labelArm, 3, 1, 1, 1)
        self.tabWidget.addTab(self.tabMain, "")
        self.tabHead = QtWidgets.QWidget()
        self.tabHead.setObjectName("tabHead")
        self.widgetHead = QtWidgets.QWidget(self.tabHead)
        self.widgetHead.setGeometry(QtCore.QRect(10, 10, 731, 501))
        self.widgetHead.setObjectName("widgetHead")
        self.tabWidget.addTab(self.tabHead, "")
        self.tabArm = QtWidgets.QWidget()
        self.tabArm.setObjectName("tabArm")
        self.tabWidget.addTab(self.tabArm, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "CEMIRA - Control Panel"))
        self.labelHead.setText(_translate("MainWindow", "Launch Head Control Nodes"))
        self.pushHead.setText(_translate("MainWindow", "OFF"))
        self.pushArm.setText(_translate("MainWindow", "OFF"))
        self.labelArm.setText(_translate("MainWindow", "Launch Arm Control Nodes"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabMain), _translate("MainWindow", "Main"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabHead), _translate("MainWindow", "Head"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabArm), _translate("MainWindow", "Arm"))

