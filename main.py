import pygame, sys, random
from pygame.locals import *
pygame.init()
screen = pygame.display.set_mode((800, 500))
pygame.display.set_caption('Stewart')
background = pygame.image.load("img/back.png")


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.image = pygame.image.load('img/Stewart.png').convert()
        self.image.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.image.get_rect(
            center=(100,100))
    def update(self, pressed_keys):
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-6, 0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(6, 0)
        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > 800:
            self.rect.right = 800
        if self.rect.top <= 0:
            self.rect.top = 0
        elif self.rect.bottom >= 500:
            self.rect.bottom = 500

player = Player()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

while True:
    pygame.time.delay(20)
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                sys.exit()
        elif event.type == QUIT:
            sys.exit()

screen.blit(background, (0,0))
pressed_keys = pygame.key.get_pressed()
player.update(pressed_keys)
for entity in all_sprites:
    screen.blit(entity.image, entity.rect)
pygame.display.flip()
