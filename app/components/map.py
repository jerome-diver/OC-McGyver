'''
The Map object is the uniq map object who contain the labirynth map with his walls designs.
The map has 8 lines of 8 culumns rooms (64 rooms).
'''

import os
import binascii


class Map:

    _walls = { }    # { (row,column): byte }
    _wallsN = (b'\x02',b'\x05',b'\x06',b'\x07',b'\x0b',b'\x0c',b'\x0e',b'\x0f')
    _wallsS = (b'\x03',b'\x07',b'\x09',b'\x0a',b'\x0c',b'\x0d',b'\x0e',b'\x0f')
    _wallsE = (b'\x04',b'\x06',b'\x08',b'\x0a',b'\x0b',b'\x0d',b'\x0e',b'\x0f')
    _wallsW = (b'\x02',b'\x05',b'\x08',b'\x09',b'\x0b',b'\x0c',b'\x0d',b'\x0f')

    def __init__(self):
        pass

    def __del__(self):
        if self.__dict__:
            for attr_keys in list(self.__dict__.keys()):
                del(self.__dict__[attr_keys])
        print(self.__class__.__name__,"attributes has has been deleted")

    def wallPositions(self):
        return self._walls

    def wallPosition(self, room_coordonates):
        return self._walls[room_coordonates]

    def wallClockWisePosition(self,room_coordonates):
        checkCoordonates(room_coordonates)
        return (self._walls[room_coordonates] in self._wallsN, \
                self._walls[room_coordonates] in self._wallsE, \
                self._walls[room_coordonates] in self._wallsS, \
                self._walls[room_coordonates] in self._wallsW)

    def getMap(self):
        return self