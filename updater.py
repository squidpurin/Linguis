import zipfile
import os, distutils.dir_util
import shutil

class Updater:
    def __init__(self, path):
        version_file = open("version.v","r")
        self.ver = int(version_file.read())
        version_file.close()
        self.path = path
        self.updateable = False
        
    def validateApp(self):
        try:
            print(self.path)
            zip_ref = zipfile.ZipFile(self.path, 'r')
            zip_ref.extractall('./update')
            zip_ref.close()
            #check if current version is latest already'
            version_file = open("./update/version.v","r")
            updater_file_ver = int(version_file.read())
            version_file.close()
            if updater_file_ver > self.ver:
                self.updateable = True
                return 1
            else:
                print("Linguis is already in the latest version")
                return 0                
        except:
            print("Invalid updater package.")
            return -1
        
    def updateApp(self):
        if self.updateable == True:
            distutils.dir_util.copy_tree("./update", "./")
            #remove empty files
            for dirName, subdirList, fileList in os.walk("./"):
                for fname in fileList:
                    if os.stat(dirName + "\\" + fname).st_size == 0 and fname[-2:0]:
                        os.remove(dirName + "\\" + fname)
            #delete updater cache
            shutil.rmtree("./update")
            return True
        return False
        
def main():
    u = Updater("E:\\Studium\\Universitat\\2018-1\\SEP\\s9\\version.zip")
    u.updateApp()
