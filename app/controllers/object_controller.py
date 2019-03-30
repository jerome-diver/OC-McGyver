"""
This controller care about objects and actions when it does
collid with hero.
"""
import pygame as pg

from controllers import Controller


class ObjectController(Controller):

  def __init__(self, labyrinth_model, game_engine):
    self().__init__(game_engine)
    self._labyrinth_model = labyrinth_model
    self._object_model = ObjectModel(self)
    self._object_view = ObjectView(self, self._object_model, game_engine)
    self.setting_collisions()

  def setting_collisions(self):
    objects = self._objectModel.get_objects()
    for object in objects:
      object.can_collid_with("hero", self._game_engine.get_group("hero"))

  def manage_collisions(self, caller):
    collisions = {}
