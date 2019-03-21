'''
The Map object is the uniq map object who contain the labirynth map with his walls designs.
The map has 8 lines of 8 culumns rooms (64 rooms).
'''
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
