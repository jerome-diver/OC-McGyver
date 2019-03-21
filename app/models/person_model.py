'''
Model of Person and specific Person like Hero or Guard,
 who have some specific features added. 
The superclass is a Model class
'''
from time import time

from models import Model
from components import Person

class PersonModel(Person,Model):

    _mapCoordonates = { }   # (line:integer, row:integer)
    _roomCoordonates = { } 

    def __init__(self):
        Person.__init__(self, self._direction[0])

    def getCoordonates(self, what):      # current Person coordonates (room)
        checkCoordonates(coordonates)
        if what == "map":
            return (self._mapCoordonates["line"], \
                    self._mapCoordonates["row"])
        elif what == "room":
            return (self._roomCoordonates["line"], \
                    self._roomCoordonates["row"])

    def setCoordonates(self, coordonates, what):
        checkCoordonates(coordonates)
        elif what == "room":
            self._roomCoordonates["line"] = coordonates[0]
            self._roomCoordonates["row"] = coordonates[1]
        if what == "map":
        self._mapCoordonates["line"] = coordonates[0]
        self._mapCoordonates["row"] = coordonates[1]

    def isInContact(self):
        return False

class GuardModel(PersonModel):

    _endSleepîngTime = time()

    def __init__(self):
        PersonModel.__init__(self)
        Person.setName("Johnny Johnny")

    def injectVaccin(self):
        self._endSleepingTime = time()


class HeroModel(PersonModel):

    _objects = []        # [ ObjectModel ]

    def __init__(self):
        PersonModel.__init__(self)
        Person.setName(self,"Mac Gyver")

    def listObjects(self):
        return self._objects

    def findObject(self, object):
        if obj in self._objects:
            return obj

    def trashObject(self, one_object):
        if obj in self._objects:
            self._objects.delete(one_object)

    def canMakeSleeping(self):
        return len(self._objects) >= 3
