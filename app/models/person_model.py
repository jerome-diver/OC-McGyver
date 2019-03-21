'''
Model of Person and specific Person like Hero or Guard,
 who have some specific features added. 
The superclass is a Model class
'''
from time import time

from models import Model
from components import Person

class PersonModel(Person,Model):

    mapCoordonates = { }   # (line:integer, row:integer)
    roomCoordonates = { } 

    def __init__(self):
        Person(self)
        isLookingAt(self.direction[0])

    def getCoordonates(self, what):      # current Person room position coordonates
        checkCoordonates(coordonates)
        if what == "map":
            return (self.mapCoordonates["line"], \
                    self.mapCoordonates["row"])
        elif what == "room":
            return (self.roomCoordonates["line"], \
                    self.roomCoordonates["row"])

    def setCoordonates(self, coordonates, what):
        checkCoordonates(coordonates)
        elif what == "room":
            self.roomCoordonates["line"] = coordonates[0]
            self.roomCoordonates["row"] = coordonates[1]
        if what == "map":
        self.mapCoordonates["line"] = coordonates[0]
        self.mapCoordonates["row"] = coordonates[1]

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
