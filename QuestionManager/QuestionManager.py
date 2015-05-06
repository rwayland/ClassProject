__author__ = 'derek'
__doc__ = "UC007"
from QuestionFetcher import QuestionFetcher
from CustomExceptions import CategoryDNEError, NoMoreUniqueQuestions, NoAnswerSetForQuestion


class QuestionManager:
    __questionFetcher = None

    def __init__(self):
        self.__questionFetcher = QuestionFetcher()

    def getUniqueQuestion(self, category):
        """Retrieves a unique question
            @returns string array with question and possible answers
        """
        question = None
        try:
            question = self.__questionFetcher.fetchQuestion(category)
        except CategoryDNEError:
            print("Aww Snap! Category doesn't exist!")
        except NoMoreUniqueQuestions:
            print("Aww Snap! No more unique Questions!")
        return question  # should be Question

    def getAnswerToQuestion(self, questionHash):
        """Retrieves the Answer to the current question
            @returns string with answer
        """
        answer = None
        try:
            answer = self.__questionFetcher.fetchAnswer(questionHash)
        except NoAnswerSetForQuestion:
            print("Aww Snap! No Answer set for this Question, let's pick a new one!")
        return answer
