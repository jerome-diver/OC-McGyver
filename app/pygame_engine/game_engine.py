'''
pygame engine shoudl run the game when all objects/models/view and controllers are loaded.
'''

import pygame


class PyGameEngine():

    _width = 800
    _height = 800

    def __init__(self):
        pygame.init()
        self._display = pygame.display
        self._window = self._display.set_mode((_width, _height))
        self._display.set_caption("OpenClassRoom -- project3 -- Mac Gyver")
        self._clk = pygame.time.Clock()
        self._crashed = False
        self._posX, self.posY = 0,0
        self._rootSpritesGroup = pygame.sprite.Group()

    def start(self):
        while not self._crashed:
            for ev in pygame.event.get():
                if ev.type == pygame.KEYDOWN:
                    self.keysDownEvents(ev)
            self.keyPressed()
            self._rootSpritesGroup.update()
            self._clk.tick(60)
            self._window.fill(self._black)
            self._rootSpritesGroup.draw(self._window)
            self._display.flip()

    def keysDownEvents(self, event):
        if event.key == pygame.K_LEFT:
            print("moving left")
        if event.key == pygame.K_RIGHT:
            print("moving right")
        if event.key == pygame.K_UP:
            print("moving up")
        if event.key == pygame.K_DOWN:
            print("moving down")
        if event.key == pygame.K_q:
            print("bye bye, see you soon !")
            self._crashed = True
        if event.key == pygame.K_m:
            # show the map



    def keyPressed(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            self.posX -= 1
        if key[pygame.K_RIGHT]:
            self.posX += 1
        if key[pygame.K_UP]:
            self.posY -= 1
        if key[pygame.K_DOWN]:
            self.posY += 1

    def addGroupsSprites(self, name, parent=None):
        self._sprites[name] = pygame.sprite.Group()
        if parent == None:
            self._rootSpritesGroup.addGroup(self._sprites[name])
        else:
            self._sprites[parent].addGRoup(self._sprites[name])

    def addSpriteToGroup(self, sprite, groupName=None):
        if groupName == None:
            self._rootSpritesGroup.add(sprite)
        else:
            self._sprites[groupName].add(sprite)


    def __del__(self):
        pygame.quit()      