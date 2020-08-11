import pygame

class Button():
    def __init__(self, picture:str, location:tuple):
        self.picture = pygame.image.load(picture)
        self.width, self.height = self.picture.get_width(), self.picture.get_height()
        self.x, self.y = location

    @property
    def hitbox(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)

    def draw(self, surface):
        pygame.draw.rect(surface, (255, 0, 0), self.hitbox, 1)
        surface.blit(self.picture, (self.x, self.y))