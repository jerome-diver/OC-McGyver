'''
Controller for Map who load map and his rooms.
'''

import os
import sys

import pygame as pg

from components.labyrinth import *
from controllers.controller import *
from models.labyrinth_model import *
from views.labyrinth_view import *
from views.sprites import *


class LabyrinthController(Controller):

  def __init__(self, pyGameEngine):
    super().__init__(pyGameEngine)
    self._model = LabyrinthModel()
    labyrinthGroup = pg.sprite.Group()
    self._view = LabyrinthView(self._model, labyrinthGroup)

  def hotKeys(self):
    pass
