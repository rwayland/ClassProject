__author__ = 'derek'

from QuestionManager import QuestionManager
from Player import Player
from GameBoard import GameBoard
from DialogQuestion import DialogQuestion
from GuiMain import FrameMain, DialogDice
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
        app = wx.PySimpleApp()
        self.frameMain = FrameMain("Hello")
        self.frameMain.Show()
        self._initiatePlayers(4)
        self.gameBoard = GameBoard()
        self.currentPlayer = self.players[0]
        # self.currentPlayer = Player()
        self.mainGameLoop()
        app.MainLoop()

    def mainGameLoop(self):
        while self.winner is None:
            currentPlayerString = "Player " + str(self.players.index(self.currentPlayer) + 1) + " Turn!"
            blah = wx.MessageDialog(None, currentPlayerString)
            if blah.ShowModal() == wx.ID_OK:
                pass
            blah.Destroy()
            self.executeCurrentPlayersTurn()
            self._incrementCurrentPlayer()
        return

    def executeCurrentPlayersTurn(self):
        roll = self.currentPlayer.getRollResult()
        dicer = DialogDice(roll)
        if dicer.ShowModal() == wx.ID_OK:
            pass
        dicer.Destroy()
        rollResult = roll[0] + roll[1]
        currentPosition = self.currentPlayer.getCurrentPosition()
        if currentPosition == any([2, 7, 12, 17]):
            getOnSpoke = wx.MessageDialog(None, "Go Up Spoke?")
            if getOnSpoke.ShowModal() == wx.ID_OK:
                val = getOnSpoke.getSelection()
            getOnSpoke.Destroy()


        if not self.currentPlayer.inSpoke():
            newPosition = currentPosition + rollResult
            if newPosition == any([2, 7, 12, 17]):
                self.frameMain.gameboard.MovePlayer(self.players.index(self.currentPlayer), currentPosition, newPosition % 20)
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
            self.frameMain.gameboard.scoreboard.AwardCake(self.players.index(self.currentPlayer),color)
        self.currentPlayer.finalizeTurn()
        self.executeCurrentPlayersTurn()
        return

    def executeQuestionPhase(self, color):
        question = self.questionManager.getUniqueQuestion(color)
        # app = wx.PySimpleApp()
        val = self.questionToGui(question)
        # app.MainLoop()
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
        self.currentPlayer.finalizeTurn()
        # self._incrementCurrentPlayer()
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
        newIndex = (currentIndex + 1) % len(self.players)
        self.currentPlayer = self.players[newIndex]
        return

    def _initiatePlayers(self, numberOfPlayers):
        for index in range(numberOfPlayers):
            self.players.append(Player())
            self.frameMain.gameboard.MovePlayer(index, 0, 0)
        return

    def __setWinner(self, player):
        self.winner = player
