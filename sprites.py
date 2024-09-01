import pygame
import random
class Korabl:
    def __init__(self) -> None:
        self.kartinka = pygame.image.load("kartinki/корабль.png") 
        self.kartinka = pygame.transform.scale(self.kartinka, [200, 200])
        width = self.kartinka.get_width()
        height = self.kartinka.get_height()
        self.hitbox = pygame.Rect([100, 500], [width, height])
        self.hp = 5
    def otrisovka(self,window):
        window.blit(self.kartinka, self.hitbox)
    def move(self):
        sostoyaniya = pygame.key.get_pressed()
        if sostoyaniya[pygame.K_w] == True:
            self.hitbox.y = self.hitbox.y-10
        if sostoyaniya[pygame.K_s] == True:
            self.hitbox.y = self.hitbox.y+10
class Meteorit:
    def __init__(self) -> None:
        self.speedx = random.randint(1, 10)
        self.speedy = random.randint(-2, 2)
        self.kartinka = pygame.image.load("kartinki/метеорит.png") 
        self.kartinka = pygame.transform.scale(self.kartinka, [300, 300])
        width = self.kartinka.get_width()
        height = self.kartinka.get_height()
        self.hitbox = pygame.Rect([1600, random.randint(0, 1000)], [width, height])
    def otrisovka(self, window):
        window.blit(self.kartinka, self.hitbox)
    def move(self):
        self.hitbox.x = self.hitbox.x-self.speedx
        self.hitbox.y = self.hitbox.y-self.speedy
class Lazer:
    def __init__(self, x, y) -> None:
        self.speedx = 10   
        self.kartinka = pygame.image.load("kartinki/лазер.png")
        self.kartinka = pygame.transform.scale(self.kartinka, [100, 100])
        width = self.kartinka.get_width()
        height = self.kartinka.get_height()
        self.hitbox = pygame.Rect([x, y], [width, height])
    def otrisovka(self,window):
        window.blit(self.kartinka, self.hitbox)
    def move(self):
        self.hitbox.x = self.hitbox.x+self.speedx
class Buttons:
    def __init__(self, x, y, txt, kartinka):
        self.kartinka = kartinka
        width = self.kartinka.get_width()
        height = self.kartinka.get_height()
        self.hitbox = pygame.Rect([x, y], [width, height])
        # смотреть тут
        self.shrift = pygame.freetype.Font("kartinki/шрифт.ttf", 28)
        kartinkaihitbox = self.shrift.render(txt)
        self.kartinkatxt = kartinkaihitbox[0]
        self.hitboxtxt = kartinkaihitbox[1]
        self.txt = txt
        self.hitboxtxt.center = self.hitbox.center
    def otrisovka(self, window):
        window.blit(self.kartinka, self.hitbox)
        # и тут
        window.blit(self.kartinkatxt, self.hitboxtxt)

