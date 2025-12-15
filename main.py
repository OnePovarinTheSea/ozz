from pygame import *
from OOO import *
from random import randint


font.init()
mixer.init()

# создание окна размером 700 на 500
window = display.set_mode((WIN_W, WIN_H))
# создание таймера
clock = time.Clock()

# название окна
display.set_caption("СОСАЛКИ>:3")
cirbi = mixer.Sound('src/muhahaha.mp3')
cirbi.set_volume(0.2)
font_min = font.SysFont('Times New Roman',30)
font_max = font.SysFont('Times New Roman',90)
lost_txt = font_min.render('Конец Земли не будет концом для нас!',True, YELLOW)
capture_txt = font_min.render('Нашей колонии роботов нужны здоровые рабы.',True, YELLOW)

# задать картинку фона такого же размера, как размер окна
background = WorkClass("src/fon.png", 0, 0, WIN_W, WIN_H)
dom_2 = Puu('src/BFG9000.png',0,0,SIZE_BFG)
dom_2.rect.centerx = WIN_W//2
dom_2.rect.bottom = WIN_H
vragi = sprite.Group()
for i in range(4):
    vrag = Enemies('src/Demon_noname_1.png',randint(0, WIN_W),0,(1,1))
    vragi.add(vrag)

game = True
finish_cleaner_fordishes = False
while game:
    if not finish_cleaner_fordishes:
        score_txt = font_min.render(f'Оуе :{dom_2.score}', True, RED)
        background.drawing(window)
        window.blit(score_txt,(10,10))

        vragi.draw(window)
        vragi.update(dom_2)
        dom_2.drawing(window)
        dom_2.update()
        dom_2.bull.draw(window)
        dom_2.bull.update()

        pvz_ozona = sprite.groupcollide(vragi,dom_2.bull,True,True)
        for collide in pvz_ozona:
            dom_2.score += 1
            vrag = Enemies('src/Demon_noname_1.png', randint(0, WIN_W), 0, (1, 1))
            vragi.add(vrag)
        if dom_2.score > WIN_SCORE :
            window.blit(capture_txt,(50,WIN_H//2-25))
            display.update()
            finish_cleaner_fordishes = True
        if dom_2.score < LOSE_SCORE :
            window.blit(lost_txt,(50,WIN_H//2-25))
            display.update()
            finish_cleaner_fordishes = True

    for e in event.get():
        if e.type == MOUSEBUTTONDOWN and e.button == 1:
            dom_2.shooting_stars()
        if e.type == KEYDOWN:
            if e.key == K_SPACE:
                cirbi.play()
        # выйти, если нажат "крестик"
        if e.type == QUIT:
            game = False
    # обновить экран, чтобы отобрзить все изменения
    display.update()
    clock.tick(FPS)