'''
MapModel is uniq and hold map datas get from ./app/map/map.txt file
The map has walls (8x8) stored by coordonates keys for binary values
each binary value (half octet) represent a scheme of 
wall position around a room (who is a square in this map, so there is 64 roomss).
narth_walls is a tuple list contain possible binary code for an existing north wall
and so on for each direction of each room of the map.
'''

from model import Model


class MapModel(Model):

    walls = { }    # { (line, row) => byte value }
    north_walls = (b'\x02',b'\x05',b'\x06',b'\x07',b'\x0b',b'\x0c',b'\x0e',b'\x0f')
    south_walls = (b'\x03',b'\x07',b'\x09',b'\x0a',b'\x0c',b'\x0d',b'\x0e',b'\x0f')
    east_walls = (b'\x04',b'\x05',b'\x08',b'\x09',b'\x0b',b'\x0c',b'\x0d',b'\x0f')
    west_walls = (b'\x01',b'\x06',b'\x08',b'\x0a',b'\x0b',b'\x0d',b'\x0e',b'\x0f')
    rooms = { }

    def __init__(self):
        self.walls = loadMap()

    def wallPositions(self):
        return walls

    def wallPosition(self, room):   # room is tuple matrix: (line, row)
        checkRoom(room)
        return walls[room]

    def wallClockWisePosition(self,room):
        checkRoom(room)
        return (walls[room] in north_wall, \
                walls[room] in west_wall,  \
                walls[room] in south_wall, \
                walls[room] in east_wall)

    def hasWallAt(self, room, edge):
        checkDirection(edge)
        checkRoom(room)
        if edge == "north":
            return walls[room] in north_walls
        elif edge == "south":
            return walls[room] in south_walls
        elif edge == "east":
            return walls[room] in east_walls
        elif edge == "west":
            return walls[room] in west_walls

    def loadMap(self):
        with open("../map/map.txt", "r") as mapFile:
            for line,readLine in enumerate(mapFile):
                for row, value in enumerate(readLine.strip()):
                    map[(line,row)] = binascii.unhexlify("0"+value)
        return map

    def appendRoom(self, roomModel):
        self.rooms[roomModel.getCoordonates()] = rooModel
