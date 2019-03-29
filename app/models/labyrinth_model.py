'''
LabyrinthModel is embed labyrinth map datas get from
./app/map/map.txt file and provide some Model typed methods
to access Labyrinth object.
The map has walls stored by coordonates keys binary values.
Each binary value (a half octet) represent a scheme of
wall position for one cell of the labyrinth
(a cell is a square in this map, and there is 15x15 cells or 225 total cells).
Each wall is constructed from these binary data stored in map.txt file.
'''

import binascii
import os.path

import pygame as pg
from pygame.sprite import *

from components.labyrinth import *
from models.model import *
from settings import *


class LabyrinthModel(Labyrinth, Model):

  def __init__(self):
    super().__init__()
    self._walls = []       # [ Wall ]
    self._rowsColumns = ()
    self._name = "labyrinth"
    self.loadMap()

  def getName(self):
    return self._name

  def hasWallAt(self, room_coordonates, edge_position):
    checkDirection(edge_position)
    checkCoordonates(room_coordonates)
    if edge_position == "north":
      return self._labyrinth.wallPosition(room_coordonates) \
          in Labyrinth._wallsN
    elif edge_position == "south":
      return self._labyrinth.wallPosition(room_coordonates) \
          in Labyrinth._wallsS
    elif edge_position == "east":
      return self._labyrinth.wallPosition(room_coordonates) \
          in Labyrinth._wallsE
    elif edge_position == "west":
      return self._labyrinth.wallPosition(room_coordonates) \
          in Labyrinth._wallsW

  def wallPosition(self, room_coordonates):
    checkCoordonates(room_coordonates)
    return self._labyrinth.wallsPosition(room_coordonates)

  def wallClockWisePosition(self, room_coordonates):
    checkCoordonates(room_coordonates)
    return (self._l._walls_bytes[room_coordonates] in Labyrinth._wallsN,
            self._l._walls_bytes[room_coordonates] in Labyrinth._wallsE,
            self._l._walls_bytes[room_coordonates] in Labyrinth._wallsS,
            self._l._walls_bytes[room_coordonates] in Labyrinth._wallsW)

  def getbestHeroPosition(self):  # return initial best HHero position
    return (int(self._rowsColumns[0] * 40 + adjX - 35),
            int(self._rowsColumns[1] * 40 + adjY - 33))

  def getGuardPosition(self):
    return (250, 150)

  def loadMap(self):
    row, col = 0, 0
    with open(labyrinthFile, "r") as mapFile:
      for row, line in enumerate(mapFile):
        row += 1
        col = 0
        for column, char in enumerate(line.strip()):
          col += 1
          self._walls_bytes[(row, column)
                            ] = binascii.unhexlify("0" + char)
    self._rowsColumns = (row, col)

  def getWalls(self):
    return self._walls
