import pygame as pg
import math
from config import *


class Raycast:
    def __init__(self, game):
        self.game = game
        self.ray_cast_result = []
        self.objs_to_render = []
        self.textures = self.game.object_renderer.wall_textures
        self.max_vert = ()
        self.max_hor = ()

    def get_objs_to_render(self):
        self.objs_to_render = []
        for ray, vals in enumerate(self.ray_cast_result):
            depth, proj_height, texture, offset = vals

            if proj_height < height: 

                wall_column = self.textures[texture].subsurface(
                    offset * (texture_size - scale), 0, scale, texture_size
                )
                wall_column = pg.transform.scale(wall_column, (scale, proj_height))
                wall_pos = (ray * scale, half_height - proj_height // 2)
            else:
                texture_height = texture_size * height / proj_height
                wall_column = self.textures[texture].subsurface(
                    offset * (texture_size - scale), half_texture_size - texture_height // 2,
                    scale, texture_height
                )
                wall_column = pg.transform.scale(wall_column, (scale, height))
                wall_pos = (ray * scale, 0)


            self.objs_to_render.append((depth, wall_column, wall_pos))

    def ray_cast(self, get_edges=False):
        self.ray_cast_result = []
        ox, oy = self.game.player.pos              # Coordinates of player
        x_map, y_map = self.game.player.map_pos    # Top left coordinates of players tile

        ray_angle = self.game.player.angle - half_fov + 0.0001
        for ray in range(num_rays):
            sin_a = math.sin(ray_angle)
            cos_a = math.cos(ray_angle)

            y_hor, dy = (y_map + 1, 1) if sin_a > 0 else (y_map - 1e-6, -1)
            depth_hor = (y_hor - oy) / sin_a
            x_hor = ox + depth_hor * cos_a
            delta_depth = dy / sin_a
            dx = delta_depth * cos_a

            for i in range(max_depth):
                tile_hor = int(x_hor), int(y_hor)
                if tile_hor in self.game.map.world_map:
                    texture_hor = self.game.map.world_map[tile_hor]
                    #self.max_hor = x_hor, y_hor
                    break
                x_hor += dx
                y_hor += dy
                depth_hor += delta_depth

            x_vert, dx = (x_map + 1, 1) if cos_a > 0 else (x_map - 1e-6, -1)
            depth_vert = (x_vert - ox) / cos_a
            y_vert = oy + depth_vert * sin_a
            delta_depth = dx / cos_a
            dy = delta_depth * sin_a

            for i in range(max_depth):
                tile_vert = int(x_vert), int(y_vert)
                if tile_vert in self.game.map.world_map:
                    texture_vert = self.game.map.world_map[tile_vert]
                    #self.max_vert = x_vert, y_vert
                    break
                x_vert += dx
                y_vert += dy
                depth_vert += delta_depth

            if depth_vert < depth_hor:
                depth, texture = depth_vert, texture_vert
                y_vert %= 1
                offset = y_vert if cos_a > 0 else (1 - y_vert)
            else:
                depth, texture = depth_hor, texture_hor
                x_hor %= 1
                offset = (1 - x_hor) if sin_a > 0 else x_hor


            # Draw the fov
            #self.map_fov_coords = (20 * ox, 20 * oy), (20 * ox + 20 * depth * cos_a, 20 * oy + 20 * depth * sin_a)
            #pg.draw.line(self.game.screen, 'yellow', (20 * ox, 20 * oy), 
            #    (20 * ox + 20 * depth * cos_a, 
            #    20 * oy + 20 * depth * sin_a), 2)

            # correct for polar coords
            depth *= math.cos(self.game.player.angle - ray_angle)
            
            proj_height = screen_dist / (depth + 0.0001)

            #color = [255 / (1 + depth ** 5 * 0.00002)] * 3
            #pg.draw.rect(self.game.screen, color, 
            #    (ray * scale, half_height - proj_height // 2, scale, proj_height))

            self.ray_cast_result.append((depth, proj_height, texture, offset))

            ray_angle += delta_angle

    # Cast two rays to edges of map, return their coordinates
    def get_edges(self):

        #self.ray_cast_result = []
        ox, oy = self.game.player.pos              # Coordinates of player
        x_map, y_map = self.game.player.map_pos    # Top left coordinates of players tile

        ray_angle_l = self.game.player.angle - half_fov #+ 0.0001
        ray_angle_r = self.game.player.angle + half_fov #+ 0.0001
        #print(ray_angle_l, ray_angle_r)

        depths = []

        for ray_angle in [ray_angle_l, ray_angle_r]:
            sin_a = math.sin(ray_angle)
            cos_a = math.cos(ray_angle)

            y_hor, dy = (y_map + 1, 1) if sin_a > 0 else (y_map - 1e-6, -1)
            depth_hor = (y_hor - oy) / sin_a
            x_hor = ox + depth_hor * cos_a
            delta_depth = dy / sin_a
            dx = delta_depth * cos_a

            for i in range(max_depth):
                tile_hor = int(x_hor), int(y_hor)
                if tile_hor in self.game.map.border:
                    break
                x_hor += dx
                y_hor += dy
                depth_hor += delta_depth
                '''
                if tile_hor in self.game.map.world_map:
                    texture_hor = self.game.map.world_map[tile_hor]
                    break
                '''

            x_vert, dx = (x_map + 1, 1) if cos_a > 0 else (x_map - 1e-6, -1)
            depth_vert = (x_vert - ox) / cos_a
            y_vert = oy + depth_vert * sin_a
            delta_depth = dx / cos_a
            dy = delta_depth * sin_a

            for i in range(max_depth):
                tile_vert = int(x_vert), int(y_vert)
                if tile_vert in self.game.map.border:
                    break
                x_vert += dx
                y_vert += dy
                depth_vert += delta_depth
                '''
                if tile_vert in self.game.map.world_map:
                    texture_vert = self.game.map.world_map[tile_vert]
                    self.max_vert = x_vert, y_vert
                    break
                '''
            
            '''
            if depth_vert < depth_hor:
                depth, texture = depth_vert, texture_vert
                y_vert %= 1
                offset = y_vert if cos_a > 0 else (1 - y_vert)
            else:
                depth, texture = depth_hor, texture_hor
                x_hor %= 1
                offset = (1 - x_hor) if sin_a > 0 else x_hor
            '''
            # 
            depth = min(depth_vert, depth_hor)
            
            # correct for polar coords
            depth *= math.cos(self.game.player.angle - ray_angle) # possibly get rid of to see what it does
            
            # Get the coordinates of the point
            #x = depth * math.sin(half_fov)
            #y = depth * math.cos(half_fov)

            #depths.append((x, y))
            depths.append(depth)

        

        xr = (ox - (depths[1] * math.cos(ray_angle_r+math.pi)))
        yr = (oy - (depths[1] * math.sin(ray_angle_r+math.pi)))

        xl = (ox - (depths[0] * math.cos(ray_angle_l+math.pi)))
        yl = (oy - (depths[0] * math.sin(ray_angle_l+math.pi)))

        return (xl, yl),(xr, yr)


    def update(self):
        self.ray_cast()
        self.get_objs_to_render()