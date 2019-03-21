'''
The Person object has a game life...
'''

class Person:

    name = ""
    isLookingAt =""

    def __init__(self, name):
        self.name = name

    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name

    def isLookingWhere(self):
        return self.isLookingAt

    def isLookingAt(self, direction):  # is looking in front of him (set where)
        checkDirection(direction)
        self.isLookingAt = direction


