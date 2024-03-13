from ursina import *

wall_height = 5
wall_thickness = 0.5
wall_length = 100
wall_texture = 'wallTexture4.png'

def load_entities():
    entities = {

        'ground': Entity(model='plane', texture='textured-background.png', scale=(100, 0, 100)),

        'north_wall': Entity(model='cube', texture=wall_texture, collider='box', scale=(wall_length, wall_height, wall_thickness), position=(0, wall_height / 2, -wall_length / 2)),
        'south_wall': Entity(model='cube', texture=wall_texture, collider='box', scale=(wall_length, wall_height, wall_thickness), position=(0, wall_height / 2, wall_length / 2)),
        'east_wall': Entity(model='cube', texture=wall_texture, collider='box', scale=(wall_thickness, wall_height, wall_length), position=(wall_length / 2, wall_height / 2, 0)),
        'west_wall': Entity(model='cube', texture=wall_texture, collider='box', scale=(wall_thickness, wall_height, wall_length), position=(-wall_length / 2, wall_height / 2, 0)),

        'tree2_leaves-0': Entity(model='MapleTreeLeaves.obj', texture='grass-grass_track.png', position=(-36, 0, 40), scale=(0.2, 0.2, 0.2)),
        'tree2_barks-0': Entity(model='MapleTreeStem.obj', texture='thintree-grass.png', position=(-36, 0, 40), scale=(0.1, 0.1, 0.1), collider='sphere'),
        'tree2_leaves-1': Entity(model='MapleTreeLeaves.obj', texture='grass-grass_track.png', position=(-36, 0, 14), scale=(0.2, 0.2, 0.2)),
        'tree2_barks-1': Entity(model='MapleTreeStem.obj', texture='thintree-grass.png', position=(-36, 0, 14), scale=(0.1, 0.1, 0.1), collider='sphere'),
        'tree2_leaves-2': Entity(model='MapleTreeLeaves.obj', texture='grass-grass_track.png', position=(-36, 0, -12), scale=(0.2, 0.2, 0.2)),
        'tree2_barks-2': Entity(model='MapleTreeStem.obj', texture='thintree-grass.png', position=(-36, 0, -12), scale=(0.1, 0.1, 0.1), collider='sphere'),
        'tree2_leaves-3': Entity(model='MapleTreeLeaves.obj', texture='grass-grass_track.png', position=(-36, 0, -38), scale=(0.2, 0.2, 0.2)),
        'tree2_barks-3': Entity(model='MapleTreeStem.obj', texture='thintree-grass.png', position=(-36, 0, -38), scale=(0.1, 0.1, 0.1), collider='sphere'),

        'tree2_barks0': Entity(model='MapleTreeStem.obj', texture='thintree-grass.png', position=(1, 0, 23), scale=(0.3, 0.3, 0.3), collider='sphere'),
        'tree2_barks1': Entity(model='MapleTreeStem.obj', texture='thintree-grass.png', position=(-3, 0, 17), scale=(0.3, 0.3, 0.3), collider='sphere'),
        'tree2_barks2': Entity(model='MapleTreeStem.obj', texture='thintree-grass.png', position=(1, 0, 11), scale=(0.3, 0.3, 0.3), collider='sphere'),
        'tree2_barks3': Entity(model='MapleTreeStem.obj', texture='thintree-grass.png', position=(-3, 0, 5), scale=(0.3, 0.3, 0.3), collider='sphere'),
        'tree2_barks00': Entity(model='MapleTreeStem.obj', texture='thintree-grass.png', position=(1, 0, -23), scale=(0.3, 0.3, 0.3), collider='sphere'),
        'tree2_barks11': Entity(model='MapleTreeStem.obj', texture='thintree-grass.png', position=(-3, 0, -17), scale=(0.3, 0.3, 0.3), collider='sphere'),
        'tree2_barks22': Entity(model='MapleTreeStem.obj', texture='thintree-grass.png', position=(1, 0, -11), scale=(0.3, 0.3, 0.3), collider='sphere'),
        'tree2_barks33': Entity(model='MapleTreeStem.obj', texture='thintree-grass.png', position=(-3, 0, -5), scale=(0.3, 0.3, 0.3), collider='sphere'),

        'building2-1': Entity(model='Cyprys_House.obj', position=(-49, 0, -30), scale=(0.9, 0.9, 0.9), rotation=(0, -90, 0), collider='box'),
        'building2-3': Entity(model='Cyprys_House.obj', position=(-49, 0, -4), scale=(0.9, 0.9, 0.9), rotation=(0, -90, 0), collider='box'),
        'building2-5': Entity(model='Cyprys_House.obj', position=(-49, 0, 22), scale=(0.9, 0.9, 0.9), rotation=(0, -90, 0), collider='box'),
        'building2-7': Entity(model='Cyprys_House.obj', position=(-49, 0, 48), scale=(0.9, 0.9, 0.9), rotation=(0, -90, 0), collider='box'),

        'building3-4': Entity(model='Bambo_House.obj', position=(-10, 0, 21), scale=(0.9, 0.9, 0.9), rotation=(0, 45, 0), collider='box'),
        'building3-5': Entity(model='Bambo_House.obj', position=(-15, 0, -13), scale=(0.9, 0.9, 0.9), rotation=(0, -45, 0), collider='box'),
        'building3-0': Entity(model='Bambo_House.obj',  position=(50, 0, -45), scale=(0.9, 0.9, 0.9), rotation=(0, 90, 0), collider='box'),
        'building3-1': Entity(model='Bambo_House.obj',  position=(50, 0, -20), scale=(0.9, 0.9, 0.9), rotation=(0, 90, 0), collider='box'),
        'building3-2': Entity(model='Bambo_House.obj',  position=(50, 0, 5), scale=(0.9, 0.9, 0.9), rotation=(0, 90, 0), collider='box'),
        'building3-3': Entity(model='Bambo_House.obj',  position=(50, 0, 30), scale=(0.9, 0.9, 0.9), rotation=(0, 90, 0), collider='box'),

        'building4-0': Entity(model='Rv_Building_3.obj', texture='particle_grass_track.png', position=(10, -0.5, 38), scale=(0.55, 0.7, 0.7), rotation=(0, 30, 0), collider='box'),
        'building4-1': Entity(model='Rv_Building_3.obj', texture='particle_grass_track.png', position=(15, -0.5, 0), scale=(0.55, 0.7, 0.7), rotation=(0, 90, 0), collider='box'),
        'building4-2': Entity(model='Rv_Building_3.obj', texture='particle_grass_track.png', position=(10, -0.5, -38), scale=(0.55, 0.7, 0.7), rotation=(0, 150, 0), collider='box'),

        'building6-0': Entity(model='Warehouse.obj', texture='particle_forest_track.png', position=(35, 0, 20), scale=(0.5, 0.5, 0.5), rotation=(0, -60, 0), collider='box'),
        'building6-1': Entity(model='Warehouse.obj', texture='particle_forest_track.png', position=(33, 0, -35), scale=(0.5, 0.5, 0.5), rotation=(0, 50, 0), collider='box'),

        'rock1-0': Entity(model='rock2.obj', texture='rock-grass.png', position=(40, -1, 10), scale=(2, 2, 2), collider='box'),
        'rock1-00': Entity(model='rock2.obj', texture='rock-grass.png', position=(38, -1, 10), scale=(2, 2, 2), collider='box'),
        'rock1-1': Entity(model='rock1.obj', texture='rock-grass.png', position=(40, -0.9, 8), scale=(2, 2, 2), collider='box'),
        'rock1-3': Entity(model='rock4.obj', texture='rock-grass.png', position=(40, -0.9, 12), scale=(2, 2, 2), collider='box'),
        'rock1-11': Entity(model='rock1.obj', texture='rock-grass.png', position=(42, -0.9, 7), scale=(2, 2, 2), collider='box'),
        'rock1-4': Entity(model='rock5.obj', texture='rock-grass.png', position=(41, -0.7, 10), scale=(2, 2, 2), collider='box'),
        'rock1-5': Entity(model='rock5.obj', texture='rock-grass.png', position=(-15, -0.7, 3), scale=(2, 2, 2), collider='box'),
        'rock1-6': Entity(model='rock4.obj', texture='rock-grass.png', position=(-59, -0.9, -17), scale=(2, 2, 2), rotation=(0, -90, 0), collider='box'),
        'rock1-7': Entity(model='rock5.obj', texture='rock-grass.png', position=(-12, -0.7, -2), scale=(2, 2, 2), collider='box'),
        'rock1-8': Entity(model='rock1.obj', texture='rock-grass.png', position=(-13, -0.9, -9), scale=(2, 2, 2), collider='box'),
        'rock1-9': Entity(model='rock2.obj', texture='rock-grass.png', position=(-12, -1, -8), scale=(2, 2, 2), collider='box'),

        'fence1-0': Entity(model='woodFence.obj', texture='wallTexture5.png', position=(32, -0.5, -4), scale=(0.1, 0.02, 0.04), rotation=(-90, 90, 0), collider='box'),
        'fence1-1': Entity(model='woodFence.obj', texture='wallTexture5.png', position=(27, -0.5, -4), scale=(0.1, 0.02, 0.04), rotation=(-90, 90, 0), collider='box'),

        'fence2-0': Entity(model='13077_Gothic_Picket_Fence_Panel_v3_l3.obj', texture='wallTexture5.png', position=(-18, 0, 2), scale=(0.08, 0.02, 0.02), rotation=(-90, 0, 0), collider='box'),
        'fence2-1': Entity(model='13077_Gothic_Picket_Fence_Panel_v3_l3.obj', texture='wallTexture5.png', position=(-18, 0, -2), scale=(0.08, 0.02, 0.02), rotation=(-90, 0, 0), collider='box'),

        'car': Entity( model='sports-car.obj', texture='sports-black.png', position=(0, 0.6, 0), collider='box', scale=(0.5, 0.5, 0.5))
    }
    return entities


