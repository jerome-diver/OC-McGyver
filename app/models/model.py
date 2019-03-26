"""
Superclass Model embed 
model from MVC design pattern
"""

import os
import binascii
from pygame.sprite import *


class Model(Sprite):

    _directions = ("north", "east", "south", "west")
    _sides = ("top", "right", "bottom", "left")
    _red = (255,0,0)
    _black = (0,0,0)
    _white = (255,255,255)
    _width = 600
    _height = 600

    def __init__(self, pyGameEngine):
        super().__init__()
        self._gameEngine = pyGameEngine

    def checkCoordonates(self, coordonates):
        line = (coordonates[0] >= 0 and coordonates[0] <= 7)
        row = (coordonates[1] >= 0 and coordonates[1] <= 7)
        if not (line and row):
            raise Exception("Coordonates are wrong")

    def checkDirection(self, direction):
        if direction not in self._directions:
            raise Exception("direction syntax is wrong")

    def checkSide(self, side):
        if side not in self._sides:
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

    def getModel(self):
        return self

    def gameEngine(self):
        return self._gameEngine

    def setImage(self, img, color):
        self._image = img
        self._image.fill(color)

    def getImage(self):
        return self._image