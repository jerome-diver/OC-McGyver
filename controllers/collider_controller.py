'''
This class is a collider controller decorator.
It gives the ability to an other child class to remember
with which group she can collide.
It get the name of the Sprite also
'''

import pygame as pg

from washer import Washer

class Collider(Washer):

  def __init__(self, game_engine):
    self._game_engine = game_engine
    self._collided_groups_actions = {}

  # it is possible there to create a collision event to be handle by
  # the controller
  def can_collid_with(self, group):
    self._collided_groups_actions[group] = None
    print("can collid with:", group, "of name:", group._name)

  def setting_collisions_for(self, target, order,
                             do_kill=False, if_collid=True):
    # target:str  |  order:function()
    group_target = self._game_engine.get_group(target)
    self.can_collid_with(group_target)
    self._collided_groups_actions[group_target] = (order,
                                                   do_kill,
                                                   if_collid)

  def manage_collisions(self, caller, *args):
    for group, actions in self._collided_groups_actions.items():
      do_kill, if_collid = actions[1], actions[2]
      collisions = pg.sprite.spritecollide(caller, group, do_kill)
      if if_collid:
        if len(collisions) != 0:
          self._collided_groups_actions[group][0](caller, *args)
      else:
        if len(collisions) == 0:
          self._collided_groups_actions[group][0](caller, *args)
