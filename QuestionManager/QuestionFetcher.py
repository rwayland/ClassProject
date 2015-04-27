__author__ = 'derek'
__doc__ = "UC007"
from Utility import Utility
class QuestionFetcher:

    category1File = "redCategory.txt"
    category2File = "whiteCategory.txt"
    category3File = "blueCategory.txt"
    category4File = "greenCategory.txt"
    answersFile = "answers.txt"

    def __init__(self):
        self.currentQuestion
        self.__loadCategories()
        self.__loadAnswerFile()

    def fetchQuestion(self, category):
        return

    def fetchAnswer(self, questionHash):
        answer = ""
        return answer

    def __openFile(self, category):
        return

    def __checkIfQuestionUsed(self, questionHash):
        return True

    def __markQuestionAsUsed(self, questionHash): #doSomething
        return

    def __closeFile(self, category):
        return

    def __loadCategories(self):
        categories = Utility.getCategoryFileNames
        self.category1File = categories[0]
        self.category2File = categories[1]
        self.category3File = categories[2]
        self.category4File = categories[3]

    def __loadAnswerFile(self):
        self.answersFile = Utility.getAnswerFileName