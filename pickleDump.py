import pickle
import user

def initiatePickle(fn):
    pickle.dump([], open(fn, "wb"))

def clearPickle(fn):
    c = pickle.load(open(fn, "rb"))
    initiatePickle(fn)

initiatePickle("userlist.p")
