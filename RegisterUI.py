import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


class RegistrationUI(QWidget):
    def __init__(self):
        super(RegistrationUI, self).__init__()
        p = self.palette()
        p.setColor(self.backgroundRole(), QColor("#A9E3FF"))
        self.setPalette(p)

        self.setWindowTitle("Login and Registration")
        self.setFixedSize(900,600)

        self.horizontalGroupBox = QGroupBox()

        layout = QHBoxLayout()
        #------------------------------------------------------#

        #Login Part
        self.loginLayout = QFormLayout()
        loginpage = LoginWidget()
        loginpage.setGeometry(0,0,400,600)

        self.loginLayout.addRow(loginpage)
        layout.addLayout(self.loginLayout)

        #------------------------------------------------------#
        #Registration Part
        self.registrationLayout = QFormLayout()
        registrationpage = RegistrationWidget()
        registrationpage.setGeometry(450, 0, 400, 600)
        self.registrationLayout.addRow(registrationpage)
        layout.addLayout(self.registrationLayout)

        # ------------------------------------------------------#
        self.horizontalGroupBox.setLayout(layout)
        windowLayout = QVBoxLayout()


        image = QPixmap("SEP_Images/speech_organ.jpg")
        pic = QLabel()
        width = 300
        height = image.scaledToWidth(width).height()
        pic.setPixmap(image.scaledToWidth(width))
        pic.setFixedSize(width, height)
        windowLayout.addWidget(pic)

        windowLayout.addWidget(self.horizontalGroupBox)
        self.setLayout(windowLayout)

        self.show()

class RegistrationWidget(QWidget):
    def __init__(self, parent = None):
        super(RegistrationWidget, self).__init__(parent)

        e1 = QLineEdit()
        e2 = QLineEdit()

        flo = QFormLayout()
        Registrationtitle = QLabel("Registration")
        splitter2 = QLabel("-" * 60)
        Registrationtitle.setFont(QFont("Times", 30, QFont.Bold))
        Registrationtitle.setStyleSheet('color: white')
        splitter2.setStyleSheet('color: white')

        flo.addRow(Registrationtitle)
        flo.addRow(splitter2)

        Label1 = QLabel("{:<33}".format('First name'))
        Label1.setFont(QFont("Helvetica", 15))
        Label1.setStyleSheet('color: white')
        Label1.setAlignment(Qt.AlignLeft)

        Label2 = QLabel("{:<32}".format('Last name'))
        Label2.setFont(QFont("Helvetica", 15))
        Label2.setStyleSheet('color: white')
        Label2.setAlignment(Qt.AlignLeft)

        flo.addRow(Label1, e1)
        flo.addRow(Label2, e2)

        e3 = QLineEdit()
        Label3 = QLabel("{:<36}".format('Email'))
        Label3.setFont(QFont("Helvetica", 15))
        Label3.setStyleSheet('color: white')
        Label3.setAlignment(Qt.AlignLeft)
        flo.addRow(Label3, e3)

        e4 = QLineEdit()
        Label4 = QLabel("{:<31}".format('Username'))
        Label4.setFont(QFont("Helvetica", 15))
        Label4.setStyleSheet('color: white')
        Label4.setAlignment(Qt.AlignLeft)
        flo.addRow(Label4, e4)

        e5 = QLineEdit()
        e5.setEchoMode(QLineEdit.Password)
        Label5 = QLabel("{:<32}".format('Password'))
        Label5.setFont(QFont("Helvetica", 15))
        Label5.setStyleSheet('color: white')
        Label5.setAlignment(Qt.AlignLeft)
        flo.addRow(Label5, e5)

        e6 = QLineEdit()
        e6.setEchoMode(QLineEdit.Password)
        Label6 = QLabel("{:<23}".format('Password Confirmation'))
        Label6.setFont(QFont("Helvetica", 15))
        Label6.setStyleSheet('color: white')
        Label6.setAlignment(Qt.AlignLeft)
        flo.addRow(Label6, e6)

        signupButton = QPushButton("Sign Up")
        signupButton.setFixedWidth(100)
        flo.addRow(signupButton)

        self.setLayout(flo)

        self.setFixedSize(400, 500)

class LoginWidget(QWidget):
    def __init__(self, parent=None):
        super(LoginWidget, self).__init__(parent)

        flo = QFormLayout()

        Logintitle = QLabel("Login")
        splitter1 = QLabel("-" * 60)
        Logintitle.setFont(QFont("Times", 30, QFont.Bold))
        flo.addRow(Logintitle)
        flo.addRow(splitter1)

        # Username
        Label1 = QLabel("{:<7}".format('Username'))
        Label1.setFont(QFont("Helvetica", 15))
        Label1.setStyleSheet('color: black')

        e1 = QLineEdit()
        e1.setFixedWidth(200)
        e1.setMaxLength(12)
        e1.setAlignment(Qt.AlignLeft)
        e1.setFont(QFont("Helvetica", 12))

        flo.addRow(Label1)
        flo.addRow(e1)

        # Password
        Label2 = QLabel("{:<7}".format('Password'))
        Label2.setFont(QFont("Helvetica", 15))
        Label2.setStyleSheet('color: black')

        e2 = QLineEdit()
        e2.setFixedWidth(200)
        e2.setMaxLength(12)
        e2.setAlignment(Qt.AlignLeft)
        e2.setEchoMode(QLineEdit.Password)

        flo.addRow(Label2)
        flo.addRow(e2)
        self.b1 = QCheckBox("Remember me")
        self.b1.setChecked(False)
        self.b1.stateChanged.connect(lambda: self.btnstate(self.b1))
        flo.addRow(self.b1)

        signupButton = QPushButton("Login")
        signupButton.setFixedWidth(100)
        flo.addRow(signupButton)

        self.setLayout(flo)

    def btnstate(self, b):
        ans = b.text()
        if ans == "Remember me":
            if b.isChecked() == True:
                print(ans + " is selected")
            else:
                print(ans + " is deselected")



def main():
    app = QApplication(sys.argv)
    ex = RegistrationUI()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()