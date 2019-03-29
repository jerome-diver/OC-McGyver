'''
Controller for persons like Hero or guard who make them alive
in the game.
This class hold action's control for them.
'''

import pygame as pg

from controllers.controller import Controller
from models.person_model import *
from views.person_view import *


class PersonController(Controller):

  def __init__(self, labyrinthModel, pyGameEngine):
    super().__init__(pyGameEngine)
    self._labyrinthModel = labyrinthModel
    self._heroModel = HeroModel(self)
    self._heroView = HeroView(self, self._heroModel, pyGameEngine)
    self._guardModel = GuardModel(self)
    self._guardView = GuardView(self, self._guardModel, pyGameEngine)
    self.settingCollisions()

  def settingCollisions(self):
    hero = self._heroModel.getHero()
    hero.canCollidWith("labyrinth", self._gameEngine.getGroup("labyrinth"))
    hero.canCollidWith("guard", self._gameEngine.getGroup("guard"))

  def manageCollisions(self, caller, collidGroups, posit):
    collisions = {}
    issue = False
    for name, group in collidGroups.items():
      collisions[name] = pg.sprite.spritecollide(caller, group, False)
    if "labyrinth" in collisions.keys():
      if not collisions["labyrinth"]:
        caller._posX += posit[0]
        caller._posY += posit[1]
    if "guard" in collisions.keys():
      print("have guard group exist")
      if collisions["guard"]:
        print("have a real collision with the guard")
        issue = self.conflictualContact()
        if issue == False:
          self._gameEngine.endGame()

  def getLabyrinthModel(self):
    return self._labyrinthModel

  def getHero(self):
    return self.heroModel.getHero()

  def conflictualContact(self):
    hero = self._heroModel
    guard = self._guardModel
    if hero.canMakeSleeping():
      guard.injectPill()
    return guard.isSleeping()
