__author__ = 'derek'


class GameBoard(object):
    def __init__(self):
        self.colors = self._setColors()
        self.gameBoardPerimeter = self._buildGameBoard()
        self.spokes = self._buildSpokes()
        self.maxPosition = len(self.gameBoardPerimeter)

        return

    def _buildGameBoard(self):
        gameBoardPerimeter = []
        colors = self.colors
        for index in range(2, 14):
            if index % 3 == 0:
                if index != 0:
                    gameBoardPerimeter.append("RollAgain")
                gameBoardPerimeter.append(colors[index % 4] + "Hub")
                gameBoardPerimeter.append("RollAgain")
            else:
                gameBoardPerimeter.append(colors[index % 4])
        return gameBoardPerimeter

    def _setColors(self):
        colors = ("Green", "Red", "White", "Blue")
        return colors

    def _buildSpokes(self):
        spokes = list(self.colors)
        return spokes

    def getColor(self, position, inSpoke = False):
        if inSpoke:
            returnValue = self.spokes[position % len(self.spokes)]
        else:
            returnValue = self.gameBoardPerimeter[position % self.maxPosition]

        return returnValue