from config import *
import pygame as pg
import math


class Player:
    def __init__(self, game):
        self.game = game
        self.x, self.y = player_pos
        self.angle = player_angle
        self.angle_diff = 0 
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
        if keys[pg.K_a]:
            dx += speed_sin
            dy += -speed_cos
        if keys[pg.K_d]:
            dx += -speed_sin
            dy += speed_cos


        self.check_wall_collision(dx, dy)
        ta = self.angle

        if keys[pg.K_LEFT]:
            self.angle -= player_rot_speed * self.game.delta_time
        if keys[pg.K_RIGHT]:
            self.angle += player_rot_speed * self.game.delta_time
        
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
        bs = 20
        #pg.draw.line(self.game.screen, 'yellow', 
        #    (self.x * bs, self.y * bs), 
        #    (self.x * bs + width * math.cos(self.angle),
        #    self.y * bs + width * math.sin(self.angle)), 2)
        pg.draw.circle(self.game.screen, 'green', (self.x * bs, self.y * bs), 15)

            


    def update(self):
        self.movement()

    @property
    def pos(self):
        return self.x, self.y
    
    @property
    def map_pos(self):
        return int(self.x), int(self.y)