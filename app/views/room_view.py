from views import View


class RoomView(View):

    _SquareLength = 40  # 30 + 2 walls enclosure thickness of 5 = 40
    _roomLength = 580   # 70 * 8 + 2 * 10 = 580
    _wallSqThickness = 5
    _wallRoomThickness = 10
    _wallMpSqLength = 40
    _wallEigthsPart = 70    # (580 - 2*10) / 8 = 70

    def __init__(self, roomModel):
        self.__init__(roomModel)
        mapModel.setImage(self.drawSquare(), roomModelgetColor())
        self.createSprite()

    def createSprite(self):
        self._sprite = MapSprite(self._model)
        self._gameEngine.addGroupSprites("Room")
        self._gameEngine.addSpriteToGroup(self._sprite, "Map")

    def drawRoom(self):
        externalSurf = pygame.Surface((_roomLength,_roomLength))    # image for pygame
        pygame.draw.rect(externalSurf, (255,0,0), [0,0,560,560],10)
        return externalSurf

    def drawMapSquare(self):  # tot = 40x40 (enclosure wall=5, center sq=30)
        externalSurf = pygame.Surface((_SquareLength,_SquareLength))
        pygame.draw.rect(externalSurf, (255,0,0), [0,0,30,30],5)
        return externalSurf