import pickle
from user import *
from PasswordVerifier import *
from reportFIN import *

class Register(PasswordVerifier):
    def __init__(self):
        PasswordVerifier.__init__(self)
        self.user = None

    def createUser(self,user):
        self.user = user
        if self.is_duplicate():
            pass
            #loop back
        else:
            #load db user
            print(type(self.user))
            if(type(self.user) == User):
                ulist = pickle.load(open("userlist.p","rb"))
                ulist.append(self.user)
                pickle.dump(ulist, open("userlist.p", "wb"))
                print(398274)
                s = Reporter(self.user)
                print(19283)
                s.report("Registered")
                print(28274)
                s = Notifier(self.user)
                print(888)
                s.notify("Thank you for registering Linguis!")
                print(927)
                
            else:
                print("Object is not User")

    def is_duplicate(self):
        #load db
        uList = pickle.load(open("userlist.p","rb"))
        for p in uList:
           if p.username == self.user.username:
               return True
        pickle.dump(uList, open("userlist.p","wb"))
        return False

def main():
    h = Register()
    h.createUser(User("babi", "khinzir", "c.dswibowo@yahoo.com.tw", "1337", "abcd0AVC"))
