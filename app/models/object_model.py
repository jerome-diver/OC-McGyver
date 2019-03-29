"""
This model has objects dictionary attributes (and not inherit from Object)
because when the hero has 3 objects, he will get the power to make sleep the guard.
Also, this model will create 3 objects, then put them somewhere in the labyrinth,
and each one can be in the possesion of no one or the hero.
The strategy is close to the reality:
We create 3 objects and put them in the labyrinth, then when a collision happen
with the hero, the hero get the object and the object disapear from the labyrinth.
Also, the hero can release the object somewhere... and it will re-appear in this place.
The object doesn't know if he is in the possesion of the hero or not,
it just know if it is in collision with the hero and if it has to be shown.
"""

from components.object import Object
from models.model import Model


class ObjectModel(Model):

  def __init__(self, controller):
    super().__init__()
    self._objects = {}      # { "name": Object } (must have 3 keys maximum)
    self._canMakeSleep = False

  def setCoordonates(self, coordonates, which):
    checkCoordonates(coordonates)
    if isinstance(which, str):
      self._objects[which]._coordonates = coordonates
    if isinstance(which, Object):
      which.setCoordinates(coordinates)

  def getCoordonates(self, which):
    if isinstance(which, str):
      return self._objects[which]
    if isinstance(which, Object):
      return which.getCoordinates()
