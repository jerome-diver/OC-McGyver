"""
Superclass View embed
model from MVC design pattern
and this is inherited from View class
who is also inherited from Sprite class
"""

from models.object_model import ObjectModel


class View():

  def __init__(self, controller,  model, game_engine):
    self._controller = controller
    self._model = model
    self._game_engine = game_engine
    # only if the view is not an objectView,
    # ask to create  the Sprite Group
    if not isinstance(model, ObjectModel):
     self._game_engine.create_group(self._model.get_name())
