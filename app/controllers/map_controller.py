'''
Controller for Map who load map and his rooms.
'''

import os
import sys

from controllers.controller import *
from components.map import *
from views.map_view import *
from models.map_model import *
from model.room_model import *
from views.sprites import *


class MapController(Controller):

    def __init__(self, pyGameEngine):
        super().__init__(pyGameEngine)
        self._model = MapModel(pyGameEngine)
        _map = self._model.getMap()
        self._view = MapView(_map)
        self.roomController = RoomController(pyGameEngine, _map)
        

