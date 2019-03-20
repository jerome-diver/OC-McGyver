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

    def checkCoordonates(self, coordonates):
        line = (coordonates[0] >= 0 and coordonates[0] <= 7)
        row = (coordonates[1] >= 0 and coordonates[1] <= 7)
        if not (line and row):
            raise Exception("Coordonates are wrong")

    def checkDirection(self, direction):
        if direction not in ["north","south","east","west"]:
            raise Exception("direction syntax is wrong")

    def oppositDirection(self, direction):
        if direction == "north":
          return "south"
        if direction == "south":
            return "north"
        if direction == "east":
            return "west"
        if direction == "west":
            return "east"