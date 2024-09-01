import pygame
import settings
import sprites
import pygame.freetype

pygame.init()

menuiliigra = 1

meteorits = []

podbitie = 0

lazers = []

window = pygame.display.set_mode([settings.SHIRINA, settings.VYSOTA])
clock = pygame.time.Clock()

fon = pygame.image.load("kartinki/допфон.jpg")
fon = pygame.transform.scale(fon, [settings.SHIRINA, settings.VYSOTA])

fonmenu = pygame.image.load("kartinki/фон.png")
fonmenu = pygame.transform.scale(fonmenu, [settings.SHIRINA, settings.VYSOTA])

muzika = pygame.mixer.Sound("kartinki/музыка.wav")

zvuklazera = pygame.mixer.Sound("kartinki/звук лазера.wav")

shrift = pygame.freetype.Font("kartinki/шрифт.ttf", 128)


serdce = pygame.image.load("kartinki/сердце.png")
serdce = pygame.transform.scale(serdce, [120, 120])

korabl = sprites.Korabl()

buttonblue = pygame.image.load("PNG/UI/buttonBlue.png")
buttongreen = pygame.image.load("PNG/UI/buttonGreen.png")
buttonred = pygame.image.load("PNG/UI/buttonRed.png")
buttonyellow = pygame.image.load("PNG/UI/buttonYellow.png")

buttonstart = sprites.Buttons(1500, 500, "начать", buttonblue)
buttonprodolzhit = sprites.Buttons(300, 500, "продолжить", buttongreen)
buttonquit = sprites.Buttons(800, 500, "выйти", buttonred)

gf = 100

sobitiemeteorit = pygame.USEREVENT

pygame.time.set_timer(sobitiemeteorit, 500)

sobitielazer = pygame.USEREVENT

pygame.time.set_timer(sobitielazer, 500)

muzika.set_volume(0.3)
muzika.play(-1)

while gf == 100:
    sobitiya = pygame.event.get()
    for sobitie in sobitiya:
        if sobitie.type == pygame.QUIT:
            gf = gf+1
        if sobitie.type == sobitiemeteorit:
            meteorit = sprites.Meteorit()
            meteorits.append(meteorit)
        if sobitie.type == pygame.MOUSEBUTTONDOWN and menuiliigra == 1:
            lazer = sprites.Lazer(korabl.hitbox.centerx, korabl.hitbox.centery-50)
            lazers.append(lazer)
            zvuklazera.play()
        if sobitie.type == pygame.MOUSEBUTTONDOWN and menuiliigra == 2:
            if buttonstart.hitbox.collidepoint(sobitie.pos):
                menuiliigra = 1
                meteorits = []
                podbitie = 0
                lazers = []
                korabl.hp = 5
            if buttonprodolzhit.hitbox.collidepoint(sobitie.pos):
                menuiliigra = 1
            if buttonquit.hitbox.collidepoint(sobitie.pos):
                gf = gf+1

        if sobitie.type == pygame.KEYDOWN:
            if sobitie.key == pygame.K_ESCAPE:
                if menuiliigra == 1:
                    menuiliigra = 2
                else:
                    menuiliigra = 1

    if menuiliigra == 1:
        korabl.move()

        for l in lazers:
            l.move()

        for m in meteorits:
            m.move()
            if m.hitbox.colliderect(korabl.hitbox) == True:
                korabl.hp = korabl.hp-1
                meteorits.remove(m)
                
        for l in lazers:
            for m in meteorits:
                if l.hitbox.colliderect(m.hitbox) == True:
                    meteorits.remove(m)
                    lazers.remove(l)
                    podbitie = podbitie + 1
        
        if korabl.hp == 0:
            menuiliigra = 2


                
        window.blit(fon, [0, 0])
        ui = 0
        xs = 100
        while ui != korabl.hp:
            window.blit(serdce, [xs, 100])
            xs = xs+100
            ui=ui+1

        shrift.render_to(window, [1500, 100], str(podbitie))

        for l in lazers:
            l.otrisovka(window)

        korabl.otrisovka(window)
        for m in meteorits:
            m.otrisovka(window)
    else:
        window.blit(fonmenu, [0, 0])
        buttonstart.otrisovka(window)
        buttonprodolzhit.otrisovka(window)
        buttonquit.otrisovka(window)

    
    pygame.display.update()

    clock.tick(120)