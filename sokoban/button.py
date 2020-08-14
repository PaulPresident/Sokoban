import pygame

class Button():
    def __init__(self, image:str, location:tuple):
        self.image = pygame.image.load(image)
        self.width, self.height = self.image.get_width(), self.image.get_height()
        self.x, self.y = location

    @property
    def hitbox(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)

    def draw(self, screen):
        pygame.draw.rect(screen, (255, 0, 0), self.hitbox, 1)
        screen.blit(self.image, (self.x, self.y))

    def resize(self, screen, w, h):
        self.image = pygame.transform.scale(self.image, (self.width + w, self.height + h))
        self.draw(screen=screen)