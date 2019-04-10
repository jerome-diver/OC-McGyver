'''
Mac Gyver 2D Board Labyrinth game
OpenClassRooms
Projet-3
Auhtor: Jerome Lanteri
'''


from controllers.labyrinth_controller import LabyrinthController
from controllers.object_controller import ObjectController
from controllers.person_controller import HeroController, GuardController
from game_engine import GameEngine


def main():
    '''The main programme (to run first)'''
    # create the game engine 'pygame'
    game_engine = GameEngine()
    # create controllers for objects to construct inside the game
    labyrinth_ctrl = LabyrinthController(game_engine)
    guard_ctrl = GuardController(labyrinth_ctrl, game_engine)
    hero_ctrl = HeroController(labyrinth_ctrl, guard_ctrl, game_engine)
    ObjectController(labyrinth_ctrl,
                     hero_ctrl, guard_ctrl,
                     game_engine)
    hero_ctrl.setting_collisions()
    # start the game
    game_engine.start()


if __name__ == "__main__":
    main()
