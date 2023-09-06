from config import *
import pygame as pg
import math


class Player:
    def __init__(self, game, sprite):
        '''Sprite: name of player sprite in config.py'''
        self.game = game
        self.x, self.y = player_pos
        self.angle = player_angle
        self.angle_diff = 0
        self.screen = game.screen
        self.turning_right = False
        self.turning_left = False

        self.sprites = {
        }
        
        for d in ['left', 'right', 'forward']:
            img = pg.image.load(f'{player_sprites[sprite]}/{d}.png').convert_alpha()
            img = pg.transform.scale(img, (img.get_width()*player_sprite_scale, img.get_height()*player_sprite_scale))
            self.sprites[d] = img

        #self.sprite = pg.image.load(player_sprites[sprite]).convert_alpha()
        #self.sprite_pos = (half_width-self.sprites['forward'].get_width()/2, height*0.8)
        #self.alt = 1.0

    def movement(self):
        sin_a = math.sin(self.angle)
        cos_a = math.cos(self.angle)
        
        dx, dy = 0, 0
        speed = player_speed * self.game.delta_time
        speed_sin = speed * sin_a
        speed_cos = speed * cos_a

        keys = pg.key.get_pressed()
        if keys[pg.K_w]:
            dx += speed_cos
            dy += speed_sin
        if keys[pg.K_s]:
            dx += -speed_cos
            dy += -speed_sin

        # Do not strafe
        '''
        if keys[pg.K_a]:
            dx += speed_sin
            dy += -speed_cos
        if keys[pg.K_d]:
            dx += -speed_sin
            dy += speed_cos
        '''


        self.check_wall_collision(dx, dy)
        ta = self.angle

        if keys[pg.K_a]:
            self.turning_left = True
            self.angle -= player_rot_speed * self.game.delta_time
        else:
            self.turning_left = False
        if keys[pg.K_d]:
            self.turning_right = True
            self.angle += player_rot_speed * self.game.delta_time
        else:
            self.turning_right = False
        
        '''
        if keys[pg.K_q]:
            self.alt += speed
        if keys[pg.K_e]:
            self.alt -= speed
        '''

        #self.alt = min(max(self.alt, 0.3), 4.0)
        self.angle %= math.tau
        self.angle_diff = self.angle - ta

        #print(self.angle_diff)


    def check_wall(self, x, y):
        return (x, y) not in self.game.map.world_map

    def check_wall_collision(self, dx, dy):
        scale = player_size_scale / self.game.delta_time
        if self.check_wall(int(self.x + dx * scale), int(self.y)):
            self.x += dx
        if self.check_wall(int(self.x), int(self.y + dy * scale)):
            self.y += dy


    def draw(self):
        bs = 5
        '''
        pg.draw.line(self.game.screen, 'yellow', 
            (self.x * bs, self.y * bs), 
            (self.x * bs + width * math.cos(self.angle),
            self.y * bs + width * math.sin(self.angle)), 2)
        '''
        img = self.sprites['forward']
        if self.turning_right:
            img = self.sprites['right']
        elif self.turning_left:
            img = self.sprites['left']

        self.game.screen.blit(img, (half_width-img.get_width()/2, player_sprite_height))
        pg.draw.circle(self.game.screen, 'green', (self.x * bs, self.y * bs), 15)
        #print(self.sprite_pos)

            


    def update(self):
        self.movement()
        #print(self.x, self.y)

    @property
    def pos(self):
        return self.x, self.y
    
    @property
    def map_pos(self):
        return int(self.x), int(self.y)