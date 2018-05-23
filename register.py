import pickle
from user import *
from PasswordVerifier import *

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
                new_user = self.user
                ulist.append(new_user)
                pickle.dump(ulist, open("userlist.p","wb"))
            else:
                print("Object is not User")



    def is_duplicate(self):
        #load db
        uList = pickle.load(open("userlist.p","rb"))
        for p in uList:
           if p.uid == self.username:
               return True
        return False

