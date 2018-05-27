import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from user import *

import ContentGUI as pgui

import ipa_chart_soundsFIN as ipa

class FavouriteUI(QWidget):
    def __init__(self, user):
        super(FavouriteUI, self).__init__()
        self.phonemelist = QListWidget()
        self.contentlist = QListWidget()
        self.user = user

        for num in range(len(user.favorites_phoneme)):
            self.addPhonemeFavouriteTab(num, user.favorites_phoneme[num])

        for favcontent in range(len(user.favorites_content)):
            self.addContentFavouriteTab(favcontent, user.favorites_content[favcontent].getPageTitle())


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

        self.setLayout(hbox)
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
        listItems = self.contentlist.selectedItems()
        if not listItems:
            return
        for item in listItems:
            to_read = item.text()
        self.hide()
        for i in range(len(self.user.pageUI.contentlist)):
            if self.user.pageUI.contentlist.item(i).text() == to_read:
                self.user.pageUI.contentlist.setCurrentRow(i)
        self.user.pageUI.show()


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
            itemToTake = self.contentlist.takeItem(self.contentlist.row(item)).text()
        for content in self.user.favorites_content:
            if(itemToTake == content.getPageTitle()):
                self.user.delFavoriteContent(content)
        print(self.user.favorites_content)


def main():
    app = QApplication(sys.argv)
    user_ = User("A", "B", "C", "1515", "12ABhf--")
    import page
    page1 = page.Page("00150","Consonants","00150-Consonants.html")
    user_.pageUI = pgui.ContentGUI(user_)
    user_.favorites_content.append(page1)
    ex = FavouriteUI(user_)
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()

