__author__ = 'derek'


class GamePiece(object):

    wedges = None

    def __init__(self):
        self.wedges = list()

    def getWedge(self, categoryName):
        if categoryName not in self.wedges:
            self.wedges.append(categoryName)
        else:
            print("You already have that wedge!")


#
# class Wedge(object):
#
#     categoryName = None
#
#     def __init__(self, categoryName):
#         self.categoryName = categoryName