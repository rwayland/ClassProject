__author__ = 'derek'
import Question


class TrueFalseQuestion(Question):
    qType = "MC"
    question = ""

    def __init__(self):
        Question.__init__(self, self.qType)