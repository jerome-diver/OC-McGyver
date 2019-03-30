'''
The Person object has a boring gamer life...
The Hero object's one has a little bit action to provide in the controller
But the Person base class care about set collisions handler
and usual's attributes eventually
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

  # it is possible there to create a collision event to be handle by
  # the controller manageCollisions() method
  # it is also possible to make this method
  # inside the view or the controller
  def canCollidWith(self, name, group):
    self._collidGroups[name] = group


"""
This Hero class is also a Sprite pygame class inherited from.
A Sprite is a container who handle the view
and must have minimum 2 attributs:
    self.image  (for handle image view)
    self.rect   (for handle position of this image)

The pygame idea is to create a surface
(who is also an image you can draw on)
then you can have this sprite to put inside a sprite-group
for handle events collisions or what ever it will happen in the game

This Sprite Hero class for example, who is also a Person,
can move and can react to collisions events
"""


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
    # but because of pygame way to do, it start there first...
    self.rect.topleft = (self._posX, self._posY)
    self._controller.keyPressed(self)

  def move(self, dx=0, dy=0):
    self.rect.topleft = (self._posX + dx, self._posY + dy)
    self._controller.manageCollisions(self, self._collidGroups, (dx, dy))

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
