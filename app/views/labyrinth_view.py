'''
The specific view of the map.
This load image of map inside the game view
'''

import os

import pygame as pg
from pygame.sprite import *

from models.labyrinth_model import LabyrinthModel
from views.sprites import LabyrinthSprite
from views.view import View


class LabyrinthView(View):

  _walls = {}       # { (row, col, side): LabyrinthView.Wall }
  _width = 600
  _height = 600
  _labyrinth_bg = (0, 240, 50)

  def __init__(self, labyrinthModel, group):
    super().__init__(labyrinthModel)
    self.group = group
    labyrinthModel.setImage(pg.Surface((_height, _width)), _map_bg)
    self._model = labyrinthModel
    self._image = labyrinthModel.getImage()
    self._rect = self._image.get_rect()
    self._rect.center = (_width, _height)

  @staticmethod
  def wallExist(wall):
    if LabyrinthView._walls:
      for oldWall in LabyrinthView._walls.values():
        if (wall.rect.topleft == oldWall.rect.topleft) and\
                (wall.rect.bottomright == oldWall.rect.bottomright):
          return True
    return False

  @staticmethod
  def showWalls(wall):
    for key, value in LabyrinthView._walls:
      sides = ("top", "right", "bottom", "left")
      bin_code = "{0:b}".format(ord(value)).zfill(4)[::-1]
      for index, power in enumerate(bin_code):
        if int(power) == 1:
          idd = (key[0], key[1], sides[index])
          newWall = self.Wall(idd)
          if not self.wallExist(newWall):
            LabyrinthView._walls[idd] = newWall
            self.group.add(LabyrinthView._walls[idd])
    print("there is", len(LabyrinthView._walls), "walls in the labyrinth")

    class Wall(Sprite):

      def __init__(self, idd):
        super().__init__()
        row, col, side = idd
