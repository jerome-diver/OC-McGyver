#! /usr/bin/python3
import binascii
import os.path
import sys

import pygame
import pygame.locals

'''
  this test pygame game who can grab dimension of window and images from
  arguments at command call,
  It will also create a labyrinth from a data file (half-byte code inside)
  You should hit "q" for quit this demo game.
  You can also move the image with arrows keyboards keys.
  This test pygame use Sprite inherited class for embed groups of sprites
  to manage collisions from the game loop.
'''


"""
define global variables catch from command line and test them
"""
thisFilePath = os.path.dirname(os.path.abspath(__file__))
img = os.path.join("img", sys.argv[3])
width = 0
height = 0

if len(sys.argv) != 4:
  print("you should call it like this example:")
  print("./pygame_demo 600 400 image_name.png")
  print("and the png/jpeg/bmp image has to be inside ./img/ directory")
  raise Exception("You have to use correct syntax call for this command")
if not os.path.isfile(img):
  raise Exception("last argument has to be an existing file, ",
                  img, " doesn't exist.")

try:
  width = int(sys.argv[1])
except ValueError:
  print("first argument has to be a valid integer.")
  quit()

try:
  height = int(sys.argv[2])
except ValueError:
  print("second argument has to be a valid interger.")
  quit()


red = (255, 0, 0)
black = (0, 0, 0)
white = (255, 255, 255)


class Labyrinth(pygame.sprite.Sprite):
  '''
  static dictionnaries for read map byte codes from file and Sprite's Walls
  The file has on each line a char who represent a byte 1/2 hex code.
  This, inside the file is a representation of a cell/room of the labyrinth
  position (by its own data position inside the file) and anclosure walls of
  this room/cell. The byte code is simple and can be decrypted as a bin value.
  first unit bin is for "top" side cell/room wall, second for the left side
  wall of this cell, etc... clock-wise turn around the cell.
  (use of static attribute reduce memory usage)
  '''
  _walls_bytes = {}  # { (row, col): byte }
  _walls = {}       # { (row, col, side): Labyrinth.Wall }
  adjX = (width - 600) / 2
  adjY = (height - 600) / 2
  rows, columns = 0, 0

  def __init__(self, group):  # will use own group sprite for collisions check
    super().__init__()
    self.group = group
    self.image = pygame.Surface((600, 600))
    if not Labyrinth._walls_bytes:  # only at first class creation time
      self.readLabyrinth()
      self.printLabyrinth()

  @staticmethod
  def readLabyrinth():  # load map from file to static var _walls_bytes
    cwd = os.path.dirname(os.path.abspath(__file__))
    _file = os.path.join(cwd, "map/map.txt")
    with open(_file, "r") as mapFile:
      for row, line in enumerate(mapFile):
        Labyrinth.rows += 1
        for col, char in enumerate(line.strip()):
          Labyrinth.columns += 1
          Labyrinth._walls_bytes[(row, col)] = binascii.unhexlify("0" + char)
      Labyrinth.columns = int(Labyrinth.columns / Labyrinth.rows)

  @staticmethod
  def wallExist(wall):    # check for existing same wall in the labyrinth
    if Labyrinth._walls:
      for oldWall in Labyrinth._walls.values():
        if (wall.rect.topleft == oldWall.rect.topleft) and \
           (wall.rect.bottomright == oldWall.rect.bottomright):
          return True
    return False

  @staticmethod
  def getbestHeroPosition():  # return initial best HHero position
    return (Labyrinth.rows * 40 + Labyrinth.adjX - 35,
            Labyrinth.columns * 40 + Labyrinth.adjY - 35)

  def printLabyrinth(self):  # create Sprites Walls from bytes cells codes
    for key, value in Labyrinth._walls_bytes.items():
      sides = ("top", "right", "bottom", "left")
      bin_code = "{0:b}".format(ord(value)).zfill(4)[::-1]
      for index, power in enumerate(bin_code):
        if int(power) == 1:
          idd = (key[0], key[1], sides[index])
          newWall = self.Wall(idd)
          if not self.wallExist(newWall):  # do not accept doubles
            Labyrinth._walls[idd] = newWall
            self.group.add(Labyrinth._walls[idd])
    print("there is", len(Labyrinth._walls), "walls in the labyrinth")

  class Wall(pygame.sprite.Sprite):
    '''
    Create Wall(Sprite) object from cell's position and his own byte data
    '''

    def __init__(self, idd):
      super().__init__()
      row, col, side = idd
      # adapt the surface to the wall orientation
      self.image = pygame.Surface((45, 5)) if side in ["top", "bottom"] \
          else pygame.Surface((5, 40))
      if side in ["top", "bottom"]:    # horizontal walls
        pygame.draw.rect(self.image, red, [0, 0, 45, 5])
      elif side in ["left", "right"]:  # vertical walls
        pygame.draw.rect(self.image, red, [0, 0, 5, 40])
      self.rect = self.image.get_rect()  # a sprite must have one
      # now a wall should be positionned inside his labyrinth
      position = (col * 40 + Labyrinth.adjX, row * 40 + Labyrinth.adjY)
      if side in ["top", "left"]:
        self.rect.topleft = position
      elif side == "bottom":
        self.rect.topleft = (position[0], position[1] + 40)
      elif side == "right":
        self.rect.topleft = (position[0] + 40, position[1])

      def update(self):
        pass


