'''
Controller for Labyrinth who load walls and make them colliisionable
'''

from controllers.controller import Controller
from models.labyrinth_model import LabyrinthModel
from views.labyrinth_view import LabyrinthView


class LabyrinthController(Controller):
    ''' Control The labyrinth component through his Model and View'''

    def __init__(self, game_engine):
        super().__init__(game_engine)
        self._model = LabyrinthModel()
        self._view = LabyrinthView(self, self._model, game_engine)
        self._game_engine.play_jingle()  # let's play the Mac-Gyver free jingle
