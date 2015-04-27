__author__ = 'derek'


class Question():
    qType = ""
    question = ""
    questionIdNum = 0

    def __init__(self, qType, question=""):
        self.qType = qType
        self.question = question

    def setQuestion(self, questionText):
        self.question = questionText
        self.setHash()
        return

    def setHash(self):
        if self.question != "":
            self.questionIdNum = hash(self.question)
        else:
            print("Question not set yet, cannot hash")
        return

    def toString(self):
        returnValue = str(self.qType) + "\n" + str(self.questionIdNum) + "\n" + str(self.question) + "\n"
        return returnValue