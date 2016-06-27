import pygame, sys, random
from pygame.locals import *
from map_1 import map1

pygame.init()
screen = pygame.display.set_mode((800, 500))
pygame.display.set_caption('Stewart')
grass = pygame.image.load("img/grass.jpg")
water = pygame.image.load("img/water.jpg")
mountian = pygame.image.load("img/mountian.jpg")
yshift=0
xshift=0

terrains = [{"sprite": grass, "passable": True}, {"sprite": water, "passable": False}, {"sprite": mountian, "passable": False}]
themap = [[-1 for y in range(150)] for x in range (150)]
for x in range (0,150):
    for y in range (0,150):
        themap[y][x] = terrains[map1[y][x]]

def is_passable(map_x, map_y):
	return themap[map_y][map_x]["passable"]

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.image = pygame.image.load('img/Stewart.png').convert()
        self.image.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.image.get_rect(
            center=(48,48))

    def update(self, pressed_keys):
        global yshift
        global xshift
        if pressed_keys[K_LEFT]:
            if self.rect.left <= 0:
                self.rect.left=0
                xshift+=32
            else:
				self.rect.move_ip(-32, 0)
				playerx=self.rect.left/32
				playery=self.rect.top/32
				if not is_passable(playerx,playery):
					self.rect.move_ip(32,0)
        if pressed_keys[K_RIGHT]:
            if self.rect.right >= 800:
                self.rect.right=800
                xshift-=32
            else:
				self.rect.move_ip(32, 0)
				playerx=self.rect.left/32
				playery=self.rect.top/32
				if not is_passable(playerx,playery):
					self.rect.move_ip(-32,0)
        if pressed_keys[K_UP]:
            if self.rect.top <=0:
                self.rect.top = 0
                yshift+=32
            else:
				self.rect.move_ip(0, -32)
				playerx=self.rect.left/32
				playery=self.rect.top/32
				if not is_passable(playerx,playery):
					self.rect.move_ip(0,32)
        if pressed_keys[K_DOWN]:
            if self.rect.bottom>=480:
                self.rect.bottom=480
                yshift-=32
            else:
				self.rect.move_ip(0, 32)
				playerx=self.rect.left/32
				playery=self.rect.top/32
				if not is_passable(playerx,playery):
					self.rect.move_ip(0,-32)

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

    for x in range (0,150):
        for y in range (0,150):
            screen.blit(themap[y][x]["sprite"], [x*32+xshift,y*32+yshift])

    pressed_keys = pygame.key.get_pressed()
    player.update(pressed_keys)
    for entity in all_sprites:
        screen.blit(entity.image, entity.rect)
    pygame.display.flip()
