import sys, os
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from updater_UI import Ui_MainWindow as Uiu

class UpdaterUI(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self, None)
        self.ui = Uiu()
        self.ui.setupUi(self)
        self.ui.searchButton.clicked.connect(self.getUpdateFileName)
        self.updaterLoc = None

    def getUpdateFileName(self):
        try:
            fn = QFileDialog.getOpenFileName(self, 'Open file', os.getcwd(),"Rar(*.rar)")
            self.updaterLoc = fn[0]
        except:
            print("No file selected.")
        print(self.updaterLoc)
        if self.updaterLoc != None:
            self.pathField.setText(self.updaterLoc)

def main():
    app = QApplication(sys.argv)
    u = UpdaterUI()
    u.show()
    return app.exec_()

main()
