"""
Superclass Model embed
model from MVC design pattern
"""

import binascii
import os

from pygame.sprite import *


class Model():

  _directions = ("north", "east", "south", "west")
  _sides = ("top", "right", "bottom", "left")

  def check_coordonates(self, coordonates):
    line = (coordonates[0] >= 0 and coordonates[0] <= 14)
    row = (coordonates[1] >= 0 and coordonates[1] <= 14)
    if not (line and row):
      raise Exception("Coordonates are wrong")
