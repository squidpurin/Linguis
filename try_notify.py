import pickle
from reportFIN import *

users = pickle.load(open('userlist.p', "rb"))
for user in users:
    print(user.email)
    s = Reporter(self.user)
    s.report("")
