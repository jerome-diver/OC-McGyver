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

  def __init__(self, labyrinth_model, game_engine):
    super().__init__(game_engine)
    self._labyrinth_model = labyrinth_model
    self._hero_model = HeroModel(self)
    self._hero_view = HeroView(self, self._hero_model, game_engine)
    self._guard_model = GuardModel(self)
    self._guard_view = GuardView(self, self._guard_model, game_engine)
    self.setting_collisions()

  def setting_collisions(self):
    hero = self._hero_model.get_hero()
    hero.can_collid_with("labyrinth", self._game_engine.get_group("labyrinth"))
    hero.can_collid_with("guard", self._game_engine.get_group("guard"))

  def manage_collisions(self, caller, collid_groups, posit):
    collisions = {}
    issue = False
    for name, group in collid_groups.items():
      collisions[name] = pg.sprite.spritecollide(caller, group, False)
    if "labyrinth" in collisions.keys():
      if not collisions["labyrinth"]:
        caller._pos_x += posit[0]
        caller._pos_y += posit[1]
    if "guard" in collisions.keys():
      if collisions["guard"]:
        issue = self.conflictual_contact()
        if issue == False:
          self._game_engine.end_game()

  def get_labyrinth_model(self):
    return self._labyrinth_model

  def get_hero(self):
    return self.hero_model.get_hero()

  def conflictual_contact(self):
    hero = self._hero_model
    guard = self._guard_model
    if hero.can_make_sleeping():
      guard.inject_pill()
    return guard.is_sleeping()
