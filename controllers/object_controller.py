"""
This controller care about objects and actions when it does
collid with hero.
"""

from controllers import Controller
from models import ObjectModel
from views import ObjectView
from settings import PILL_FILE, DILUENT_FILE, NEEDLE_FILE


class ObjectController(Controller):
    '''Ocjet own controller'''

    def __init__(self,
                 labyrinth_ctrl,
                 hero_ctrl,
                 guard_ctrl,
                 game_engine):
        super().__init__(game_engine, labyrinth_ctrl)
        self._hero_ctrl = hero_ctrl
        self._guard_ctrl = guard_ctrl
        self._model = ObjectModel(self, ("pill", PILL_FILE),
                                  ("diluent", DILUENT_FILE),
                                  ("needle", NEEDLE_FILE))
        self._view = ObjectView(self, self._model, game_engine)
        self.setting_collisions()

    def setting_collisions(self):
        '''Setting collisions abilities with the Hero'''
        group = self._game_engine.get_group("objects")
        self._hero_ctrl.can_collid_with(group)

    def get_guard_ctrl(self):
        '''Return slef GuardController'''
        return self._guard_ctrl

    def get_hero_ctrl(self):
        '''Return self HeroController'''
        return self._hero_ctrl
