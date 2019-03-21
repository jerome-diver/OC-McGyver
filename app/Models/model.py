"""
Superclass Model embed 
model from MVC design pattern
"""

import os
import binascii

class Model:

    directions = ("north", "west", "south", "east")
    sides = ("top", "right", "bottom", "left")

    def __init__(self):
        pass

    def checkCoordonates(self, coordonates):
        line = (coordonates[0] >= 0 and coordonates[0] <= 7)
        row = (coordonates[1] >= 0 and coordonates[1] <= 7)
        if not (line and row):
            raise Exception("Coordonates are wrong")

    def checkDirection(self, direction):
        if direction not in self.directiosn:
            raise Exception("direction syntax is wrong")

    def checkSide(self, side):
        if side not in self.sides:
            raise Exception("side syntax is wrong")

    def oppositDirection(self, direction):
        if direction == "north":
          return "south"
        if direction == "south":
            return "north"
        if direction == "east":
            return "west"
        if direction == "west":
            return "east"

    def oppositSide(self, side):
        if side == "top":
          return "bottom"
        if side == "bottom":
            return "top"
        if side == "left":
            return "right"
        if side == "right":
            return "left"