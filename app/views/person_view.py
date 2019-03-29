"""
Set views for Hero and guard personage
hero:
    _can move (the guerd can not)
    _can get objects he fonds inside the labyrinth
    _3 objects found give hero power of make sleeping the guard
    _can only go out of the labyrinth by the exit door.
guard:
    _can not _removedguard can _sleep
    _stay in front of the door
    _can kill someone touched him (if he is not sleeping)

"""

from settings import *
from views.view import View


class GuardView(View):

  def __init__(self, controller, model, gameEngine):
    super().__init__(controller, model, gameEngine)
    guard = self._model.getGuard()
    labyrinthModel = self._controller.getLabyrinthModel()
    print("The guard has to hold position in front of the exit, this position is",
          labyrinthModel.getGuardPosition())
    guard.setPosition(labyrinthModel.getGuardPosition())
    self._gameEngine.addSpritesToGroup([guard], "guard")
    guard.canCollidWith("hero", self._gameEngine.getGroup("hero"))


class HeroView(View):

  def __init__(self, controller, model, gameEngine):
    super().__init__(controller, model, gameEngine)
    self._gameEngine.createGroup("hero")
    labyrinthModel = self._controller.getLabyrinthModel()
    hero = self._model.getHero()
    print("best position for hero is",
          labyrinthModel.getbestHeroPosition())
    hero.setPosition(labyrinthModel.getbestHeroPosition())
    self._gameEngine.addSpritesToGroup([hero], "hero")
    hero.canCollidWith("labyrinth", self._gameEngine.getGroup("labyrinth"))
