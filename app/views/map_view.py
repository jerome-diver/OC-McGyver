'''
The specific view of the map.
This load image of map inside the game view
'''

import os
import pygame

from views.view import *
from views.sprites import MapSprite


class MapView(View):

    _width = 600
    _height = 600
    _map_bg= (0,240,50)

    def __init__(self, mapModel):
        super().__init__(mapModel)
        mapModel.setImage(pygame.Surface((_height,_width)), _map_bg)
        self.createSprite()

    def createSprite(self):
        self._sprite = MapSprite(self._model)
        self._gameEngine.addGroupSprites("Map")
        self._gameEngine.addSpriteToGroup(self._sprite, "Map")
        
