'''
pg engine shoudl run the game when all objects/models/view and controllers are loaded.
'''

import pygame as pg

from settings import *


class PyGameEngine():

  def __init__(self):
    self._crashed = False
    self._sprites_groups = {}
    self.hero = None
    pg.init()
    self._display = pg.display
    self._window = self._display.set_mode((WIDTH, HEIGHT))
    self._display.set_caption("OpenClassRoom -- project3 -- Mac Gyver")
    self._clk = pg.time.Clock()

  def __del__(self):
    pg.quit()

  def start(self):
    while not self._crashed:
      self.keys_down_events()
      self._clk.tick(50)
      self._window.fill(BLACK)
      self.update_sprites_groups()
      pg.display.flip()
    pg.quit()

  def keys_down_events(self):
    for ev in pg.event.get():
      if ev.type == pg.KEYDOWN:
        if ev.key == pg.K_q:
          print("bye bye, see you soon !")
          self._crashed = True
      if ev.type == pg.QUIT:
        self._crashed = True

  def create_group(self, name):
    print("created group:", name)
    self._sprites_groups[name] = pg.sprite.Group()

  def add_sprites_to_group(self, sprites, group_name):
    for sprite in sprites:
      self._sprites_groups[group_name].add(sprite)

  def update_sprites_groups(self):
    for group in self._sprites_groups.values():
      group.update()
      group.draw(self._window)

  def get_group(self, name):
    return self._sprites_groups[name]

  def end_game(self):
    self._crashed = True
