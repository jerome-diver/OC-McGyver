from controllers.labyrinth_controller import *
from controllers.object_controller import *
from controllers.person_controller import *
from pygame_engine.game_engine import *


def Main():
  # create the game engine 'pygame'
  gameEngine = PyGameEngine()
  # create controllers for objects to construct inside the game
  labyrinthCtrl = LabyrinthController(gameEngine)
  personCtrl = PersonController(labyrinthCtrl.getModel(), gameEngine)
  # this is not finish, i have to implement some controllers methods
  # and test this Object codes. Then it should be finish for the project
  objectCtrl = ObjectController(labyrinthCtrl.getModel(), gameEngine)
  # start the game
  gameEngine.start()


if __name__ == "__main__":
  Main()
