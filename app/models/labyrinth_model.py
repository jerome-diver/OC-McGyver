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

from components.labyrinth import *
from models.model import *


class LabyrinthModel(Labyrinth, Model):

  def __init__(self):
    super().__init__()
    if not Labyrinth._walls_bytes:  # only at first class creation time
      self.loadMap()

  def hasWallAt(self, room_coordonates, edge_position):
    checkDirection(edge_position)
    checkCoordonates(room_coordonates)
    if edge_position == "north":
      return Labyrinth.wallPosition(room_coordonates) in Labyrinth._wallsN
    elif edge_position == "south":
      return Labyrinth.wallPosition(room_coordonates) in Labyrinth._wallsS
    elif edge_position == "east":
      return Labyrinth.wallPosition(room_coordonates) in Labyrinth._wallsE
    elif edge_position == "west":
      return Labyrinth.wallPosition(room_coordonates) in Labyrinth._wallsW

  @staticmethod
  def wallPosition(room_coordonates):
    checkCoordonates(room_coordonates)
    return Labyrinth._walls_bytes[room_coordonates]

  @staticmethod
  def wallClockWisePosition(room_coordonates):
    checkCoordonates(room_coordonates)
    return (Labyrinth._walls_bytes[room_coordonates] in Labyrinth._wallsN,
            Labyrinth._walls_bytes[room_coordonates] in Labyrinth._wallsE,
            Labyrinth._walls_bytes[room_coordonates] in Labyrinth._wallsS,
            Labyrinth._walls_bytes[room_coordonates] in Labyrinth._wallsW)

  @staticmethod
  def loadMap():
    cwd = os.path.dirname(os.path.abspath(__file__))
    file = os.path.join(cwd, "../map/map.txt")
    with open(file, "r") as mapFile:
      for row, line in enumerate(mapFile):
        Labyrinth._rows += 1
        for column, char in enumerate(line.strip()):
          Labyrinth._columns += 1
          Labyrinth._walls_bytes[(row, column)
                                 ] = binascii.unhexlify("0" + char)
      Labyrinth._columns = int(Labyrinth._columns / Labyrinth._rows)
