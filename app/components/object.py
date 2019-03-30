'''
The Object class contain each object who can be find inside any room randomly.
it has to get a name at create time, because this name
is specific for the object image to show.
'''
import pygame as pg
from pygame.sprite import Sprite


class Object(Sprite):

  def __init__(self, controller, name):
    super().__init__()
    self._counter = 0   # i prefer to slow down the update rate for manageCollisions
    self._controller = controller
    self._name = name
    img = ""
    # depend of the kind of object to create (there is only 3 possibilities)
    # we have to know which one image to show for each of them
    if name == "pill":
      img = pillFile
    elif name == "needle":
      img = needleFile
    elif name == "diluent":
      img = diluentFile
    # but we have to check this file is readable and accepted by pygame too
    try:
      self.image = pg.image.load(img).convert()
    except pg.error:
      print("can not load image:", img)
      raise SystemExit
    self.image = pg.transform.scale(self.image, (30, 30))
    self.rect = self.image.get_rect()  # now the object has a position for the Sprite

  def upadate(self):
    self.counter += 1
    if self.counter == 20:
      self.counter = 0
      # the controller will make this job (MVC)
      self._controller.manageCollisions(self)

  """
  the controller or the view can do these following's jobs...
  But ok, if i accept to let the controller or the view
  do this jobs, i also need to indcate there which
  Object to set position and can collid,
  And then, overload a basic method inside the specific view or
  controller for Object because of the signature will no more
  be the same than other Hero/Guard or Labyrinth
  and that is too much for just this little jobs
  """

  def setPosition(self, pos):
    self._posX, self._posY = pos

  def canCollidWith(self, name, group):
    self._collidGroups[name] = group

  def getName(self):
    return self._name
