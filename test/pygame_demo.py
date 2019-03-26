#! /usr/bin/python3
'''
  this test pygame game who can grab dimension of window and images from
  arguments at command call,
  It will also create a labyrinth from a data file (half-byte code inside)
  You should hit "q" for quit this demo game.
  You can also move the image with arrows keyboards keys.
  This test pygame use Sprite inherited class for embed groups of sprites
  to manage collisions from the game loop.
'''

import sys
import os.path
import binascii

"""
define global variables catch from command line and test them
"""

img = os.path.join("img",sys.argv[3])
width = 0
height = 0

if len(sys.argv) != 4:
    print("you should call it like this:")
    print("pygame_demo 600 400 my_file_absolute_name.png")
    raise Exception("You have to use correct syntax call for this command")
if not os.path.isfile(img):
    raise Exception("last argument has to be an existing file, ",img," doesn't exist.")

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


import pygame
import pygame.locals


red = (255,0,0)
black = (0,0,0)
white = (255,255,255)

class Labyrinth(pygame.sprite.Sprite):
  '''
  static dictionnaries for read map byte codes from file and Sprite's Walls
  The file has on each line a char who represent a byte 1/2 hex code.
  This, inside the file is a representation of a cell/room of the labyrinth
  position (by its own data position inside the file) and anclosure walls of
  this room/cell. The byte code is simple and can be decrypted as a bin value.
  first unit bin is for "top" side cell/room wall, second for the left side
  wall of this cell, etc... clock-wise turn around the cell.
  '''
  _walls_bytes = {} # { (row, col): byte }
  _walls = {}       # { (row, col, side): Labyrinth.Wall }
  adjX = (width - 600) / 2
  adjY = (height - 600) / 2
  rows = 0
  columns = 0

  def __init__(self, group):
    super().__init__()
    self.group = group
    self.image = pygame.Surface((600,600))
    if not Labyrinth._walls_bytes:  # only at first class creation time
      self.readLabyrinth()
      self.printLabyrinth()

  @staticmethod
  def readLabyrinth():  # load map from file to static var _walls_bytes
    cwd = os.path.dirname(os.path.abspath(__file__))
    _file = os.path.join(cwd,"map/map.txt")
    with open(_file, "r") as mapFile:
      for row,line in enumerate(mapFile):
        Labyrinth.rows += 1
        for col, char in enumerate(line.strip()):
          Labyrinth.columns += 1
          Labyrinth._walls_bytes[(row,col)] = binascii.unhexlify("0"+char)
      Labyrinth.columns = int(Labyrinth.columns / Labyrinth.rows)

  @staticmethod
  def wallExist(wall):
    if Labyrinth._walls:
      for oldWall in Labyrinth._walls.values():
        if (wall.rect.topleft == oldWall.rect.topleft) and \
           (wall.rect.bottomright == oldWall.rect.bottomright):
          return True
    return False

  @staticmethod
  def getbestHeroPosition():
    return (Labyrinth.rows * 40 + Labyrinth.adjX - 35, \
            Labyrinth.columns * 40 + Labyrinth.adjY  - 35)

  def printLabyrinth(self): # create Sprites Walls from bytes cells codes
    for key,value in Labyrinth._walls_bytes.items():
      sides = ("top","right","bottom","left")
      bin_code =  "{0:b}".format(ord(value)).zfill(4)[::-1]
      for index,power in enumerate(bin_code):
        if int(power) == 1:
          idd = (key[0], key[1], sides[index])
          newWall = self.Wall(idd)
          if not self.wallExist(newWall):
            Labyrinth._walls[idd] = newWall
            self.group.add(Labyrinth._walls[idd])
    print("there is",len(Labyrinth._walls),"walls in the labyrinth")

  class Wall(pygame.sprite.Sprite):

    def __init__(self, idd):
      super().__init__()
      row, col, side = idd
      position = (col * 40 + Labyrinth.adjX, row * 40 + Labyrinth.adjY)
      self.image = pygame.Surface((45,5)) if side in ["top","bottom"] \
              else pygame.Surface((5,40))
      if side in ["top","bottom"]:
        pygame.draw.rect(self.image,red, [0,0,45,5])
      elif side in ["left","right"]:
        pygame.draw.rect(self.image,red,[0,0,5,40])
      self.rect = self.image.get_rect()
      if side in ["top", "left"]:
       self.rect.topleft = (position[0], position[1])
      if side == "bottom":
        self.rect.topleft = (position[0], position[1]+40)
      if side == "right":
        self.rect.topleft = (position[0]+40, position[1])

      def update(self):
        pass

