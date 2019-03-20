"""
Superclass Model embed 
model from MVC design pattern
"""

import os
import binascii

class Model:

	rooms = { }		# { (line,row): { position: (boolean) } }
	directions = ("north", "west", "south", "east")

	def __init__(self):
	pass

    def Get(self, param):
    	pass

    def Set(self, param):
    	pass

    def checkRoom(self, room):
    	line = (room[0] >= 0 and room[0] <= 7)
    	row = (room[1] >= 0 and room[1] <= 7)
    	if not (line and row):
    		raise Exception("Room doesn't exist")

    def checkDirection(self, direction):
    	if direction not in ["north","south","east","west"]:
    		raise Exception("direction definition is wrong")
    		
	def oppositDirection(self, direction):
		if direction == "north":
			return "south"
		if direction == "south":
			return "north"
		if direction == "east":
			return "west"
		if direction == "west":
			return "east"