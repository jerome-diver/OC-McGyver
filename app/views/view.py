"""
Superclass View embed
model from MVC design pattern
and this is inherited from View class
who is also injherited from Sprite class
So... this is a Sprite too
"""

import pygame as pg
from pygame.sprite import *


class View(Sprite):

  _black = (0, 0, 0)
  _white = (255, 255, 255)
  _red = (255, 0, 0)
  _width = 600
  _height = 600

  def __init__(self, model, gameEngine):
    super().__init__()
    self._model = model
    self.gameEngine = gameEngine
