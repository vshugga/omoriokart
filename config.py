import math

res = width, height = 1080, 720

half_width = width // 2
half_height = height // 2
fps = 60 #Make this adaptive?


player_pos = 10, 5
player_angle = 0
player_speed = 0.004
player_rot_speed = 0.001
player_size_scale = 60

floor_color = (30, 30, 30)

fov = math.pi / 3
#fov = 3
half_fov = fov / 2
num_rays = width // 2
half_num_rays = num_rays // 2
delta_angle = fov / num_rays
max_depth = 20

screen_dist = half_width / math.tan(half_fov)

texture_size = 256
half_texture_size = texture_size // 2
scale = width // num_rays

focal_len = 250
p_scale = 100 # projection scale
#p_scale = 90 / fov * (width / 1200)


# player sprites should be: forward, left, right
player_sprites = {
    'omori':'./resources/sprites/players/omori',
}


player_sprite_height = height*0.7
player_sprite_scale = 4


car_path = [
    (62, 16),
    (40, 21),
    (34, 32),
    (42, 42),
    (60, 57),
    (60, 66),
    (20, 72),
    (69, 84),
    (77, 64),
    (80, 40),
    (85, 31),
    (86, 15)
]
