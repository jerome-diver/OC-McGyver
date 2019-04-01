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
    self._exit_coordonates = None # cell position (row,col)
    self._exit_position = None    # exit position (x,y)
    self._name = "labyrinth"
    self.load_map()

  def get_name(self):
    return self._name

  def set_exit_coordonates(self, row, col):
    self._exit_coordonates = (row, col)
    self.set_exit_position(row, col)

  def get_exit_coordonates(self):
    return self._exit_coordonates

  def get_exit_position(self):
    return self._exit_position

  def set_exit_position(self, row, col):
    self._exit_position = (int(col * 40 + ADJ_X),
                           int(row * 40 + ADJ_Y))

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

