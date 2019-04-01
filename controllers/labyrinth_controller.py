'''
Controller for Labyrinth who load walls and make them colliisionable
'''

from controllers.controller import *
from models.labyrinth_model import *
from views.labyrinth_view import *


class LabyrinthController(Controller):

  def __init__(self, game_engine):
    super().__init__(game_engine)
    self._model = LabyrinthModel()
    self._view = LabyrinthView(self, self._model, game_engine)

  def get_model(self):
    return self._model
