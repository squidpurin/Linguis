class Page:
    def __init__(self, pid, title, fn):
        self.pid = pid
        self.title = title
        self.html = fn
    def getPageID(self):
        return self.pid
    def getPageTitle(self):
        return self.title
    def getHTMLFilename(self):
        return self.html
    def __lt__(self, other):
        return self.pid < other.pid