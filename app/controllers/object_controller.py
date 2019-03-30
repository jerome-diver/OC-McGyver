"""
This controller care about objects and actions when it does
collid with hero.
"""
import pygame as pg

from controllers import Controller


class ObjectController(Controller):

  def __init__(self, labyrinthModel, pyGameEngine):
    self().__init__(pyGameEngine)
    self._labyrinthModel = labyrinthModel
    self._objectModel = ObjectModel(self)
    self._objectViex = ObjectView(self, self._objectModel, pyGameEngine)
    self.settingCollisions()
    self.setPositionsObjects()

  def settingCollisions(self):
    objects = self._objectModel.getObjects()
    for object in objects:
      object.canCollidWith("hero", self._gameEngine.getGroup("hero"))

  def manageCollisions(self, caller):
    collisions = {}

  def setPositionsObjects(self):
    pass
