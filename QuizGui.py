import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from QuestionType import *
import Question as question
import Quiz as quiz
import UserAnswer as userAnswer
import QAPair as qapair
import QuizEvaluator as evaluator
from quizList import *
import pickle
from user import *

class QuizApplication(QWidget):
    def __init__(self, quiz_, user, parent = None):
        super(QuizApplication, self).__init__()
        self.leftlist = QListWidget()

        self.stack = []
        self.user = user
        self.quiz = quiz_
        self.parent = parent

        self.useranswer = userAnswer.UserAnswerList(1)
        self.quizEvaluator = evaluator.QuizEvaluator(self.useranswer, self.quiz)

        #Layouting and creating question tabs
        for i in range(self.quiz.getSize()):
            self.addQuestionTab(i, self.quiz.questions[i].questionID)
            self.addNewQuestion() #QWidget
            if self.quiz.questions[i].getQuestionType() == "MultipleChoice":
                self.stack[i].setLayout(self.CreateMultipleChoiceQuestion(self.quiz.questions[i]))
            elif self.quiz.questions[i].getQuestionType() == "TrueFalse":
                self.stack[i].setLayout(self.CreateTrueFalseQuestion(self.quiz.questions[i]))
            elif self.quiz.questions[i].getQuestionType() == "Fill":
                self.stack[i].setLayout(self.CreateFillInAnswerQuestion(self.quiz.questions[i]))

        #Create a StackWidget containing each QWidget in each tab
        self.Stack = QStackedWidget(self)
        for i in range(len(self.leftlist)):
            self.Stack.addWidget(self.stack[i])

        #Create fixed size of tab
        self.leftlist.setFixedSize(100, 500)
        #Add both tab and question to the page
        hbox = QHBoxLayout(self)
        hbox.addWidget(self.leftlist)
        hbox.addWidget(self.Stack)

        #Create Submit Button
        confirmbtn = QPushButton('Submit')
        confirmbtn.clicked.connect(self.submitAnswer)

        #Create Exit Button
        exitbtn = QPushButton('Quit quiz')
        exitbtn.clicked.connect(self.exitQuiz)

        vbox = QVBoxLayout(self)
        hbox.addLayout(vbox)
        vbox.addWidget(confirmbtn)
        vbox.addWidget(exitbtn)

        #Create the layout
        self.setLayout(hbox)
        self.leftlist.currentRowChanged.connect(self.display)
        self.setFixedSize(900, 600)
        self.setWindowTitle('Quiz Demo')

        self.show()

    #Display the question with respect to the question number
    def display(self, i):
        self.Stack.setCurrentIndex(i)

    def clearAnswerList(self):
        del self.useranswer.getAnswerList()[:]

    #Get All studentAnswer and return
    def getAllStudentAnswer(self):
        self.clearAnswerList()
        for i in range(len(self.stack)):
            widgetitem = self.stack[i].layout().itemAt(0).widget()
            if (widgetitem.getClass() == 'FillTheWord'):
                questionpair = qapair.QAPair(widgetitem.getQuestion(),str(widgetitem.getuseranswer().text()))
                self.useranswer.addAnswer(questionpair)
            else:
                questionpair = qapair.QAPair(widgetitem.getQuestion(),str(widgetitem.getuseranswer()))
                self.useranswer.addAnswer(questionpair)
        return self.useranswer.getAnswerList()

    #Method called after submit the answer
    def submitAnswer(self):
        self.getAllStudentAnswer()
        if not(self.isAllQuestionCompleted()):
            self.NotifyIncompleteMessage()
            self.showIncompleteQuestion()
        self.showFinalResult()
        print(self.quizEvaluator.getFinalScore())

    #Classify correct and wrong question
    def showFinalResult(self):
        elem = 0
        self.quizEvaluator.getCorrectAnswer()
        for question in self.quiz.getQAList():
            item = self.leftlist.item(elem)
            for result in self.useranswer.getAnswerList():
                if question.getQuestion() == result.getQuestion():
                    if not(question.getAnswer() == result.getAnswer()):
                        if (isinstance(item, QListWidgetItem)):
                            self.markAsInvalid(item)
                    else:
                        if(isinstance(item, QListWidgetItem)):
                            self.markAsCorrect(item)
            elem += 1

        result = self.quizEvaluator.getFinalScore()
        self.quizEvaluator.setFinalScore(result)
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText("Final result for quiz " + self.quiz.id + " : " + str(result))
        msg.setWindowTitle("Result")
        msg.setStandardButtons(QMessageBox.Ok)
        overwrite = False
        if self.user.quizResult == {}:
            self.user.quizResult = []
            print(self.user.quizResult)
        elif len(self.user.quizResult) > 0:
            for qres in self.user.quizResult:
                if qres[0] == self.quiz.id:
                    qres[1] = result
                    overwrite = True
        if overwrite == False:
            self.user.quizResult.append([self.quiz.id, result])
        print(self.user.quizResult)
        retval = msg.exec_()
       
    #Check if all question is completed
    def isAllQuestionCompleted(self):
        for elem in range(len(self.stack)):
            widgetitem = self.stack[elem].layout().itemAt(0).widget()
            if (widgetitem.getuseranswer() == ''):
                return False

            if(widgetitem.getClass() == 'FillTheWord'):
                if(widgetitem.getuseranswer().text() == ''):
                    return False
        return True

    #Show which questions are incomplete
    def showIncompleteQuestion(self):
        tmp = []
        for elem in range(len(self.stack)):
            widgetitem = self.stack[elem].layout().itemAt(0).widget()
            item = self.leftlist.item(elem)
            if(widgetitem.getuseranswer() == ''):
                tmp.append(elem)
                if(isinstance(item, QListWidgetItem)):
                    self.markAsUndone(item)
            if(widgetitem.getClass() == 'FillTheWord'):
                if(widgetitem.getuseranswer().text() == ''):
                    tmp.append(elem)
                    if (isinstance(item, QListWidgetItem)):
                        self.markAsUndone(item)

    #Mark the question as Correct
    def markAsCorrect(self,item):
        item.setBackground(QBrush(QColor("#98FB98")))
        item.setForeground(QBrush(QColor(0,0,0)))

    #Mark the Invalid question
    def markAsInvalid(self, item):
        item.setBackground(QBrush(QColor(255,0,0)))
        item.setForeground(QBrush(QColor(255, 255, 255)))

    #Mark the question as undone
    def markAsUndone(self,item):
        item.setBackground(QBrush(QColor("#FFFF91")))
        item.setForeground(QBrush(QColor(0, 0, 0)))

    def NotifyFinalScoreMessage(self):
        pass

    #MesssageBox notifying user question is not completed
    def NotifyIncompleteMessage(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText("Submission")
        msg.setInformativeText("Incompleted quiz? Finish first?")
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        msg.exec_()

    #Add the question tab on leftlist
    def addQuestionTab(self, item_num, name):
        self.leftlist.insertItem(item_num, name)

    #Construct new QWidget in order to add Layout to it
    def addNewQuestion(self):
        tmp = QWidget()
        self.stack.append(tmp)
        print("New question added successfully")

    #Create fill in the blank question
    def CreateFillInAnswerQuestion(self, question):
        layout = QFormLayout()
        if(type(question).__name__ == 'Question' and question.getQuestionType() == 'Fill'):
            tmp = FillTheWord(question)
            layout.addRow(tmp)
        return layout

    #Create True False question
    def CreateTrueFalseQuestion(self,question):
        layout = QFormLayout()
        if(type(question).__name__ == 'Question' and question.getQuestionType() == 'TrueFalse'):
            tmp = TrueFalse(question)
            layout.addRow(tmp)
        return layout

    #Create Multiplechoice question
    def CreateMultipleChoiceQuestion(self,question):
        layout = QFormLayout()
        if(type(question).__name__ == 'Question' and question.getQuestionType() == 'MultipleChoice'):
            tmp = MultipleChoice(question)
            layout.addRow(tmp)
        return layout

    def exitQuiz(self):
        self.hide()
        self.parent.show()

def main():
    app = QApplication(sys.argv)
    #Parse quizzes
    quizzes = parseToQuizzes("quizzes.txt")
    for q in quizzes:
        if q.id == "Quiz2-IPA":
            quiz_ = q
    ex = QuizApplication(quiz_, User("A","B","C","19419","12Ab=IUU"))
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
