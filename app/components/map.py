'''
The Map object is the uniq map object who contain the labirynth map with his walls designs.
The map has 8 lines of 8 culumns rooms (64 rooms).
'''
class Map:

    _walls = { }    # { (row,column): byte }
    _rooms = { }    # { (row,column): Room }
    _wallsN = (b'\x02',b'\x05',b'\x06',b'\x07',b'\x0b',b'\x0c',b'\x0e',b'\x0f')
    _wallsS = (b'\x03',b'\x07',b'\x09',b'\x0a',b'\x0c',b'\x0d',b'\x0e',b'\x0f')
    _wallsE = (b'\x04',b'\x05',b'\x08',b'\x09',b'\x0b',b'\x0c',b'\x0d',b'\x0f')
    _wallsW = (b'\x01',b'\x06',b'\x08',b'\x0a',b'\x0b',b'\x0d',b'\x0e',b'\x0f')

    def __init__(self):
        loadMap(self)

    def loadMap(self):
        with open("../map/map.txt", "r") as mapFile:
            for line,readLine in enumerate(mapFile):
                for row, value in enumerate(readLine.strip()):
                    self._walls[(line,row)] = binascii.unhexlify("0"+value)

    def wallPositions(self):
        return self._walls

    def wallPosition(self, room_coordonates):
        return self._walls[room_coordonates]

    def wallClockWisePosition(self,room_coordonates):
        checkCoordonates(room_coordonates)
        return (self._walls[room_coordonates] in self._wallsN, \
                self._walls[room_coordonates] in self._wallsE, \
                self._walls[room_coordonates] in self._wallsS, \
                self._walls[room_coordonates] in self._wallsW)

    def appendRoom(self, room):
        self._rooms[room.getCoordonates()] = room

    def getRooms(self):
        rooms_list = []
        for room in self._rooms.values():
            rooms_list.append(room)
        return rooms_list

    def getRoomsDictionary(self):
        return self._rooms

    def getRoomAt(self, room_coordonates):
        return self._rooms[room_coordonates]
