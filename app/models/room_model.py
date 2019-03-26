"""
RoommModel abject represent a room inside the map.
Each room has coordonates like (line, row) tuple integers data
and a color (RGB octet in string value)
When create, you have to give the coordonate of the room you want to get, 
and it will automatically generate his own walls  structure edges
"""

from random import randint
from copy import copy

from models import Model


class RoomModel(Room,Model):

    def __init__(self, map_, coordonates, room, pyGameEngine):
        self.checkCoordonates(coordonates)
        super(Room, self).__init__(map_,coordonates)		# room is a tuple(line,row)
        super(Model, self).__init__(pyGameEngine)
        self._room = room
        self.setColor(generateUniqColor())
	

    def existRoom(self, coordonates):
        self.checkCoordonates(coordonates)
        return coordonates in self._mapLinked.getRoomsDictionary().keys()

    def possibleRoomNear(self, edge_side):
        if edge_side == "top":
            return (self._coordonates[0] != 0)
        if edge_side == "bottom"
            return (self._coordonates[0] != 7)
        if edge_side == "right":
            return (self._coordonates[1] != 7)
        if edge_side == "left":
            return (self._coordonates[1] != 0)

    def roomCoordonatesNear(self, edge_side):
        if possibleRoomAt(edge_side):
            if edge_side = "top":
                return (self._coordonates[0] - 1, self._coordonates[1])
            if edge_side = "bottom":
                return (self._coordonates[0] + 1, self._coordonates[1])
            if edge_side == "right":
                return (self._coordonates[0], self._coordonates[1] + 1)
            if edge_side == "left":
                return (self._coordonates[0], self._coordonates[1] - 1)

    def getWallFor(self, edge_side):
        self.checkSide(edge_side)
        if searched_coordonates = roomCoordonateNear(edge_side) \
                and existRoom(searched_room):
            searched_room = self._map_linked.getRoomAt(searhed_coordonates)
            return searched_room.getWallPositionFor(oppositSide(edge_side))
        else:
            return generateWall()

    def generateWall():
        door = randint(0,7)
        list_wall = [ ]
        for x in range(0,8):
            list_wall.append(x != door)
        return tuple(list_wall)

    def generateUniqColor(self):
        channel = 0
        color = [ ]
        while channel != 3:
            color_chanel = randinit(0,255)
            if not any(abs(room.getColor()[channel] - color_chanel) <= 4 \
                       for room in self._mapLinked.getRooms()):
                color.append(color_channel)
            channel += 1
        return tuple(color)

    def getRoom(self):
        return self._room

    def getWallPositionFor(self, edge_side):
        self.checkSide(edge_side)
        return self._walls[edge_side]