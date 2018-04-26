from QAPair import *

class UserAnswerList:
    def __init__(self, id):
        self.id = id
        self.answerlist = []

    def addAnswer(self, pair):
        if (isinstance(pair, QAPair)):
            self.answerlist.append(pair)

    def getAnswerList(self):
        return self.answerlist

    def itemAt(self, num):
        return self.answerlist[num]

    def getSize(self):
        return len(self.answerlist)

    def isEmpty(self):
        return len(self.answerlist) == 0

    def displayUserAns(self):
        for i in self.answerlist:
            print(str("Question: " + i.getQuestion()) + "Answer: " + str(i.getAnswer()))

