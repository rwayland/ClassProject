__author__ = 'derek'

from QuestionManager import QuestionManager
from Player import Player
import uuid


class GameController:

    gameId = None
    players = None
    currentPlayer = None
    questionManager = None
    winner = None

    def __init__(self):
        self.gameId = uuid.uuid4()
        self.questionManager = QuestionManager()

    def mainGameLoop(self):
        while self.winner is None:
            self.executeCurrentPlayersTurn()
            self._incrementCurrentPlayer()
        return

    def executeCurrentPlayersTurn(self):
        return

    def checkForWinner(self):
        return

    def executeQuestionPhase(self):
        return

    def _incrementCurrentPlayer(self):
        return

    def _initiatePlayers(self, numberOfPlayers):
        for index in numberOfPlayers:
            self.players[index] = Player()
        return

    def __setWinner(self, player):
        self.winner = player