'''
Controller for Labyrinth who load walls and make them colliisionable
'''

from controllers.controller import *
from models.labyrinth_model import *
from views.labyrinth_view import *


class LabyrinthController(Controller):

  def __init__(self, pyGameEngine):
    super().__init__(pyGameEngine)
    self._model = LabyrinthModel()
    self._view = LabyrinthView(self, self._model, pyGameEngine)

  def getModel(self):
    return self._model
