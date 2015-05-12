__author__ = 'derek'

import random


class Dice(object):
    """
        Simulates rolling of the dice.
        @:return tuple containing the result of the roll.
    """

    @staticmethod
    def rollDice():
        roll1 = random.randint(1, 6)
        roll2 = random.randint(1, 6)
        return roll1, roll2