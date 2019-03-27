from pygame_engine.game_engine import *


def Main():
  gameEngine = PyGameEngine()
  mapCtrl = MapController(gameEngine)
  personCtrl = PersonController(gameEngine)
  objectCtrl = ObjectController(gameEngine)
  gameEngine.start()


if __name__ = "__main__":
  Main()
