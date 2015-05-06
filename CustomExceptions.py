__author__ = 'derek'


class CustomExceptions(Exception):
    pass


class QuestionAlreadyExistsError(CustomExceptions):

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


class CategoryDNEError(CustomExceptions):

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


class NoMoreUniqueQuestions(CustomExceptions):

    def __init__(self, category):
        self.value = category

    def __str__(self):
        return repr(self.value)

class NoAnswerSetForQuestion(CustomExceptions):

    def __init__(self, questionHash):
        self.value = questionHash

    def __str__(self):
        return repr(self.value)