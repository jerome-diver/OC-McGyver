#! /usr/bin/python3
'''
  this test pygame game who can grab dimension of window and images from arguments at command call,
  then open a windiw and can move image with cursor inside this window created area
  you should hit "q" for quit this demo game.
'''

import sys
import os.path

if len(sys.argv) != 4:
    print("you should call it like this:")
    print("pygame_demo 600 400 my_file_absolute_name.png")
    raise Exception("You have to use correct syntax call for this command")
if not os.path.isfile(sys.argv[3]):
    raise Exception("last argument has to be an existing file... this one doesn't exist.")

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

img = sys.argv[3]
widht = int(sys.argv[1])
height = int(sys.argv[2])

import pygame


def setupPygame(width, height, image): 
  pygame.init() 
  display = pygame.display 
  window = display.set_mode((width,height)) 
  display.set_caption("Mac Gyver -- OpenClassRooms projetc 3 --") 
  clk = pygame.time.Clock() 
  crashed = False 
  posX, posY = 0,0 
  red = (255,0,0) 
  black = (0,0,0) 
  mcGyverIMG = pygame.image.load(image)
  def hero(x,y):
    window.blit(mcGyverIMG, (x,y))
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
      posX -= 1 
    if key[pygame.K_RIGHT]: 
      posX += 1 
    if key[pygame.K_UP]: 
      posY -= 1 
    if key[pygame.K_DOWN]: 
      posY += 1 
    clk.tick(60) 
    window.fill(black) 
    #pygame.draw.rect(window, red, (posX, posY,50,50)) 
    hero(posX,posY)
    pygame.display.flip() 
  pygame.quit() 
  quit()

setupPygame(width, height, img)
