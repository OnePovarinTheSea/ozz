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
display.set_caption("УБИВАЛКИ>:3")
cirbi = mixer.Sound('src/muhahaha.mp3')
cirbi.set_volume(0.2)

# задать картинку фона такого же размера, как размер окна
background = WorkClass("src/fon.png", 0, 0, WIN_W, WIN_H)
dom_2 = Puu('src/BFG9000.png',0,0,SIZE_BFG)
dom_2.rect.centerx = WIN_W//2
dom_2.rect.bottom = WIN_H


game = True
finish_cleaner_fordishes = False
while game:
    if not finish_cleaner_fordishes:
        background.drawing(window)
        dom_2.drawing(window)
        dom_2.update()
        dom_2.bull.draw(window)
        dom_2.bull.update()

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