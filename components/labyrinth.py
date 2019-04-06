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

  def __init__(self):
    self._walls_bytes = {}    # { (row,column): byte }

  def wall_positions(self):
    return self._walls_bytes


class Wall(Sprite):  # wall is a part view of a byte cell from Labyrinth()

  _numbers = 0
  _removed = 0

  def __init__(self, idd, adj):
    super().__init__()
    Wall._numbers += 1
    self.row, self.col, side = idd
    self.adjust = adj
    self._name = "Wall"
    self.image = pg.Surface((45, 5)) if side in ["top", "bottom"] \
        else pg.Surface((5, 45))
    self.image.fill(LABYRINTH_WALL_COLOR)
    self.rect = self.image.get_rect()  # a sprite must have one
    # now a wall should be positionned inside his labyrinth
    position = (self.col * 40 + self.adjust[0],
                self.row * 40 + self.adjust[1])
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
