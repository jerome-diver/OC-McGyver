'''
The Person object has a game life...
'''

class Person:

    _name = ""
    _sLookingAt =""

    def __init__(self, looking_where):
        isLookingAt(looking_where)

    def getName(self):
        return self._name

    def setName(self, name):
        self._name = name

    def isLookingWhere(self):
        return self._isLookingAt

    def isLookingAt(self, direction):  # is looking in front of him (set where)
        checkDirection(direction)
        self._isLookingAt = direction


