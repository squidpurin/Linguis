import mainMenu as ma
import pickle
from PasswordVerifier import *
from mainMenu import *

class Login(PasswordVerifier):
    def __init__(self, uid, password):
        PasswordVerifier.__init__(self)
        self.username = uid
        self.user = None
        self.password = password
        #import uList
        self.uList = pickle.load(open("userlist.p","rb"))
        self.mainApp = None

    def match(self):
        for p in self.uList:
            print(p.getUserName(), self.username.text())
            if (p.getUserName() == self.username.text()) and (p.getPassword() == self.password.text()):
                self.user = p
                return self.user
        return False

    def openApp(self):
        if self.match() != False:
            self.mainApp = ma.MainMenu(self.user)
        else:
            pass #loop back

    
