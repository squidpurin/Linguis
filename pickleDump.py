import pickle
import user

def initiatePickle(fn):
    pickle.dump([user.User("aca","asc","csac","cscs","ppppppP1")], open(fn, "wb"))

def clearPickle(fn):
    c = pickle.load(open(fn, "rb"))
    initiatePickle(fn)

initiatePickle("userlist.p")
