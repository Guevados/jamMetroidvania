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
            ],
            'attack_right': [
                pygame.image.load(
                    "src/assets/sprites/player/attack_right_4.png"),
                pygame.image.load(
                    "src/assets/sprites/player/attack_right_5.png"),
                pygame.image.load(
                    "src/assets/sprites/player/attack_right_6.png"),
                pygame.image.load(
                    "src/assets/sprites/player/attack_right_7.png"),
            ],
            'attack_left': [
                pygame.image.load(
                    "src/assets/sprites/player/attack_left_0.png"),
                pygame.image.load(
                    "src/assets/sprites/player/attack_left_1.png"),
                pygame.image.load(
                    "src/assets/sprites/player/attack_left_2.png"),
                pygame.image.load(
                    "src/assets/sprites/player/attack_left_3.png"),
            ]

        }
        self.image = self.images['idle_right']
        self.imageIndex = 0
        self.animationTimer = 0
        self.animationSpeed = 4
        self.direction = 'right'

    def setAnimationTimer(self):
        self.animationTimer += 1
        if self.animationTimer >= self.animationSpeed:
            self.animationTimer = 0
            self.imageIndex += 1
            if self.imageIndex >= len(self.image):
                self.imageIndex = 0

    def on_key_up(self):
        self.animationSpeed = 4
        self.image = self.images['idle_right'] if self.direction == 'right' else self.images['idle_left']

    def update(self):
        self.setAnimationTimer()
        self.dt = self.clock.tick(60) / 1000

        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.pos.y -= 500 * self.dt
        if keys[pygame.K_DOWN]:
            self.pos.y += 500 * self.dt
        if keys[pygame.K_LEFT]:
            self.direction = 'left'
            self.animationSpeed = 2
            self.image = self.images['run_left']
            self.pos.x -= 500 * self.dt
        if keys[pygame.K_RIGHT]:
            self.direction = 'right'
            self.animationSpeed = 2
            self.image = self.images['run_right']
            self.pos.x += 500 * self.dt
        elif keys[pygame.K_d]:
            self.animationSpeed = 4
            self.image = self.images['attack_right'] if self.direction == 'right' else self.images['attack_left']

    def draw(self):
        self.screen.blit(self.image[self.imageIndex], self.pos)
