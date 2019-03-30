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

  def __init__(self, controller, model, game_engine):
    super().__init__(controller, model, game_engine)
    guard = self._model.get_guard()
    labyrinth_model = self._controller.get_labyrinth_model()
    guard.set_position(labyrinth_model.get_guard_position())
    self._game_engine.add_sprites_to_group([guard], "guard")


class HeroView(View):

  def __init__(self, controller, model, game_engine):
    super().__init__(controller, model, game_engine)
    labyrinth_model = self._controller.get_labyrinth_model()
    hero = self._model.get_hero()
    print("best position for hero is",
          labyrinth_model.get_best_hero_position())
    hero.set_position(labyrinth_model.get_best_hero_position())
    self._game_engine.add_sprites_to_group([hero], "hero")
