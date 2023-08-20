import pygame
from settings import screen_width, screen_height
from player import Player
from components.level import Level 
from components.gameData import level_0

pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
running = True
dt = 0
level = Level(level_0, screen)

player_pos = pygame.math.Vector2(
    (screen.get_width() / 2) - 64, (screen.get_height() / 2) - 80)
player = Player(screen, clock, player_pos)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYUP:
            player.on_key_up(event)

    screen.fill("gray")
    level.run()

    player.draw()
    player.animate()
    player.update()

    pygame.display.flip()

    dt = clock.tick(60) / 1000

pygame.quit()
