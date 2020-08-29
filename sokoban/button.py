import pygame

class Button():
    def __init__(self, image:str, location:tuple, size:int=None):
        self.image = pygame.image.load(image)
        self.width, self.height = self.image.get_width(), self.image.get_height()
        self.x, self.y = location

    @property
    def hitbox(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)

    def resize(self, width, height):
        size = (round(self.width/(1920/width)), round(self.height/(1080/height)))
        self.image = pygame.transform.scale(self.image, size)
        self.width, self.height = self.image.get_width(), self.image.get_height()

    def draw(self, screen):
        pygame.draw.rect(screen, (255, 0, 0), self.hitbox, 1)
        screen.blit(self.image, (self.x, self.y))

    def is_clicked(self, mouse_pos):
        mouse_rect = pygame.Rect(*mouse_pos, 0, 0)
        return mouse_rect.colliderect(self.hitbox)

    @classmethod
    def medium(cls, image:str, location:tuple):
        cls(image=image, location=location)