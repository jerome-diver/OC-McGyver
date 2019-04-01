'''
pg engine shoudl run the game when all objects/models/view and controllers are loaded.
'''

import pygame as pg
from pygame.sprite import Group

from settings import *


class SpritesGroupNamed(Group):

  def __init__(self, name):
    super().__init__()
    self._name = name


class PyGameEngine():

  def __init__(self):
    self._crashed = False
    self._sprites_groups = []
    pg.init()
    self._window = pg.display.set_mode((WIDTH, HEIGHT))
    pg.display.set_caption("OpenClassRoom -- project3 -- Mac Gyver")
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
    self._sprites_groups.append(SpritesGroupNamed(name))

  def add_sprites_to_group(self, sprites, group_name):
    for group in self._sprites_groups:
      if  group._name == group_name:
        for sprite in sprites:
          group.add(sprite)

  def update_sprites_groups(self):
    for group in self._sprites_groups:
      group.update()
      group.draw(self._window)

  def get_group(self, name):
    for group in self._sprites_groups:
      if group._name == name:
        return group
    return None

  def end_game(self):
    self._crashed = True
