'''
The Person object has a game life...
'''


class Person:

  _name = ""
  _sLookingAt = ""

  def __init__(self, looking_where):
    isLookingAt(looking_where)

  def getName(self):
    return self._name

  def setName(self, name):
    self._name = name

  def isLookingWhere(self):
    return self._isLookingAt

  def isLookingAt(self, direction):  # is looking in front of him (set where)
    checkDirection(direction)
    self._isLookingAt = direction


class Hero(Sprite):

  def __init_(self):
    super().__init__()

  def update(self):
    self.keyPressed()

  def move(self, dx=0, dy=0):
    pass
    
  def keyPressed(self):
    key = pg.key.get_pressed()
    if key[pg.K_LEFT]:
      self.move(dx -= 1)
    if key[pg.K_RIGHT]:
      self.move(dx += 1)
    if key[pg.K_UP]:
      self.move(dy -= 1)
    if key[pg.K_DOWN]:
      self.move(dy += 1)
    if key[pg.K_LEFT] and (key[pg.K_LSHIFT] or key[pg.K_RSHIFT]):
      self.move(dx -= 2)
    if key[pg.K_RIGHT] and (key[pg.K_LSHIFT] or key[pg.K_RSHIFT]):
      self.move(dx += 2)
    if key[pg.K_UP] and (key[pg.K_LSHIFT] or key[pg.K_RSHIFT]):
      self.move(dy -= 2)
    if key[pg.K_DOWN] and (key[pg.K_LSHIFT] or key[pg.K_RSHIFT]):
      self.move(dy += 2)
