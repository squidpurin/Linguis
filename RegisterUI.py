import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

import user
import login
import register
import pickle

class RegistrationUI(QWidget):
    def __init__(self):
        super(RegistrationUI, self).__init__()

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

        image = QPixmap("SEP_Images/logo/Linguis_Logo_F_T.png")
        pic = QLabel()

        width = 200
        height = image.scaledToWidth(width).height()

        pic.setPixmap(image.scaledToWidth(width))
        pic.setFixedSize(width, height)

        windowLayout.addWidget(pic)
        windowLayout.addWidget(self.horizontalGroupBox)
        self.setLayout(windowLayout)

    def closeEvent( self, event ):
        reply = QMessageBox.question( self, 'Message', "Are you sure to quit?", QMessageBox.Yes,
                                      QMessageBox.No )
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

class RegistrationWidget(QWidget):
    def __init__(self, parent = None):
        super(RegistrationWidget, self).__init__(parent)
        self.register = register.Register()

        #Attribuites for all information added to user registration
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
        Registrationtitle.setFont(QFont("DIN Alternate", 30, QFont.Bold))
        Registrationtitle.setStyleSheet('color: black')
        splitter2.setStyleSheet('color: black')

        flo.addRow(Registrationtitle)
        flo.addRow(splitter2)

        #Firstname
        Label1 = QLabel("{:<33}".format('First name'))
        Label1.setFont(QFont("Helvetica", 15))
        Label1.setStyleSheet('color: black')
        Label1.setAlignment(Qt.AlignLeft)
        flo.addRow(Label1, self.firstname)

        #Lastname
        Label2 = QLabel("{:<32}".format('Last name'))
        Label2.setFont(QFont("Helvetica", 15))
        Label2.setStyleSheet('color: black')
        Label2.setAlignment(Qt.AlignLeft)
        flo.addRow(Label2, self.lastname)

        #Email
        Label3 = QLabel("{:<36}".format('Email'))
        Label3.setFont(QFont("Helvetica", 15))
        Label3.setStyleSheet('color: black')
        Label3.setAlignment(Qt.AlignLeft)
        flo.addRow(Label3, self.email)

        #Username
        Label4 = QLabel("{:<31}".format('Username'))
        Label4.setFont(QFont("Helvetica", 15))
        Label4.setStyleSheet('color: black')
        Label4.setAlignment(Qt.AlignLeft)
        flo.addRow(Label4, self.username)

        #Password
        Label5 = QLabel("{:<32}".format('Password'))
        Label5.setFont(QFont("Helvetica", 15))
        Label5.setStyleSheet('color: black')
        Label5.setAlignment(Qt.AlignLeft)
        flo.addRow(Label5, self.password)

        #Password Confirmation
        Label6 = QLabel("{:<23}".format('Password Confirmation'))
        Label6.setFont(QFont("Helvetica", 15))
        Label6.setStyleSheet('color: black')
        Label6.setAlignment(Qt.AlignLeft)
        flo.addRow(Label6, self.confirmedpassword)

        #Sign up button
        signupButton = QPushButton("Sign Up")
        signupButton.clicked.connect(self.signup)
        signupButton.setFixedWidth(100)
        flo.addRow(signupButton)

        self.setLayout(flo)
        self.setFixedSize(400, 500)

    #Add user profile into the pickledb system
    def signup(self):
        newuser = user.User(self.firstname.text(), self.lastname.text(),self.email.text(), self.username.text(), self.password.text())
        if(self.firstname.text() != "" or self.lastname.text() != "" or self.email.text() != ""
                or self.username.text() != "" or self.password.text() != "" or self.confirmedpassword.text() != ""):
            if (newuser.PasswordConfirmation(self.confirmedpassword.text())):
                print(newuser.passwordVerification(self.password.text()))
                if (newuser.passwordVerification(self.password.text())):
                    self.register.createUser(newuser)
                    print("Sign up a user successfully")
                    succ = QMessageBox()
                    succ.setIcon(QMessageBox.Warning)
                    succ.setText("Signed up successfully")
                    succ.setStandardButtons(QMessageBox.Ok)
                    succ.exec_()
                else:
                    self.NotifyInvalidPasswordForm()
                    print("Warning Message Invalid form of password")
            else:
                self.NotifyUnmatchedPassword()
                print("Cannot the password is not the same")
        else:
            self.NotifyImproperRegistration()

    #Notify invalid password
    def NotifyUnmatchedPassword(self):
        invalid_box = QMessageBox()
        invalid_box.setIcon(QMessageBox.Warning)
        invalid_box.setText("Invalid Password")
        invalid_box.setInformativeText("Unmatched Password")
        invalid_box.setStandardButtons(QMessageBox.Ok)
        invalid_box.exec_()

    #Notify invalid password form
    def NotifyInvalidPasswordForm(self):
        invalid_box = QMessageBox()
        invalid_box.setIcon(QMessageBox.Warning)
        invalid_box.setText("Password Verification")
        invalid_box.setInformativeText("Password must contain at least 1 capital letter, and 1 number")
        invalid_box.setStandardButtons(QMessageBox.Ok)
        invalid_box.exec_()

    def NotifyImproperRegistration(self):
        invalid_box = QMessageBox()
        invalid_box.setIcon(QMessageBox.Warning)
        invalid_box.setText("Registration Failure")
        invalid_box.setInformativeText("Please fill in further information")
        invalid_box.setStandardButtons(QMessageBox.Ok)
        invalid_box.exec_()

