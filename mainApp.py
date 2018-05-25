import pickle

class MainApp:
    def __init__(self, user):
        self.user = user

    def addFavorite(self, pid):
        pickle.dump(pid, open("favories.p", "wb"))

    
