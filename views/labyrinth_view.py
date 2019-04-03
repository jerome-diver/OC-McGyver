'''
The specific view of the map.
This load image of map inside the game view
'''

import time

from components.labyrinth import Wall
from settings import *
from views.view import View


class LabyrinthView(View):

  start_time = int(time.time())

  def __init__(self, controller, model, game_engine):
    super().__init__(controller, model, game_engine)
    self.create_walls()
    self._game_engine.add_sprites_to_group(self._model.get_walls(),
                                           "labyrinth")
    self.start_timer()

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
      # format the char to be a representation of
      # binary code with 4 default chars long
      bin_code = "{0:b}".format(ord(value)).zfill(4)[::-1]
      # split it with index
      for index, bit in enumerate(bin_code):
        if bit == "1":    # bit high mean that ther is a wall there
          idd = (key[0], key[1], sides[index])
          new_wall = Wall(idd, (ADJ_X, ADJ_Y))
          # we add it only if it doesn't exist allready
          if not self.wall_exist(new_wall):
            self._model._walls.append(new_wall)
          else:
            del new_wall
        else:       # bit down => no wall there
          # if the exit is not define allready
          if not self._model._exit_position:
            # try to find if this wall is the exit of the labyrinth
            self.find_exit_position(key, index)

  # is it an exit there ?
  def find_exit_position(self, key, index):
    # i test only the concerned peripheral's cells AND externals walls:
    # first row, last column, last row and first column (clock wise from top
    # AND for each, clk wise from top side wall index: 0 -> 3 are tested
    if (key[0] == 0 and index == 0) or \
       (key[1] == (self._model._rows_columns[1] - 1) and index == 1) or \
       (key[0] == (self._model._rows_columns[0] - 1) and index == 2) or \
       (key[1] == 0 and index == 3):
      self._model.set_exit_coordonates(key[0], key[1])

  # print the timer of the labyrinth game
  def show_timer(self):
    timer = MAX_TIMER_GAME - (int(time.time()) -
                              LabyrinthView.start_time)
    text = "time left: " + str(timer) + " seconds"
    y_pos = HEIGHT - 50
    self._game_engine.message(text, 24, WHITE, 20, y_pos)

  # send the timer rint to background action as long as
  # the game as the timer max time is define
  def start_timer(self):
    en = self._game_engine
    en.actions_delayed(tempo = MAX_TIMER_GAME,
                       action_start=self.show_timer,
                       action_end=en.end_game,
                       e_args=None)


