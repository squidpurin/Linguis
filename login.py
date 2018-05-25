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
        self.openApp()

    def match(self):
        for p in self.uList:
            if (p.getUserName() == self.username) and (p.getPassword() == self.password):
                self.user = p
                return True
        return False

    def openApp(self):
        if self.match():
            self.mainApp = ma.MainApp(self.user)
        else:
            pass #loop back

    
