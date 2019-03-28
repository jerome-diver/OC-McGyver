from controllers.labyrinth_controller import *
from controllers.object_controller import *
from controllers.person_controller import *
from pygame_engine.game_engine import *


def Main():
  # create the game engine 'pygame'
  gameEngine = PyGameEngine()
  # create controllers for objects to construct inside the game
  labyrinthCtrl = LabyrinthController(gameEngine)
#  personCtrl = PersonController(gameEngine)
#  objectCtrl = ObjectController(gameEngine)
  # start the game
  gameEngine.start()


if __name__ == "__main__":
  Main()
