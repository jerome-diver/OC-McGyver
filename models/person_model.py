'''
Model of Person and specific Person like Hero or Guard,
 who have some specific features added.
The superclass is a Model class
'''

from components.person import Guard, Hero
from models.model import Model
from settings import *


class GuardModel(Guard, Model):

  def __init__(self, controller):
    Guard.__init__(self, controller)
    Model.__init__(self)
    self._sleeping = False
    exit_coordonates = self._controller\
                           ._labyrinth_ctrl\
                           ._model\
                           .get_exit_coordonates()
    self.set_coordonates(exit_coordonates)

  def inject_pill(self):
    self._sleeping = True

  def is_sleeping(self):
    return self._sleeping

  def set_position(self, position):
    super(GuardModel, self).set_position(position)

class HeroModel(Hero, Model):

  def __init__(self, controller):
    Hero.__init__(self, controller)
    Model.__init__(self)
    max_cells = self._controller.\
                     _labyrinth_ctrl.\
                     _model._rows_columns
    hero_coordonates = (max_cells[0] - 1, max_cells[1] - 1)
    self.set_coordonates(hero_coordonates)

  def can_make_sleeping(self):
    return len(self._objects) == 3

  def set_position(self, coordonates):
    pos = (int(coordonates[0] * 40 + ADJ_X + 8),
           int(coordonates[1] * 40 + ADJ_Y + 8))
    super(HeroModel, self).set_position(pos)
