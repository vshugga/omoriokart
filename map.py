import pygame as pg
from config import *

_ = 0
'''
mini_map = [ # Should be equivalent to resolution? (maybe auto-adjust block size based on it)
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 1],
    [1, _, 1, _, _, 1, 1, _, 2, _, _, _, _, _, _, _, 1],
    [1, _, 1, _, _, 1, 1, _, 2, _, _, _, _, _, _, _, 1],
    [1, _, 1, 1, 1, 1, 1, _, 2, _, _, _, _, _, _, _, 1],
    [1, _, 1, 2, 2, 2, _, _, 2, _, _, _, _, _, _, _, 1],
    [1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 1],
    [1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]
'''



class Map:
    def __init__(self, game):
        self.game = game
        #self.mini_map = mini_map
        self.world_map = {}
        self.border = set()
        self.block_size = 32 # Size of tiles
        self.generate_map()
        self.get_map()

    def generate_map(self):
        floor = self.game.floor_projection.floor_tex
        w, h = floor.get_width(), floor.get_height()
        w //= self.block_size
        h //= self.block_size

        #print(w, h)

        top = [1 for i in range(w)]
        mid = [[1 if i == 0 or i+1 == w else 0 for i in range(w)] for j in range(h)]
        mid.insert(0, top)
        mid.insert(-1, top)
        self.mini_map = mid
        

    def get_map(self):
        for r, row in enumerate(self.mini_map):
            for c, col in enumerate(row):
                if col:
                    self.world_map[(c, r)] = col
                if (r == 0 or r >= len(self.mini_map)-1) or \
                   (c == 0 or c >= len(self.mini_map[0])-1):
                    self.border.add((c, r))

    def draw(self):
        bs = 5 
        
        # NEW METHOD: perspective projection / texture mapping
        '''
        floor = self.game.object_renderer.floor_sprite
        
        scale_factor = width / floor.get_width()
        vert_shift = height // 2

        floor_surface = pg.Surface((width, height))
        
        for y in range(height):
            texture_y = int(y / scale_factor)

            for x in range(width):
                texture_x = int(x / scale_factor)

                texture_color = floor.get_at((texture_x, texture_y))
                floor_surface.set_at((x, y), texture_color)

        '''

        # Draw the mini map blocks
        
        #self.game.screen.blit(sel, (0, vert_shift))
        img = self.game.floor_projection.floor_tex
        w, h = img.get_width(), img.get_height()
        minimap = pg.transform.scale(img, (w/bs, h/bs))
                                     
        #rect = (x * bs, y * bs, bs, bs)
        self.game.screen.blit(minimap, (0, 0))
        for x, y in self.world_map:
            pg.draw.rect(self.game.screen, 'gray', (x * bs, y * bs, bs, bs), 2)

        

'''

# OLD CODE

        #self.game.screen.blit(floor_sprite, (0, 0)) # show the floor sprite in minimap
        #ox, oy = self.game.player.pos
        #xv, yv = self.game.raycast.max_vert
        #xh, yh = self.game.raycast.max_hor

        #print(f'player: {ox, oy}\nVert:{xv, yv}\nHor:{xh, yh}')
        #pg.draw.circle(self.game.screen, 'red', (xv * bs, yv * bs), 10.0)
        #pg.draw.circle(self.game.screen, 'orange', (xh * bs, yh * bs), 10.0)
        #start, end = self.game.raycast.map_fov_coords
        #pg.draw.line(self.game.screen, 'yellow', start, end, 2) 
        #first, last = self.game.raycast.ray_cast_result[0], self.game.raycast.ray_cast_result[-1] # USE THIS TO MORPH FLOOR SPRITE
        #print(first, last)
        #print(len(self.game.raycast.ray_cast_result))

        #w, h = len(self.mini_map[0]), len(self.mini_map) # Could possibly be used to transform floor sprite
        
        #bs = self.block_size
        bs = 20
        
        floor_sprite = self.game.object_renderer.floor_sprite

        l, r = self.game.raycast.get_edges()
        xl, yl = l
        xr, yr = r
        xl *= bs
        yl *= bs
        xr *= bs
        yr *= bs


        #print(left, right)
        #print(self.game.player.pos)

        pg.draw.circle(self.game.screen, 'red', (xl, yl), 2.0)
        pg.draw.circle(self.game.screen, 'orange', (xr, yr), 2.0)
        px, py = self.game.player.pos 

        v1 = px*bs, py*bs
        v2 = (xl, yl)
        v3 = (xr, yr)

        #mask = pg.mask.from_surface(floor_sprite)
        #mask_polygon = pg.draw.polygon(pg.Surface(floor_sprite.get_size(), pg.SRCALPHA), (0, 0, 0), [v1, v2, v3])
        #mask.blit(mask_polygon, (0, 0), special_flags=pg.BLEND_RGBA_MULT)

        mask_surface = pg.Surface(floor_sprite.get_size(), pg.SRCALPHA)
        pg.draw.polygon(mask_surface, (255, 255, 255), [v1, v2, v3])
        masked_surface = floor_sprite.copy()
        masked_surface.blit(mask_surface, (0, 0), special_flags=pg.BLEND_RGBA_MULT)
        
        #triangular_surface = floor_sprite.subsurface(mask.get_bounding_rect())
        #self.game.screen.blit(masked_surface, (0, 0)) # Need to make this better (show full visible area)
        
        triangle = pg.Surface(masked_surface.get_size(), pg.SRCALPHA)
        #pg.draw.polygon(triangle, (255, 255, 255), points)
        #pg.draw.polygon(triangle, (255, 0, 0), [v1, v2, v3])  # Draw a triangle on the surface
        #rect_surface = pg.Surface(width, half_height)  # Create a rectangle surface
        #rect_surface.fill((0, 255, 0))
        
        scaled_triangle = pg.transform.scale(triangle, (width, half_height))
        self.game.screen.blit(scaled_triangle, (0, half_height))



'''