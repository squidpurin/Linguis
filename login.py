import mainApp as ma
import pickle
from PasswordVerifier import *
from mainMenu import *

class Login(PasswordVerifier):
    def __init__(self, uid, password):
        PasswordVerifier.__init__(self)
        self.username = uid
        self.password = password
        #import uList
        self.uList = pickle.load(open("userlist.p","rb"))
        self.mainApp = None
        self.openApp()

    def match(self):
        for p in self.uList:
            if (p.getUserName() == self.username) and (p.getPassword() == self.password):
                return True
        return False

    def openApp(self):
        if self.match():
            self.mainApp = ma.MainApp(self.uid)
        else:
            pass #loop back

    