def load_corridor():
    point_light = PointLight(position=(0, 20, 0))

    walls = {
        'ground': Entity(model='plane', texture='textured-background.png', scale=(40, 0, 40)),

        'wall1': Entity(model='cube', texture=wall_texture, scale=(0.5, 4, 19),
                             position=(2, 2, -4.35), collider='box'),
        'wall4': Entity(model='cube', texture=wall_texture, scale=(0.5, 4, 10),
                        position=(5.5, 2, 1.5), rotation=(0, -45, 0), collider='box'),
        'wall2': Entity(model='cube', texture=wall_texture, scale=(0.5, 4, 10),
                        position=(-2, 2, 0), collider='box'),
        'wall22': Entity(model='cube', texture=wall_texture, scale=(0.5, 4, 6),
                        position=(-2, 2, 12), collider='box'),
        'wall3': Entity(model='cube', texture=wall_texture, scale=(0.5, 4, 20),
                        position=(5, 2, 8), rotation=(0, -45, 0), collider='box'),
        'wall5': Entity(model='cube', texture=wall_texture, scale=(0.5, 4, 6),
                         position=(-5, 2, 9.25), rotation=(0, 90, 0), collider='box'),
        'wall55': Entity(model='cube', texture=wall_texture, scale=(0.5, 4, 6),
                        position=(-5, 2, 4.75), rotation=(0, 90, 0), collider='box'),
        'wall6': Entity(model='cube', texture=wall_texture, scale=(0.5, 4, 8),
                        position=(-8, 2, 13), rotation=(0, 0, 0), collider='box'),
        'wall66': Entity(model='cube', texture=wall_texture, scale=(0.5, 4, 8),
                        position=(-8, 2, 1), rotation=(0, 0, 0), collider='box'),
        'wall7': Entity(model='cube', texture=wall_texture, scale=(0.5, 4, 12),
                         position=(-12, 2, 7), rotation=(0, 0, 0), collider='box'),
        'wall77': Entity(model='cube', texture=wall_texture, scale=(0.5, 4, 4),
                        position=(-14, 2, 12.75), rotation=(0, 90, 0), collider='box'),
        'wall777': Entity(model='cube', texture=wall_texture, scale=(0.5, 4, 4),
                        position=(-14, 2, 1.25), rotation=(0, 90, 0), collider='box'),
        'wall7777': Entity(model='cube', texture=wall_texture, scale=(0.5, 4, 12),
                        position=(-16, 2, 7), rotation=(0, 0, 0), collider='box'),

        'wall8': Entity(model='cube', texture=wall_texture, scale=(0.5, 4, 12),
                         position=(-14, 2, 17), rotation=(0, 90, 0), collider='box'),
        'wall88': Entity(model='cube', texture=wall_texture, scale=(0.5, 4, 20),
                           position=(-20, 2, 7), rotation=(0, 0, 0), collider='box'),
        'wall888': Entity(model='cube', texture=wall_texture, scale=(0.5, 4, 8.5),
                          position=(-16, 2, -3), rotation=(0, 90, 0), collider='box'),

        'wall9': Entity(model='cube', texture=wall_texture, scale=(0.5, 4, 2),
                         position=(9.45, 2, -2.8), rotation=(0, -30, 0), collider='box'),
        'wall99': Entity(model='cube', texture=wall_texture, scale=(0.5, 4, 4),
                         position=(13, 2, -0.7), rotation=(0, -30, 0), collider='box'),

        'wall10': Entity(model='cube', texture=wall_texture, scale=(0.5, 4, 2),
                        position=(10.2, 2, -4.6), rotation=(0, -15, 0), collider='box'),
        'wall100': Entity(model='cube', texture=wall_texture, scale=(0.5, 4, 4),
                         position=(14.45, 2, -4.2), rotation=(0, -15, 0), collider='box'),

        'wall11': Entity(model='cube', texture=wall_texture, scale=(0.5, 4, 2),
                         position=(10.45, 2, -6.5), rotation=(0, 0, 0), collider='box'),
        'wall111': Entity(model='cube', texture=wall_texture, scale=(0.5, 4, 3),
                          position=(14.95, 2, -7.6), rotation=(0, 0, 0), collider='box'),

        'wall12': Entity(model='cube', texture=wall_texture, scale=(0.5, 4, 2),
                         position=(10.2, 2, -8.35), rotation=(0, 15, 0), collider='box'),
        'wall122': Entity(model='cube', texture=wall_texture, scale=(0.5, 4, 3),
                          position=(14.55, 2, -10.45), rotation=(0, 15, 0), collider='box'),

        'wall13': Entity(model='cube', texture=wall_texture, scale=(0.5, 4, 2),
                         position=(9.52, 2, -10), rotation=(0, 30, 0), collider='box'),
        'wall133': Entity(model='cube', texture=wall_texture, scale=(0.5, 4, 3),
                          position=(13.4, 2, -13.1), rotation=(0, 30, 0), collider='box'),

        'wall14': Entity(model='cube', texture=wall_texture, scale=(0.5, 4, 2),
                         position=(8.35, 2, -11.5), rotation=(0, 45, 0), collider='box'),
        'wall144': Entity(model='cube', texture=wall_texture, scale=(0.5, 4, 3),
                          position=(11.6, 2, -15.4), rotation=(0, 45, 0), collider='box'),

        'wall15': Entity(model='cube', texture=wall_texture, scale=(0.5, 4, 2),
                         position=(6.85, 2, -12.65), rotation=(0, 60, 0), collider='box'),
        'wall155': Entity(model='cube', texture=wall_texture, scale=(0.5, 4, 3),
                          position=(9.5, 2, -17), rotation=(0, 60, 0), collider='box'),

        'wall16': Entity(model='cube', texture=wall_texture, scale=(0.5, 4, 2),
                         position=(5.1, 2, -13.38), rotation=(0, 75, 0), collider='box'),
        'wall166': Entity(model='cube', texture=wall_texture, scale=(0.5, 4, 4),
                          position=(6.4, 2, -18.2), rotation=(0, 75, 0), collider='box'),

        'wall17': Entity(model='cube', texture=wall_texture, scale=(0.5, 4, 2.4),
                         position=(3.3, 2, -13.6), rotation=(0, 90, 0), collider='box'),
        'wall177': Entity(model='cube', texture=wall_texture, scale=(0.5, 4, 2.6),
                          position=(3.4, 2, -18.68), rotation=(0, 90, 0), collider='box'),

        'wall18': Entity(model='cube', texture=wall_texture, scale=(0.5, 4, 15),
                          position=(-4.5, 2, -18.68), rotation=(0, 90, 0), collider='box'),
        'wall188': Entity(model='cube', texture=wall_texture, scale=(0.5, 4, 16),
                          position=(-12, 2, -10.9), rotation=(0, 0, 0), collider='box'),

        'wall19': Entity(model='cube', texture=wall_texture, scale=(0.5, 4, 6),
                         position=(-5, 2, -3.75), rotation=(0, -70, 0), collider='box'),
        'wall20': Entity(model='cube', texture=wall_texture, scale=(0.5, 4, 6),
                         position=(-8, 2, -11), rotation=(0, 0, 0), collider='box'),
        'wall202': Entity(model='cube', texture=wall_texture, scale=(0.5, 4, 6),
                         position=(-5, 2, -13.75), rotation=(0, 90, 0), collider='box'),

        'car': Entity(model='sports-car.obj', texture='sports-black.png', position=(0, 0.6, 0), collider='box',
                      scale=(0.5, 0.5, 0.5))

    }
    return walls

