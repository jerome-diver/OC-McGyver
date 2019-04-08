"""
Superclass Controller embed
model from MVC design pattern
"""

from pygame import key
from pygame.locals import K_LEFT, K_RIGHT, K_UP, K_DOWN, \
                            K_LSHIFT, K_RSHIFT

from washer import Washer


class Controller(Washer):
    ''' Is controller base of all controllers'''

    def __init__(self, game_engine, labyrinth_ctrl=None):
        self._game_engine = game_engine
        self._labyrinth_ctrl = labyrinth_ctrl  # LabyrinthController doesn't

    def get_model(self):
        '''Return his model'''
        return self._model

    def get_labyrinth_ctrl(self):
        '''Return LabyrinthController if himself is not LabyrinthController'''
        return self._labyrinth_ctrl

    @staticmethod
    def key_pressed(person):
        '''When a key is pressed Down'''
        _key = key.get_pressed()
        if _key[K_LEFT]:
            person.move(_dx=-2)
        if _key[K_RIGHT]:
            person.move(_dx=2)
        if _key[K_UP]:
            person.move(_dy=-2)
        if _key[K_DOWN]:
            person.move(_dy=2)
        if _key[K_LEFT] and \
                (_key[K_LSHIFT] or _key[K_RSHIFT]):
            person.move(_dx=-4)
        if _key[K_RIGHT] and \
                (_key[K_LSHIFT] or _key[K_RSHIFT]):
            person.move(_dx=4)
        if _key[K_UP] and \
                (_key[K_LSHIFT] or _key[K_RSHIFT]):
            person.move(_dy=-4)
        if _key[K_DOWN] and \
                (_key[K_LSHIFT] or _key[K_RSHIFT]):
            person.move(_dy=4)
