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
    self._rows_columns = ()
    self._exit_coordonates = None
    self._name = "labyrinth"
    self.load_map()

  def get_name(self):
    return self._name

  def has_wall_at(self, room_coordonates, edge_position):
    check_direction(edge_position)
    check_coordonates(room_coordonates)
    if edge_position == "north":
      return self._labyrinth.wall_position(room_coordonates) \
          in Labyrinth._walls_N
    elif edge_position == "south":
      return self._labyrinth.wall_position(room_coordonates) \
          in Labyrinth._walls_S
    elif edge_position == "east":
      return self._labyrinth.wall_position(room_coordonates) \
          in Labyrinth._walls_E
    elif edge_position == "west":
      return self._labyrinth.wall_position(room_coordonates) \
          in Labyrinth._walls_W

  def wall_position(self, room_coordonates):
    check_coordonates(room_coordonates)
    return self._labyrinth.walls_position(room_coordonates)

  def wall_clock_wise_position(self, room_coordonates):
    check_coordonates(room_coordonates)
    return (self._l._walls_bytes[room_coordonates] in Labyrinth._walls_N,
            self._l._walls_bytes[room_coordonates] in Labyrinth._walls_E,
            self._l._walls_bytes[room_coordonates] in Labyrinth._walls_S,
            self._l._walls_bytes[room_coordonates] in Labyrinth._walls_W)

  def get_best_hero_position(self):  # return initial best HHero position
    return (int((self._rows_columns[0] - 1) * 40 + ADJ_X + 7),
            int((self._rows_columns[1] - 1) * 40 + ADJ_Y + 7))

  def get_guard_position(self):
    return self._exit_coordonates

  def load_map(self):
    _row, _col = 0, 0
    with open(LABYRINTH_FILE, "r") as file:
      for row, line in enumerate(file):
        _row += 1
        _col = 0
        for column, char in enumerate(line.strip()):
          _col += 1
          self._walls_bytes[(row, column)
                            ] = binascii.unhexlify("0" + char)
    self._rows_columns = (_row, _col)

  def get_walls(self):
    return self._walls

  def set_exit_coordonates(self, row, col):
    self._exit_coordonates = (int(col * 40 + ADJ_X + 8),
                              int(row * 40 + ADJ_Y))
