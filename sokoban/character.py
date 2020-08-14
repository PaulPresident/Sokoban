import pygame

from sokoban.movement import Movement

class Character(Movement):
    def __init__(self, x, y):
        self.image = pygame.image.load("resources/images/character (Mini) (Custom).png")
        self.width, self.height = self.image.get_width(), self.image.get_height()
        self.unoccupied_nodes = []
        self.x = x
        self.y = y

    # @property
    # def node(self):
    #     return (round(self.x/60), round(self.y/60))

    @property
    def hitbox(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))
        pygame.draw.rect(screen, (255, 0, 0), self.hitbox, 1)

    def move(self, key):
        if key in self.controls:
            self.controls.get(key)()