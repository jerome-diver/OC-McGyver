'''
The Map object is the uniq map object who contain the labirynth map with his walls designs.
The map has 8 lines of 8 culumns rooms (64 rooms).
'''

import binascii
import os

import pygame as pg
from pygame.sprite import Sprite

from settings import *


class Labyrinth:

  _walls_N = (b'\x01', b'\x05', b'\x06', b'\x07',
              b'\x0b', b'\x0c', b'\x0e', b'\x0f')
  _walls_W = (b'\x02', b'\x05', b'\x08', b'\x09',
              b'\x0b', b'\x0c', b'\x0d', b'\x0f')
  _walls_S = (b'\x03', b'\x07', b'\x09', b'\x0a',
              b'\x0c', b'\x0d', b'\x0e', b'\x0f')
  _walls_E = (b'\x04', b'\x06', b'\x08', b'\x0a',
              b'\x0b', b'\x0d', b'\x0e', b'\x0f')

  def __init__(self):
    self._walls_bytes = {}    # { (row,column): byte }

  def __del__(self):
    if self.__dict__:
      for attr_keys in list(self.__dict__.keys()):
        del(self.__dict__[attr_keys])
        print(self.__class__.__name__, "attributes has has been deleted")

  def wall_positions(self):
    return self._walls_bytes

  def walls_position(self, room_coordonates):
    return self._walls_bytes[room_coordonates]


class Wall(Sprite):  # wall is a part view of a byte cell from Labyrinth()

  _numbers = 0
  _removed = 0

  def __init__(self, idd, adj):
    super().__init__()
    Wall._numbers += 1
    row, col, side = idd
    self.adjust = adj
    self.image = pg.Surface((45, 5)) if side in ["top", "bottom"] \
        else pg.Surface((5, 45))
    self.image.fill(LABYRINTH_WALL_COLOR)
    self.rect = self.image.get_rect()  # a sprite must have one
    # now a wall should be positionned inside his labyrinth
    position = (col * 40 + self.adjust[0],
                row * 40 + self.adjust[1])
    if side in ["top", "left"]:
      self.rect.topleft = position
    elif side == "bottom":
      self.rect.topleft = (position[0], position[1] + 40)
    elif side == "right":
      self.rect.topleft = (position[0] + 40, position[1])

  def __del__(self):
    Wall._numbers -= 1
    Wall._removed += 1

  def update(self):
    pass
