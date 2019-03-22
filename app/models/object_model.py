"""
"""

from models import Model
from components import Object


class ObjectModel(components.Object, Model):

    _mapCoordonates = ()       # tuple of integers as line and row
    _roomCoordonates = ()      # tuple of integers as line and row


    def __init__(self):
        super.__init__()

    def setCoordonates(self, coordonates, what):
        checkCoordonates(coordonates)
        if what == "map":
            self._mapCoordonates = coordonates
        elif what == "room":
        self._roomCoordonates = coordonates

    def getCoordonates(self, what):
        if what == "map":
            return self._mapCoordonates
        elif what == "room":
            return self._roomCoordonates

