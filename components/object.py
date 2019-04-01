'''
The Object class contain each object who can be find inside any room randomly.
it has to get a name at create time, because this name
is specific for the object image to show.
'''
import pygame as pg
from pygame.sprite import Sprite

from settings import *
from controllers.collider_controller import Collider


class Object(Sprite):

  _collid_groups = []

  def __init__(self, name):
    Sprite.__init__(self)
    self._name = name
    self._pos = None          # screen position in pixels (x,y)
    self._coordonates = None  # cells position (row,col)
    img = ""
    # depend of the kind of object to create (there is 3 ways)
    # we have to know which one image to show for each of them
    if name == "pill":
      img = PILL_FILE
    elif name == "needle":
      img = NEEDLE_FILE
    elif name == "diluent":
      img = DILUENT_FILE
    # but we have to check this file is  accepted by pygame too
    try:
      self.image = pg.image.load(img).convert()
    except pg.error:
      print("can not load image:", img)
      raise SystemExit
    self.image = pg.transform.scale(self.image, (30, 30))
    self.rect = self.image.get_rect()  # now the Sprite has a position

  def update(self):
    self.rect.topleft = self._pos

  def set_position(self, position):
    self._pos = position

  def set_coordonates(self, coordonates):
    self._coordonates = coordonates
