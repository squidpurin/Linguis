import QAPair as pair
class Quiz:
    def __init__(self,id,name = ""):
        self.id = id
        self.name = name
        self.questionanswerlist = []

    def addQuestion(self, question):
        if(type(question).__name__ == 'Question'):
            tmp = pair.QAPair(question.getQuestionText(),question.getAnswer())
            self.questionanswerlist.append(tmp)

    def getAnswer(self):
        tmp = []
        for i in self.questionanswerlist:
            tmp.append(i.getAnswer())
        return tmp
    def getSize(self):
        return len(self.questionanswerlist)
    def getQAList(self):
        return self.questionanswerlist
    def getQuestionIndex(self, num):
        return self.questionanswerlist[num]
