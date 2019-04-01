'''
The specific view of the map.
This load image of map inside the game view
'''

from components.labyrinth import Wall
from models.labyrinth_model import LabyrinthModel
from settings import *
from views.view import View


class LabyrinthView(View):

  def __init__(self, controller, model, game_engine):
    super().__init__(controller, model, game_engine)
    self.create_walls()
    self._game_engine.add_sprites_to_group(self._model.get_walls(),
                                           "labyrinth")

  def wall_exist(self, wall):
    if len(self._model._walls) != 0:
      for old_wall in self._model.get_walls():
        if (wall.rect.topleft == old_wall.rect.topleft) and\
           (wall.rect.bottomright == old_wall.rect.bottomright):
          return True
    return False

  def create_walls(self):
    for key, value in self._model.wall_positions().items():
      sides = ("top", "right", "bottom", "left")
      bin_code = "{0:b}".format(ord(value)).zfill(4)[::-1]
      for index, bit in enumerate(bin_code):
        if bit == "1":
          idd = (key[0], key[1], sides[index])
          new_wall = Wall(idd, (ADJ_X, ADJ_Y))
          if not self.wall_exist(new_wall):
            self._model._walls.append(new_wall)
          else:
            del new_wall
        else:
          if not self._model._exit_position:
            self.find_exit_position(key, index)
    print("There is", Wall._numbers, "walls in the labyrinth\n",
          Wall._removed, "has been remouved (doubles found).")

  def find_exit_position(self, key, index):
    # i test only the concerned peripheral's cells AND externals walls:
    # first row, last column, last row and first column (clock wise from top
    # AND for each, clk wise from top side wall index: 0 -> 3 are tested
    if (key[0] == 0 and index == 0) or \
       (key[1] == (self._model._rows_columns[1] - 1) and index == 1) or \
       (key[0] == (self._model._rows_columns[0] - 1) and index == 2) or \
       (key[1] == 0 and index == 3):
      self._model.set_exit_coordonates(key[0], key[1])
