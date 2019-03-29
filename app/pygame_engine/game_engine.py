'''
pg engine shoudl run the game when all objects/models/view and controllers are loaded.
'''

import pygame as pg

from settings import *


class PyGameEngine():

  def __init__(self):
    self._crashed = False
    self._posX, self.posY = 0, 0
    self._spritesGroups = {}
    self.hero = None
    pg.init()
    self._display = pg.display
    self._window = self._display.set_mode((width, height))
    self._display.set_caption("OpenClassRoom -- project3 -- Mac Gyver")
    self._clk = pg.time.Clock()

  def __del__(self):
    pg.quit()

  def start(self):
    while not self._crashed:
      self.keysDownEvents()
      self._clk.tick(50)
      self._window.fill(black)
      self.updateSpritesGroups()
      pg.display.flip()
    pg.quit()

  def keysDownEvents(self):
    for ev in pg.event.get():
      if ev.type == pg.KEYDOWN:
        if ev.key == pg.K_q:
          print("bye bye, see you soon !")
          self._crashed = True
      if ev.type == pg.QUIT:
        self._crashed = True

  def createGroup(self, name):
    print("created group:", name)
    self._spritesGroups[name] = pg.sprite.Group()

  def addSpritesToGroup(self, sprites, groupName):
    for sprite in sprites:
      self._spritesGroups[groupName].add(sprite)

  def updateSpritesGroups(self):
    for group in self._spritesGroups.values():
      group.update()
      group.draw(self._window)

  def getGroup(self, name):
    return self._spritesGroups[name]

  def endGame(self):
    self._crashed = False
