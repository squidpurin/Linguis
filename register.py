class Register:
    def __init__(self, uid, password, email):
        self.uid = uid
        self.pw = password
        self.email = email
        self.createUser()

    def createUser(self):
        if self.is_duplicate():
            pass
            #loop back
        else:
            #load db user
            ulist = pickle.load(open("userlist.p","rb"))
            new_user = User(self.uid, self.name, self.pw, self.email)
            ulist.append(new_user)
            pickle.dump(ulist, open("userlist.p","wb"))

    def is_duplicate():
        #load db
        ulist = pickle.load(open("userlist.p","rb"))
        for p in uList:
           if p.uid == self.uid:
               return True
        return False
            
