import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from user import *

import ipa_chart_soundsFIN as ipa

class FavouriteUI(QWidget):
    def __init__(self, user):
        super(FavouriteUI, self).__init__()
        self.phonemelist = QListWidget()
        self.contentlist = QListWidget()
        self.user = user

        self.phonemestack = []
        self.contentstack = []

        for num in range(len(user.favorites_phoneme)):
            self.addPhonemeFavouriteTab(num, user.favorites_phoneme[num])

        for favcontent in range(10):
            self.addContentFavouriteTab(favcontent, "content" + str(favcontent))

        self.PhonemeStack = QStackedWidget(self)
        self.ContentStack = QStackedWidget(self)

        #for i in range(len(self.leftlist)):
        #    self.PhonemeStack.addWidget(self.phonemestack[i])

        self.ContentStack = QStackedWidget(self)
        #for i in range(len(self.leftlist)):
        #    self.Stack.addWidget(self.contentstack[i])

        windowLayout = QVBoxLayout()

        button = QPushButton("Back")
        button.setFixedSize(100,60)

        windowLayout.addWidget(button)


        self.phonemelist.setFixedSize(300, 400)
        self.contentlist.setFixedSize(300, 400)

        hbox = QHBoxLayout()
        left = QFormLayout()
        right = QFormLayout()

        phonemetitle = QLabel("Favourite Phoneme")
        phonemetitle.setFont(QFont("DIN Alternate", 30, QFont.Bold))
        left.addRow(phonemetitle)

        pronounceButton =QPushButton("Pronounce")
        pronounceButton.clicked.connect(self.pronouncefavouritephoneme)
        pronounceButton.setFixedWidth(100)
        deletePhonemeButton = QPushButton("Delete")
        deletePhonemeButton.clicked.connect(self.deletefavouritephoneme)
        deletePhonemeButton.setFixedWidth(100)

        contenttitle = QLabel("Favourite Content")
        contenttitle.setFont(QFont("DIN Alternate", 30, QFont.Bold))
        right.addRow(contenttitle)

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
        windowLayout.addLayout(hbox)

        self.setLayout(windowLayout)
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
        audioplayer = ipa.AudioPlayer()
        listItems = self.phonemelist.selectedItems()
        if not listItems:
            return
        for item in listItems:
            to_play = item.text()
        audioplayer.play_audio(to_play)

    #Show selected Content
    def readfavouritecontent(self):
        pass

    def deletefavouritephoneme(self):
        listItems = self.phonemelist.selectedItems()
        if not listItems:
            return
        for item in listItems:
            self.phonemelist.takeItem(self.phonemelist.row(item))
        self.user.delFavoritePhoneme(item.text())
        print(self.user.favorites_phoneme)

    def deletefavouritecontent(self):
        listItems = self.contentlist.selectedItems()
        if not listItems: return
        for item in listItems:
            self.contentlist.takeItem(self.contentlist.row(item))

    def display(self, i):
        self.PhonemeStack.setCurrentIndex(i)
        self.ContentStack.setCurrentIndex(i)


def main():
    app = QApplication(sys.argv)
    ex = FavouriteUI(User("A", "B", "C", "1515", "12ABhf--"))
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()

