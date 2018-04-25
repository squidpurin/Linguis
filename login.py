import mainApp as ma
class Login:
    def __init__(self, uid, password):
        self.uid = uid
        self.pw = password
        #import uList
        self.uList = None #put uList here
        self.mainApp = None
        self.openApp()

    def match(self):
        for p in in uList:
            if p.uid = self.uid and p.pw = self.pw
                return true
        pass

    def openApp(self):
        if self.match():
            self.mainApp = ma.MainApp(self.uid)
        else:
            pass #loop back
        

    
