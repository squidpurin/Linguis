import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from mainAppUI import Ui_MainWindow as Uim
from user import *
import quiz

class MainMenu(QMainWindow):
    def __init__(self, user):
        QMainWindow.__init__(self, None)
        self.user = user
        self.ui = Uim()
        self.ui.setupUi(self)
        self.ui.btn_IPA.clicked.connect(self.user.ipaLabUI.show())
        self.ui.btn_Material.clicked.connect(self.user.pageUI.show())
        self.ui.btn_Quiz.clicked.connect(self.user.quizUI.show())
        self.ui.btn_Favourite.clicked.connect(self.user.favUI.show())
        self.ui.btn_Options.clicked.connect(self.user.helpUI.show())
        self.ui.btn_Quit.clicked.connect(sys.exit())

def main():
    app = QApplication(sys.argv)
    bufferUser = User("A", "B", "C", "12354", "aA7aaa")
    w = MainMenu(bufferUser)
    w.show()
    return app.exec_()

if __name__ == "__main__":
    sys.exit(main())
