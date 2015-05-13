__author__ = 'derek'
from Question import Question


class MultipleChoiceQuestion(Question):
    qType = "MC"
    # question = ""
    possibleAnswer1 = ""
    possibleAnswer2 = ""
    possibleAnswer3 = ""
    possibleAnswer4 = ""

    def __init__(self, question, *args):
        Question.__init__(self, self.qType, question)

    def toList(self):

        return [self.questionIdNum, self.qType, self.question]