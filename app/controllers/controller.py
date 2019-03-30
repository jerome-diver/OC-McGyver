"""
Superclass Controller embed
model from MVC design pattern
"""

import pygame as pg


class Controller:

  def __init__(self, game_engine):
    self._game_engine = game_engine

  def key_pressed(self, person):
    key = pg.key.get_pressed()
    if key[pg.K_LEFT]:
      person.move(dx=-1)
    if key[pg.K_RIGHT]:
      person.move(dx=1)
    if key[pg.K_UP]:
      person.move(dy=-1)
    if key[pg.K_DOWN]:
      person.move(dy=1)
    if key[pg.K_LEFT] and \
       (key[pg.K_LSHIFT] or key[pg.K_RSHIFT]):
      person.move(dx=-2)
    if key[pg.K_RIGHT] and \
       (key[pg.K_LSHIFT] or key[pg.K_RSHIFT]):
      person.move(dx=2)
    if key[pg.K_UP] and \
       (key[pg.K_LSHIFT] or key[pg.K_RSHIFT]):
      person.move(dy=-2)
    if key[pg.K_DOWN] and \
       (key[pg.K_LSHIFT] or key[pg.K_RSHIFT]):
      person.move(dy=2)
