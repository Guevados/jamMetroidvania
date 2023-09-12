import pygame
from settings import DEBUG, tile_size
from components import (
    StaticTile,
    import_csv_layout,
    import_cut_graphics
)


GROUND_TILES = [6, 1, 2, 3, 31, 30, 26, 251,
                126, 127, 128, 126, 129, 151, 152, 154]
WALL_TILES = [29,  54, 125, 150, 175, 179, 204, 252, 277]  # 25, 50

TILES = {
    'ground': GROUND_TILES,
    'wall': WALL_TILES,
}


class Level():
    def __init__(self, levelData, surface):
        self.display_surface = surface
        self.world_shift = 0

        terrain_layout = import_csv_layout(levelData['terrain'])

        self.terrain_sprites = self.create_tile_group(
            terrain_layout, 'terrain')
        self.ground_sprites = self.create_tile_group(
            terrain_layout, 'ground')
        self.wall_sprites = self.create_tile_group(
            terrain_layout, 'wall')

        self.level_sprites = pygame.sprite.Group()
        self.level_sprites.add(self.terrain_sprites)
        self.level_sprites.add(self.ground_sprites)
        self.level_sprites.add(self.wall_sprites)

    def create_tile_group(self, layout, type):
        terrain_tile_list = import_cut_graphics(
            'src/graphics/tileset/Tiles.png')
        sprite_group = pygame.sprite.Group()

        for row_index, row in enumerate(layout):
            for col_index, val in enumerate(row):
                if val != '-1':
                    x = col_index * tile_size
                    y = row_index * tile_size

                    if type == 'wall' and int(val) in TILES['wall']:
                        tile_surface = terrain_tile_list[int(val)]
                        sprite_group.add(StaticTile(
                            tile_size, x, y, tile_surface))
                    elif type == 'ground' and int(val) in TILES['ground']:
                        tile_surface = terrain_tile_list[int(val)]
                        sprite_group.add(StaticTile(
                            tile_size, x, y, tile_surface))
                    elif type == 'terrain' and int(val) not in (TILES['ground'] + TILES['wall']):
                        tile_surface = terrain_tile_list[int(val)]
                        sprite_group.add(StaticTile(
                            tile_size, x, y, tile_surface))

        return sprite_group

    def run(self):
        self.level_sprites.draw(self.display_surface)
        self.level_sprites.update(self.world_shift)
        if DEBUG:
            # Show sprites rect
            for ground in self.ground_sprites:
                pygame.draw.rect(self.display_surface,
                                 (255, 0, 0), ground.rect, 2)
            for wall in self.wall_sprites:
                pygame.draw.rect(self.display_surface,
                                 (0, 0, 255), wall.rect, 2)
