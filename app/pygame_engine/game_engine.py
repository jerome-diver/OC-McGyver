'''
pg engine shoudl run the game when all objects/models/view and controllers are loaded.
'''

import pygame as pg


class pgEngine():

  _width = 800
  _height = 800

  def __init__(self):
    pg.init()
    self._display = pg.display
    self._window = self._display.set_mode((_width, _height))
    self._display.set_caption("OpenClassRoom -- project3 -- Mac Gyver")
    self._clk = pg.time.Clock()
    self._crashed = False
    self._posX, self.posY = 0, 0
    self._rootSpritesGroup = pg.sprite.Group()

  def start(self):
    while not self._crashed:
      for ev in pg.event.get():
        if ev.type == pg.KEYDOWN:
          self.keysDownEvents(ev)
          self.keyPressed()
          self._rootSpritesGroup.update()
          self._clk.tick(60)
          self._window.fill(self._black)
          self._rootSpritesGroup.draw(self._window)
          self._display.flip()

  def keysDownEvents(self, event):
    if event.key == pg.K_LEFT:
      print("moving left")
    if event.key == pg.K_RIGHT:
      print("moving right")
    if event.key == pg.K_UP:
      print("moving up")
    if event.key == pg.K_DOWN:
      print("moving down")
    if event.key == pg.K_q:
      print("bye bye, see you soon !")
      self._crashed = True
    if event.key == pg.K_m:
      pass
            # show the map

  def keyPressed(self):
    key = pg.key.get_pressed()
    if key[pg.K_LEFT]:
      self.posX -= 1
    if key[pg.K_RIGHT]:
      self.posX += 1
    if key[pg.K_UP]:
      self.posY -= 1
    if key[pg.K_DOWN]:
      self.posY += 1
    if key[pg.K_LEFT] and (key[pg.K_LSHIFT] or key[pg.K_RSHIFT]):
      self.posX -= 2
    if key[pg.K_RIGHT]] and (key[pg.K_LSHIFT] or key[pg.K_RSHIFT]):
      self.posX += 2
    if key[pg.K_UP]] and (key[pg.K_LSHIFT] or key[pg.K_RSHIFT]):
      self.posY -= 2
    if key[pg.K_DOWN]] and (key[pg.K_LSHIFT] or key[pg.K_RSHIFT]):
      self.posY += 2

  def addGroupsSprites(self, name, parent=None):
    self._sprites[name] = pg.sprite.Group()
    if parent == None:
      self._rootSpritesGroup.addGroup(self._sprites[name])
    else:
      self._sprites[parent].addGRoup(self._sprites[name])

  def addSpriteToGroup(self, sprite, groupName=None):
    if groupName == None:
      self._rootSpritesGroup.add(sprite)
    else:
      self._sprites[groupName].add(sprite)


  def __del__(self):
    pg.quit()
