import pygame
from settings import tile_size
from components.support_lvl import import_csv_layout, import_cut_graphics
from components.tiles import Tile, StaticTile

class Level:
    def __init__(self, levelData, surface):
        self.display_surface = surface
        self.world_shift = 0

        terrain_layout = import_csv_layout(levelData['terrain'])
        self.terrain_sprites = self.create_tile_group(terrain_layout, 'terrain') 

        building_layout = import_csv_layout(levelData['buildingDoors'])
        self.building_sprites = self.create_tile_group(building_layout, 'buildingDoors')

    def create_tile_group(self, layout, type):
        sprite_group = pygame.sprite.Group()

        for row_index, row in enumerate(layout):
            for col_index, val in enumerate(row):
                if val != '-1':
                    x = col_index * tile_size
                    y = row_index * tile_size

                    if type == 'terrain':
                        terrain_tile_list = import_cut_graphics('src/graphics/tileset/Tiles.png')
                        tile_surface = terrain_tile_list[int(val)]
                        sprite = StaticTile(tile_size, x, y, tile_surface)

                    if type == 'buildingDoors':
                        building_tile_list = import_cut_graphics('src/graphics/tileset/Buildings.png')
                        tile_surface = building_tile_list[int(val)]
                        sprite = StaticTile(tile_size, x, y, tile_surface)
                        
                    sprite_group.add(sprite)


        return sprite_group

    def run(self):

        self.terrain_sprites.draw(self.display_surface)
        self.terrain_sprites.update(self.world_shift)

        self.building_sprites.draw(self.display_surface) 
        self.building_sprites.update(self.world_shift)