class LoginWidget(QWidget):
    def __init__(self, parent=None):
        super(LoginWidget, self).__init__(parent)

        flo = QFormLayout()

        Logintitle = QLabel("Login")
        splitter1 = QLabel("-" * 60)
        Logintitle.setFont(QFont("DIN Alternate", 30, QFont.Bold))
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

        try: 
            [un, pw] = pickle.load(open("rememberme.p", "rb")) 
            self.username.setText(un) 
            self.password.setText(pw) 
            pickle.dump([un, pw], open("rememberme.p", "wb"))
            self.b1.setChecked(True)
        except:
            print("No remember data")
            
        signinButton = QPushButton("Login")
        signinButton.clicked.connect(self.LoginApp)
        signinButton.setFixedWidth(100)
        flo.addRow(signinButton)

        self.setLayout(flo)

    #Method called after click radioButton Remember me
    def Rememberme(self, b):
        ans = b.text()
        if ans == "Remember me":
            if b.isChecked() == True:
                print(ans + " is selected")
            else:
                print(ans + " is deselected")

    #Login Appplication
    def LoginApp(self):
        self.userlogin  = login.Login(self.username, self.password)
        print(self.userlogin.match())
        if(self.userlogin.match() != False):
            #Switch to other pages
            #test showing the messagebox
            self.NotifyValidUserPassword()
            if self.b1.isChecked() == True: 
                try: 
                    pickle.dump([self.username.text(), self.password.text()], open("rememberme.p", "wb")) 
                except: 
                    print("Pickle error")
            else:
                try: 
                    pickle.dump([], open("rememberme.p", "wb")) 
                except: 
                    print("Pickle error")
            self.userlogin.openApp()
        else:
            #In case that the password is invalid
            self.NotifyInvalidUserPassword()
            #print("Invalid ID or Password")

    #Information box display when invalid username or password
    def NotifyInvalidUserPassword(self):
        invalid_box = QMessageBox()
        invalid_box.setIcon(QMessageBox.Information)
        invalid_box.setText("Login Failure")
        invalid_box.setInformativeText("Invalid username or password")
        invalid_box.setStandardButtons(QMessageBox.Ok)
        invalid_box.exec_()

    def NotifyValidUserPassword(self):
        invalid_box = QMessageBox()
        invalid_box.setIcon(QMessageBox.Information)
        invalid_box.setText("Login Successful.")
        invalid_box.setInformativeText("Welcome to Linguis!")
        invalid_box.setStandardButtons(QMessageBox.Ok)
        invalid_box.exec_()

def main():
    app = QApplication(sys.argv)
    ex = RegistrationUI()
    ex.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
