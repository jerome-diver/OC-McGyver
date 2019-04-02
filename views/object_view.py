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

  # ok, let's place objects randomly
  # in the labyrinth without collid anything else...
  def setting_positions(self):
    for _object in self._objects:
      accepted = False
      # wee need to select things, i will not put things somewhere wrong
      blacklist = self.blacklisted_coordonates()
      while not accepted:
        # let's try something randomly...
        coordonates = self.generate_random_coordonates()
        # and if i can put this object there...
        if not any(coordonates == c for c in blacklist):
          # then i will do it
          self._model.set_position(coordonates, _object)
          # next...
          accepted = True

  def generate_random_coordonates(self):
    row = randint(0,14)
    col = randint(0,14)
    return (row, col)

  # we don't want to put something onside these blacklisted things
  def blacklisted_coordonates(self):
    blacklist = []
    targets = []
    labyrinth_model = self._controller._labyrinth_ctrl._model
    hero_model = self._controller._hero_ctrl._model
    guard_model = self._controller._guard_ctrl._model
    # we don't want to put object on tess guys...
    targets.append(hero_model._coordonates)
    targets.append(guard_model._coordonates)
    # and not inside wall closed structural cells...
    for closed_wall in labyrinth_model.get_closed_walls():
      c_of_cwall = labyrinth_model.get_coordonates_of_wall(closed_wall)
      targets.append(c_of_cwall)
    # if there is already some objects, we don't want to collid them
    for o in self._objects:
      if o._coordonates:
        targets.append(o._coordonates)
    # and better if they are not just to much closer of
    # anything or any one
    for target in targets:
      for i in range(-4,4):
        for j in range(-4,4):
          x = target[0] + i
          y = target[1] + j
          # and we exclude the ones who are out of
          # cells coordonates range
          if x >= 0 and x <= 14 and y >= 0  and y <= 14:
            blacklist.append((x, y))
    return blacklist
