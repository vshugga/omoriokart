import pygame as pg


_ = 0
mini_map = [ # Should be equivalent to resolution? (maybe auto-adjust block size based on it)
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 1],
    [1, _, 1, _, _, 1, 1, _, 1, _, _, _, _, _, _, 1],
    [1, _, 1, _, _, 1, 1, _, 1, _, _, _, _, _, _, 1],
    [1, _, 1, 1, 1, 1, 1, _, 1, _, _, _, _, _, _, 1],
    [1, _, 1, 1, 1, 1, _, _, 1, _, _, _, _, _, _, 1],
    [1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 1],
    [1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]


class Map:
    def __init__(self, game):
        self.game = game
        self.mini_map = mini_map
        self.world_map = {}
        self.get_map()
        self.block_size = 100 # Size of each map chunk

    def get_map(self):
        for ri, row in enumerate(self.mini_map):
            for i, val in enumerate(row):
                if val:
                    self.world_map[(i, ri)] = val


    def draw(self):
        #bs = self.block_size
        bs = 20
        for x, y in self.world_map:
            rect = (x * bs, y * bs, bs, bs)
            pg.draw.rect(self.game.screen, 'gray', (x * bs, y * bs, bs, bs), 2)