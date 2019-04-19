'''Setting global variables file'''

import os

WIDTH = 800
HEIGHT = 800
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
#ORANGE = (249, 112, 14)
LABYRINTH_WIDTH = 600
LABYRINTH_HEIGHT = 600
LABYRINTH_WALL_COLOR = (14, 249, 195)
MAX_TIMER_GAME = 120                   #  in seconds
CLK = 50    # game clock speed (try between 30 and 120)
# Project ROOT Directory
CWD = os.path.dirname(os.path.abspath(__file__))
# LABYRINTH map file
LABYRINTH_FILE = os.path.join(CWD, "map/map.txt")
# IMAGES of sprites
HERO_FILE = os.path.join(CWD, "img/MacGyver.png")
GUARD_FILE = os.path.join(CWD, "img/guard.png")
PILL_FILE = os.path.join(CWD, "img/magic powder modified.png")
DILUENT_FILE = os.path.join(CWD, "img/ether modified.png")
NEEDLE_FILE = os.path.join(CWD, "img/seringue modified.png")
# FONT file
FONT = os.path.join(CWD, "fonts/Ubuntu-M.ttf")
# MUSIC file
JINGLE_FILE = os.path.join(CWD, 'music/Mac Gyver theme.mp3')

"""
Variables to be calculate
Relative position for adjust labyrinth in the middle of the window
-- D o   n o t   t o u c h   t h i s   p l e a s e --
"""
ADJ_X = int(WIDTH - LABYRINTH_WIDTH) / 2
ADJ_Y = int(HEIGHT - LABYRINTH_HEIGHT) / 2
