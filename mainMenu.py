import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from mainAppUI import Ui_MainWindow as Ui
from user import *
from mainAppUI import Ui_MainWindow as Ui

class MainMenu(QMainWindow):
    def __init__(self, user):
        QMainWindow.__init__(self, None)
        self.user = user
        self.ui = Ui()
        self.ui.setupUi()
        self.ui.btn_IPA.clicked.connect(self.user.ipaLabUI.show())
        self.ui.btn_Material.clicked.connect(self.user.pageUI.show())
        self.ui.btn_Quiz.clicked.connect(self.user.quizUI.show())
        self.ui.btn_Favourite.clicked.connect(self.user.favUI.show())
        self.ui.btn_Options.clicked.connect(self.user.helpUI.show())
        self.ui.btn_Quit.clicked.connect(sys.exit())

def main():
    app = QApplication(sys.argv)
    bufferUser = User("A", "B", "C", "12354", "aA7;aaaa")
    w = MainMenu(bufferUser)
    w.show()
    return app.exec_()

if __name__ == "__main__":
    sys.exit(main())