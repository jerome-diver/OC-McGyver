"""
This controller care about objects and actions when it does
collid with hero.
"""
import pygame as pg

from controllers.controller import Controller
from models.object_model import ObjectModel
from views.object_view import ObjectView
from components.object import Object


class ObjectController(Controller):

  def __init__(self, labyrinth_ctrl, hero_ctrl, guard_ctrl, \
               game_engine):
    super().__init__(game_engine, labyrinth_ctrl)
    self._hero_ctrl = hero_ctrl
    self._guard_ctrl = guard_ctrl
    self._model = ObjectModel()
    self._view = ObjectView(self, self._model, game_engine)
    # this one know the hero instance, because ObjectController instance was
    # create after the HeroControlleur instance... that is why he call him
    # for explain it will collide with him probably.
    self.setting_collisions()

  # set hero
  def setting_collisions(self):
    group = self._game_engine.get_group("objects")
    self._hero_ctrl.can_collid_with(group)
