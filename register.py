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
            new_user = User(self.uid, self.name, self.pw, self.email)
            #save to db

    def is_duplicate():
        #load db
        for p in uList:
           if p.uid == self.uid:
               return True
        return False
            
