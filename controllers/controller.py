"""
Superclass Controller embed
model from MVC design pattern
"""
import pygame as pg

from washer import Washer

class Controller(Washer):

  def __init__(self, game_engine, labyrinth_ctrl=None):
    self._game_engine = game_engine
    self._labyrinth_ctrl = labyrinth_ctrl

  def key_pressed(self, person):
    key = pg.key.get_pressed()
    if key[pg.K_LEFT]:
      person.move(dx=-2)
    if key[pg.K_RIGHT]:
      person.move(dx=2)
    if key[pg.K_UP]:
      person.move(dy=-2)
    if key[pg.K_DOWN]:
      person.move(dy=2)
    if key[pg.K_LEFT] and \
       (key[pg.K_LSHIFT] or key[pg.K_RSHIFT]):
      person.move(dx=-4)
    if key[pg.K_RIGHT] and \
       (key[pg.K_LSHIFT] or key[pg.K_RSHIFT]):
      person.move(dx=4)
    if key[pg.K_UP] and \
       (key[pg.K_LSHIFT] or key[pg.K_RSHIFT]):
      person.move(dy=-4)
    if key[pg.K_DOWN] and \
       (key[pg.K_LSHIFT] or key[pg.K_RSHIFT]):
      person.move(dy=4)

  def get_labyrinth_model(self):
    return self._labyrinth_ctrl._model

