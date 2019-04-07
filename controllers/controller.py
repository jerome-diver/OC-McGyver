"""
Superclass Controller embed
model from MVC design pattern
"""
from pygame import key
from pygame.locals import *

from washer import Washer

class Controller(Washer):

  def __init__(self, game_engine, labyrinth_ctrl=None):
    self._game_engine = game_engine
    self._labyrinth_ctrl = labyrinth_ctrl # LabyrinthController doesn't need

  def key_pressed(self, person):
    _key = key.get_pressed()
    if _key[K_LEFT]:
      person.move(dx=-2)
    if _key[K_RIGHT]:
      person.move(dx=2)
    if _key[K_UP]:
      person.move(dy=-2)
    if _key[K_DOWN]:
      person.move(dy=2)
    if _key[K_LEFT] and \
       (_key[K_LSHIFT] or _key[K_RSHIFT]):
      person.move(dx=-4)
    if _key[K_RIGHT] and \
       (_key[K_LSHIFT] or _key[K_RSHIFT]):
      person.move(dx=4)
    if _key[K_UP] and \
       (_key[K_LSHIFT] or _key[K_RSHIFT]):
      person.move(dy=-4)
    if _key[K_DOWN] and \
       (_key[K_LSHIFT] or _key[K_RSHIFT]):
      person.move(dy=4)

