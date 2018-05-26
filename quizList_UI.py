# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'quizListUI.ui'
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
        self.quizLabel = QtWidgets.QLabel(self.centralwidget)
        self.quizLabel.setGeometry(QtCore.QRect(30, 20, 124, 38))
        self.quizLabel.setStyleSheet("font: 75 16pt \"Verdana\";")
        self.quizLabel.setObjectName("quizLabel")
        self.quiz_list = QtWidgets.QListWidget(self.centralwidget)
        self.quiz_list.setGeometry(QtCore.QRect(30, 70, 831, 411))
        self.quiz_list.setObjectName("quiz_list")
        self.proceedButton = QtWidgets.QPushButton(self.centralwidget)
        self.proceedButton.setGeometry(QtCore.QRect(750, 500, 112, 34))
        self.proceedButton.setObjectName("proceedButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Quizzes"))
        self.quizLabel.setText(_translate("MainWindow", "Quizzes"))
        self.proceedButton.setText(_translate("MainWindow", "Proceed"))

