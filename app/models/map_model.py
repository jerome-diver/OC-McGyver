'''
MapModel is uniq and hold map datas get from ./app/map/map.txt file
The map has walls (8x8) stored by coordonates keys for binary values
each binary value (half octet) represent a scheme of 
wall position around a room (who is a square in this map, so there is 64 roomss).
narth_walls is a tuple list contain possible binary code for an existing north wall
and so on for each direction of each room of the map.
'''

from models import Model
from components import Map


class MapModel(Map,Model):

    def __init__(self):
        super().__init__()

    def hasWallAt(self, room_coordonates, edge_position):
        checkDirection(edge_position)
        checkCoordonates(room_coordonates)
        if edge_position == "north":
            return self.wallPosition(room_coordonates) in self._wallsN
        elif edge_position == "south":
            return self.wallPosition(room_coordonates) in self._wallsS
        elif edge_position == "east":
            return self.wallPosition(room_coordonates) in self._wallsE
        elif edge_position == "west":
            return self.wallPosition(room_coordonates) in self._wallsW

