"""
"""

from models import Model


class Object:

    logoFile = ""
    name = ""
    def __init__(self):
        pass

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    def setLogoFile(self, file):
        self.logoFile = file

class ObjectModel(Object, Model):

    mapCoordonates = ()       # tuple of integers as line and row
    roomCoordonates = ()      # tuple of integers as line and row


    def __init__(self):
        Object(self)

    def setCoordonates(self, coordonates, what):
        checkCoordonates(coordonates)
        if what == "map":
            self.mapCoordonates = coordonates
        elif what == "room":
        self.roomCoordonates = coordonates

    def getCoordonates(self, what):
        if what == "map":
            return self.mapCoordonates
        elif what == "room":
            return self.roomCoordonates

