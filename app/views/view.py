"""
Superclass View embed
model from MVC design pattern
and this is inherited from View class
who is also injherited from Sprite class
So... this is a Sprite too
"""

from settings import *


class View():

  def __init__(self, controller,  model, gameEngine):
    self._controller = controller
    self._model = model
    self._gameEngine = gameEngine
