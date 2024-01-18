#Imports
from pygame import *
from random import randint
#Window definition
window = display.set_mode((700, 500))
#Background definitionjpg
background = transform.scale(image.load("background.jpg"), (700, 500))
#Window name
display.set_caption('Ping Pong')
#SuperClass gamesprite
#SuperClass gamesprite
class GameSprite(sprite.Sprite):
 #class constructor
   def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
       #Call for the class (Sprite) constructor:
       sprite.Sprite.__init__(self)
 
 
       #every sprite must store the image property
       self.image = transform.scale(image.load(player_image), (size_x, size_y))
       self.speed = player_speed
 
 
       #every sprite must have the rect property – the rectangle it is fitted in
       self.rect = self.image.get_rect()
       self.rect.x = player_x
       self.rect.y = player_y
 #method drawing the character on the window
   def reset(self):
       window.blit(self.image, (self.rect.x, self.rect.y))
#Player class
class Player(GameSprite):
    def move(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 1:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y < 365:
            self.rect.y += self.speed
PlayerInst=Player("palled.png", 10, 200, 39, 136, 5)
#Enemy bot
#class Enemy(GameSprite):
#    def update(self):
#Clock
clock = time.Clock()
FPS = 60
#Game true
game = True
#Game while
while game:
    window.blit(background,(0, 0))
    for e in event.get():
        if e.type == QUIT:
            game = False
    #collides = sprite.groupcollide(monsters, bullets, True, True)
    PlayerInst.move()
    PlayerInst.reset()
    display.update()
    clock.tick(FPS)