class Hero(pygame.sprite.Sprite):

  def __init__(self, window, img, posit):
    super().__init__()
    self.posX, self.posY = posit
    self.image = pygame.image.load(img)
    self.image = pygame.transform.scale(self.image, (30,30))
    self.rect = self.image.get_rect()
    window.blit(self.image, (self.posX, self.posY))

  def move(self, dx=0, dy=0):
    self.rect.topleft = (self.posX + dx, self.posY + dy)
    willCollid = pygame.sprite.spritecollide(self, self.collideGroup, False)
    if not willCollid:
      self.posX += dx
      self.posY += dy

  def canCollideWith(self, group):
    self.collideGroup = group

  def update(self):
    self.rect.topleft = (self.posX, self.posY)

def setupPygame(width, height, image):
  pygame.init()
  display = pygame.display
  window = display.set_mode((width,height))
  display.set_caption("Mac Gyver -- OpenClassRooms projetc 3 --")
  clk = pygame.time.Clock()
  crashed = False
  posX, posY = 0,0
  try:
    mcGyverIMG = pygame.image.load(image)
  except pygame.error:
    print("can not load image",mcGyverIMG)
    raise SystemExit

  rootGroup = pygame.sprite.Group()
  labyrinthGroup = pygame.sprite.Group()
  labyrinth = Labyrinth(labyrinthGroup)
  rootGroup.add(labyrinthGroup)
  hero = Hero(window, img, labyrinth.getbestHeroPosition())
  hero.canCollideWith(labyrinthGroup)
  rootGroup.add(hero)

  def message(text):
    font = pygame.font.Font("Ubuntu-M.ttf",12)
    surf = font.render(text, True, white)
    container = surf.get_rect()
    container.topright = (width, 0)
    window.blit(surf, container)
    pygame.display.update()

  while not crashed:
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
          print ("moving up")
        elif ev.key == pygame.K_q:
          print("bye bye... see you soon !")
          crashed = True
      elif ev.type == pygame.QUIT:
        crashed = True
    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT]:
      hero.move(dx = -1)
    if key[pygame.K_RIGHT]:
      hero.move(dx = 1)
    if key[pygame.K_UP]:
      hero.move(dy = -1)
    if key[pygame.K_DOWN]:
      hero.move(dy = 1)
    if key[pygame.K_DOWN] and (key[pygame.K_LSHIFT] or key[pygame.K_RSHIFT]):
      hero.move(dy = 2)
    if key[pygame.K_UP] and (key[pygame.K_LSHIFT] or key[pygame.K_RSHIFT]):
      hero.move(dy = -2)
    if key[pygame.K_LEFT] and (key[pygame.K_LSHIFT] or key[pygame.K_RSHIFT]):
      hero.move(dx = -2)
    if key[pygame.K_RIGHT] and (key[pygame.K_LSHIFT] or key[pygame.K_RSHIFT]):
      hero.move(dx = 2)
    clk.tick(40)

    rootGroup.update()
    window.fill(black)
    rootGroup.draw(window)

    message('hit "q" key to exit')
    pygame.display.flip()
  pygame.quit()

setupPygame(width, height, img)
quit()
