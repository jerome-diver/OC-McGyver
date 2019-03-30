'''
Model of Person and specific Person like Hero or Guard,
 who have some specific features added.
The superclass is a Model class
'''

from components.person import Guard, Hero
from models.model import Model


class GuardModel(Guard, Model):

  def __init__(self, controller):
    Guard.__init__(self, controller, "guard")
    Model.__init__(self)
    self._sleeping = False

  def inject_pill(self):
    self._sleeping = True

  def is_sleeping(self):
    return self._sleeping


class HeroModel(Hero, Model):

  def __init__(self, controller):
    Hero.__init__(self, controller, "hero")
    Model.__init__(self)
    self._objects = []  # list of Object() found

  def get_objects(self):
    return self._objects

  def get_object(self, object):
    if obj in self._objects:
      return obj

  def add_object(self, object):
    if len(self._objects) <= 3:
      self._objects.append(object)
      return True
    return False

  def trash_object(self, one_object):
    if obj in self._objects:
      self._objects.delete(one_object)

  def can_make_sleeping(self):
    return len(self._objects) >= 3
