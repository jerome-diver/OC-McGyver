'''
'''
from time import time

from model import Model

class PersonModel(Model):

    name = ""
    mapPosition = { }   # { "line": int, "row": int }
    roomPosition = { }  # { "line": int, "row": int }

    def __init__(self):
        isLookingAt = self.direction[0]

    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name

    def getRoomPosition(self):      # current Person room position coordonates
        return (self.roomPosition["line"], self.roomPosition["row"])

    def setRoomPosition(self, coordonates):
        self.roomPosition["line"] = coordonates[0]
        self.roomPosition["row"] = coordonates[1]

    def getMapPosition(self):       # current Person map coordonates position
        return (self.mapPosition["line"], self.mapPosition["row"])

    def setMapPosition(self, coordonates):
        self.mapPosition["line"] = coordonates[0]
        self.mapPosition["row"] = coordonates[1]

    def isLookingWhere(self):
        return self.isLookingAt

    def isLookingAt(self, direction):  # is looking in front of him (set where)
        checkDirection(direction)
        self.isLookingAt = direction

    def isInContact(self):

        return bool

class GuardModel(PersonModel):

    endSleepîngTime = time()

    def __init__(self):
        pass

    def injectVaccin(self):
        endSleepingTime = time()


class HeroModel(PersonModel):

    objects = []        # [ ObjectModel ]

    def __init__(self):
        pass

    def canWalkAhead(self):
        pass

    def listObjects(self):
        pass

    def findObject(self, object):
        pass

    def trashObject(self, object):
        pass

    def canMakeSleeping(self):
        pass
