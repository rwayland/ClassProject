__author__ = 'derek'
import ConfigParser
import os


class Utility:

    category1DefaultFile = "redCategory.txt"
    category2DefaultFile = "whiteCategory.txt"
    category3DefaultFile = "blueCategory.txt"
    category4DefaultFile = "greenCategory.txt"
    defaultsLoaded = False
    gameOptionsName = "GameOptions"
    gameOptionsPath = ''
    supportFilesDir = "SupportFiles"
    categorySection = "Category"
    answerSection = "Answers"
    answerFile = "AnswerFile"
    _defaultCategories = []

    def __init__(self):
        self.config = ConfigParser.RawConfigParser()
        self.gameOptionsPath = os.path.join(os.path.dirname(__file__), self.supportFilesDir, self.gameOptionsName)
        self.config.read(self.gameOptionsPath)

    @property
    def getCategoryFileNames(self):

        index = 0
        newEntriesAdded = False
        fileNames = list()

        if not self.config.has_section(self.categorySection):
            self._createCategorySection()

        while index < 4:
            catName = "category" + str(index+1)  # creates the category name based off of the index

            if not self.config.has_option(self.categorySection, catName):
                if not self.defaultsLoaded:  # checks to ensure the default file names are loaded
                    self._defaultCategories = self._loadDefaultFileNames()
                self._createCategoryFileName(catName, index)  # creates the missing category
                newEntriesAdded = True  # tells the method that it must write the new results to disk

            fileNames.append(self.config.get(self.categorySection, catName))
            index += 1

        if newEntriesAdded:
            self._writeToFile()

        return fileNames  # stringArray

    # gets the path to the Answers file for the QuestionFetcher
    def getAnswerFileName(self):

        newEntriesAdded = False

        if not self.config.has_section(self.answerSection):
            self._createAnswerSection()
            newEntriesAdded = True

        # checks to make sure the kev:value pair exists, if not, writes the default to the file in this method.
        if not self.config.has_option(self.answerSection, self.answerFile):
            self.config.set('Answers', "AnswerFile", "AnswerFile")
            newEntriesAdded = True
        if newEntriesAdded:
            self._writeToFile()
        return self.config.get('Answers', "AnswerFile")

    def _createAnswerSection(self):
        self.config.add_section(self.answerSection)
        self.config.set(self.answerSection, self.answerFile, self.answerFile)

    # Creates a CategorySection if it is not already in the GameOptions file
    def _createCategorySection(self):
        self.config.add_section(self.categorySection)

    # Creates a Category and assigns it the default value if it is not already in the GameOptions file
    def _createCategoryFileName(self, categoryName, index):
        self.config.set(self.categorySection, categoryName, self._defaultCategories[index])

    # loads the default file names.
    def _loadDefaultFileNames(self):
        defaultCategories = [self.category1DefaultFile, self.category2DefaultFile,
                             self.category3DefaultFile, self.category4DefaultFile]
        self.defaultsLoaded = True
        return defaultCategories

    def _writeToFile(self):
        with open(self.gameOptionsPath, 'wb') as configfile:
                self.config.write(configfile)