class Question(object):
    def __init__(self, questionID, questiontype, questionText, answer, questionImage=""):
        self.questionID = questionID
        self.questiontype = questiontype
        self.questionImage = questionImage
        self.questionText = questionText
        self.answer = answer

    def getQuestionType(self):
        return self.questiontype

    def checkAnswer(self, ans):
        return self.answer == ans

    def setAnswer(self, answer):
        self.answer = answer

    def getAnswer(self):
        return self.answer

    def setQuestionImage(self, im):
        self.questionImage = im

    def getQuestionImage(self):
        return self.questionImage

    def setQuestionText(self, question):
        self.questionText = question

    def getQuestionText(self):
        return self.questionText

    def getQuestionID(self):
        return self.questionID

    def setQuestionID(self, questionID):
        self.questionID = questionID


class Options:
    def __init__(self, options):
        if(type(options) == list):
            self.options = options
        else:
            raise TypeError

    def getOptions(self):
        return self.options

    def setOptions(self, option):
        if(type(option) == list and len(option) == 5):
            self.options = option