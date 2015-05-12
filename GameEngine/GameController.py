__author__ = 'derek'

from QuestionManager import QuestionManager
from Player import Player
from GameBoard import GameBoard
from DialogQuestion import DialogQuestion
import wx
import uuid


class GameController:

    gameId = None
    players = list()
    currentPlayer = None
    questionManager = None
    gameBoard = None
    winner = None

    def __init__(self):
        self.gameId = uuid.uuid4()
        self.questionManager = QuestionManager.QuestionManager()
        self._initiatePlayers(4)
        self.gameBoard = GameBoard()
        self.currentPlayer = self.players[0]
        # self.currentPlayer = Player()
        self.mainGameLoop()

    def mainGameLoop(self):
        while self.winner is None:
            self.executeCurrentPlayersTurn()
            self._incrementCurrentPlayer()
        return

    def executeCurrentPlayersTurn(self):
        roll = self.currentPlayer.getRollResult()
        # TODO move number of spaces depending on players selection
        if not self.currentPlayer.inSpoke():
            newPosition = self.currentPlayer.getCurrentPosition() + roll
            self.currentPlayer.setCurrentPosition(newPosition % 20)  # since there are 20 items in the main gameboard
        else:
            # ToDO add the logic if you are in the spoke.
            return
        color = self.gameBoard.getColor(newPosition)  # ToDo add logic for in spoke
        if color != "RollAgain":
            self.executeQuestionPhase(color)
        else:
            self.currentPlayer.finalizeTurn()
            self.executeCurrentPlayersTurn()
        self.currentPlayer.finalizeTurn()
        return

    def checkForWinner(self):
        return

    def correctLogic(self, color):
        if "hub" in color:
            isColorHub = True
        else:
            isColorHub = False
        if isColorHub:
            self.currentPlayer.receiveWedge(color)
        self.currentPlayer.finalizeTurn()
        self.executeCurrentPlayersTurn()
        return

    def executeQuestionPhase(self, color):
        question = self.questionManager.getUniqueQuestion(color)
        app = wx.PySimpleApp()
        val = self.questionToGui(question)
        app.MainLoop()
        answer = self.questionManager.getAnswerToQuestion(question[0])

        if question[1] == "TF":
            if val == 0:
                choice = True
            else:
                choice = False
        if answer == choice:
            self.correctLogic(color)
            self.checkForWinner()
        else:
            print(answer)
        return

    def questionToGui(self, question):
        if question[1] == "TF":
            dlg = DialogQuestion(question[2], ["True", "False"])
        else:
            dlg = DialogQuestion(question[2], [question[3], question[4], question[5], question[6]])
        if dlg.ShowModal() == wx.ID_OK:
            val = dlg.getSelection()
            print(val)
        dlg.Destroy()
        return val

    def _incrementCurrentPlayer(self):
        currentIndex = self.players.index(self.currentPlayer)
        self.currentPlayer = self.players[currentIndex]
        return

    def _initiatePlayers(self, numberOfPlayers):
        for index in range(numberOfPlayers):
            self.players.append(Player())
        return

    def __setWinner(self, player):
        self.winner = player