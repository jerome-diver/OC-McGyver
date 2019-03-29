'''
The specific view of the map.
This load image of map inside the game view
'''

from components.labyrinth import Wall
from models.labyrinth_model import LabyrinthModel
from settings import *
from views.view import View


class LabyrinthView(View):

  def __init__(self, controller, model, gameEngine):
    super().__init__(controller, model, gameEngine)
    self.createWalls()
    self._gameEngine.addSpritesToGroup(self._model.getWalls(),
                                       "labyrinth")

  def wallExist(self, wall):
    if len(self._model._walls) != 0:
      for oldWall in self._model.getWalls():
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
          newWall = Wall(idd, (adjX, adjY))
          if not self.wallExist(newWall):
            self._model._walls.append(newWall)
          else:
            del newWall
    print("There is", Wall._numbers, "walls in the labyrinth\n",
          Wall._removed, "has been remouved (doubles found).")
