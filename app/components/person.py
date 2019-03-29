'''
The Person object has a boring gamer life...
The Hero object's one has a little bit action to provide in the controller
'''

import pygame as pg
from pygame.sprite import Sprite

from settings import *


class Person:

  def __init__(self, controller, name):
    self._controller = controller
    self._name = name
    self._posX, self._posY = (0, 0)
    self._collidGroups = {}

  def getName(self):
    return self._name

  def setName(self, name):
    self._name = name

  def setPosition(self, pos):
    self._posX, self._posY = pos

  def canCollidWith(self, name, group):
    self._collidGroups[name] = group


class Hero(Person, Sprite):

  def __init__(self, controller, name):
    Person.__init__(self, controller, name)
    Sprite.__init__(self)
    try:
      self.image = pg.image.load(heroFile).convert()
    except pg.error:
      print("can not load image:", heroFile)
      raise SystemExit
    self.image = pg.transform.scale(self.image, (30, 30))
    self.rect = self.image.get_rect()

  def update(self):
    # what's need to get control goes in the controller
    self.rect.topleft = (self._posX, self._posY)
    self._controller.keyPressed(self)

  def move(self, dx=0, dy=0):
    self.rect.topleft = (self._posX + dx, self._posY + dy)
    collisions = {}
    for name, group in self._collidGroups.items():
      collisions[name] = pg.sprite.spritecollide(self, group, False)
    if "labyrinth" in collisions.keys():
      if not collisions["labyrinth"]:
        self._posX += dx
        self._posY += dy
    if "guard" in collisions:
      pass

  def getHero(self):
    return self


class Guard(Person, Sprite):

  def __init__(self, controller, name):
    Person.__init__(self, controller, name)
    Sprite.__init__(self)
    try:
      self.image = pg.image.load(guardFile).convert()
    except pg.error:
      print("can not load guard file:", guardFile)
      raise SystemExit
    self.image = pg.transform.scale(self.image, (30, 30))
    self.rect = self.image.get_rect()

  def update(self):
    self.rect.topleft = (self._posX, self._posY)

  def getGuard(self):
    return self
