'''
Models of Hero or Guard,
'''

from components.elements import Element, Hero
from washer import Washer
from settings import GUARD_FILE, HERO_FILE, ADJ_X, ADJ_Y


class GuardModel(Element, Washer):
    '''Model of Guard'''

    def __init__(self, controller, labyrinth_ctrl):
        ''' The guard is just a simple Element who has his own model and

        view, because it react to collision differently and has is
        own group for collisions'''
        Element.__init__(self, controller, "guard", GUARD_FILE)
        self._sleeping = False
        labyrinth_model = labyrinth_ctrl.get_model()
        exit_coordonates = labyrinth_model.get_exit_coordonates()
        self.set_coordonates(exit_coordonates)

    def inject_pill(self):
        '''The Hero can make sleeping and inject the pill'''
        self._sleeping = True

    def is_sleeping(self):
        '''Check if Guard is sleeping'''
        return self._sleeping

    def get_elements(self):
        '''Return list of unique self Element'''
        return [self.get()]


class HeroModel(Hero, Washer):
    '''Model of Hero'''

    def __init__(self, controller, labyrinth_ctrl):
        Hero.__init__(self, controller, HERO_FILE)
        labyrinth_model = labyrinth_ctrl.get_model()
        max_rows = labyrinth_model.get_labyrinth_rows()
        max_columns = labyrinth_model.get_labyrinth_columns()
        hero_coordonates = (max_rows - 1, max_columns - 1)
        self.set_coordonates(hero_coordonates)

    def can_make_sleeping(self):
        '''Check if Hero has power to make sleeping'''
        return len(self._objects) == 3

    def set_position_from(self, coordonates):
        '''Setting pixels position from cell coordonate:

        tuple(row:int, column:int)'''
        pos = (int(coordonates[0] * 40 + ADJ_X + 8),
               int(coordonates[1] * 40 + ADJ_Y + 8))
        self.set_position(pos)

    def get_elements(self):
        '''Return list of unique self Element'''
        return [self.get()]
