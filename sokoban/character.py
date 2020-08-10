import pygame

class Character():
    def __init__(self):
        self.surface = pygame.image.load('resources/images/character (Mini) (Custom).png')
        self.x = 0
        self.y = 0
        self.hitbox = ((self.x, self.y), (self.x+60, self.y), (self.x, self.y+60), (self.x + 60, self.y + 60))

    def draw(self, surface):
        surface.blit(self.surface, (self.x, self.y))