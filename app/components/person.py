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
    self._pos_x, self._pos_y = (0, 0)
    self._collid_groups = {}

  def get_name(self):
    return self._name

  def set_name(self, name):
    self._name = name

  def set_position(self, pos):
    self._pos_x, self._pos_y = pos

  # it is possible there to create a collision event to be handle by
  # the controller manageCollisions() method
  # it is also possible to make this method
  # inside the view or the controller
  def can_collid_with(self, name, group):
    self._collid_groups[name] = group


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
      self.image = pg.image.load(HERO_FILE).convert()
    except pg.error:
      print("can not load image:", HERO_FILE)
      raise SystemExit
    self.image = pg.transform.scale(self.image, (30, 30))
    self.rect = self.image.get_rect()

  def update(self):
    # what's need to get control goes in the controller
    # but because of pygame way to do, it start there first...
    self.rect.topleft = (self._pos_x, self._pos_y)
    self._controller.key_pressed(self)

  def move(self, dx=0, dy=0):
    self.rect.topleft = (self._pos_x + dx, self._pos_y + dy)
    self._controller.manage_collisions(self, self._collid_groups, (dx, dy))

  def get_hero(self):
    return self


class Guard(Person, Sprite):

  def __init__(self, controller, name):
    Person.__init__(self, controller, name)
    Sprite.__init__(self)
    try:
      self.image = pg.image.load(GUARD_FILE).convert()
    except pg.error:
      print("can not load guard file:", GUARD_FILE)
      raise SystemExit
    self.image = pg.transform.scale(self.image, (30, 30))
    self.rect = self.image.get_rect()

  def update(self):
    self.rect.topleft = (self._pos_x, self._pos_y)

  def get_guard(self):
    return self
