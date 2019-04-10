"""
ALL of classes there are Elements inherited from pygame Sprite.
Except for Wall who is just a wall Sprite image.
A Sprite is a container who handle the view
and must have minimum 2 attributs:
    self.image  (for handle image view)
    self.rect   (for handle position of this image)

The pygame idea is to create a surface
(who is also an image you can draw on)
then you can put this sprite inside a sprite-group
for handle events collisions or what ever it will happen in the game
"""


import pygame as pg
from pygame.sprite import Sprite

from settings import LABYRINTH_WALL_COLOR


class Element(Sprite):
    '''Each Element is a pygame.sprites.Sprite

    It must have a self.image and self.rect (because Sprite need)
    It has self: controller, name, position and coordonate'''

    def __init__(self, controller, name, file):
        super().__init__()
        self._controller = controller
        self._name = name
        self._pos = None  # screen position in pixels (x,y)
        self._coordonates = None  # cells position (row,col)
        try:
            self.image = pg.image.load(file).convert()
        except pg.error:
            print("can not load image:", file)
            raise SystemExit
        self.image = pg.transform.scale(self.image, (30, 30))
        self.rect = self.image.get_rect()

    def set_position(self, position):
        '''Setting position in pixel (tuple(x:int, y:int)'''
        self._pos = position

    def set_coordonates(self, coordonates):
        '''Setting cell coordonate: tuple(row:int, column:int)'''
        self._coordonates = coordonates

    def get_coordonates(self):
        '''Return self cell's coordonates: tuple(row:int, column:int)'''
        return self._coordonates

    def get_position(self):
        '''Return self pixel position: tuple(x:int, y:int)'''
        return self._pos

    def get_name(self):
        'Return his _name:str'
        return self._name

    def get(self):
        '''Return himself'''
        return self

    def update(self, *args):
        '''Update his position'''
        self.rect.topleft = self._pos


class Hero(Element):
    '''Hero is an Element (and then, a Sprite)

    but Hero can move and has objects'''

    def __init__(self, controller, file):
        super().__init__(controller, "hero", file)
        self._objects = []  # list of objects found

    def update(self, *args):
        '''Update current position and search for key hold pressed'''
        self.rect.topleft = self._pos
        self._controller.key_pressed(self)

    def move(self, _dx=0, _dy=0):
        '''Go for a move and ask to manage collisions to his controller'''
        self.rect.topleft = (self._pos[0] + _dx, self._pos[1] + _dy)
        self._controller.manage_collisions(self, _dx, _dy)
        self._controller.check_exit()

    def add_object(self, obj):
        '''Add an Object'''
        if len(self._objects) < 3:
            self._objects.append(obj)

    def get_objects(self):
        '''Return his objects'''
        return self._objects


class Wall(Sprite):
    '''A Sprite Wall'''

    _numbers = 0
    _removed = 0

    def __init__(self, idd, adj):
        super().__init__()
        Wall._numbers += 1
        self.row, self.col, side = idd
        self.adjust = adj
        self._name = "Wall"
        _form = (45, 5) if side in ["top", "bottom"] else (5, 45)
        self.image = pg.Surface(_form)
        self.image.fill(LABYRINTH_WALL_COLOR)
        self.rect = self.image.get_rect()  # a sprite must have one
        # now a wall should be positionned inside his labyrinth
        position = (self.col * 40 + self.adjust[0],
                    self.row * 40 + self.adjust[1])
        if side in ["top", "left"]:
            self.rect.topleft = position
        elif side == "bottom":
            self.rect.topleft = (position[0], position[1] + 40)
        elif side == "right":
            self.rect.topleft = (position[0] + 40, position[1])

    def __del__(self):
        '''Wash statics variables'''
        Wall._numbers -= 1
        Wall._removed += 1

    def update(self, *args):
        '''Update does nothing there'''

