"""
This is an object view to be abe to show Object
"""

from random import randint

from views.view import View


class ObjectView(View):

  def __init__(self, controller, model, game_engine):
    super().__init__(controller, model, game_engine)
    self._objects = self._model.get_objects()
    # create a Sprite group for each objects
    self._game_engine.create_group("objects")
    self._game_engine.add_sprites_to_group(self._objects, "objects")
    # and setting there own position in the labyrinth
    self.setting_positions()

  def setting_positions(self):
    for _object in self._objects:
      accepted = False
      while not accepted:
        coordonates = self.generate_random_coordonates()
        if any(coordonates != c for c in self.blacklisted_coordonates()):
          self._model.set_position(coordonates, _object)
          accepted = True

  def generate_random_coordonates(self):
    row = randint(0,14)
    col = randint(0,14)
    return (row, col)

  def blacklisted_coordonates(self):
    blacklist = []
    targets = []
    hero_model = self._controller._hero_ctrl._model
    guard_model = self._controller._guard_ctrl._model
    targets.append(hero_model._coordonates)
    targets.append(guard_model._coordonates)
    for o in self._objects:
      if o._coordonates:
        targets.append(o._coordonates)
    for target in targets:
      for i in range(-5,6):
        for j in range(-5,6):
          blacklist.append((target[0] + i, \
                            target[1] + j))
    return blacklist
