import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

import user
import login
import register


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
        self.register = register.Register()


        self.firstname = QLineEdit()
        self.lastname = QLineEdit()
        self.email = QLineEdit()
        self.username = QLineEdit()
        self.password = QLineEdit()
        self.password.setEchoMode(QLineEdit.Password)
        self.confirmedpassword = QLineEdit()
        self.confirmedpassword.setEchoMode(QLineEdit.Password)

        #Registration Title
        flo = QFormLayout()
        Registrationtitle = QLabel("Registration")
        splitter2 = QLabel("-" * 60)
        Registrationtitle.setFont(QFont("Times", 30, QFont.Bold))
        Registrationtitle.setStyleSheet('color: white')
        splitter2.setStyleSheet('color: white')

        flo.addRow(Registrationtitle)
        flo.addRow(splitter2)

        #Firstname
        Label1 = QLabel("{:<33}".format('First name'))
        Label1.setFont(QFont("Helvetica", 15))
        Label1.setStyleSheet('color: white')
        Label1.setAlignment(Qt.AlignLeft)
        flo.addRow(Label1, self.firstname)

        #Lastname
        Label2 = QLabel("{:<32}".format('Last name'))
        Label2.setFont(QFont("Helvetica", 15))
        Label2.setStyleSheet('color: white')
        Label2.setAlignment(Qt.AlignLeft)
        flo.addRow(Label2, self.lastname)

        #Email
        Label3 = QLabel("{:<36}".format('Email'))
        Label3.setFont(QFont("Helvetica", 15))
        Label3.setStyleSheet('color: white')
        Label3.setAlignment(Qt.AlignLeft)
        flo.addRow(Label3, self.email)


        #Username
        Label4 = QLabel("{:<31}".format('Username'))
        Label4.setFont(QFont("Helvetica", 15))
        Label4.setStyleSheet('color: white')
        Label4.setAlignment(Qt.AlignLeft)
        flo.addRow(Label4, self.username)

        #Password
        Label5 = QLabel("{:<32}".format('Password'))
        Label5.setFont(QFont("Helvetica", 15))
        Label5.setStyleSheet('color: white')
        Label5.setAlignment(Qt.AlignLeft)
        flo.addRow(Label5, self.password)

        #Password Confirmation
        Label6 = QLabel("{:<23}".format('Password Confirmation'))
        Label6.setFont(QFont("Helvetica", 15))
        Label6.setStyleSheet('color: white')
        Label6.setAlignment(Qt.AlignLeft)
        flo.addRow(Label6, self.confirmedpassword)

        signupButton = QPushButton("Sign Up")
        signupButton.clicked.connect(self.signup)
        signupButton.setFixedWidth(100)
        flo.addRow(signupButton)

        self.setLayout(flo)
        self.setFixedSize(400, 500)

    def signup(self):
        newuser = user.User(self.firstname.text(), self.lastname.text(),self.email.text(), self.username.text(), self.password.text())
        print(self.firstname.text())
        print(self.confirmedpassword.text())
        if (newuser.PasswordConfirmation(self.confirmedpassword.text())):
            if not(newuser.passwordVerification(self.password.text())):
                print("Warning Message Invalid form of password")
            else:
                self.register.createUser(newuser)
                print("Sign up a user successfully")
        else:
            print("Cannot the password is not the same")


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

        self.username = QLineEdit()
        self.username.setFixedWidth(200)
        self.username.setMaxLength(12)
        self.username.setAlignment(Qt.AlignLeft)
        self.username.setFont(QFont("Helvetica", 12))

        flo.addRow(Label1)
        flo.addRow(self.username)

        # Password
        Label2 = QLabel("{:<7}".format('Password'))
        Label2.setFont(QFont("Helvetica", 15))
        Label2.setStyleSheet('color: black')

        self.password = QLineEdit()
        self.password.setFixedWidth(200)
        self.password.setMaxLength(12)
        self.password.setAlignment(Qt.AlignLeft)
        self.password.setEchoMode(QLineEdit.Password)

        flo.addRow(Label2)
        flo.addRow(self.password)
        self.b1 = QCheckBox("Remember me")
        self.b1.setChecked(False)
        self.b1.stateChanged.connect(lambda: self.Rememberme(self.b1))
        flo.addRow(self.b1)

        signupButton = QPushButton("Login")
        signupButton.setFixedWidth(100)
        flo.addRow(signupButton)

        self.setLayout(flo)

    def Rememberme(self, b):
        ans = b.text()
        if ans == "Remember me":
            if b.isChecked() == True:
                print(ans + " is selected")
            else:
                print(ans + " is deselected")

    def LoginApp(self):
        userlogin  = login.Login(self.username, self.password)
        if(userlogin.match()):
            pass
        else:
            print("Invalid ID or Password")




def main():
    app = QApplication(sys.argv)
    ex = RegistrationUI()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
