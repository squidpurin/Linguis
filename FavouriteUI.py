import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class FavouriteUI(QWidget):
    def __init__(self):
        super(FavouriteUI, self).__init__()
        self.phonemelist = QListWidget()
        self.contentlist = QListWidget()

        self.phonemestack = []
        self.contentstack = []

        #for favphoneme in phonemelist:
        #   pass

        #for favcontent in contentlist:
        #    pass

        self.PhonemeStack = QStackedWidget(self)
        self.ContentStack = QStackedWidget(self)

        #for i in range(len(self.leftlist)):
        #    self.PhonemeStack.addWidget(self.phonemestack[i])

        self.ContentStack = QStackedWidget(self)
        #for i in range(len(self.leftlist)):
        #    self.Stack.addWidget(self.contentstack[i])

        self.phonemelist.setFixedSize(300, 400)
        self.contentlist.setFixedSize(300, 400)

        hbox = QHBoxLayout(self)
        left = QFormLayout(self)
        right = QFormLayout(self)

        phonemetitle = QLabel("Favourite Phoneme")
        splitter1 = QLabel("-" * 60)
        phonemetitle.setFont(QFont("Times", 30, QFont.Bold))
        left.addRow(phonemetitle)
        left.addRow(splitter1)

        pronounceButton =QPushButton("Pronounce")
        pronounceButton.clicked.connect(self.pronouncefavouritephoneme)
        pronounceButton.setFixedWidth(100)
        deletePhonemeButton = QPushButton("Delete")
        deletePhonemeButton.clicked.connect(self.deletefavouritephoneme)
        deletePhonemeButton.setFixedWidth(100)



        contenttitle = QLabel("Favourite Content")
        splitter2 = QLabel("-" * 60)
        contenttitle.setFont(QFont("Times", 30, QFont.Bold))
        right.addRow(contenttitle)
        right.addRow(splitter2)

        readButton = QPushButton("Read")
        readButton.clicked.connect(self.readfavouritecontent)
        readButton.setFixedWidth(100)
        deleteFavouriteContentButton =QPushButton("Delete")
        deleteFavouriteContentButton.clicked.connect(self.deletefavouritecontent)
        deleteFavouriteContentButton.setFixedWidth(100)

        left.addRow(self.phonemelist)
        left.addRow(pronounceButton, deletePhonemeButton)


        right.addRow(self.contentlist)
        right.addRow(readButton, deleteFavouriteContentButton)

        hbox.addLayout(left)
        hbox.addLayout(right)

        self.setLayout(hbox)
        self.phonemelist.currentRowChanged.connect(self.display)
        self.contentlist.currentRowChanged.connect(self.display)
        self.setFixedSize(900, 600)
        self.setWindowTitle('Favourite')
        self.show()

    def addPhonemeFavouriteTab(self, item_num, name):
        self.phonemelist.insertItem(item_num, name)

    def addContentFavouriteTab(self, item_num, name):
        self.contentlist.insertItem(item_num, name)

    def pronouncefavouritephoneme(self):
        pass

    def readfavouritecontent(self):
        pass

    def deletefavouritephoneme(self):
        pass

    def deletefavouritecontent(self):
        pass

    def display(self, i):
        self.PhonemeStack.setCurrentIndex(i)
        self.ContentStack.setCurrentIndex(i)
def main():
    app = QApplication(sys.argv)
    ex = FavouriteUI()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()

