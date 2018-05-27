import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from optMenu_UI import Ui_OptionsMenu as Uio
import reportFIN as rep

import user

class OptionMenuUI(QMainWindow):
    def __init__(self, user_):
        QMainWindow.__init__(self, None)
        self.user = user_
        self.ui = Uio()
        self.ui.setupUi(self)

        version_file = open("version.v", "r")
        ver = version_file.read()
        version_file.close()
        
        self.ui.firstName.setText(self.user.firstname)
        self.ui.lastName.setText(self.user.lastname)
        self.ui.userName.setText(self.user.username)
        self.ui.userEmail.setText(self.user.email)
        self.ui.versionNum.setText(ver)
        self.ui.quizRes.setText(self.user.getQuizResults())
        help_file = open("./helpfile.txt", "r")
        self.ui.helpText.setText(help_file.read())
        help_file.close()
        
        self.reporter = rep.Reporter(self.user)
        self.ui.sendButton.clicked.connect(self.reportSend)

    def reportSend(self):
        repmessage = self.ui.messageReport.text()
        self.ui.messageReport.setText('')
        self.reporter.report(repmessage)
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText("Report sent.")
        msg.setWindowTitle("")
        msg.setStandardButtons(QMessageBox.Ok)
        retval = msg.exec_()

def main():
    app = QApplication(sys.argv)
    user_k = user.User("A","A","c.dswibowo@yahoo.com.tw","BB","11PPp-pp")
    user_k.quizResult.append(["1",5])
    ex = OptionMenuUI(user_k)
    ex.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
