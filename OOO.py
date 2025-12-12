from pygame import *
from random import *

BLACK = (0,0,0)
RED = (255,0,0)
YELLOW = (255,255,0)
WIN_W = 700
WIN_H = 500
FPS = 150
X1, Y1 = 50 , 350
X2, Y2 = 625 , 300
SIZE_BFG = 300,100
SIZE_FUFEL = 25

class WorkClass(sprite.Sprite):
    def __init__(self, img, x, y, w, h):
        super().__init__()
        self.image = transform.scale(
            image.load(img),
            (w, h)
        )
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def drawing(self, widow):
        widow.blit(self.image,(self.rect.x, self.rect.y))

class Puu(WorkClass):
    def __init__(self, img, x, y, size, blitz=10):
        super().__init__(img, x, y, size[0],size[1])
        self.blitz = blitz
        self.score = 0
        self.bull = sprite.Group()
        self.isleft = True
    def update(self, right=K_d, left=K_a):
        keys_pressed = key.get_pressed()
        if keys_pressed[left] and self.rect.centerx > 0:
            self.rect.x -= self.blitz
            self.isleft = True
        #       self.image = transform.flip(self.image, True, False)
        if keys_pressed[right] and self.rect.centerx < WIN_W:
            self.rect.x += self.blitz
            self.isleft = False
    #        self.image = transform.flip(self.image, True, False)
    def shooting_stars(self):
        bull = INMB('src/Bullet_BFG9000.png',self.rect.centerx-22,self.rect.top,(SIZE_FUFEL,SIZE_FUFEL))
        if self.isleft :
            bull.hell_and_back()
        else:
            bull.youtube_director()
        self.bull.add(bull)

class INMB(WorkClass):
    def __init__(self, img, x, y, size, blitz=5):
        super().__init__(img, x, y, size[0], size[1])
        self.blitzx = blitz//3
        self.blitzy = blitz
    def update(self):
        self.rect.x -= self.blitzx
        self.rect.y -= self.blitzy
        if  self.rect.x < 0 or self.rect.y < 0:
            self.kill()
    def youtube_director(self):
        self.blitzx = -1*abs(self.blitzx)
    def hell_and_back(self):
        self.blitzx = abs(self.blitzx)

class Enemies(WorkClass):
    def __init__(self, img, x, y, size, blitz=5):
        super().__init__(img, x, y, size[0], size[1])
        self.blitzy = blitz
        self.restock()
    def update(self):
        self.rect.x += self.blitzx
        self.rect.y += self.blitzy
        if  self.rect.x > WIN_W or self.rect.y > WIN_H:
            self.restock()
    def restock(self):
        self.rect.x = randint(0, WIN_W - self.rect.width)
        self.rect.y = 0
        self.blitzx = randint(1, 7) * choice((1, -1))

class Area:
    def __init__(self,x,y,w,h,color=RED):
        self.rect = Rect(x,y,w,h)
        self.color = color
    def set_color(self,color):
        self.color = color
    def draw(self,window):
        draw.rect(window,self.color,self.rect)\

class Card(Area):
    def __init__(self,x,y,w,h,color=YELLOW):
        super().__init__(x,y,w,h,color)
    def set_txt(self,txt,size=70,color=BLACK,my_font='Times New Roman'):
        title = font.SysFont(my_font,size)
        self.image = title.render(txt,True,color)
    def draw(self,window,shift_x=10,shift_y=5):
        super().draw(window)
        window.blit(self.image,(self.rect.x+shift_x,self.rect.y+shift_y))
