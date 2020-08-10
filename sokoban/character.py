import pygame

class Character():
    def __init__(self):
        self.surface = pygame.image.load('resources/images/character (Mini) (Custom).png')
        self.x = 0
        self.y = 0
        self.hitbox = (self.x, self.y, self.x + 60, self.y + 60)

    def draw(self, surface):
        surface.blit(self.surface, (self.x, self.y))

    def move(self, key, box):
        if key == pygame.K_w and self.y > 0:
            self.y -= 60
        if key == pygame.K_a and self.x > 0:
            self.x -= 60
        if key == pygame.K_s and self.y < 780 - 60:
            self.y += 60
        if key == pygame.K_d and self.x < 720 - 60:
            self.x += 60