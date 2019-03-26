''' 
Sprites class inherited from pygame.sprites.Sprite base class
to be used inside own views class as composite attribute
'''

from pygame.sprites import *


class MapSprite(Sprite):

    _red = (255,0,0)
    _black = (0,0,0)
    _white = (255,255,255)
    _width = 600
    _height = 600

    def __init__(self, mapModel):
        super().__init__()
        self._model = mapModel
        self._image = mapModel.getImage()
        self._rect = self._image.get_rect()
        self._rect.center = (_width, _height)   

    def update(self):
        pass


class RoomSprite(Sprite):

    def __init__(self, _map):
        super().__init__()


class HeroSprite(Sprite):

    def __init__(self, _map):
        super().__init__()


class GuardSprite(Sprite):

    def __init__(self, _map):
        super().__init__()


class ObjectSprite(Sprite):

    def __init__(self, _map):
        super().__init__()