import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class QuestionType(object):
    def __init__(self):
        self.question = ""
        self.imagename = ""
        self.useranswer = ""

    def getImagename(self):
        return self.imagename

    def setImagename(self, imname):
        self.imagename = imname

    def setQuestion(self, question):
        self.question = question

    def getQuestion(self):
        return self.question

    def getuseranswer(self):
        return self.useranswer

    def setuseranswer(self, answer):
        self.useranswer = answer

    def getClass(self):
        return self.__class__.__name__

class MultipleChoice(QWidget, QuestionType):
    def __init__(self, questionclass,parent=None):
        super(MultipleChoice, self).__init__(parent)
        QuestionType.__init__(self)
        layout = QFormLayout()
        self.buttons = []

        self.setQuestion(questionclass.getQuestionText())
        self.setImagename(questionclass.getQuestionImage())

        layout.addRow(QLabel(str(self.question)))
        if(questionclass.getQuestionImage() != ""):
            self.setImagename(questionclass.getQuestionImage())

            self.image = QPixmap("SEP_Images/" + str(self.imagename))

            imagelabel = QLabel()
            width = 500
            height = self.image.scaledToWidth(width).height()
            imagelabel.setPixmap(self.image.scaledToWidth(width))
            imagelabel.setFixedSize(width, height)
            layout.addRow(imagelabel)

        self.b1 = QRadioButton(questionclass.option.options[0])
        self.b1.toggled.connect(lambda: self.btnstate(self.b1))
        layout.addRow(self.b1)

        self.b2 = QRadioButton(questionclass.option.options[1])
        self.b2.toggled.connect(lambda: self.btnstate(self.b2))
        layout.addRow(self.b2)

        self.b3 = QRadioButton(questionclass.option.options[2])
        self.b3.toggled.connect(lambda: self.btnstate(self.b3))
        layout.addRow(self.b3)

        self.b4 = QRadioButton(questionclass.option.options[3])
        self.b4.toggled.connect(lambda: self.btnstate(self.b4))
        layout.addRow(self.b4)

        self.b5 = QRadioButton(questionclass.option.options[4])
        self.b5.toggled.connect(lambda: self.btnstate(self.b5))
        layout.addRow(self.b5)

        self.setLayout(layout)
        self.setWindowTitle("RadioButton demo")

    def btnstate(self, b):
        ans = b.text()[:1]
        if ans == "A":
            if b.isChecked() == True:
                print(ans + " is selected")
                self.setuseranswer('A')
            else:
                print(ans + " is deselected")

        if ans == "B":
            if b.isChecked() == True:
                print(ans + " is selected")
                self.setuseranswer('B')
            else:
                print(ans + " is deselected")

        if ans == "C":
            if b.isChecked() == True:
                print(ans + " is selected")
                self.setuseranswer('C')
            else:
                print(ans + " is deselected")

        if ans == "D":
            if b.isChecked() == True:
                print(ans + " is selected")
                self.setuseranswer('D')
            else:
                print(ans + " is deselected")

        if ans == "E":
            if b.isChecked() == True:
                print(ans + " is selected")
                self.setuseranswer('E')
            else:
                print(ans + " is deselected")

class TrueFalse(QWidget, QuestionType):
    def __init__(self,questionclass, parent=None):
        super(TrueFalse, self).__init__(parent)
        QuestionType.__init__(self)
        layout = QFormLayout()
        choicelayout = QHBoxLayout()

        self.setQuestion(questionclass.getQuestionText())
        self.setImagename(questionclass.getQuestionImage())
        layout.addRow(QLabel(self.question))
        if (questionclass.getQuestionImage() != ""):
            self.setImagename(questionclass.getQuestionImage())

            self.image = QPixmap("SEP_Images/" + str(self.imagename))

            imagelabel = QLabel()
            width = 500
            height = self.image.scaledToWidth(width).height()
            imagelabel.setPixmap(self.image.scaledToWidth(width))
            imagelabel.setFixedSize(width, height)
            layout.addRow(imagelabel)

        self.truebtn = QRadioButton("True")
        self.truebtn.toggled.connect(lambda: self.btnstate(self.truebtn))
        choicelayout.addWidget(self.truebtn)

        self.falsebtn = QRadioButton("False")
        self.falsebtn.toggled.connect(lambda: self.btnstate(self.falsebtn))
        choicelayout.addWidget(self.falsebtn)

        layout.addItem(choicelayout)
        self.setLayout(layout)
        self.setWindowTitle("TrueFalseDemo")

    def btnstate(self, btn):
        if btn.text() == "True":
            if btn.isChecked() == True:
                print(btn.text() + " is selected")
                self.setuseranswer('true')
            else:
                print(btn.text() + " is deselected")

        elif btn.text() == "False":
            if btn.isChecked() == True:
                print(btn.text() + " is selected")
                self.setuseranswer('false')
            else:
                print(btn.text() + " is deselected")


class FillTheWord(QWidget, QuestionType):
    def __init__(self,questionclass, parent=None):
        super(FillTheWord, self).__init__(parent)
        QuestionType.__init__(self)
        layout = QFormLayout()

        self.setQuestion(questionclass.getQuestionText())
        self.setImagename(questionclass.getQuestionImage())
        layout.addRow(QLabel(self.question))
        if (questionclass.getQuestionImage() != ""):
            self.setImagename("SEP_Images/" + questionclass.getQuestionImage())

            self.image = QPixmap(str(self.imagename))

            imagelabel = QLabel()
            width = 500
            height = self.image.scaledToWidth(width).height()
            imagelabel.setPixmap(self.image.scaledToWidth(width))
            imagelabel.setFixedSize(width, height)
            layout.addRow(imagelabel)

        self.label = QLabel(self)

        self.useranswer = QLineEdit(self)
        layout.addRow("Answer: ", self.useranswer)

        self.setLayout(layout)
        self.show()

    def checkAnswer(self, ans):
            if (self.useranswer.text() == ans):
                return True
            return False
