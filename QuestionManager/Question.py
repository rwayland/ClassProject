__author__ = 'derek'


class Question():
    qType = ""
    question = ""
    questionIdNum = 0

    def __init__(self, qType, question):
        self.qType = qType
        self.setQuestion(question)


    def setQuestion(self, questionText):
        self.question = questionText
        self._setHash()
        return

    #
    def _setHash(self):
        """
        Removes whitespace characters from question and hashes to make the questionIdNum
        :return:
        """
        if self.question != "":
            self.questionIdNum = str(hash(self.question.replace(" ", "")))
        else:
            print("Question not set yet, cannot hash")
        return

    def toString(self):
        returnValue = str(self.qType) + "\n" + str(self.questionIdNum) + "\n" + str(self.question) + "\n"
        return returnValue

    def toList(self):
        return [self.questionIdNum, self.qType, self.question]