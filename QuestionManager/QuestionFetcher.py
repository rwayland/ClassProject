__author__ = 'derek'
__doc__ = "UC007"
from Utility import Utility
import os
import shelve
import random
from CustomExceptions import CategoryDNEError, NoMoreUniqueQuestions


class QuestionFetcher:

    categoryNames = list()
    answerFile = ""
    questionFileName = "Questions"
    questionFilePath = None
    usedQuestionsFileName = "UsedQuestions"
    usedQuestionsFilePath = None
    questionConfigParser = None
    questionShelf = None
    usedQuestionShelf = None
    questionRecycler = False

    def __init__(self):
        # self.currentQuestion
        # self.__loadCategories()
        self.__loadAnswerFile()
        utility = Utility()
        self.categoryNames = utility.getCategorySectionNames
        self.answerFile = utility.getAnswerFileName()
        self.questionFilePath = os.path.join(os.pardir, Utility.supportFilesDir, QuestionFetcher.questionFileName)
        self.usedQuestionsFilePath = os.path.join(os.pardir, Utility.supportFilesDir, self.usedQuestionsFileName)

    def fetchQuestion(self, category):
        if category in self.categoryNames:
            localShelf = self._getQuestionShelf()
            questionCandidate = None

            if category in localShelf:  # check for valid category
                questionUsed = True  # intialized to True for the while loop below
                indexer = 0  # sentry value to make sure we are not exceeding the list size
                categoryCountString = category + "Count"  # string of where the size of the list is located.
                maxValue = int(localShelf[categoryCountString])  # size of list

                # checks for unused questions, but exits if all questions are used
                while questionUsed and indexer < maxValue:
                    temp = localShelf.get(category, None)
                    questionCandidate = random.choice(temp)  # chooses a random question from the list
                    questionUsed = self.__checkIfQuestionUsed(category, questionCandidate[0])

                    if questionUsed:  # here to handle if the list is only 1 item long
                        indexer += 1
                # Check for reason that while loop exited.
                if indexer == maxValue:  # means that all questions are used
                    if self.questionRecycler:
                        self._resetUniqueQuestionsForCategory(category)
                        questionCandidate = self.fetchQuestion(category)
                    else:
                        questionCandidate = None
                        localShelf.close()
                        raise NoMoreUniqueQuestions(category)

                # while loop exited because it has a unique question
                else:
                    self.__markQuestionAsUsed(category, questionCandidate[0])

            # category is not in local shelf!
            else:
                localShelf.close()
                raise CategoryDNEError(category)
            localShelf.sync()
            localShelf.close()
        else:
            raise CategoryDNEError(category)
        return questionCandidate

    def fetchAnswer(self, questionHash):
        answer = ""
        return answer

    def __checkIfQuestionUsed(self, category, questionHash):
        localShelf = self._getUsedQuestionsShelf()
        if category not in localShelf:
            returnValue = False
        else:
            temp = localShelf.get(category, None)
            if questionHash not in temp:
                returnValue = False
            else:
                returnValue = True
        localShelf.close()
        return returnValue

    def __markQuestionAsUsed(self, category, questionHash): #doSomething
        localShelf = self._getUsedQuestionsShelf()
        if category in localShelf:
            temp = localShelf.get(category, None)
            if questionHash not in temp:
                temp.append(questionHash)
                localShelf[category] = temp
        else:
            localShelf[category] = list(questionHash)
        localShelf.sync()
        localShelf.close()
        return

    def _resetUniqueQuestionsForCategory(self, category):
        localShelf = self._getUsedQuestionsShelf()
        if category in localShelf:
            del localShelf[category]
        localShelf.sync()
        localShelf.close()
        return

    # def __loadCategories(self):
    #     categories = Utility.getCategorySectionNames
    #     self.category1File = categories[0]
    #     self.category2File = categories[1]
    #     self.category3File = categories[2]
    #     self.category4File = categories[3]

    def __loadAnswerFile(self):
        self.answersFile = Utility.getAnswerFileName

    def __openQuestionShelf(self):
        self.questionShelf = shelve.open(self.questionFilePath, "c", 2)

    def _getQuestionShelf(self):
        self.__openQuestionShelf()
        return self.questionShelf

    def __openUsedQuestionsShelf(self):
        self.usedQuestionShelf = shelve.open(self.usedQuestionsFilePath, "c", 2)

    def _getUsedQuestionsShelf(self):
        self.__openUsedQuestionsShelf()
        return self.usedQuestionShelf