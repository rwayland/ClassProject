__author__ = 'derek'

from Dice import Dice
from GamePiece import GamePiece


class Player(object):

    _teamName = None
    _currentPosition = None
    _currentRollTotal = None
    _possibleWinCondition = False
    _gamePiece = None

    def __init__(self):
        self._gamePiece = GamePiece()
        return

    def getRollResult(self):
        result = Dice.rollDice()
        self._currentRollTotal = result(0) + result(1)

    def finalizeTurn(self):
        self._currentRollTotal = None
        self._currentPosition = None