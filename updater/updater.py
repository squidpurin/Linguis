import zipfile

class Updater:
    def __init__(self, mainApp, path):
        self.mainApp = mainApp
        #self.ver = mainApp.ver
        self.path = path

    def closeMainApp(self):
        pass        
        
    def validateApp(self):
        zip_ref = zipfile.ZipFile(self.path, 'r')
        zip_ref.extractall('./update')
        zip_ref.close()
        #check if current version is latest already
        #etc

    def updateApp(self):
        pass
        #copy/overwrite/delete files
        #delete updater cache

    def relaunchApp(self):
        pass
        
