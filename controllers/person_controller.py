'''
Controller for persons like Hero or guard who make them alive

in the game. This class hold action's control for them.
'''

from controllers import Controller
from controllers import Collider
from models import HeroModel, GuardModel
from views import HeroView, GuardView
from settings import ADJ_X, ADJ_Y, GREEN, RED, BLUE


class HeroController(Controller, Collider):
    ''' Controller for Hero'''

    def __init__(self, labyrinth_ctrl, guard_ctrl, game_engine):
        Controller.__init__(self, game_engine, labyrinth_ctrl)
        Collider.__init__(self, game_engine)
        self._guard_ctrl = guard_ctrl
        self._model = HeroModel(self, labyrinth_ctrl)
        self._view = HeroView(self, self._model, game_engine)
        self._view.show_objects_collected([])

    def setting_collisions(self):
        '''What to do when collision'''
        self.setting_collisions_for("labyrinth",
                                    self.labyrinth_collision,
                                    if_collid=False)
        self.setting_collisions_for("guard",
                                    self.guard_collision)
        self.setting_collisions_for("objects",
                                    self.object_collision,
                                    do_kill=True)

    def check_exit(self):
        '''Check if this way is an exit'''
        guard = self._guard_ctrl.get_model()
        position = self._model.get_position()
        if      position[0] < ADJ_X or \
                position[1] < ADJ_Y and \
                guard.is_sleeping():
            _en = self._game_engine
            text = "You win !\n\n" \
                   "Mac Gyver can go back home now...\n\n" \
                   "Bye bye..."
            _en.actions_delayed(tempo=5,
                                action_start=_en.message,
                                sa_args=(text, 38, GREEN),
                                action_end=_en.end_game,
                                e_args=None)

    @staticmethod
    def labyrinth_collision(caller, *args):
        '''When collision happen with Labyrinth'''
        _dx, _dy = args
        old_position = caller.get_position()
        new_position = (old_position[0] + _dx, old_position[1] + _dy)
        caller.set_position(new_position)

    def guard_collision(self, caller, *args):
        '''When collision happen with Guard'''
        _dx, _dy, guard = args
        hero = self._model
        position = caller.get_position()
        if hero.can_make_sleeping():
            guard.inject_pill()
        if guard.is_sleeping():
            new_position = (position[0] + _dx, position[1] + _dy)
            caller.set_position(new_position)
        else:
            text = "You loose !\n\nGAME OVER"
            _en = self._game_engine
            _en.actions_delayed(tempo=5,
                                action_start=_en.message,
                                sa_args=(text, 38, RED),
                                action_end=_en.end_game,
                                e_args=None)

    def object_collision(self, caller, *args):
        '''When collision happen with an Object'''
        _collected = args[2]
        caller.add_object(_collected)
        _en = self._game_engine
        _objects = caller.get_objects()
        text = "Perfect !\n" \
               "Now, you get the power \n" \
               "to make sleeping everybody..."
        if len(_objects) < 3:
            text = "Yeah... you get the " + _collected.get_name()
        _en.actions_delayed(tempo=2,
                            action_start=_en.message,
                            sa_args=(text, 38, BLUE, None, None))
        self._view.show_objects_collected(_objects)


class GuardController(Controller):
    '''Controller for Guard'''

    def __init__(self, labyrinth_ctrl, game_engine):
        super().__init__(game_engine, labyrinth_ctrl)
        self._model = GuardModel(self, labyrinth_ctrl)
        self._view = GuardView(self, self._model, game_engine)
