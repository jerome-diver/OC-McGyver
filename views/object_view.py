"""
This is an object view to be abe to show Object
"""

from views.view import View, generate_random_coordonates, find_position


class ObjectView(View):
    '''View of his Object'''

    def __init__(self, controller, model, game_engine):
        super().__init__(controller, model, game_engine)
        self._objects = self._model.get_elements()
        # Setting there own position in the labyrinth
        self.setting_positions()

    def setting_positions(self):
        '''Setting position inside the Labyrinth

        random position with specific conditions'''
        for _object in self._objects:
            _accepted = False
            # wee need to select things, i will not put things somewhere wrong
            _blacklist = self.blacklisted_coordonates()
            while not _accepted:
                # let's try something randomly...
                _coordonates = generate_random_coordonates()
                # and if i can put this object there...
                if not any(_coordonates == c for c in _blacklist):
                    # then i will do it
                    _obj_pos = find_position(_coordonates)
                    _object.set_position(_obj_pos)
                    _object.set_coordonates(_coordonates)
                    # next...
                    _accepted = True

    def blacklisted_coordonates(self):
        '''Return a blacklisted coordonates list'''
        blacklist = []
        targets = []
        labyrinth_ctrl = self._controller.get_labyrinth_ctrl()
        labyrinth_model = labyrinth_ctrl.get_model()
        hero_ctrl = self._controller.get_hero_ctrl()
        guard_ctrl = self._controller.get_guard_ctrl()
        hero_model = hero_ctrl.get_model()
        guard_model = guard_ctrl.get_model()
        # we don't want to put object on tess guys...
        targets.append(hero_model.get_coordonates())
        targets.append(guard_model.get_coordonates())
        # and not inside wall closed structural cells...
        for closed_wall in labyrinth_model.get_closed_walls():
            c_of_cwall = labyrinth_model.get_coordonates_of_wall(closed_wall)
            targets.append(c_of_cwall)
        # if there is already some objects, we don't want to collid them
        for _object in self._objects:
            if _object.get_coordonates():
                targets.append(_object.get_coordonates())
        # and better if they are not just to much closer of
        # anything or anyone
        for target in targets:
            for i in range(-4, 4):
                for j in range(-4, 4):
                    _x = target[0] + i
                    _y = target[1] + j
                    # and we exclude the ones who are out of
                    # cells coordonates range
                    if _x >= 0 and \
                            _x <= 14 and \
                            _y >= 0 and \
                            _y <= 14:
                        blacklist.append((_x, _y))
        return blacklist
