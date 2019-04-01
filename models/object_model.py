"""
This model has objects dictionary attributes (and not inherit from Object)
because when the hero has 3 objects, he will get the power to make
sleep the guard.
Also, this model will create 3 objects, then put them somewhere in the
labyrinth, and each one can be in the possesion of no one or the hero.
The strategy is close to the reality:
We create 3 objects and put them in the labyrinth, then when a collision
happen with the hero, the hero get the object and the object disapear
from the labyrinth.
Also, the hero can release the object somewhere... and it will re-appear
in this place.
The object doesn't know if he is in the possesion of the hero or not,
it just know if it is in collision with the hero and if it has to be shown.
"""

from components.object import Object
from models.model import Model
from settings import *

class ObjectModel(Model):

  def __init__(self):
    super().__init__()
    self._objects = []
    # create specifics Object and store them
    self._objects.append(Object("pill"))
    self._objects.append(Object("needle"))
    self._objects.append(Object("diluent"))

  # it should have a time where the Objects need to find
  # a position in the labyrinth
  # and store this position
  # (this method is the way to set position of one of them)
  def set_position(self, coordonates, obj):
    self.check_coordonates(coordonates)
    pos = (int(coordonates[0] * 40 + ADJ_X + 8), \
           int(coordonates[1] * 40 + ADJ_Y + 8))
    obj.set_position(pos)
    obj.set_coordonates(coordonates)

  # the controller later will want to use each objects...
  # then it will ask for them, let's give him a way to haev them all
  def get_objects(self):
    return self._objects

