'''
pg engine shoudl run the game when all objects/models/view and controllers are loaded.
'''

import pygame as pg
from pygame.sprite import Group
import time

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
      #self.print_message("press \"q\" for exit the game",
      #                   (0,0), 'topright', 12, WHITE)
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

  def message(self, text, size, color, x=None, y=None):
    lines = text.splitlines()
    font = pg.font.Font("fonts/Ubuntu-M.ttf", size)
    for i, l in enumerate(lines):
      if x == None:
        x = int((WIDTH - font.size(l)[0]) / 2)
      if y == None:
        y = int((HEIGHT - font.size(text)[1]) / 2)
      self._window.blit(font.render(l, 0, color),
                        (x, y - font.get_linesize() * i))

  def actions_delayed(self,tempo,
                      action_start=None, sa_args=None,
                      action_end=None, e_args=None):
    if action_start:
      action_start(*sa_args) if sa_args else action_start()
      pg.display.update()
    time.sleep(tempo)
    if action_end:
      action_end(*e_args) if e_args else action_end()

  def end_game(self):
     self._crashed = True

