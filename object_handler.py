from sprite_object import *
from npc import *
from random import choices, randrange


class ObjectHandler:
    def __init__(self, game):
        self.game = game
        self.sprite_list = []
        self.npc_list = []
        self.npc_sprite_path = 'resources/sprites/npc/'
        self.static_sprite_path = 'resources/sprites/static/'
        self.anim_sprite_path = 'resources/sprites/animated/'
        add_sprite = self.add_sprite
        add_npc = self.add_npc
        self.npc_positions = {}

        # spawn npc
        #self.enemies = 20  # npc count
        #self.npc_types = [SoldierNPC, CacoDemonNPC, CyberDemonNPC]
        #self.weights = [70, 20, 10]
        #self.restricted_area = {(i, j) for i in range(10) for j in range(10)}
        #self.spawn_npc()

        # sprite map (possibly include in map data structure (use json for that?))
        #add_sprite(AnimatedSprite(game, path=self.anim_sprite_path + 'test/0.png', pos=(3.5, 18.5)))
        

        # npc map
        #add_npc(NPC(game, self.npc_sprite_path+'hotdogger.jpeg', pos=(5, 5)))

        add_sprite(SpriteObject(game, self.static_sprite_path+'mirror.png', pos=(20, 20), shift=1))
        add_sprite(SpriteObject(game, self.static_sprite_path+'mari.png', pos=car_path[0], shift=1))

        add_npc(NPC(game, self.npc_sprite_path+'kelcar_better.png', pos=(10, 10)))

        # add_npc(SoldierNPC(game, pos=(11.5, 4.5)))
        # add_npc(SoldierNPC(game, pos=(13.5, 6.5)))
        # add_npc(SoldierNPC(game, pos=(2.0, 20.0)))
        # add_npc(SoldierNPC(game, pos=(4.0, 29.0)))
        # add_npc(CacoDemonNPC(game, pos=(5.5, 14.5)))
        # add_npc(CacoDemonNPC(game, pos=(5.5, 16.5)))
        # add_npc(CyberDemonNPC(game, pos=(14.5, 25.5)))


    '''
    def spawn_npc(self):
        for i in range(self.enemies):
                npc = choices(self.npc_types, self.weights)[0]
                pos = x, y = randrange(self.game.map.cols), randrange(self.game.map.rows)
                while (pos in self.game.map.world_map) or (pos in self.restricted_area):
                    pos = x, y = randrange(self.game.map.cols), randrange(self.game.map.rows)
                self.add_npc(npc(self.game, pos=(x + 0.5, y + 0.5)))
    '''

    '''
    def check_win(self):
        if not len(self.npc_positions):
            self.game.object_renderer.win()
            pg.display.flip()
            pg.time.delay(1500)
            self.game.new_game()
    '''

    def update(self):
        #self.npc_positions = {npc.map_pos for npc in self.npc_list if npc.alive}
        [sprite.update() for sprite in self.sprite_list]
        [npc.update() for npc in self.npc_list]
        #self.check_win()

    def add_npc(self, npc):
        self.npc_list.append(npc)

    def add_sprite(self, sprite):
        self.sprite_list.append(sprite)