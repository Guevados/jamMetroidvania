import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self, screen, clock, pos):
        self.screen = screen
        self.clock = clock
        self.pos = pos
        self.dt = 0

        self.imageList = [
            pygame.image.load("src/assets/sprites/player/idle_0.png"),
            pygame.image.load("src/assets/sprites/player/idle_1.png"),
            pygame.image.load("src/assets/sprites/player/idle_2.png"),
            pygame.image.load("src/assets/sprites/player/idle_3.png"),
        ]
        self.imageIndex = 0
        self.animationTimer = 0
        self.animationSpeed = 5

    def idle(self):
        self.animationTimer += 1
        if self.animationTimer >= self.animationSpeed:
            self.animationTimer = 0
            self.imageIndex += 1
            if self.imageIndex >= len(self.imageList):
                self.imageIndex = 0

    def update(self):
        self.dt = self.clock.tick(60) / 1000

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.pos.y -= 300 * self.dt
        if keys[pygame.K_s]:
            self.pos.y += 300 * self.dt
        if keys[pygame.K_a]:
            self.pos.x -= 300 * self.dt
        if keys[pygame.K_d]:
            self.pos.x += 300 * self.dt

    def draw(self):
        self.screen.blit(self.imageList[self.imageIndex], self.pos)
