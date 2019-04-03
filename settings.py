import os

WIDTH = 800
HEIGHT = 800
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
CWD = os.path.dirname(os.path.abspath(__file__))
LABYRINTH_FILE = os.path.join(CWD, "map/map.txt")
HERO_FILE = os.path.join(CWD, "img/MacGyver.png")
GUARD_FILE = os.path.join(CWD, "img/guard.png")
PILL_FILE = os.path.join(CWD, "img/magic powder modified.png")
DILUENT_FILE = os.path.join(CWD, "img/ether modified.png")
NEEDLE_FILE = os.path.join(CWD, "img/seringue modified.png")
LABYRINTH_WIDTH = 600
LABYRINTH_HEIGHT = 600
LABYRINTH_WALL_COLOR = (70, 240, 50)
MAX_TIMER_GAME = 300  # in seconds


"""
Variables to be calculate from constante provide up there.
Do not touch this please.
"""
ADJ_X = int(WIDTH - LABYRINTH_WIDTH) / 2
ADJ_Y = int(HEIGHT - LABYRINTH_HEIGHT) / 2
