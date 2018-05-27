import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import QtWebEngineWidgets
import sys,os,requests,json
import urllib.parse as urlparse
import ContentList as c
import page as p
import pickle
from user import *


class ContentGUI(QWidget):
    def __init__(self, user_):
        super(ContentGUI,self).__init__()
        self.content = c.ContentCollection()
        self.content.init_pages()
        self.user = user_
        
        layout = QHBoxLayout()
        self.contentlist = QListWidget()

        self.stack = []
        for i in range(len(self.content.content_collection)):
            self.addContentTab(i, self.content.content_collection[i].getPageTitle())
            self.addNewWebpage() #QWidget
            self.stack[i].setLayout(self.createWebView(self.content.content_collection[i].getHTMLFilename()))

        self.Stack = QStackedWidget(self)
        for i in range(len(self.contentlist)):
            self.Stack.addWidget(self.stack[i])
        self.contentlist.setFixedSize(280,545)

        layout.addWidget(self.contentlist)
        #layout.addWidget(self.Stack)

        favouriteButton = QPushButton("Add to favourite")
        favouriteButton.clicked.connect(self.addToFavouriteList)
        favouriteButton.setFixedWidth(200)

        verticalLayout = QVBoxLayout()
        verticalLayout.addWidget(self.Stack)
        verticalLayout.addWidget(favouriteButton)

        self.contentlist.currentRowChanged.connect(self.display)
        layout.addLayout(verticalLayout)

        self.setFixedSize(900, 600)
        layout.setAlignment(Qt.AlignLeft)

        self.setLayout(layout)
        self.setWindowTitle("Contents")
        self.show()

    def addContentTab(self, item_num, name):
        self.contentlist.insertItem(item_num, name)

    #Construct new QWidget in order to add Layout to it
    def addNewWebpage(self):
        tmp = QWidget()
        self.stack.append(tmp)

    def createWebView(self, page):
        layout = QFormLayout()
        webView = QtWebEngineWidgets.QWebEngineView()
        webView.setFixedSize(500,500)
        URL = os.getcwd() + '/htmls/' + page
        print(URL)
        webView.load(QUrl().fromUserInput(URL))
        webView.urlChanged.connect(self.checkURL)

        layout.addRow(webView)
        return layout
    
    def addToFavouriteList(self):
        listItems = self.contentlist.selectedItems()
        if not listItems: return
        for item in listItems:
            favcontent = item.text()
        userTitles = []
        for page in self.user.favorites_content:
            userTitles.append(page.getPageTitle())
        for content in self.content.content_collection:
            if(favcontent == content.getPageTitle() and favcontent not in userTitles):
                self.user.favorites_content.append(content)
        print(self.user.favorites_content)

    
    #Display the question with respect to the question number
    def display(self, i):
        self.Stack.setCurrentIndex(i)

    def checkURL(self):
        url = self.webView.url().toDisplayString()
        data = urlparse.urlparse(url)
        print(data.netloc)
        if (data.netloc == 'localhost'):
            response_data = urlparse.parse_qs(data.query)
            self.getToken(response_data)

def main():
    app = QApplication(sys.argv)
    w = ContentGUI(User("A","B","C","1393","pP1-2222"))
    app.exec_()

if __name__ == '__main__':
    main()
