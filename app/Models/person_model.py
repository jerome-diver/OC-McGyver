'''
Model of Person and specific Person like Hero or Guard,
 who have some specific features added. 
The superclass is a Model class
'''
from time import time

from model import Model


class Person:

    name = ""
    mapPosition = { }   # { "line": int, "row": int }
    roomPosition = { }  # { "line": int, "row": int }
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


class PersonModel(Person,Model):

    def __init__(self):
        self.person = Person()
        self.person.isLookingAt(self.direction[0])

    def getRoomPosition(self):      # current Person room position coordonates
        return (self.roomPosition["line"], self.roomPosition["row"])

    def setRoomPosition(self, coordonates):
        checkCoordonates(coordonates)
        self.roomPosition["line"] = coordonates[0]
        self.roomPosition["row"] = coordonates[1]

    def getMapPosition(self):       # current Person map coordonates position
        return (self.mapPosition["line"], self.mapPosition["row"])

    def setMapPosition(self, coordonates):
        checkCoordonates(coordonates)
        self.mapPosition["line"] = coordonates[0]
        self.mapPosition["row"] = coordonates[1]

    def isInContact(self):
        return False

class GuardModel(PersonModel):

    endSleepîngTime = time()

    def __init__(self):
        self.person.setName("Johnny")

    def injectVaccin(self):
        endSleepingTime = time()


class HeroModel(PersonModel):

    objects = []        # [ ObjectModel ]

    def __init__(self):
        self.person.setName("McGyver")

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
