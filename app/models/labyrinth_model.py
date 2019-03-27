'''
MapModel is uniq and hold map datas get from ./app/map/map.txt file
The map has walls stored by coordonates keys for binary values
each binary value (half octet) represent a scheme of
wall position around a room (who is a square in this map with 15x15 rooms,
so there is 224 rooms).
_wallsN is a tuple contain possible binary code for an existing
north wall and so on for each direction of each room of the map.
'''

import binascii
import os.path

from models.model import *


class LabyrinthModel(Labyrinth, Model):

  def __init__(self, pyGameEngine):
    super(Labyrinth, self).__init__()
    super(Model, self).__init__(pyGameEngine)
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

  @statismethod
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
          self._walls_bytes[(row, column)] = binascii.unhexlify("0" + char)
      Labyrinth._columns = int(Labyrinth.columns / Labyrinth.rows)
