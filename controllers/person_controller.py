'''
Controller for persons like Hero or guard who make them alive
in the game.
This class hold action's control for them.
'''

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

  def check_exit(self):
    if self._model._pos[0] < ADJ_X or self._model._pos[1] < ADJ_Y:
      en = self._game_engine
      text = "You win !\n\nMac Gyver can go back home now...\n\nBye bye..."
      en.actions_delayed(tempo=5,
                         action_start=en.message,
                         sa_args=(text, 38, GREEN),
                         action_end=en.end_game, e_args=None)

  def labyrinth_collision(self, caller, dx, dy):
    pos = (caller._pos[0] + dx, caller._pos[1] + dy)
    caller._pos = pos

  def guard_collision(self, caller, dx, dy, sprite):
    hero = self._model
    guard = self._guard_ctrl._model
    if hero.can_make_sleeping():
      guard.inject_pill()
    if guard.is_sleeping():
      pos = (caller._pos[0] + dx, caller._pos[1] + dy)
      caller._pos = pos
    else:
      text = "You loose !\n\nGAME OVER"
      en = self._game_engine
      en.actions_delayed(tempo=5,
                         action_start=en.message,
                         sa_args=(text, 38, RED),
                         action_end= en.end_game, e_args=None)
      #self._game_engine.game_over()

  def object_collision(self, caller, *args):
    caller.add_object(args[2])
    en = self._game_engine
    text = "Yeh... you get an other the " + args[2]._name
    en.actions_delayed(tempo=2,
                       action_start=en.message,
                       sa_args=(text, 38, GREEN, None, 0))


class GuardController(Controller):

  def __init__(self, labyrinth_ctrl, game_engine):
    super().__init__(game_engine, labyrinth_ctrl)
    self._model = GuardModel(self)
    self._view = GuardView(self, self._model, game_engine)

  def get_guard(self):
    return self._model.get_guard()


