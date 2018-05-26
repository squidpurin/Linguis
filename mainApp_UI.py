# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainAppUI.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(900, 600)
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btn_IPA = QtWidgets.QPushButton(self.centralwidget)
        self.btn_IPA.setGeometry(QtCore.QRect(40, 160, 251, 301))
        self.btn_IPA.setStyleSheet("background-color: rgb(240, 80, 80);\n"
"color: rgb(255, 255, 255);\n"
"font: 20pt \"Gill Sans MT\";")
        self.btn_IPA.setObjectName("btn_IPA")
        self.btn_Material = QtWidgets.QPushButton(self.centralwidget)
        self.btn_Material.setGeometry(QtCore.QRect(320, 160, 251, 301))
        self.btn_Material.setStyleSheet("background-color: rgb(80, 240, 80);\n"
"color: rgb(255, 255, 255);\n"
"font: 20pt \"Gill Sans MT\";")
        self.btn_Material.setObjectName("btn_Material")
        self.btn_Quiz = QtWidgets.QPushButton(self.centralwidget)
        self.btn_Quiz.setGeometry(QtCore.QRect(600, 160, 261, 301))
        self.btn_Quiz.setStyleSheet("background-color: rgb(80, 80, 240);\n"
"color: rgb(255, 255, 255);\n"
"font: 20pt \"Gill Sans MT\";")
        self.btn_Quiz.setObjectName("btn_Quiz")
        self.btn_Favourite = QtWidgets.QPushButton(self.centralwidget)
        self.btn_Favourite.setGeometry(QtCore.QRect(40, 480, 251, 51))
        self.btn_Favourite.setStyleSheet("background-color: rgb(240, 240, 240);\n"
"color: rgb(80, 80, 80);\n"
"font: 16pt \"Gill Sans MT\";")
        self.btn_Favourite.setObjectName("btn_Favourite")
        self.btn_Options = QtWidgets.QPushButton(self.centralwidget)
        self.btn_Options.setGeometry(QtCore.QRect(320, 480, 251, 51))
        self.btn_Options.setStyleSheet("background-color: rgb(240, 240, 240);\n"
"color: rgb(80, 80, 80);\n"
"font: 16pt \"Gill Sans MT\";")
        self.btn_Options.setObjectName("btn_Options")
        self.btn_Quit = QtWidgets.QPushButton(self.centralwidget)
        self.btn_Quit.setGeometry(QtCore.QRect(600, 480, 261, 51))
        self.btn_Quit.setStyleSheet("background-color: rgb(240, 240, 240);\n"
"color: rgb(80, 80, 80);\n"
"font: 16pt \"Gill Sans MT\";")
        self.btn_Quit.setObjectName("btn_Quit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(233, 20, 434, 112))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("SEP_Images/logo/Linguis_Logo_F.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 900, 31))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Linguis"))
        self.btn_IPA.setText(_translate("MainWindow", "IPA"))
        self.btn_Material.setText(_translate("MainWindow", "Material"))
        self.btn_Quiz.setText(_translate("MainWindow", "Quiz"))
        self.btn_Favourite.setText(_translate("MainWindow", "Favourite"))
        self.btn_Options.setText(_translate("MainWindow", "Options"))
        self.btn_Quit.setText(_translate("MainWindow", "Quit"))

