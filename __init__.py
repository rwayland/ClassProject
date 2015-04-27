__author__ = 'derek'
from Utility import Utility

utility = Utility()
fileNames = utility.getCategoryFileNames
index = 0
while index < 4:
    print(fileNames[index])
    index += 1
