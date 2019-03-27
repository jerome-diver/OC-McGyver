from controllers.labyrinth_controller import *
from controllers.object_controller import *
from controllers.person_controller import *
from pygame_engine.game_engine import *


def Main():
  gameEngine = PyGameEngine()
  mapCtrl = LabyrinthController(gameEngine)
  personCtrl = PersonController(gameEngine)
  objectCtrl = ObjectController(gameEngine)
  gameEngine.start()


if __name__ = "__main__":
  Main()
