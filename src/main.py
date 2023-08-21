import pygame
from player import Player

pygame.init()
screen = pygame.display.set_mode((1200, 720))
clock = pygame.time.Clock()
running = True
dt = 0

player_pos = pygame.math.Vector2(
    (screen.get_width() / 2) - 64, (screen.get_height() / 2) - 80)
player = Player(screen, clock, player_pos)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYUP:
            player.on_key_up()

    screen.fill("gray")

    player.draw()
    player.update()

    pygame.display.flip()

    dt = clock.tick(60) / 1000

pygame.quit()
