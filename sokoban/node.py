import pygame

class Node():
    def __init__(self, x, y, size):
        self.wall = pygame.image.load("resources/images/custom Character.png")
        self.x = x
        self.y = y
        # self.node = self.x * self.y
        self.size = size
        self.closed = True
        self.open = False
        self.has_box = False
        self.occupied = False

    @property
    def hitbox(self):
        return pygame.Rect(self.x*self.size, self.y*self.size, self.size, self.size)

    def reset(self):
        self.closed = True
        self.open = False
        self.has_box = False
        self.occupied = False