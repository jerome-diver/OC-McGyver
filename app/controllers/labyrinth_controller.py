'''
Controller for Map who load map and his rooms.
'''

import os
import sys

from components.labyrinth import *
from controllers.controller import *
from models.labyrinth_model import *
from views.labyrinth_view import *
from views.sprites import *


class LabyrinthController(Controller):

  def __init__(self, pyGameEngine):
    super().__init__(pyGameEngine)
    self._model = LabyrinthModel()
    self._view = LabyrinthView(self._model)

  def hotKeys(self):
    pass
