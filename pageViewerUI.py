# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pageViewerUI_.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(900, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.materialLabel = QtWidgets.QLabel(self.centralwidget)
        self.materialLabel.setGeometry(QtCore.QRect(30, 20, 124, 38))
        self.materialLabel.setStyleSheet("font: 75 16pt \"Verdana\";")
        self.materialLabel.setObjectName("materialLabel")
        self.favButton = QtWidgets.QPushButton(self.centralwidget)
        self.favButton.setGeometry(QtCore.QRect(671, 500, 191, 34))
        self.favButton.setObjectName("favButton")
        self.quizList = QtWidgets.QListWidget(self.centralwidget)
        self.quizList.setGeometry(QtCore.QRect(30, 70, 221, 411))
        self.quizList.setObjectName("quizList")
        self.tempArea = QtWidgets.QLabel(self.centralwidget)
        self.tempArea.setGeometry(QtCore.QRect(280, 70, 581, 411))
        self.tempArea.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.tempArea.setObjectName("tempArea")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Content"))
        self.materialLabel.setText(_translate("MainWindow", "Quizzes"))
        self.favButton.setText(_translate("MainWindow", "Add to Favourite"))
        self.tempArea.setText(_translate("MainWindow", "TextLabel"))

