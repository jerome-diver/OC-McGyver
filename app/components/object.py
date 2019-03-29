'''
The Object class contain each object who can be find inside any room randomly.
'''
import pygame as pg
from pygame.sprite import Sprite


class Object(Sprite):

  def __init__(self, controller, name):
    super().__init__()
    self._counter = 0   # i prefer to slow down the update rate for manageCollisions
    self._controller = controller
    self._name = name
    if name == "pill":
      self.image = pg.image.load(pillImage).convert()
    elif name == "needle":
      self.image = pg.image.load(needleImage).convert()
    elif name == "diluent":
      self.image = pg.image.load(diluantImage).convert()

  def upadate(self):
    self.counter += 1
    if self.counter == 20:
      self.counter = 0
      self._controller.manageCollisions(self)
