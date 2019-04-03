'''
pg engine shoudl run the game when all objects/models/view and controllers are loaded.
'''

import pygame as pg
from pygame.sprite import Group
import time

from settings import *
from washer import Washer


class SpritesGroupNamed(Group, Washer):

  def __init__(self, name):
    super().__init__()
    self._name = name


class PyGameEngine(Washer):

  def __init__(self):
    self._crashed = False
    self._sprites_groups = []
    self._background_jobs = []
    pg.init()
    self._window = pg.display.set_mode((WIDTH, HEIGHT))
    pg.display.set_caption("OpenClassRoom -- project3 -- Mac Gyver")
    self._clk = pg.time.Clock()

  def start(self):
    while not self._crashed:
      #self.print_message("press \"q\" for exit the game",
      #                   (0,0), 'topright', 12, WHITE)
      self.keys_down_events()
      self._clk.tick(50)
      self._window.fill(BLACK)
      self.update_sprites_groups()
      self.exec_jobs_background()
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
    x_arg, y_arg = False, False
    if x != None:
      x_arg = True
    if y != None:
      y_arg = True
    lines = text.splitlines()
    font = pg.font.Font("fonts/Ubuntu-M.ttf", size)
    for i, l in enumerate(lines):
      if not x_arg:
        x = int((WIDTH - font.size(l)[0]) / 2)
      if not y_arg:
        y = int((HEIGHT - font.size(text)[1]) / 2)
      self._window.blit(font.render(l, 0, color),
                        (x, y - font.get_linesize() * i))

  def actions_delayed(self,tempo,
                      action_start=None, sa_args=None,
                      action_end=None, e_args=None):
    new_background_job = {}
    if action_start:
      new_background_job["start_job"] = { "action": action_start,
                                          "args": sa_args }
      new_background_job["time_start"] = int(time.time())
      new_background_job["delay"] = tempo
      if action_end:
        new_background_job["end_job"] = {"action": action_end }
        if e_args:
          new_background_job["end_job"]["args"] = e_args
      self._background_jobs.append(new_background_job)

  def exec_jobs_background(self):
    finished_jobs = []
    if self._background_jobs:
      for index, job in enumerate(self._background_jobs):
        if "args" in job["start_job"]:
          job["start_job"]["action"](*job["start_job"]["args"])
        else:
          job["start_job"]["action"]()
        now = int(time.time())
        if job["delay"] <= now - job["time_start"]:
          finished_jobs.append(index)
          if "end_job" in job:
            if "args" in job["end_job"]:
              job["end_job"]["action"](*job["end_job"]["args"])
            else:
              job["end_job"]["action"]()
        pg.display.update()
      for job_to_remove in finished_jobs:
        del self._background_jobs[job_to_remove]

  def end_game(self):
     self._crashed = True

