"""
Set views for Hero and guard personage
hero and guard for give them a position inside screen
(care about walls collisions by coordinates simple calculus)
and add them to there own sprite group:
"""

from settings import MAX_TIMER_GAME, WHITE, HEIGHT
from views import View


class GuardView(View):
    '''View of Guard'''

    def __init__(self, controller, model, game_engine):
        super().__init__(controller, model, game_engine)
       # guard = self._model.get()
       # self._game_engine.add_sprites_to_group([guard], "guard")
        self.setting_position()

    def setting_position(self):
        '''Setting automation for position of the Guard'''
        labyrinth_ctrl = self._controller.get_labyrinth_ctrl()
        labyrinth_model = labyrinth_ctrl.get_model()
        exit_position = labyrinth_model.get_exit_position()
        guard_position = (exit_position[0] + 8, exit_position[1])
        self._model.set_position(guard_position)


class HeroView(View):
    '''Viex of the Hero'''

    def __init__(self, controller, model, game_engine):
        super().__init__(controller, model, game_engine)
        hero = self._model.get()
        self._game_engine.add_sprites_to_group([hero], "hero")
        self.setting_position()

    def setting_position(self):
        '''Setting fixed position for th Hero'''
        hero_coordonates = self._model.get_coordonates()
        self._model.set_position_from(hero_coordonates)

    def show_objects_collected(self, objects):
        '''Return Hero's objects collected'''
        _en = self._game_engine
        text = "Objects list:          "
        y_pos = HEIGHT - 75
        for i, obj in enumerate(objects):
            if i != 0:
                text += ", "
            text += obj.get_name()
        _en.actions_delayed(tempo=MAX_TIMER_GAME,
                            action_start=_en.message,
                            sa_args=(text, 24, WHITE, 20, y_pos))
