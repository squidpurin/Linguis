from PasswordVerifier import *
try:
    import IPALab_UI as ipalab
except:
    print("no pyaudio")
import quizList

class User(PasswordVerifier):
    def __init__(self,fname, lname, email, username, password):
        PasswordVerifier.__init__(self)
        self.firstname = fname
        self.lastname = lname
        self.email = email
        self.username = username
        self.password = password
        self.favorites_phoneme = []
        self.favorites_content = []
        self.quizResult = {}
        self.mainUI = None
        self.pageUI = None
        self.quizUI = None #quizList.QuizList(self)
        try:
            self.ipaLabUI = None #ipalab.IPALabUI(self)
        except:
            print("no pyaudio 2")
        self.favUI = None
        self.optionUI = None

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

    def addFavoritePhoneme(self, phoneme):
        self.favorites_phoneme.append(phoneme)

    def delFavoritePhoneme(self, phoneme):
        if phoneme in self.favorites_phoneme:
            self.favorites_phoneme.remove(phoneme)

    def addFavoriteContent(self, page):
        self.favorites_content.append(page)

    def delFavoriteContent(self, page):
        if page in self.favorites_content:
            self.favorites_content.remove(page)

    def getFavoritePhoneme(self):
        return self.favorites_phoneme

    def getFavoriteContent(self):
        return self.favorites_content

    def __str__(self):
        return self.firstname + self.lastname + self.email + self.username + self.password
