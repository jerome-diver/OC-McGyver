'''
MapModel is uniq and hold map datas get from ./app/map/map.txt file
The map has walls (8x8) stored by coordonates keys for binary values
each binary value (half octet) represent a scheme of 
wall position around a room (who is a square in this map, so there is 64 roomss).
narth_walls is a tuple list contain possible binary code for an existing north wall
and so on for each direction of each room of the map.
'''

from model import Model


class Map:

    walls = { }    # { (line, row) => byte value }
    rooms = { }     # { (line,row): Room }

    def __init__(self):
        pass

    def loadMap(self):
        with open("../map/map.txt", "r") as mapFile:
            for line,readLine in enumerate(mapFile):
                for row, value in enumerate(readLine.strip()):
                    self.walls[(line,row)] = binascii.unhexlify("0"+value)

    def wallPositions(self):
        return walls

    def wallPosition(self, room_coordonates):
        return walls[room_coordonates]

    def wallClockWisePosition(self,room_coordonates):
        checkCoordonates(room_coordonates)
        return (walls[room_coordonates] in north_wall, \
                walls[room_coordonates] in west_wall,  \
                walls[room_coordonates] in south_wall, \
                walls[room_coordonates] in east_wall)

    def appendRoom(self, room):
        self.rooms[room.getCoordonates()] = room

    def getRooms(self):
        rooms_list = []
        for room in self.rooms.values():
            rooms_list.append(room)
        return rooms_list

    def getRoomsDictionary(self):
        return self.rooms

    def getRoomAt(self, room_coordonates):
        return self.rooms[room_coordonates]

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

