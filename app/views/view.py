"""
Superclass View embed
model from MVC design pattern
and this is inherited from View class
who is also injherited from Sprite class
So... this is a Sprite too
"""

from pygame.sprite import *

from settings import *


class View(Sprite):

  _width = 600
  _height = 600

  def __init__(self, model, gameEngine):
    super().__init__()
    self._model = model
    self.gameEngine = gameEngine
