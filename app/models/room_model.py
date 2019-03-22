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
from components import Room


class RoomModel(components.Room,Model):

    def __init__(self, map_, coordonates):		# room is a tuple(line,row)
        checkCoordonates(coordonates)
        super().__init__(map_,coordonates)
        self.setColor(genereateUniqColor(map_))
	

    def existRoom(self, coordonates):
        checkCoordonates(coordonates)
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
        checkSide(edge_side)
        if searched_room = roomCoordonateNear(edge_side) \
                and existRoom(searched_room):
            return self._rooms[searched_room[oppositSide(edge_side)]]
        else:
            return generateWall()

    def generateWall():
        door = randint(0,7)
        list_wall = [ ]
        for x in range(0,8):
            list_wall.append(x != door)
        return tuple(list_wall)

    def generateUniqColor(self):
        while True:
            color_chanel = randinit(0,255)
            if not any(int(room.getColor().split('#')[1], 16) \
                       - color_chanel <= 4 \
                       for room in self._mapLinked.getRooms()):
                return str("#" + hex(color_chanel).split('0x')[1].zfill(3))
