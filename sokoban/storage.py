import pygame

class Storage():
    def __init__(self):
        self.picture = pygame.image.load("resources\images\circle 45.png")
        self.width, self.height = self.picture.get_width(), self.picture.get_height()
        self.x = 15
        self.y = 15

    @property
    def hitbox(self):
        return (self.x, self.y, self.x + self.width, self.y + self.height)

    def draw(self, surface):
        surface.blit(self.picture, (self.x, self.y))

