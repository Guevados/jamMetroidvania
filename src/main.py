import pygame
from settings import screen_width, screen_height
from components import Player, Level, level_0

PJ_INITIAL_POSITION = pygame.math.Vector2(0, 220)

pygame.init()

screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
running = True
dt = 0
level = Level(level_0, screen)
player = Player(screen, clock, PJ_INITIAL_POSITION)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYUP:
            player.on_key_up()

    screen.fill("gray")
    level.run()

    player.draw()
    player.update()

    ground_collision = pygame.sprite.spritecollide(
        player, level.ground_sprites, False)
    if ground_collision:
        player.on_vertical_collision()

    wall_collision = pygame.sprite.spritecollide(
        player, level.wall_sprites, False)
    if wall_collision:
        player.on_horizontal_collision()

    pygame.display.flip()

    dt = clock.tick(60) / 1000

pygame.quit()
