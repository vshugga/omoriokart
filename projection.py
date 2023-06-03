import pygame as pg
import numpy as np
from config import *
from numba import njit, prange

class Projection:
    def __init__(self, game):
        self.game = game
        self.floor_tex = self.game.object_renderer.get_texture('resources/sprites/maps/vastforest.png', (1600, 900))
        self.tex_size = self.floor_tex.get_size()
        self.floor_array = pg.surfarray.array3d(self.floor_tex)

        self.screen_array = pg.surfarray.array3d(pg.Surface(res))
        self.screen_array[:] = (255, 255, 0)
        self.alt = 1.0


    def update(self):
        #self.movement()
        self.screen_array = self.render_frame(self.floor_array, 
                                              self.screen_array, 
                                              self.tex_size, 
                                              self.game.player.angle, 
                                              self.game.player.pos)



    @staticmethod
    @njit(fastmath=True, parallel=True)
    def render_frame(floor_array, screen_array, tex_size, angle, player_pos):

        sin, cos = np.sin(angle), np.cos(angle)
        fov_factor = 2 * np.tan(np.radians(half_fov))


        for i in prange(width):
            #new_alt = alt
            for j in range(half_height, height):
                x = half_width - i 
                y = j + focal_len
                z = j - half_height + 0.01

                px = (x * sin + y * cos) * np.tan(half_fov)
                py = (x * cos - y * sin) * np.tan(half_fov)

                floor_x = px / z + player_pos[0]
                floor_y = py / z - player_pos[1]

                floor_x *= p_scale
                floor_y *= p_scale

                floor_x %= tex_size[0]
                floor_y %= tex_size[1]

                floor_pos = int(floor_x), int(floor_y)
                floor_col = floor_array[floor_pos]

                screen_array[i, j] = floor_col

        return screen_array

    def draw(self):
        pg.surfarray.blit_array(self.game.screen, self.screen_array)

