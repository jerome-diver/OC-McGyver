#! /usr/bin/python3
'''
  This test pygame game who can grab dimension of window and images from
  arguments at command call,
  It will also create a labyrinth from a data file (half-byte code inside)
  You should hit "q" for quit this demo game.
  You can also move the image with arrows keyboards keys.
  This test pygame use Sprite inherited class for embed groups of sprites
  to manage collisions from the game loop.
'''

import binascii
import os.path
import sys

import pygame
import pygame.locals

IMG = os.path.join("img", sys.argv[3])
WIDTH = 0
HEIGHT = 0

if len(sys.argv) != 4:
    print("you should call it like this example:")
    print("./pygame_demo 600 400 image_name.png")
    print("and the png/jpeg/bmp image has to be inside ./img/ directory")
    raise Exception("You have to use correct syntax call for this command")
if not os.path.isfile(IMG):
    raise Exception("last argument has to be an existing file, ",
                    IMG, " doesn't exist.")

try:
    WIDTH = int(sys.argv[1])
except ValueError:
    print("first argument has to be a valid integer.")
    quit()

try:
    HEIGHT = int(sys.argv[2])
except ValueError:
    print("second argument has to be a valid interger.")
    quit()

RED = (255, 0, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


class Labyrinth(pygame.sprite.Sprite):
    '''Static dictionnaries for read map byte codes from file and Sprite's Walls

    The file has on each line a char who represent a byte 1/2 hex code.
    This, inside the file is a representation of a cell/room of the labyrinth
    position (by its own data position inside the file) and anclosure walls of
    this room/cell. The byte code is simple and can be decrypted as a bin value.
    first unit bin is for "top" side cell/room wall, second for the left side
    wall of this cell, etc... clock-wise turn around the cell.
    (use of static attribute reduce memory usage)
    '''
    _walls_bytes = {}  # { (row, col): byte }
    _walls = {}  # { (row, col, side): Labyrinth.Wall }
    _adj_x = (WIDTH - 600) / 2
    _adj_y = (HEIGHT - 600) / 2
    _rows, _columns = 0, 0

    def __init__(self,
                 group):  # will use own group sprite for collisions check
        super().__init__()
        self.group = group
        self.image = pygame.Surface((600, 600))
        if not Labyrinth._walls_bytes:  # only at first class creation time
            self.read_labyrinth()
            self.print_labyrinth()

    @staticmethod
    def read_labyrinth():
        '''Load map from file to static var _walls_bytes'''
        _cwd = os.path.dirname(os.path.abspath(__file__))
        _file = os.path.join(_cwd, "map/map.txt")
        with open(_file, "r") as _map_file:
            for _row, _line in enumerate(_map_file):
                Labyrinth._rows += 1
                for _col, _char in enumerate(_line.strip()):
                    Labyrinth._columns += 1
                    Labyrinth._walls_bytes[(_row, _col)] = binascii.unhexlify(
                        "0" + _char)
            Labyrinth._columns = int(Labyrinth._columns / Labyrinth._rows)

    @staticmethod
    def wall_exist(wall):
        '''check for existing same wall in the labyrinth'''
        if Labyrinth._walls:
            for _old_wall in Labyrinth._walls.values():
                if (wall.rect.topleft == _old_wall.rect.topleft) and \
                        (wall.rect.bottomright == _old_wall.rect.bottomright):
                    return True
        return False

    @staticmethod
    def get_hero_position():
        '''return initial best HHero position'''
        return (Labyrinth._rows * 40 + Labyrinth._adj_x - 35,
                Labyrinth._columns * 40 + Labyrinth._adj_y - 35)

    def print_labyrinth(self):
        '''create Sprites Walls from bytes cells codes'''
        for _key, _value in Labyrinth._walls_bytes.items():
            _sides = ("top", "right", "bottom", "left")
            _bin_code = "{0:b}".format(ord(_value)).zfill(4)[::-1]
            for _index, _power in enumerate(_bin_code):
                if int(_power) == 1:
                    _idd = (_key[0], _key[1], _sides[_index])
                    _new_wall = self.Wall(_idd)
                    if not self.wall_exist(_new_wall):  # do not accept
                        # doubles
                        Labyrinth._walls[_idd] = _new_wall
                        self.group.add(Labyrinth._walls[_idd])
        print("there is", len(Labyrinth._walls), "walls in the labyrinth")


    class Wall(pygame.sprite.Sprite):
        '''Create Wall(Sprite) object from cell's position and his own byte data'''

        def __init__(self, idd):
            super().__init__()
            _row, _col, _side = idd
            # adapt the surface to the wall orientation
            _dim = (45, 5) if _side in ["top", "bottom"] \
                          else (5, 45)
            self.image = pygame.Surface(_dim)
            if _side in ["top", "bottom"]:  # horizontal walls
                pygame.draw.rect(self.image, RED, [0, 0, 45, 5])
            elif _side in ["left", "right"]:  # vertical walls
                pygame.draw.rect(self.image, RED, [0, 0, 5, 40])
            self.rect = self.image.get_rect()  # a sprite must have one
            # now a wall should be positionned inside his labyrinth
            _position = (_col * 40 + Labyrinth._adj_x, _row * 40 +
                         Labyrinth._adj_y)
            if _side in ["top", "left"]:
                self.rect.topleft = _position
            elif _side == "bottom":
                self.rect.topleft = (_position[0], _position[1] + 40)
            elif _side == "right":
                self.rect.topleft = (_position[0] + 40, _position[1])

            def update(self, *args):
                '''Sprite need it'''
                pass


class Hero(pygame.sprite.Sprite):
    '''This is the Hero Sprite'''

    def __init__(self, img, posit):
        super().__init__()
        self._pos_x, self._pos_y = posit
        self.image = pygame.image.load(img)
        # should be able to run inside the labyrinth
        self.image = pygame.transform.scale(self.image, (30, 30))
        self.rect = self.image.get_rect()  # a sprite must have one

    def move(self, _dx=0, _dy=0):
        '''Move action if can do'''
        self.rect.topleft = (self._pos_x + _dx, self._pos_y + _dy)
        _will_collid = pygame.sprite.spritecollide(self,
                                                   self._collide_group,
                                                   False)
        if not _will_collid:  # can not overlap a wall
            self._pos_x += _dx
            self._pos_y += _dy

    def can_collide_with(self, group):
        '''Setting group for collisions'''
        self._collide_group = group

    def update(self):
        '''Update himself'''
        self.rect.topleft = (self._pos_x, self._pos_y)


def setup_game(width, height, image):
    '''Setup the game engine PyGame'''
    pygame.init()
    _display = pygame.display
    _window = _display.set_mode((width, height))
    _display.set_caption("Mac Gyver -- OpenClassRooms projetc 3 --")
    _clk = pygame.time.Clock()
    _crashed = False
    _pos_x, _pos_y = 0, 0
    try:
        _mac_gyver_img = pygame.image.load(image)
    except pygame.error:
        print("can not load image", _mac_gyver_img)
        raise SystemExit
    # the groups of sprites for ability of collisions and more...
    _root_group = pygame.sprite.Group()
    _labyrinth_group = pygame.sprite.Group()
    _labyrinth = Labyrinth(_labyrinth_group)
    _root_group.add(_labyrinth_group)
    hero = Hero(IMG, _labyrinth.get_hero_position())
    hero.can_collide_with(_labyrinth_group)
    _root_group.add(hero)

    def message(text):
        '''Can create a message text to read'''
        _font = pygame.font.Font("Ubuntu-M.ttf", 12)
        _surf = _font.render(text, True, WHITE)
        _container = _surf.get_rect()
        _container.topright = (WIDTH, 0)
        _window.blit(_surf, _container)
        pygame.display.update()

    while not _crashed:  # the game loop actions
        # define events key bindings (no repeat bounds)
        for _ev in pygame.event.get():
            if _ev.type == pygame.KEYDOWN:
                print("you pressed keyboard key", pygame.key.name(_ev.key))
                if _ev.key == pygame.K_LEFT:
                    print("moving left...")
                elif _ev.key == pygame.K_RIGHT:
                    print("moving right")
                elif _ev.key == pygame.K_DOWN:
                    print("moving down")
                elif _ev.key == pygame.K_UP:
                    print("moving up")
                elif _ev.key == pygame.K_q:
                    print("bye bye... see you soon !")
                    _crashed = True
            elif _ev.type == pygame.QUIT:
                _crashed = True
        # define key bindings holded (move actions of hero)
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            hero.move(dx=-1)
        if key[pygame.K_RIGHT]:
            hero.move(dx=1)
        if key[pygame.K_UP]:
            hero.move(dy=-1)
        if key[pygame.K_DOWN]:
            hero.move(dy=1)
        if key[pygame.K_DOWN] and (
                key[pygame.K_LSHIFT] or key[pygame.K_RSHIFT]):
            hero.move(dy=2)
        if key[pygame.K_UP] and (key[pygame.K_LSHIFT] or key[pygame.K_RSHIFT]):
            hero.move(dy=-2)
        if key[pygame.K_LEFT] and (
                key[pygame.K_LSHIFT] or key[pygame.K_RSHIFT]):
            hero.move(dx=-2)
        if key[pygame.K_RIGHT] and (
                key[pygame.K_LSHIFT] or key[pygame.K_RSHIFT]):
            hero.move(dx=2)
        _clk.tick(40)

        _root_group.update()
        _window.fill(BLACK)
        _root_group.draw(_window)

        message('hit "q" key to exit')
        pygame.display.flip()
    pygame.quit()


setup_game(WIDTH, HEIGHT, IMG)
quit()
