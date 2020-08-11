import pygame

from sokoban.movement import Movement

class Character(Movement):
    def __init__(self):
        self.picture = pygame.image.load("resources/images/character (Mini) (Custom).png")
        self.width, self.height = self.picture.get_width(), self.picture.get_height()
        self.x = 0
        self.y = 0

    @property
    def hitbox(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)

    def draw(self, surface):
        pygame.draw.rect(surface, (255, 0, 0), self.hitbox, 1)
        surface.blit(self.picture, (self.x, self.y))

    def move(self, key):
        if key in self.controls:
            self.controls.get(key)()