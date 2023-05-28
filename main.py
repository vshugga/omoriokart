import pygame as pg
import sys
from config import *
from map import *
from player import *
from raycast import *

class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode(res)
        self.clock = pg.time.Clock()
        self.delta_time = 1
        self.new_game()

    def new_game(self):
        self.map = Map(self)
        self.player = Player(self)
        self.raycast = Raycast(self)

    def update(self):
        self.player.update()
        self.raycast.update()
        pg.display.flip()
        self.delta_time = self.clock.tick(fps)
        pg.display.set_caption(f'{self.clock.get_fps():.1f}')

    def draw(self):
        self.screen.fill('black')
        self.map.draw()
        #self.player.draw()

    def check_events(self):
        for e in pg.event.get():
            if e.type == pg.QUIT or (e.type == pg.KEYDOWN and e.key == pg.K_ESCAPE):
                pg.quit()
                sys.exit()

    def run(self):
        while True:
            self.check_events()
            self.update()
            self.draw()

if __name__ == '__main__':
    game = Game()
    game.run()




'''

pygame.init()
font = pygame.font.Font("OMORI_GAME2.ttf", 100)
text_str = "Welcome to Omorikart, here is kel:"
text = font.render(text_str, True, (0,0,0))

screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()

kel = pygame.image.load('imgs/kelcar_better.png').convert_alpha()
carsize = (100, 150)
kel = pygame.transform.scale(kel, carsize)

class GameObject:
    def __init__(self, image, height, speed):
        self.speed = speed
        self.image = image
        self.pos = image.get_rect().move(0, height)

    def move(self):
        self.pos.right += self.speed[3]
        self.pos.right -= self.speed[2]
        self.pos.top += self.speed[1]
        self.pos.top -= self.speed[0]

        if self.pos.right > screen.get_width():
            self.pos.left = 0
        if self.pos.top > screen.get_height()-self.image.get_height():
            self.pos.top = 0
        if self.pos.right < self.image.get_width():
            self.pos.right = screen.get_width()
        if self.pos.top < 0:
            self.pos.top = screen.get_height()-self.image.get_height()


kelcar = GameObject(kel, 100, [0,0,0,0])


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    keys = pygame.key.get_pressed()
    screen.fill("purple")


    #kelcar.move()
    for i, key in enumerate([pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT]):
        if keys[key] and kelcar.speed[i] < 10:
            kelcar.speed[i] += 0.1
        elif kelcar.speed[i] > 0:
            kelcar.speed[i] -= 0.1
    print(kelcar.speed)

    kelcar.move()
    screen.blit(kelcar.image, kelcar.pos)
    screen.blit(text, (50, 50))


    
    pygame.display.update()
    clock.tick(144)

pygame.quit()
'''