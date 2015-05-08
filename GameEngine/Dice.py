__author__ = 'derek'

import random


class Dice:

    @classmethod
    def rollDice(cls):
        roll1 = random.randint(1, 6)
        roll2 = random.randint(1, 6)
        return roll1, roll2