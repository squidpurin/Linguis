import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from mainAppUI import Ui_MainWindow as Ui
from user import *

class MainMenu(QMainWindow):
    def __init__(self, user):
        QMainWindow.__init__(self, None)
        self.user = user
