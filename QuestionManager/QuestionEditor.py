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
    questionShelf = None
    answerShelf = None
    answerPath = None
    util = None

    def __init__(self):
        util = Utility()
        self.answerPath = util.getAnswerPath()
        self.questionFilePath = os.path.join(os.pardir, Utility.supportFilesDir, QuestionFetcher.questionFileName)

    def createNewQuestion(self, category, questionType, question, answer, *args):
        newQuestion = None

        if questionType == "TF":
            newQuestion = TrueFalseQuestion(question)
        elif questionType == "MC":
             newQuestion = MultipleChoiceQuestion()
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

        localShelf[formattedQuestion[0]] = formattedQuestion
        countString = category + "Count"
        if countString in localShelf:
            localShelf[countString] = str(int(localShelf[countString]) + 1)
        else:
            localShelf[countString] = str(1)

        localShelf.sync()
        localShelf.close()
        self._setAnswerToQuestion(answer, formattedQuestion[0])
        return

    def editQuestion(self):
        return

    def _setAnswerToQuestion(self, answer, questionHash):
        localShelf = self._getAnswerShelf()
        localShelf[questionHash] = answer
        return

    def _openAnswerShelf(self):
        path = self.answerPath
        self.answerShelf = shelve.open(path, "c", 2)
        return

    def _getAnswerShelf(self):
        self._openAnswerShelf()
        return self.answerShelf

    def _openShelf(self):
        self.questionShelf = shelve.open(self.questionFilePath, "c", 2)

    def _getShelf(self):
        self._openShelf()
        return self.questionShelf

    # def _addNewQuestion(self, formattedQuestion):

    # def writeToCategoryFile(self, category):
