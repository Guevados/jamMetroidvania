import pygame
from tiles import Avatar
from settings import *
from support_lvl import *

class BoarWarriorBase(Avatar):
  def __init__(self, game, pos, groups, obstacle_sprites, sprite_type, health):
    super().__init__(groups)
    self.import_assets(sprite_type)
    self.game = game
    self.health = health
    self.image = self.animations["idle"][self.frame_index]
    self.rect = self.image.get_rect(bottomleft = (pos[0], pos[1] + tile_size))
    self.hitbox = self.rect.inflate(-20, -20)
    self.attacking = False
    self.on_ground = False
    self.on_ceiling = False
    self.on_right = False
    self.on_left = False
    self.moving_right = True
    self.move_timer = 0
    self.idle_timer = 0
    self.idling = False
    self.invincible = False
    self.invincibility_timer = 0
    self.vel = pygame.math.Vector2()
    self.obstacle_sprites = obstacle_sprites

  def import_assets(self, name):
    path = f"../assets/enemies/{name}"
    self.animations = {"Attack": [], "Death": [], "Idle": [], "Walk": []}

    for animation in self.animations.keys():
      full_path = path + animation
      self.animations[animation] = import_folder(full_path)