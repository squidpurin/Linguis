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
import pickle

class QuizApplication(QWidget):
    def __init__(self):
        super(QuizApplication, self).__init__()
        self.leftlist = QListWidget()

        self.stack = []
        q1 = question.Question(1, "MultipleChoice", "How going to do", "A")
        q2 = question.Question(2, "Fill", "What is your name", "a", "speech_organ.jpg")
        q3 = question.Question(3, "TrueFalse", "Am I handsome? ", "true", "speech_organ.jpg")
        q4 = question.Question(4, "MultipleChoice", "Select the following sentence", "B")
        q5 = question.Question(5, "Fill", "How old are you? ", "a", "speech_organ.jpg")
        q6 = question.Question(6, "MultipleChoice", "What is current temperature?", "C")
        q7 = question.Question(7, "Fill", "Where is my food?", "Refridgerator")
        q8 = question.Question(8, "TrueFalse", "Today is the bad day", "true")
        q9 = question.Question(9, "Fill", "What is the distance between KMITL and home?", "100")
        q10 = question.Question(10,"MultipleChoice", "How old is my mother", "C")

        self.quiz = quiz.Quiz(1)
        self.quiz.addQuestion(q1)
        self.quiz.addQuestion(q2)
        self.quiz.addQuestion(q3)
        self.quiz.addQuestion(q4)
        self.quiz.addQuestion(q5)
        self.quiz.addQuestion(q6)
        self.quiz.addQuestion(q7)
        self.quiz.addQuestion(q8)
        self.quiz.addQuestion(q9)
        self.quiz.addQuestion(q10)

        self.useranswer = userAnswer.UserAnswerList(1)
        self.quizEvaluator = evaluator.QuizEvaluator(self.useranswer, self.quiz)

        #Create question tabs
        for i in range(self.quiz.getSize()):
            self.addQuestionTab(i, 'question' + str(i + 1))

        #create new QWidget based on number of tabs
        for i in range(len(self.leftlist)):
            self.addNewQuestion()

        self.stack[0].setLayout(self.CreateMultipleChoiceQuestion(q1))
        self.stack[1].setLayout(self.CreateFillInAnswerQuestion(q2))
        self.stack[2].setLayout(self.CreateTrueFalseQuestion(q3))
        self.stack[3].setLayout(self.CreateMultipleChoiceQuestion(q4))
        self.stack[4].setLayout(self.CreateFillInAnswerQuestion(q5))
        self.stack[5].setLayout(self.CreateMultipleChoiceQuestion(q6))
        self.stack[6].setLayout(self.CreateFillInAnswerQuestion(q7))
        self.stack[7].setLayout(self.CreateTrueFalseQuestion(q8))
        self.stack[8].setLayout(self.CreateFillInAnswerQuestion(q9))
        self.stack[9].setLayout(self.CreateMultipleChoiceQuestion(q10))


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

        #Create SubmitButton
        confirmbtn = QPushButton('Submit')
        confirmbtn.clicked.connect(self.submitAnswer)
        hbox.addWidget(confirmbtn)

        #Create the layout
        self.setLayout(hbox)
        self.leftlist.currentRowChanged.connect(self.display)
        self.setFixedSize(900, 600)
        self.setWindowTitle('Quiz Demo')

        self.show()

    def  clearAnswerList(self):
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

    #Display the question with respect to the question number
    def display(self, i):
        self.Stack.setCurrentIndex(i)

def main():
    app = QApplication(sys.argv)
    ex = QuizApplication()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
