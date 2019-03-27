'''
The specific view of the map.
This load image of map inside the game view
'''

import os

import pygame as pg
from pygame.sprite import *

from models.labyrinth_model import LabyrinthModel
from views.view import View


class LabyrinthView(View):

  _walls = {}       # { (row, col, side): LabyrinthView.Wall }
  _width = 600
  _height = 600
  _labyrinth_bg = (0, 240, 50)
  adjX = (View._width - 600) / 2
  adjY = (View._height - 600) / 2

  def __init__(self, labyrinthModel, gameEngine, groupName):
    super().__init__(labyrinthModel, gameEngine)
    self.groupName = groupName
    self.image = pg.Surface((LabyrinthView._width, LabyrinthView._height))
    if not LabyrinthView._walls:    # only at first class creation time
      self.showWalls()

  @staticmethod
  def getbestHeroPosition():  # return initial best HHero position
    return (LabyrinthView.rows * 40 + LabyrinthView.adjX - 35,
            LabyrinthView.columns * 40 + LabyrinthView.adjY - 35)

  @staticmethod
  def wallExist(wall):
    if LabyrinthView._walls:
      for oldWall in LabyrinthView._walls.values():
        if (wall.rect.topleft == oldWall.rect.topleft) and\
                (wall.rect.bottomright == oldWall.rect.bottomright):
          return True
    return False

  def showWalls(self):
    for key, value in self._model.wallPositions().items():
      sides = ("top", "right", "bottom", "left")
      bin_code = "{0:b}".format(ord(value)).zfill(4)[::-1]
      for index, power in enumerate(bin_code):
        if int(power) == 1:
          idd = (key[0], key[1], sides[index])
          newWall = self.Wall(idd)
          if not self.wallExist(newWall):
            LabyrinthView._walls[idd] = newWall
            self.gameEngine.addSpriteToGroup(LabyrinthView._walls[idd],
                                             self.groupName)
    print("there is", len(LabyrinthView._walls), "walls in the labyrinth")

  class Wall(Sprite):

    def __init__(self, idd):
      super().__init__()
      row, col, side = idd
      self.image = pg.Surface((45, 5)) if side in ["top", "bottom"] \
          else pg.Surface((5, 40))
      if side in ["top", "bottom"]:    # horizontal walls
        pg.draw.rect(self.image, View._red, [0, 0, 45, 5])
      elif side in ["left", "right"]:  # vertical walls
        pg.draw.rect(self.image, View._red, [0, 0, 5, 40])
      self.rect = self.image.get_rect()  # a sprite must have one
      # now a wall should be positionned inside his labyrinth
      position = (col * 40 + LabyrinthView.adjX,
                  row * 40 + LabyrinthView.adjY)
      if side in ["top", "left"]:
        self.rect.topleft = position
      elif side == "bottom":
        self.rect.topleft = (position[0], position[1] + 40)
      elif side == "right":
        self.rect.topleft = (position[0] + 40, position[1])

    def update(self):
      pass
