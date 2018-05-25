import zipfile
import os, distutils.dir_util

class Updater:
    def __init__(self, mainApp, path):
        #self.mainAppPath = ...........
        self.mainApp = mainApp
        #self.ver = mainApp.ver
        self.path = path
        self.updateable = False

    def closeMainApp(self):
        pass        
        
    def validateApp(self):
        zip_ref = zipfile.ZipFile(self.path, 'r')
        zip_ref.extractall('./update')
        zip_ref.close()
        #check if current version is latest already'
        for d, s, fn in os.walk("./ver"):
            if fname < self.ver:
                self.updateable = True
        #check update validity

    def updateApp(self):
        distutils.dir_util.copy_tree(self.path, self.mainAppPath)
        #remove empty files
        for dirName, subdirList, fileList in os.walk(self.mainAppPath):
            for fname in fileList:
                if os.stat(dirName + "\\" + fname).st_size == 0 && fname[-2:0]:
                    os.remove(dirName + "\\" + fname)
        #delete updater cache
        os.remove(self.path)

    def relaunchApp(self):
        pass
