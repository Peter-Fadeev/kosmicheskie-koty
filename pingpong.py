import pygame
import pygame.freetype

pygame.init()

window = pygame.display.set_mode([1900, 1000])
clock = pygame.time.Clock()

pong = pygame.mixer.Sound("kartinki/pong.wav")

score = pygame.mixer.Sound("kartinki/score.wav")

vragzabil = 0

win = "you win!"

igrokzabil = 0

gameover = "game over"

restart = "для перезапуска нажмите R"

shrift = pygame.freetype.Font("kartinki/шрифт.ttf", 128)

hitboxball = pygame.Rect([950, 500], [180, 180])

hitboxrect1 = pygame.Rect([1825, 500], [75, 250])
hitboxrect2 = pygame.Rect([0, 500], [75, 250])

speedx = 10

speedy = 10

gf = 100
while gf == 100:
    sobitiya = pygame.event.get()
    for sobitie in sobitiya:
        if sobitie.type == pygame.QUIT:
            gf = gf+1

    hitboxball.x = hitboxball.x+speedx
    if hitboxball.right >= 1900:
        speedx = -10
        hitboxball.x = 950
        hitboxball.y = 500
        vragzabil = vragzabil + 1
        score.play()
    if hitboxball.x <= 0:
        speedx = 10
        hitboxball.x = 950
        hitboxball.y = 500
        igrokzabil = igrokzabil + 1
        score.play()

    hitboxball.y = hitboxball.y+speedy
    if hitboxball.top <= 0:
        speedy = 10
    if hitboxball.bottom >= 1000:
        speedy = -10

    sostoyaniya = pygame.key.get_pressed()
    if sostoyaniya[pygame.K_w] == True:
        hitboxrect1.y = hitboxrect1.y-10
    if sostoyaniya[pygame.K_s] == True:
        hitboxrect1.y = hitboxrect1.y+10

    sostoyaniya2 = pygame.key.get_pressed()
    if sostoyaniya2[pygame.K_q] == True:
        hitboxrect2.y = hitboxrect2.y+10
    if sostoyaniya2[pygame.K_e] == True:
        hitboxrect2.y = hitboxrect2.y-10

    sostoyaniya3 = pygame.key.get_pressed()
    if sostoyaniya3[pygame.K_r] == True and (igrokzabil == 5 or vragzabil == 5):
        igrokzabil = 0
        vragzabil = 0
        hitboxball.x = 950
        hitboxball.y = 500
        speedx = 10
        speedy = 10

    
    if hitboxball.colliderect(hitboxrect1) == True:
        speedx = -10
        pong.play()
       
    if hitboxball.colliderect(hitboxrect2) == True:
        speedx = 10
        pong.play()

    shrift.render_to(window, [1500, 100], str(igrokzabil))

    shrift.render_to(window, [400, 100], str(vragzabil))

    if igrokzabil == 5:
        shrift.render_to(window, [950, 500], str(win))
        speedx = 0
        speedy = 0
        hitboxball.x = 950
        hitboxball.y = 500

    if vragzabil == 5:
        shrift.render_to(window, [950, 500], str(gameover))
        speedx = 0
        speedy = 0
        hitboxball.x = 950
        hitboxball.y = 500





    window.fill([104, 45, 61])
    pygame.draw.rect(window, [11, 100, 178], hitboxrect1)
    pygame.draw.rect(window, [190, 23, 58], hitboxrect2)
    pygame.draw.ellipse(window, [11, 100, 61], hitboxball)
    
    shrift.render_to(window, [1500, 100], str(igrokzabil))

    shrift.render_to(window, [400, 100], str(vragzabil))

    if igrokzabil == 5:
        shrift.render_to(window, [950, 500], str(win))
        shrift.render_to(window, [100, 250], str(restart))
    if vragzabil == 5:
        shrift.render_to(window, [950, 500], str(gameover))
        shrift.render_to(window, [100, 250], str(restart))
    pygame.display.update()

    clock.tick(120)
