import os

width = 800
height = 800
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
cwd = os.path.dirname(os.path.abspath(__file__))
labyrinthFile = os.path.join(cwd, "map/map.txt")
heroFile = os.path.join(cwd, "img/MacGyver.png")
guardFile = os.path.join(cwd, "img/guard.png")
pillFile = os.path.join(cwd, "img/magic powder modified.png")
diluentFile = os.path.join(cwd, "img/ether modified.png")
needleFile = os.path.join(cwd, "img/seringue modified.png")
labyrinthWidth = 600
labyrinthHeight = 600
labyrinthWallColor = (70, 240, 50)


"""
Variables to be calculate from constante provide up there.
Do not touch this please.
"""
adjX = int(width - labyrinthWidth) / 2
adjY = int(height - labyrinthHeight) / 2
