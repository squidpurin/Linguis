import sys, os
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from updater_UI import Ui_MainWindow as Uiu
import updater as updater_

class UpdaterUI(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self, None)
        self.ui = Uiu()
        self.ui.setupUi(self)
        self.ui.searchButton.clicked.connect(self.getUpdateFileName)
        self.updaterLoc = None
        self.updater = None
        self.ui.updateButton.clicked.connect(self.updateFirmware)

    def getUpdateFileName(self):
        try:
            fn = QFileDialog.getOpenFileName(self, 'Open file', os.getcwd(),"Zip file (*.zip)")
            self.updaterLoc = fn[0]
        except:
            print("No file selected.")
        if self.updaterLoc != None:
            self.ui.pathField.setText(self.updaterLoc)
            self.updater = updater_.Updater(self.updaterLoc)
            self.ui.pathField.setText(self.updaterLoc)

    def updateFirmware(self):
        self.updaterLoc = self.ui.pathField.text()
        if self.updaterLoc != None:
            self.updater = updater_.Updater(self.updaterLoc)
            stat = self.updater.validateApp()
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setStandardButtons(QMessageBox.Ok)
            if stat == 1:
                self.updater.updateApp()
                msg.setText("Linguis is updated to version "+ str(self.))
                msg.setWindowTitle("Updated.")
            elif stat == 0:
                msg.setText("Linguis is already in the latest version.")
                msg.setWindowTitle("Not updated.")
            else:
                msg.setText("Invalid installer package")
                msg.setWindowTitle("Not updated.")
            msg.exec_()
                
def main():
    app = QApplication(sys.argv)
    u = UpdaterUI()
    u.show()
    return app.exec_()
