import pickle

class MainApp:
    def __init__(self, uid):
        self.userId = uid

    def addFavorite(self, pid):
        pickle.dump(pid, open("favories.p", "wb"))

    
