class QAPair:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer
        self.isAnswered = False

    def getAnswered(self):
        return self.isAnswered

    def setAnswered(self):
        self.isAnswered = True

    def setQuestion(self, question):
        self.question = question

    def getQuestion(self):
        return self.question

    def setAnswer(self, answer):
        self.answer = answer

    def getAnswer(self):
        return self.answer

    def isAnswerNotFilled(self):
        return self.answer == ""