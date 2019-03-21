'''
The Room object is one of the 64 rooms of the map.
'''

class Room:

    coordonates = ( )    # self room coordonates inside the map
    walls = { }         # {"edge_direction": (8 boolean) }
    color = "#FFF"

    def __init__(self, map_linked, coorodnates):
        self.coordonates = coordonates
        self.mapLinked = map_linked
        self.loadRoom(map_linked)

    def loadRoom(self, map_):
        for index,wall_cwp in enumerate(map_.clockWisePosition(self.coordonates)):
            if wall_cwp:
                direction = self.directions[index]
                self.walls[direction] = getWallFor(direction)
            else:
                self.walls[direction] = copy(self.full_close)

    def setColor(self, rgb):
        self.color = rgb

    def getColor(self)
    return color

    def getCoordonates(self):
        return self.coordonates

