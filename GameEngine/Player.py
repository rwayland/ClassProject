__author__ = 'derek'

from Dice import Dice
from GamePiece import GamePiece


class Player(object):

    _teamName = None
    # _currentPosition = None
    _currentRollTotal = 0
    _possibleWinCondition = False
    _gamePiece = None
    _inSpoke = False

    def __init__(self):
        self._gamePiece = GamePiece()
        self._currentPosition = 0
        return

    def getRollResult(self):
        result = Dice.rollDice()
        return result

    def finalizeTurn(self):
        self._currentRollTotal = 0

    def getCurrentPosition(self):
        return self._currentPosition

    def inSpoke(self):
        return self._inSpoke

    def setCurrentPosition(self, position, inSpoke = False):
        self._currentPosition = position
        self._inSpoke = inSpoke

    def receiveWedge(self, color):
        self._gamePiece.getWedge(color)