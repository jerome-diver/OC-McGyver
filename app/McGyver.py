from controllers.labyrinth_controller import *
from controllers.object_controller import *
from controllers.person_controller import *
from pygame_engine.game_engine import *


def Main():
  # create the game engine 'pygame'
  game_engine = PyGameEngine()
  # create controllers for objects to construct inside the game
  labyrinth_ctrl = LabyrinthController(game_engine)
  person_ctrl = PersonController(labyrinth_ctrl.get_model(), game_engine)
  #object_ctrl = ObjectController(labyrinth_ctrl.getModel(), game_engine)
  # start the game
  game_engine.start()


if __name__ == "__main__":
  Main()
