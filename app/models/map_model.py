'''
MapModel is uniq and hold map datas get from ./app/map/map.txt file
The map has walls stored by coordonates keys for binary values
each binary value (half octet) represent a scheme of 
wall position around a room (who is a square in this map with 15x15 rooms, 
so there is 224 rooms).
_wallsN is a tuple contain possible binary code for an existing 
north wall and so on for each direction of each room of the map.
'''

import os

from models.model import *


class MapModel(Map,Model):

    def __init__(self, pyGameEngine):
        super(Map,self).__init__()
        super(Model, self).__init__(pyGameEngine)
        self.loadMap()

    def hasWallAt(self, room_coordonates, edge_position):
        checkDirection(edge_position)
        checkCoordonates(room_coordonates)
        _map = self.getMap()
        if edge_position == "north":
            return _map.wallPosition(room_coordonates) in self._wallsN
        elif edge_position == "south":
            return _map.wallPosition(room_coordonates) in self._wallsS
        elif edge_position == "east":
            return _map.wallPosition(room_coordonates) in self._wallsE
        elif edge_position == "west":
            return _map.wallPosition(room_coordonates) in self._wallsW

    def getMap(self):
        return self._map

    def loadMap(self):
        cwd = os.path.dirname(os.path.abspath(__file__))
        _file = os.path.join(cwd,"/map/map.txt")
        with open(_file, "r") as mapFile:
            for row,line in enumerate(mapFile):
                for column, char in enumerate(line.strip()):
                    self._walls[(row,column)] = binascii.unhexlify("0"+char)
