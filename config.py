import math

res = width, height = 1600, 900
half_width = width // 2
half_height = height // 2
fps = 60 #Make this adaptive?


player_pos = 1.5, 5
player_angle = 0
player_speed = 0.004
player_rot_speed = 0.002

fov = math.pi / 3
#fov = 3
half_fov = fov / 2
num_rays = width // 2
half_num_rays = num_rays // 2
delta_angle = fov / num_rays
max_depth = 20

screen_dist = half_width / math.tan(half_fov)
scale = width // num_rays