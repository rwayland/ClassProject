__author__ = 'derek'
import unittest
import Question


class QuestionUnitTests(unittest.TestCase):

    def setUp(self):
        self.firstQuestion = Question.Question("TF")

    def test_TrueFalseTest(self):
        self.firstQuestion.setQuestion("What is your favorite Color?")
        print(self.firstQuestion.toString())