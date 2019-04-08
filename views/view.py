"""
Superclass of Views
"""

from random import randint

from washer import Washer
from settings import ADJ_X, ADJ_Y


def find_position(coordonates):
    '''Setting coordonates of given object

    coordonates:tuple(row:int, column:int), object:Object'''
    _pos = (int(coordonates[0] * 40 + ADJ_X + 8), \
           int(coordonates[1] * 40 + ADJ_Y + 8))
    return _pos

def generate_random_coordonates():
    '''Return random cells coordonates: tuple (row:int, column:int)'''
    row = randint(0, 14)
    col = randint(0, 14)
    return (row, col)

class View(Washer):
    '''Base class for all the views classes'''

    def __init__(self, controller, model, game_engine):
        self._controller = controller
        self._model = model
        self._game_engine = game_engine
        self.make_sprites_group()

    def make_sprites_group(self):
        '''Provide a group of sprite for sprites elements'''
        _group_name = self._model.get_name()
        self._game_engine.create_group(_group_name)
        if _group_name != "labyrinth":
            _elements = self._model.get_elements()
            self._game_engine.add_sprites_to_group(_group_name, _elements)
