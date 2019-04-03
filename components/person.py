'''
The Person object has a boring gamer life...
The Hero object's one has a little bit action to provide in the controller
But the Person base class care about set collisions handler
and usual's attributes eventually
'''

import pygame as pg
from pygame.sprite import Sprite

from settings import *


# common attributes and methods for Guard and Hero
class Person:

  def __init__(self, controller, name):
    self._controller = controller
    self._name = name
    self._pos = None          # screen position in pixels (x,y)
    self._coordonates = None  # cells position (row,col)

  def set_position(self, pos):
    self._pos = pos

  def set_coordonates(self, coordonates):
    self._coordonates = coordonates

  def get_name(self):
    return self._name

"""
These Hero and Guerd class are also Sprites pygame class inherited from.

A Sprite is a container who handle the view
and must have minimum 2 attributs:
    self.image  (for handle image view)
    self.rect   (for handle position of this image)

The pygame idea is to create a surface
(who is also an image you can draw on)
then you can put this sprite inside a sprite-group
for handle events collisions or what ever it will happen in the game

These Guard and Hero class for example, who are also Person and Collider,
can move and can react to collisions events and store groups they can 
collid with by the Collider class
"""


class Hero(Person, Sprite):

  def __init__(self, controller):
    Person.__init__(self, controller, "hero")
    Sprite.__init__(self)
    self._objects = []  # list of objects found
    try:
      self.image = pg.image.load(HERO_FILE).convert()
    except pg.error:
      print("can not load image:", HERO_FILE)
      raise SystemExit
    self.image = pg.transform.scale(self.image, (30, 30))
    self.rect = self.image.get_rect()

  # the sprite need it for update things
  def update(self):
    self.rect.topleft = self._pos
    self._controller.key_pressed(self)

  def move(self, dx=0, dy=0):
    self.rect.topleft = (self._pos[0] + dx, self._pos[1] + dy)
    self._controller.manage_collisions(self, dx, dy)
    self._controller.check_exit()

  def get_hero(self):
    return self

  # the objects we find... we hold them in an attribute list
  def add_object(self, obj):
    if len(self._objects) < 3:
      self._objects.append(obj)

class Guard(Person, Sprite):

  def __init__(self, controller):
    Person.__init__(self, controller, "guard")
    Sprite.__init__(self)
    try:
      self.image = pg.image.load(GUARD_FILE).convert()
    except pg.error:
      print("can not load guard file:", GUARD_FILE)
      raise SystemExit
    self.image = pg.transform.scale(self.image, (30, 30))
    self.rect = self.image.get_rect()

  def update(self):
    self.rect.topleft = self._pos

  def get_guard(self):
    return self
