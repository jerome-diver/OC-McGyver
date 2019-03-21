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

    north_walls = (b'\x02',b'\x05',b'\x06',b'\x07',b'\x0b',b'\x0c',b'\x0e',b'\x0f')
    south_walls = (b'\x03',b'\x07',b'\x09',b'\x0a',b'\x0c',b'\x0d',b'\x0e',b'\x0f')
    east_walls = (b'\x04',b'\x05',b'\x08',b'\x09',b'\x0b',b'\x0c',b'\x0d',b'\x0f')
    west_walls = (b'\x01',b'\x06',b'\x08',b'\x0a',b'\x0b',b'\x0d',b'\x0e',b'\x0f')

    def __init__(self):
        Model().__init__(self)
        Map().__init__(self)
        self.map.loadMap()

    def hasWallAt(self, room_coordonates, edge_position):
        checkDirection(edge_position)
        checkCoordonates(room_coordonates)
        if edge_position == "north":
            return self.map.wallPosition(room_coordonates) in north_walls
        elif edge_position == "south":
            return self.map.wallPosition(room_coordonates) in south_walls
        elif edge_position == "east":
            return self.map.wallPosition(room_coordonates) in east_walls
        elif edge_position == "west":
            return self.map.wallPosition(room_coordonates) in west_walls

