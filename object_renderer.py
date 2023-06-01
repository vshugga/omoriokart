import pygame as pg
from config import *

class ObjectRenderer:
    def __init__(self, game):
        self.game = game
        self.screen = game.screen
        self.wall_textures = self.load_wall_textures()
        self.sky_image = self.get_texture('resources/textures/Dreamworld_polaroidBG_FA_day_BIG.png', (width, half_height))
        #self.floor_sprite = self.get_texture('resources/sprites/maps/vastforest.png', (2560, 1440)) # < size of the mini map
        #self.ground_image = self.get_texture('resources/sprites/maps/vastforest.png', (width, half_height))
        self.sky_offset = 0

    def draw(self):
        self.draw_background()
        self.render_game_objs()
    '''+ 4.5 * self.game.player.rel'''
    def draw_background(self):
        self.sky_offset = (self.sky_offset + 750 * self.game.player.angle_diff) % width
        self.screen.blit(self.sky_image, (-self.sky_offset, 0))
        self.screen.blit(self.sky_image, (-self.sky_offset + width, 0))
        
        #self.screen.blit(self.ground_image, (-self.sky_offset, half_height))
        #self.screen.blit(self.ground_image, (-self.sky_offset + width, half_height))

        #pg.draw.rect(self.screen, 'black', (0, half_height, width, height))

    def render_game_objs(self):
        list_objs = sorted(self.game.raycast.objs_to_render, key=lambda t: t[0], reverse=True)
        for depth, image, pos in list_objs:
            self.screen.blit(image, pos)

    @staticmethod
    def get_texture(path, res=(texture_size, texture_size)):
        texture = pg.image.load(path).convert_alpha()
        return pg.transform.scale(texture, res)

    def load_wall_textures(self):
        return {
            1: self.get_texture('resources/sprites/static/tree.png'),
            2: self.get_texture('resources/textures/chaos.jpg'),
        }