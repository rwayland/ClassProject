__author__ = 'derek'
from TrueFalseQuestion import TrueFalseQuestion
import os
from Utility import Utility
from QuestionFetcher import QuestionFetcher
from CustomExceptions import QuestionAlreadyExistsError
from MultipleChoiceQuestion import MultipleChoiceQuestion
import shelve

class QuestionEditor:

    questionFilePath = None
    shelf = None


    def __init__(self):
        self.questionFilePath = os.path.join(os.pardir, Utility.supportFilesDir, QuestionFetcher.questionFileName)

    def createNewQuestion(self, category, questionType, question, *args):
        newQuestion = None

        if questionType == "TF":
            newQuestion = TrueFalseQuestion(question)
        # elif questionType == "MC":
        #     newQuestion = MultipleChoiceQuestion()
        formattedQuestion = newQuestion.toList()
        localShelf = self._getShelf()

        if category in localShelf:
            temp = localShelf.get(category, None)
            if formattedQuestion[0] not in temp:
                temp.append(formattedQuestion[0])
                localShelf[category] = temp
            else:
                raise QuestionAlreadyExistsError(formattedQuestion[0])
        else:
            tempList = list()
            tempList.append(formattedQuestion[0])
            localShelf[category] = tempList
            localShelf[formattedQuestion[0]] = list(formattedQuestion[1])
        countString = category + "Count"
        if countString in localShelf:
            localShelf[countString] = str(int(localShelf[countString]) + 1)
        else:
            localShelf[countString] = str(1)
        localShelf.sync()
        for index in localShelf:
            print(localShelf[index])
        localShelf.close()
        return

    def editQuestion(self):
        return

    def _openShelf(self):
        self.shelf = shelve.open(self.questionFilePath, "c", 2)

    def _getShelf(self):
        self._openShelf()
        return self.shelf

    # def _addNewQuestion(self, formattedQuestion):

    # def writeToCategoryFile(self, category):
