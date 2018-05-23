from PasswordVerifier import *

class User(PasswordVerifier):
    def __init__(self,fname, lname, email, username, password):
        PasswordVerifier.__init__(self)
        self.firstname = fname
        self.lastname = lname
        self.email = email
        self.username = username
        self.password = password

        #self.userData = ...................load userdata
    def getFirstName(self):
        return self.firstname

    def setFirstName(self, fname):
        self.firstname = fname

    def getLastName(self):
        return self.lastname

    def setLastName(self, lname):
        self.lastname = lname

    def getEmail(self):
        return self.email

    def setEmail(self, email):
        self.email = email

    def getUserName(self):
        return self.username

    def setUserName(self, uname):
        self.username = uname

    def getPassword(self):
        return self.password

    def setPassword(self, newPassword):
        self.password = newPassword

    def PasswordConfirmation(self,confirmedpassword):
        if(self.password == confirmedpassword):
            return True
        return False



    
