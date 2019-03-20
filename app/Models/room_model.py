"""
RoommModel abject represent a room inside the map.
Each room has coordonates like (line, row) tuple integers data
and a color (RGB octet in string value)
When create, you have to give the coordonate of the room you want to get, 
and it will automatically generate his own walls  structure edges
"""

from random import randint
from copy import copy
from model import Model


class RoomModel(Model):

	walls = { }	# {"edge_direction": (boolean) }
	full_close = (True,True,True,True,True,True,True,True)
	color = "#FFF"

	def __init__(self, map, room):		# room is a tuple(line,row)
		checkRoom(room)
		self.room = room
		self.walls = loadRoom(map)
		map.appendRoom(self)
		self.color = genereateUiqColor(map)
	
	def getCoordonates(self):
		return self.room

	def existRoom(self, room):
		checkRoom(room)
		return room in self.rooms[room]

	def hasRoomAt(self, direction):
		checkDirection(direction)
		if direction == "north":
			return (room[0] != 0)
		if direction == "south"
			return (room[0] != 7)
		if direction == "east":
			return (room[1] != 7)
		if direction == "west":
			return (room[1] != 0)

	def roomCoordonatesAt(self, direction):
		checkDirection(direction)
		if hasRoomAt(direction):
			if direction = "north":
				return (self.room[0] - 1, self.room[1])
			if direction = "south":
				return (self.room[0] + 1, self.room[1])
			if direction == "east":
				return (self.room[0], self.room[1] + 1)
			if direction == "west":
				return (self.room[0], self.room[1] - 1)

	def getWallFor(self, edge):
		if searched_room = roomCoordonateAt(edge) \
				and existRoom(searched_room):
			return self.rooms[searched_room[oppositDirection(edge)]]
		else:
			return generateWall()

	def generateWall():
		door = randint(0,7)
		list_wall = [ ]
		for x in range(0,8):
			list_wall.append(x != door)
		return tuple(list_wall)

    def loadRoom(self, map):
    	for index,wall_cwp in enumerate(map.clockWisePosition(self.room)):
    		if wall_cwp:
    			direction = self.directions[index]
    			self.walls[direction] = getWallFor(direction)
    		else:
    			self.walls[direction] = copy(self.full_close)
    	self.rooms[room] = walls

    def generateUniqColor(self, map):
    	ok_rgb = 0
    	rgb = {"R": 0, "G": 0, "B": 0}
    	while ok != 3:
    		ok_chanel = False
    		while not ok_chanel:
		    	color_chanel = randinit(0,15)
