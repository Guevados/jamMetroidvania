import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self, screen, clock, pos):
        self.screen = screen
        self.clock = clock
        self.pos = pos
        self.dt = 0

        self.images = {
            'idle_left': [
                pygame.image.load("src/assets/sprites/player/idle_left_0.png"),
                pygame.image.load("src/assets/sprites/player/idle_left_1.png"),
                pygame.image.load("src/assets/sprites/player/idle_left_2.png"),
                pygame.image.load("src/assets/sprites/player/idle_left_3.png"),
            ],
            'idle_right': [
                pygame.image.load(
                    "src/assets/sprites/player/idle_right_0.png"),
                pygame.image.load(
                    "src/assets/sprites/player/idle_right_1.png"),
                pygame.image.load(
                    "src/assets/sprites/player/idle_right_2.png"),
                pygame.image.load(
                    "src/assets/sprites/player/idle_right_3.png"),
            ],
            'run_left': [
                pygame.image.load("src/assets/sprites/player/run_left_0.png"),
                pygame.image.load("src/assets/sprites/player/run_left_1.png"),
                pygame.image.load("src/assets/sprites/player/run_left_2.png"),
                pygame.image.load("src/assets/sprites/player/run_left_3.png"),
            ],
            'run_right': [
                pygame.image.load("src/assets/sprites/player/run_right_0.png"),
                pygame.image.load("src/assets/sprites/player/run_right_1.png"),
                pygame.image.load("src/assets/sprites/player/run_right_2.png"),
                pygame.image.load("src/assets/sprites/player/run_right_3.png"),
            ]

        }
        self.image = self.images['idle_right']
        self.imageIndex = 0
        self.animationTimer = 0
        self.animationSpeed = 4

    def timer(self):
        self.animationTimer += 1
        if self.animationTimer >= self.animationSpeed:
            self.animationTimer = 0
            self.imageIndex += 1
            if self.imageIndex >= len(self.image):
                self.imageIndex = 0

    def animate(self):
        self.timer()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_d]:
            self.animationSpeed = 2
            self.image = self.images['run_right']
        elif keys[pygame.K_a]:
            self.animationSpeed = 2
            self.image = self.images['run_left']
        else:
            self.animationSpeed = 4

    def on_key_up(self, event):
        if event.key == pygame.K_d:
            self.image = self.images['idle_right']
        elif event.key == pygame.K_a:
            self.image = self.images['idle_left']
        else:
            pass

    def update(self):
        self.dt = self.clock.tick(60) / 1000

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.pos.y -= 500 * self.dt
        if keys[pygame.K_s]:
            self.pos.y += 500 * self.dt
        if keys[pygame.K_a]:
            self.pos.x -= 500 * self.dt
        if keys[pygame.K_d]:
            self.pos.x += 500 * self.dt

    def draw(self):
        self.screen.blit(self.image[self.imageIndex], self.pos)
