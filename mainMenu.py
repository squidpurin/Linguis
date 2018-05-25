import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from mainApp_UI import Ui_MainWindow as Uim
from user import *
import Quiz

class MainMenu(QMainWindow):
    def __init__(self, user):
        QMainWindow.__init__(self, None)
        self.user = user
        self.ui = Uim()
        self.ui.setupUi(self)
        self.ui.btn_IPA.clicked.connect(self.openMenu)
        self.ui.btn_Material.clicked.connect(self.openMenu)
        self.ui.btn_Quiz.clicked.connect(self.openMenu)
        self.ui.btn_Favourite.clicked.connect(self.openMenu)
        self.ui.btn_Options.clicked.connect(self.openMenu)
        self.ui.btn_Quit.clicked.connect(self.openMenu)

    def openMenu(self):
        sender = self.sender().text()
        if sender == "IPA":
            self.user.ipaLabUI.show()
        elif sender == "Material":
            self.user.pageUI.show()
        elif sender == "Quiz":
            self.user.quizUI.show()
        elif sender == "Favourite":
            self.user.favUI.show()
        elif sender == "Option":
            self.user.optionUI.show()
        elif sender == "Quit":
            sys.exit()

def main():
    app = QApplication(sys.argv)
    bufferUser = User("A", "B", "C", "12354", "aA7-=aaa")
    w = MainMenu(bufferUser)
    w.show()
    return app.exec_()

if __name__ == "__main__":
    sys.exit(main())
