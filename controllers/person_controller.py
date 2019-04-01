'''
Controller for persons like Hero or guard who make them alive
in the game.
This class hold action's control for them.
'''

import pygame as pg

from controllers.controller import Controller
from controllers.collider_controller import Collider
from models.person_model import *
from views.person_view import *


class HeroController(Controller, Collider):

  def __init__(self, labyrinth_ctrl, guard_ctrl, game_engine):
    Controller.__init__(self, game_engine, labyrinth_ctrl)
    Collider.__init__(self, game_engine)
    self._guard_ctrl = guard_ctrl
    self._model = HeroModel(self)
    self._view = HeroView(self, self._model, game_engine)

  def setting_collisions(self):
    self.setting_collisions_for("labyrinth",
                                self.labyrinth_collision,
                                if_collid=False)
    self.setting_collisions_for("guard",
                                self.guard_collision)
    self.setting_collisions_for("objects",
                                self.object_collision,
                                do_kill=True)

  def get_hero(self):
    return self._model.get_hero()

  def get_guard(self):
    return self._model.get_guard()

  def labyrinth_collision(self, caller, dx, dy):
    pos = (caller._pos[0] + dx, caller._pos[1] + dy)
    caller._pos = pos

  def guard_collision(self, caller, dx, dy):
    hero = self._model
    guard = self._guard_ctrl._model
    if hero.can_make_sleeping():
      guard.inject_pill()
    if guard.is_sleeping():
      pos = (caller._pos[0] + dx, caller._pos[1] + dy)
      caller._pos = pos
    else:
      self._game_engine.end_game()

  def object_collision(self, caller, *args):
    caller.add_object()


class GuardController(Controller):

  def __init__(self, labyrinth_ctrl, game_engine):
    super().__init__(game_engine, labyrinth_ctrl)
    self._model = GuardModel(self)
    self._view = GuardView(self, self._model, game_engine)

