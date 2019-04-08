'''
This class is a collider controller decorator.
It gives the ability to an other child class to remember
with which group she can collide.
It get the name of the Sprite also
'''

import pygame as pg

from washer import Washer


class Collider(Washer):
    '''Manage functionalities for PyGame Group/Sprites collisions'''

    def __init__(self, game_engine):
        self._game_engine = game_engine
        self._collided_groups_actions = {}

    def can_collid_with(self, group):
        '''Indicate that this Sprite can collid with this group:str'''
        self._collided_groups_actions[group] = None

    def setting_collisions_for(self, target, order,
                               do_kill=False, if_collid=True):
        '''Setting collision functions to call for this target:str

        provide a function with order:function
        kill the Sprite touched by do_kill:bool
        check happening collision when if_collid:bool'''
        group_target = self._game_engine.get_group(target)
        self.can_collid_with(group_target)
        self._collided_groups_actions[group_target] = (order,
                                                       do_kill,
                                                       if_collid)

    def manage_collisions(self, caller, *args):
        '''Manage the collision by check if this is happening

        and then, do what ordered functions want to do with own conditions'''
        for group, actions in self._collided_groups_actions.items():
            do_kill, if_collid = actions[1], actions[2]
            collisions = pg.sprite.spritecollide(caller, group, do_kill)
            if if_collid:
                if collisions:
                    self._collided_groups_actions[group][0](caller, *args,
                                                            collisions[0])
            else:
                if not collisions:
                    self._collided_groups_actions[group][0](caller, *args)
