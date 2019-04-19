"""
This model has elements list attributes
from arguments provided, it create each Element with them.
Nothing more.
"""

from components import Element
from washer import Washer


class ObjectModel(Washer):
    '''Object Model'''

    def __init__(self, ctrl, *args):
        super().__init__()
        self._objects = []
        self._group_name = "objects"
        # create specifics Object and store them
        args = [*args]
        for arg in args:
            name, file = arg
            self._objects.append(Element(ctrl, name, file))

    def get_elements(self):
        '''Return all the existing objects'''
        return self._objects

    def get_name(self):
        '''Return his _group_name'''
        return self._group_name
