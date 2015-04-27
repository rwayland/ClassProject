__author__ = 'derek'
__doc__ = "UC007"
from QuestionFetcher import QuestionFetcher

class QuestionManager:

   # __questionFetcher

    def __init__(self):
        self.__questionFetcher = QuestionFetcher()

    __doc__ = """Retrieves a unique question
                 @returns string array with question and possible answers
              """
    def getUniqueQuestion(self):
        question = self.__questionFetcher.fetchQuestion()
        return question  # should be Question

    __doc__ = """Retrieves the Answer to the current question
                 @returns string with answer
              """
    def getAnswerToQuestion(self):
        return self.__questionFetcher.fetchAnswer()