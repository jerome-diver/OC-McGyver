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

  def __init__(self):
    pass

  def check_coordonates(self, coordonates):
    line = (coordonates[0] >= 0 and coordonates[0] <= 7)
    row = (coordonates[1] >= 0 and coordonates[1] <= 7)
    if not (line and row):
      raise Exception("Coordonates are wrong")

  def check_direction(self, direction):
    if direction not in self._directions:
      raise Exception("direction syntax is wrong")

  def check_side(self, side):
    if side not in self._sides:
      raise Exception("side syntax is wrong")

  def opposit_direction(self, direction):
    if direction == "north":
      return "south"
    if direction == "south":
      return "north"
    if direction == "east":
      return "west"
    if direction == "west":
      return "east"

  def opposit_side(self, side):
    if side == "top":
      return "bottom"
    if side == "bottom":
      return "top"
    if side == "left":
      return "right"
    if side == "right":
      return "left"

  def get_model(self):
    return self

  def set_image(self, img, color):
    self._image = img
    self._image.fill(color)

  def get_image(self):
    return self._image
