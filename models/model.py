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
