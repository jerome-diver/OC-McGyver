'''
Controller for persons like Hero or guard who make them alive
in the game.
This class hold action's control for them.
'''

import pygame as pg

from controllers.controller import Controller
from models.person_model import *
from views.person_view import *


class PersonController(Controller):

  def __init__(self, labyrinthModel, pyGameEngine):
    super().__init__(pyGameEngine)
    self._labyrinthModel = labyrinthModel
    self._heroModel = HeroModel(self)
    self._heroView = HeroView(self, self._heroModel, pyGameEngine)

  def keyPressed(self, person):
    key = pg.key.get_pressed()
    if key[pg.K_LEFT]:
      person.move(dx=-1)
    if key[pg.K_RIGHT]:
      person.move(dx=1)
    if key[pg.K_UP]:
      person.move(dy=-1)
    if key[pg.K_DOWN]:
      person.move(dy=1)
    if key[pg.K_LEFT] and \
       (key[pg.K_LSHIFT] or key[pg.K_RSHIFT]):
      person.move(dx=-2)
    if key[pg.K_RIGHT] and \
       (key[pg.K_LSHIFT] or key[pg.K_RSHIFT]):
      person.move(dx=2)
    if key[pg.K_UP] and \
       (key[pg.K_LSHIFT] or key[pg.K_RSHIFT]):
      person.move(dy=-2)
    if key[pg.K_DOWN] and \
       (key[pg.K_LSHIFT] or key[pg.K_RSHIFT]):
      person.move(dy=2)

  def getLabyrinthModel(self):
    return self._labyrinthModel
