from controllers.labyrinth_controller import *
from controllers.object_controller import *
from controllers.person_controller import *
from pygame_engine.game_engine import *


def Main():
  # create the game engine 'pygame'
  game_engine = PyGameEngine()
  # create controllers for objects to construct inside the game
  labyrinth_ctrl = LabyrinthController(game_engine)
  guard_ctrl = GuardController(labyrinth_ctrl,game_engine)
  hero_ctrl = HeroController(labyrinth_ctrl, guard_ctrl, game_engine)
  object_ctrl = ObjectController(labyrinth_ctrl, \
                                 hero_ctrl, guard_ctrl, \
                                 game_engine)
  hero_ctrl.setting_collisions()
  # start the game
  game_engine.start()


if __name__ == "__main__":
  Main()
