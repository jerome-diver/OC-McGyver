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
    self._can_make_sleep = False
    # now it's time to create specifics Object
    # and in the same time, store them inside the model attributes
    # self._objects dictionary
    self._objects["pill"] = Object(self._controller, "pill")
    self._objects["needle"] = Object(self._controller, "needle")
    self._objects["diluent"] = Object(self._controller, "diluent")

  # it should have a time where the Objects need to find
  # a position in the labyrinth
  # and store this position
  # (this method is the way to set position of one of them)
  def setCoordonates(self, coordonates, which):
    check_coordonates(coordonates)
    # no one know which method will be choosed to target the object
    # so let's find if this is an Object argument or a string name
    if isinstance(which, str):
      self._objects[which]._coordonates = coordonates
    if isinstance(which, Object):
      which.set_coordinates(coordinates)

  def get_coordonates(self, which):
    if isinstance(which, str):
      return self._objects[which]
    if isinstance(which, Object):
      return which.get_coordinates()

  # the controller later will want to use each objects...
  # then it will ask for them, let's give him a way to haev them all
  def get_objects(self):
    return self._objects

  def set_positions_objects(self):
    pass