class Hero(pygame.sprite.Sprite):

  def __init__(self, img, posit):
    super().__init__()
    self.posX, self.posY = posit
    self.image = pygame.image.load(img)
    # should be able to run inside the labyrinth
    self.image = pygame.transform.scale(self.image, (30, 30))
    self.rect = self.image.get_rect()  # a sprite must have one

  def move(self, dx=0, dy=0):
    self.rect.topleft = (self.posX + dx, self.posY + dy)
    willCollid = pygame.sprite.spritecollide(self, self.collideGroup, False)
    if not willCollid:  # can not overlap a wall
      self.posX += dx
      self.posY += dy

  def canCollideWith(self, group):
    self.collideGroup = group

  def update(self):
    self.rect.topleft = (self.posX, self.posY)


def setupPygame(width, height, image):
  pygame.init()
  display = pygame.display
  window = display.set_mode((width, height))
  display.set_caption("Mac Gyver -- OpenClassRooms projetc 3 --")
  clk = pygame.time.Clock()
  crashed = False
  posX, posY = 0, 0
  try:
    mcGyverIMG = pygame.image.load(image)
  except pygame.error:
    print("can not load image", mcGyverIMG)
    raise SystemExit
  # the groups of sprites for ability of collisions and more...
  rootGroup = pygame.sprite.Group()
  labyrinthGroup = pygame.sprite.Group()
  labyrinth = Labyrinth(labyrinthGroup)
  rootGroup.add(labyrinthGroup)
  hero = Hero(img, labyrinth.getbestHeroPosition())
  hero.canCollideWith(labyrinthGroup)
  rootGroup.add(hero)

  def message(text):  # can create a message text to read
    font = pygame.font.Font("Ubuntu-M.ttf", 12)
    surf = font.render(text, True, white)
    container = surf.get_rect()
    container.topright = (width, 0)
    window.blit(surf, container)
    pygame.display.update()

  while not crashed:  # the game loop actions
    # define events key bindings (no repeat bounds)
    for ev in pygame.event.get():
      if ev.type == pygame.KEYDOWN:
        print("you pressed keyboard key", pygame.key.name(ev.key))
        if ev.key == pygame.K_LEFT:
          print("moving left...")
        elif ev.key == pygame.K_RIGHT:
          print("moving right")
        elif ev.key == pygame.K_DOWN:
          print("moving down")
        elif ev.key == pygame.K_UP:
          print("moving up")
        elif ev.key == pygame.K_q:
          print("bye bye... see you soon !")
          crashed = True
      elif ev.type == pygame.QUIT:
        crashed = True
    # define key bondings holded (move actions of hero)
    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT]:
      hero.move(dx=-1)
    if key[pygame.K_RIGHT]:
      hero.move(dx=1)
    if key[pygame.K_UP]:
      hero.move(dy=-1)
    if key[pygame.K_DOWN]:
      hero.move(dy=1)
    if key[pygame.K_DOWN] and (key[pygame.K_LSHIFT] or key[pygame.K_RSHIFT]):
      hero.move(dy=2)
    if key[pygame.K_UP] and (key[pygame.K_LSHIFT] or key[pygame.K_RSHIFT]):
      hero.move(dy=-2)
    if key[pygame.K_LEFT] and (key[pygame.K_LSHIFT] or key[pygame.K_RSHIFT]):
      hero.move(dx=-2)
    if key[pygame.K_RIGHT] and (key[pygame.K_LSHIFT] or key[pygame.K_RSHIFT]):
      hero.move(dx=2)
    clk.tick(40)

    rootGroup.update()
    window.fill(black)
    rootGroup.draw(window)

    message('hit "q" key to exit')
    pygame.display.flip()
  pygame.quit()


setupPygame(width, height, img)
quit()
