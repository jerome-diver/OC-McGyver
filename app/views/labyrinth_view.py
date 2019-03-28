'''
The specific view of the map.
This load image of map inside the game view
'''

import os

import pygame as pg
from pygame.sprite import *

from models.labyrinth_model import LabyrinthModel
from settings import *
from views.view import View


class LabyrinthView(View):

  _walls = {}       # { (row, col, side): LabyrinthView.Wall }
  _width = 600
  _height = 600
  _labyrinth_bg = (0, 240, 50)

  def __init__(self, labyrinthModel, gameEngine):
    super().__init__(labyrinthModel, gameEngine)
    self.gameEngine.createGroup("labyrinth")
    self.adjX = (width - LabyrinthView._width) / 2
    self.adjY = (height - LabyrinthView._height) / 2
    if not LabyrinthView._walls:    # only at first class creation time
      self.createWalls()
      self.gameEngine.addSpritesToGroup(LabyrinthView._walls.values(),
                                        "labyrinth")

  @staticmethod
  def getbestHeroPosition():  # return initial best HHero position
    return (LabyrinthView.rows * 40 + self.adjX - 35,
            LabyrinthView.columns * 40 + self.adjY - 35)

  @staticmethod
  def wallExist(wall):
    if LabyrinthView._walls:
      for oldWall in LabyrinthView._walls.values():
        if (wall.rect.topleft == oldWall.rect.topleft) and\
                (wall.rect.bottomright == oldWall.rect.bottomright):
          return True
    return False

  def createWalls(self):
    for key, value in self._model.wallPositions().items():
      sides = ("top", "right", "bottom", "left")
      bin_code = "{0:b}".format(ord(value)).zfill(4)[::-1]
      for index, power in enumerate(bin_code):
        if int(power) == 1:
          idd = (key[0], key[1], sides[index])
          newWall = Wall(idd, (self.adjX, self.adjY))
          if not self.wallExist(newWall):
            LabyrinthView._walls[idd] = newWall
          else:
            del newWall
    print("There is", Wall._numbers, "walls in the labyrinth\n",
          Wall._removed, "has been remouved (doubles found).")


class Wall(Sprite):

  _numbers = 0
  _removed = 0

  def __init__(self, idd, adj):
    super().__init__()
    Wall._numbers += 1
    row, col, side = idd
    self.adjX, self.adjY = adj
    self.image = pg.Surface((45, 5)) if side in ["top", "bottom"] \
        else pg.Surface((5, 40))
    self.image.fill(red)
    self.rect = self.image.get_rect()  # a sprite must have one
    # now a wall should be positionned inside his labyrinth
    position = (col * 40 + self.adjX,
                row * 40 + self.adjY)
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
