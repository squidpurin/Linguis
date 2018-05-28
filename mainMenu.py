import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

from mainApp_UI import Ui_MainWindow as Uim
from user import *
import Quiz
import IPALab_UI as ipalab
import ContentGUI as pgui
import quizList as qlst
import FavouriteUI as fvui
import optionMenu as opui
import pickle


class MainMenu( QMainWindow ):
    def __init__( self, user_ ):
        QMainWindow.__init__( self, None )
        self.user = user_
        self.ui = Uim()
        self.ui.setupUi( self )
        self.ui.btn_IPA.clicked.connect( self.openMenu )
        self.ui.btn_Material.clicked.connect( self.openMenu )
        self.ui.btn_Quiz.clicked.connect( self.openMenu )
        self.ui.btn_Favourite.clicked.connect( self.openMenu )
        self.ui.btn_Options.clicked.connect( self.openMenu )
        self.ui.btn_Quit.clicked.connect( self.openMenu )
        self.show()

    def openMenu( self ):
        sender = self.sender().text()
        if sender == "IPA":
            self.user.ipaLabUI = ipalab.IPALabUI( self.user )
            self.user.ipaLabUI.show()
        elif sender == "Material":
            self.user.pageUI = pgui.ContentGUI( self.user )
            self.user.pageUI.show()
        elif sender == "Quiz":
            self.user.quizUI = qlst.QuizList( self.user )
            self.user.quizUI.show()
        elif sender == "Favourite":
            self.user.favUI = fvui.FavouriteUI( self.user )
            self.user.favUI.show()
        elif sender == "Options":
            self.user.optionUI = opui.OptionMenuUI( self.user )
            self.user.optionUI.show()
        elif sender == "Quit":
            self.quitUtility()

    def quitUtility( self ):
        userList = pickle.load( open( "userlist.p", "rb" ) )
        self.user.mainUI = None
        self.user.pageUI = None
        self.user.quizUI = None
        self.user.ipaLabUI = None
        self.user.favUI = None
        self.user.optionUI = None
        #print( userList )
        for _user in userList:
            if self.user.username == _user.username:
                userList.remove( _user )
                userList.append( self.user )
        try:
            pickle.dump( userList, open( "userlist.p", "wb" ) )
        except Exception as ex:
            template = "An exception of type {0} occurred. Arguments:\n{1!r}"
            message = template.format( type( ex ).__name__, ex.args )
            #print( message )
        self.hide()

    def closeEvent( self, event ):
        reply = QMessageBox.question( self, 'Message', "Are you sure to quit?", QMessageBox.Yes,
                                      QMessageBox.No )
        if reply == QMessageBox.Yes:
            self.quitUtility()
            event.accept()
        else:
            event.ignore()


##def main():
##    app = QApplication( sys.argv )
##    bufferUser = User( "A", "B", "C", "12354", "aA7-=aaa" )
##    w = MainMenu( bufferUser )
##    w.show()
##    return app.exec_()
##
##
##if __name__ == "__main__":
##    sys.exit( main() )
