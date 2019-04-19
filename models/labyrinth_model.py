'''
Model of the Labyrinth.

Get the map and put inside Labyrinth._walls_byte variable.
This one will be used to provide self._walls variable
'''

import binascii

from washer import Washer
from settings import ADJ_X, ADJ_Y, LABYRINTH_FILE


class LabyrinthModel(Washer):
    '''Model of the Labyrinth'''

    def __init__(self):
        super().__init__()
        self._walls = []  # [ Wall ]
        self._walls_bytes = {}  # { (row,column): byte }
        self._rows_columns = ()
        self._exit_coordonates = None  # cell position (row,col)
        self._exit_position = None  # exit position (x,y)
        self._name = "labyrinth"
        self.load_map()

    def get_name(self):
        '''Return the self._name'''
        return self._name

    def set_exit_coordonates(self, row, col):
        '''Setting labyrinth cells exit coordonates: row:int, column:int'''
        self._exit_coordonates = (row, col)
        self.set_exit_position(row, col)

    def get_exit_coordonates(self):
        '''Give Labyrinth cells exit coordonates: (tuple(row:int, column:int)'''
        return self._exit_coordonates

    def get_exit_position(self):
        '''Return the exit position in pixels: tuple(x:int, y:int)'''
        return self._exit_position

    def set_exit_position(self, row, column):
        '''Setting the pixels exit position from coordonates:

        row:int, column:int'''
        self._exit_position = (int(column * 40 + ADJ_X),
                               int(row * 40 + ADJ_Y))

    def load_map(self):
        '''Setting self._wall_bytes from map.txt document

        and define self._rows_columns maximum map rows and columns of the map'''
        _row, _col = 0, 0
        with open(LABYRINTH_FILE, "r") as file:
            for row, line in enumerate(file):
                _row += 1
                _col = 0
                for column, char in enumerate(line.strip()):
                    _col += 1
                    self._walls_bytes[(row, column)] = binascii.unhexlify(
                        "0" + char)
        self._rows_columns = (_row, _col)

    def get_elements(self):
        '''Return the objects walls who are Sprites images

        of each Wall with own coordonates'''
        return self._walls

    def get_wall(self, coordonates):
        '''Return the Wall for this coordonates tuple(row:int, column:int)'''
        _row, _col = coordonates
        for _wall in self._walls:
            if _wall.col == _col and _wall.row == _row:
                return _wall
        return None

    def get_walls_bytes(self):
        '''Return self._walls_bytes variable reference'''
        return self._walls_bytes

    def get_closed_walls(self):
        '''Return cells where enclosure(s walls are closed'''
        closed_walls = []
        for coordonates, byte in self._walls_bytes.items():
            if byte == b'\x0f':
                closed_walls.append(self.get_wall(coordonates))
        return closed_walls

    def get_coordonates_of_wall(self, wall):
        '''Return the coordonates of this wall: tuple(row:int, column:int)'''
        _find_coordonates = None
        for _wall in self._walls:
            if _wall == wall:
                _find_coordonates = (_wall.row, _wall.col)
        return _find_coordonates

    def get_labyrinth_rows(self):
        '''Return labyrinth rows numbers'''
        return self._rows_columns[0]

    def get_labyrinth_columns(self):
        '''Return labyrinth columns numbers'''
        return self._rows_columns[1]
