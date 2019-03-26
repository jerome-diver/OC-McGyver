'''
The Room object is one of the 64 rooms of the map.
'''


class Room:

  #  self._coordonates = ( )   self room coordonates inside the map
  #  self._walls = { }         self {"edge_side": (8 boolean) }
  #  self._color = (R,G,B)     self int values Room color to render
    _full_close = (True,True,True,True,True,True,True,True)
    _directions = ("north", "east", "south", "west")

    def __init__(self, map_linked, coordonates):
        self._coordonates = coordonates
        self._mapLinked = map_linked
        self.loadRoom(map_linked)
        map_linked.appendRoom(self)

    def loadRoom(self, map_):
        for index,wall_cwp in \
                enumerate(map_.clockWisePosition(self._coordonates)):
            if wall_cwp:
                direction = self._directions[index]
                self.walls[direction] = getWallFor(direction)
            else:
                self.walls[direction] = copy(self._full_close)

    def setColor(self, rgb):
        self._color = rgb

    def getColor(self):
        return self._color

    def getCoordonates(self):
        return self._coordonates
