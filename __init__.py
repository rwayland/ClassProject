__author__ = 'derek'
from Utility import Utility
from QuestionManager import QuestionFetcher, QuestionEditor, QuestionManager
from CustomExceptions import QuestionAlreadyExistsError, CategoryDNEError, NoMoreUniqueQuestions
# from ClassProject

blah = QuestionManager.QuestionManager()
cat1 = 'redCategory'
cat2 = 'blueCategory'
# initSetup = True
initSetup = False

if initSetup:
    try:
        QuestionEditor.QuestionEditor().createNewQuestion(cat1, 'TF', "What is your Favorite Question?", "True/False")
    except QuestionAlreadyExistsError:
        print("Awww Snap! Question Already Exists!")

    try:
        QuestionEditor.QuestionEditor().createNewQuestion(cat1, 'TF', "What is your Favorite Color?", "Blue")
    except QuestionAlreadyExistsError:
        print("Awww Snap! Question Already Exists!")

    try:
        QuestionEditor.QuestionEditor().createNewQuestion(cat2, 'TF', "Who is your Favorite Person?", "Wife!")
    except QuestionAlreadyExistsError:
        print("Awww Snap! Question Already Exists!")
else:
    question1 = blah.getUniqueQuestion(cat1)
    answer1 = blah.getAnswerToQuestion(question1[0])
    print(question1)
    print(answer1)
    question2 = blah.getUniqueQuestion(cat1)
    answer2 = blah.getAnswerToQuestion(question2[0])
    print(question2)
    print(answer2)
    question3 = blah.getUniqueQuestion(cat2)
    answer3 = blah.getAnswerToQuestion(question3[0])
    print(question3)
    print(answer3)