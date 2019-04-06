'''
pg engine shoudl run the game when all objects/models/view and controllers are loaded.
'''

import pygame as pg
from pygame.sprite import Group
import time

from settings import *
from washer import Washer


# let's make our own Sprite's Groups with there own name
class SpritesGroupNamed(Group, Washer):

  def __init__(self, name):
    super().__init__()
    self._name = name


class PyGameEngine(Washer):

  def __init__(self):
    self._crashed = False       # to finish the pygame loop
    self._sprites_groups = []   # list of Sprites (to show)
    self._background_jobs = []  # list of job to run in background
    pg.mixer.init()
    self.volume = pg.mixer.music.get_volume()
    pg.init()
    self._window = pg.display.set_mode((WIDTH, HEIGHT))
    pg.display.set_caption("OpenClassRoom -- project3 -- Mac Gyver")
    self._clk = pg.time.Clock() # the refresh frequency counter
    self.play_jingle()          # let's play the Mac-Gyver free jingle

  # the loop of execution of pygame
  def start(self):
    while not self._crashed:
      # when with push down a key (one time event)
      self.keys_down_events()
      # the frequency in FPS
      self._clk.tick(60)
      # the first black background to refresh
      # (it repaint the screen for the next print)
      self._window.fill(BLACK)
      # show all the sprites contained inside the groups of sprites
      self.update_sprites_groups()
      # do the background jobs now
      self.exec_jobs_background()
      # now print the result
      pg.display.flip()
    pg.quit()

  # this is easy to read and understand, isn't it ?
  def keys_down_events(self):
    for ev in pg.event.get():
      if ev.type == pg.KEYDOWN:
        if ev.key == pg.K_q:
          print("bye bye, see you soon !")
          self._crashed = True
        if ev.key == pg.K_s:
          self.toggle_jingle_volume()
      if ev.type == pg.QUIT:
        self._crashed = True

  # create the gorup of sprite and give him a name
  def create_group(self, name):
    # this one will inherit pygame.sprite.Group... for have his name
    self._sprites_groups.append(SpritesGroupNamed(name))

  def add_sprites_to_group(self, sprites, group_name):
    for group in self._sprites_groups:
      if  group._name == group_name:
        for sprite in sprites:
          group.add(sprite)

  # when i update the pygame.sprite.Group, all the contained
  # sprites of this group are updated. pygame.sprite.Group
  # do that for us.
  def update_sprites_groups(self):
    for group in self._sprites_groups:
      group.update()
      group.draw(self._window)

  def get_group(self, name):
    for group in self._sprites_groups:
      if group._name == name:
        return group
    return None

  # let's make ability to print a message with multi lines
  def message(self, text, size, color, x=None, y=None):
    x_arg, y_arg = False, False
    # the first time only... because after, x will have a value
    if x != None:
      x_arg = True
    if y != None:
      y_arg = True
    lines = text.splitlines()
    font = pg.font.Font("fonts/Ubuntu-M.ttf", size)
    for i, l in enumerate(reversed(lines)):
      if not x_arg:
        # in the center
        x = int((WIDTH - font.size(l)[0]) / 2)
      if not y_arg:
        y = int((HEIGHT - font.size(text)[1]) / 2)
      # print the resulted text inside an image
      self._window.blit(font.render(l, 0, color),
                        (x, y - font.get_linesize() * i))

  # i let you create the content for a delayed jobs
  # in the background there...
  # it is just about create a data formated like a list
  # of dictionaries with there own significant keys and related values
  def actions_delayed(self,tempo,
                      action_start=None, sa_args=None,
                      action_end=None, e_args=None):
    new_background_job = {}
    # if there is a function to call there
    if action_start:
      new_background_job["start_job"] = { "action": action_start }
      if sa_args:
        new_background_job["start_job"]["args"] = sa_args
      new_background_job["time_start"] = int(time.time())
      new_background_job["delay"] = tempo
      if action_end:
        new_background_job["end_job"] = {"action": action_end }
        if e_args:
          new_background_job["end_job"]["args"] = e_args
      # add the formed data inside the list of background jobs to do
      self._background_jobs.append(new_background_job)

  # all the listed background jobs to do will be executed there
  def exec_jobs_background(self):
    # a job is a dictionary with a start_job, eventually his argument(s),
    # a delay, a timer start indication, and a end_job to do next
    # with, eventually, his arguments
    finished_jobs = []
    # only if have one or any background_jobs
    if self._background_jobs:
      # for each job in the list
      for index, job in enumerate(self._background_jobs):
        # and igf the is "start_job" argument(s)
        if "args" in job["start_job"]:
          job["start_job"]["action"](*job["start_job"]["args"])
        # if no argument for "start_job"
        else:
          job["start_job"]["action"]()
        # get the count timer reference (now !)
        now = int(time.time())
        # and when out of delay for this start_job
        if job["delay"] <= now - job["time_start"]:
          # give the inormation in the list of finished_job
          finished_jobs.append(index)
          # and if there is a "end_job" to do...
          if "end_job" in job:
            # with some arguments...
            if "args" in job["end_job"]:
              job["end_job"]["action"](*job["end_job"]["args"])
            else:
              job["end_job"]["action"]()
      # test because we don't want crash at end_game
      if self._background_jobs:
        # delete the finished jobs in the list
        for job_to_remove in finished_jobs:
          del self._background_jobs[job_to_remove]

  # play the jingle music
  def play_jingle(self):
    pg.mixer.music.load(JINGLE_FILE)
    pg.mixer.music.play()
    pg.mixer.music.set_volume(self.volume)

  def toggle_jingle_volume(self):
    volume = pg.mixer.music.get_volume()
    if volume == 0:
      pg.mixer.music.set_volume(self.volume)
    else:
      pg.mixer.music.set_volume(0)

  def end_game(self):
     self._crashed = True
     self._background_jobs = None

