"""
Superclass View embed
model from MVC design pattern
and this is inherited from View class
who is also injherited from Sprite class
So... this is a Sprite too
"""

from settings import *


class View():

  def __init__(self, controller,  model, game_engine):
    self._controller = controller
    self._model = model
    self._game_engine = game_engine
    self._game_engine.create_group(self._model.get_name())
