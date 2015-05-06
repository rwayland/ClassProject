__author__ = 'derek'
from Question import Question

class TrueFalseQuestion(Question):
    qType = "TF"
    # question = ""

    def __init__(self, question):
        Question.__init__(self, self.qType, question)