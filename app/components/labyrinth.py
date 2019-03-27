'''
The Map object is the uniq map object who contain the labirynth map with his walls designs.
The map has 8 lines of 8 culumns rooms (64 rooms).
'''

import binascii
import os


class Labyrinth:

  _walls_bytes = {}    # { (row,column): byte }
  _wallsN = (b'\x01', b'\x05', b'\x06', b'\x07',
             b'\x0b', b'\x0c', b'\x0e', b'\x0f')
  _wallsW = (b'\x02', b'\x05', b'\x08', b'\x09',
             b'\x0b', b'\x0c', b'\x0d', b'\x0f')
  _wallsS = (b'\x03', b'\x07', b'\x09', b'\x0a',
             b'\x0c', b'\x0d', b'\x0e', b'\x0f')
  _wallsE = (b'\x04', b'\x06', b'\x08', b'\x0a',
             b'\x0b', b'\x0d', b'\x0e', b'\x0f')
  _rows, _columns = 0, 0

  def __init__(self):
    pass

  def __del__(self):
    if self.__dict__:
      for attr_keys in list(self.__dict__.keys()):
        del(self.__dict__[attr_keys])
        print(self.__class__.__name__, "attributes has has been deleted")

  @staticmethod
  def wallPositions():
    return Labyrinth._walls_bytes

  def get(self):
    return self
