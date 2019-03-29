'''
Model of Person and specific Person like Hero or Guard,
 who have some specific features added.
The superclass is a Model class
'''
from time import time

from components.person import Guard, Hero
from models.model import Model


class GuardModel(Guard, Model):

  def __init__(self):
    super().__init__(name="Johnny Johnny")
    self._endSleepîngTime = 0

  def vaccinInjected(self):
    self._endSleepingTime = 0


class HeroModel(Hero, Model):

  def __init__(self, controller):
    Hero.__init__(self, controller=controller, name="MacGyver")
    Model.__init__(self)
    self._objects = []  # list of Object() found

  def getObjects(self):
    return self._objects

  def getObject(self, object):
    if obj in self._objects:
      return obj

  def addObject(self, object):
    if len(self._objects) <= 3:
      self._objects.append(object)
      return True
    return False

  def trashObject(self, one_object):
    if obj in self._objects:
      self._objects.delete(one_object)

  def canMakeSleeping(self):
    return len(self._objects) >= 3
