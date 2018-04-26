class QuizEvaluator:
    def __init__(self, useranswerlist, quiz):
        self.useranswerlist = useranswerlist
        self.quiz = quiz
        self.correctList = []
        self.finalscore = 0

    def getFinalScore(self):
        return self.finalscore

    def checkCompleteQuestion(self):
        return self.useranswerlist.getSize() == self.quiz.getSize()

    def getCorrectAnswer(self):
        del self.correctList[:]
        self.finalscore = 0
        for question in self.quiz.getQAList():
            for userans in self.useranswerlist.getAnswerList():
                if (question.getQuestion() == userans.getQuestion()):
                    question.setAnswered()
                    if (question.getAnswer() == userans.getAnswer()):
                        self.correctList.append(userans)
                        print("Correct Question: " + userans.getQuestion() + "Ans: " + userans.getAnswer())
                        self.finalscore += 1
                    else:
                        print("Wrong Question: " + userans.getQuestion() + "Ans: " + userans.getAnswer())
        for question in self.quiz.getQAList():
            if not (question.getAnswered()):
                print("Incomplete Q: " + question.getQuestion() + " " + question.getAnswer())

        self.setFinalScore(self.getFinalScore())
        return self.correctList

    def getCorrectList(self):
        return self.correctList

    def setFinalScore(self,finalscore):
        self.finalscore = finalscore

    def getUserAnswer(self):
        pass

    def markQuiz(self):
        pass

    def getQuizComponenet(self):
        pass

    def getResult(self):
        pass

    def postResult(self):
        pass

    def upDateDisplay(self):
        pass