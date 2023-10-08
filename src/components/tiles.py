import pygame
from support_lvl import import_folder

class Tile(pygame.sprite.Sprite):
    def __init__(self, size, x, y):
        super().__init__()
        self.image = pygame.Surface((size, size))
        self.rect = self.image.get_rect(topleft = (x, y))

    def update(self, shift):
        self.rect.x += shift

class StaticTile(Tile):
    def __init__(self, size, x, y, surface):
        super().__init__(size, x, y)
        self.image = surface

class Entity(pygame.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)

    def animate(self, type_animation):
        animation = self.animations[self.state]

        self.frame_index += self.frame_rate
        if type_animation == "death":
            if self.frame_index >= len(animation) -1:
                self.kill()

        if type_animation == "loop":
            if self.frame_index >= len(animation):
                self.frame_index = 0

        img_right = animation[int(self.frame_index)]
        if self.facing == 1:
            self.image = img_right
        else:
            img_left = pygame.transform.flip(img_right, True, False)
            self.image = img_left

class Avatar(Entity):
    def __init__(self, groups):
        super().__init__(groups)
        self.current_x = 0
        self.alive = True
        self.state = "idle"
        self.facing = 1
        self.frame_index = 0
        self.frame_rate = 0.2

    def animate(self, type_animation):
        animation = self.animations[self.state]

        self.frame_index += self.frame_rate
        if type_animation == "death":
            if self.frame_index >= len(animation) -1:
                self.kill()

        if type_animation == "loop":
            if self.frame_index >= len(animation):
                self.frame_index = 0

        img_right = animation[int(self.frame_index)]
        if self.facing == 1:
            self.image = img_right
        else:
            img_left = pygame.transform.flip(img_right, True, False)
            self.image = img_left