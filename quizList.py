import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from quizList_UI import Ui_MainWindow as Uiq
from user import *
import Quiz as quiz
import Question as question
import QuizGui as qgui

class QuizList(QMainWindow):
    def __init__(self, user):
        QMainWindow.__init__(self, None)
        self.user = user
        self.ui = Uiq()
        self.ui.setupUi(self)
        self.quizzes = parseToQuizzes("quizzes.txt")
        self.subQuiz = None

        #Put all quizzes' name in the list
        count = 0
        for quiz_ in self.quizzes:
            self.ui.quiz_list.insertItem(count, quiz_.id)
            count += 1

        self.ui.proceedButton.clicked.connect(self.openQuiz)

    def openQuiz(self):
        listItems = self.ui.quiz_list.selectedItems()
        if not listItems:
            return
        for item in listItems:
            quiz_text = item.text()
        self.hide()
        for q in self.quizzes:
            if q.id == quiz_text:
                quiz_ = q
        self.subQuiz = qgui.QuizApplication(quiz_, self.user, self)
        self.subQuiz.show()
        

def parseToQuizzes(fn):
    f = open(fn, "r", encoding='utf-8-sig')
    quizzes = []
    for line in f:
        line = line.strip()
        if line == '#':
            pass
            quizzes.append(quiz_)
        elif line.find('%') == -1:
            quiz_ = quiz.Quiz(line)
        else:
            e = line.split('%')
            qname = e[0]
            question_ = e[2]
            if e[3] != 'none':
                if e[1] == 'MultipleChoice':
                    options = e[4].split(',')
                    answer = e[5]
                    s = question.Question(qname, e[1], question_, answer, question.Options(options), e[3])
                else:
                    answer = e[4]
                    s = question.Question(qname, e[1], question_, answer, questionImage = e[3])
            else:
                if e[1] == 'MultipleChoice':
                    options = e[4].split(',')
                    answer = e[5]
                    s = question.Question(qname, e[1], question_, answer, question.Options(options))
                else:
                    answer = e[4]
                    s = question.Question(qname, e[1], question_, answer)
            quiz_.addQuestion(s)
    f.close()
    return quizzes
 
##def main():
##    app = QApplication(sys.argv)
##    bufferUser = User("A", "B", "C", "12354", "aA7;aaaa")
##    w = QuizList(bufferUser)
##    w.show()
##    return app.exec_()
##
##if __name__ == "__main__":
##    sys.exit(main())
