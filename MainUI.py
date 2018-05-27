import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

QApplication.setAttribute(Qt.AA_EnableHighDpiScaling, True)

class MainUI(QWidget):
    def __init__(self):
        super(MainUI, self).__init__()

        # p = self.palette()
        # p.setColor(self.backgroundRole(), QColor("#A9E3FF"))
        # self.setPalette(p)

        self.setWindowTitle("Main Menu")
        self.setFixedSize(900,600)

        windowLayout = QHBoxLayout()

        # ------------------------------------------------------#

        image = QPixmap("SEP_Images/logo/Linguis_Logo_F_T.png")
        pic = QLabel()

        width = 500
        height = image.scaledToWidth(width).height()

        pic.setPixmap(image.scaledToWidth(width))
        pic.setFixedSize(width, height)
        pic.setAlignment(Qt.AlignCenter)
        windowLayout.addWidget(pic)

        # ------------------------------------------------------#
        # Buttons

        self.mainButtonLayout = QHBoxLayout()
        btn_IPA = QPushButton( 'IPA', self )
        self.mainButtonLayout.addWidget( btn_IPA )

        # ------------------------------------------------------#


        self.setLayout(windowLayout)

        self.show()

class MainButtonWidget(QWidget):
    def __init__(self, parent = None):
        super(MainButtonWidget, self).__init__(parent)



def main():
    app = QApplication(sys.argv)
    ex = MainUI()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
