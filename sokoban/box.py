import pygame

from sokoban.movement import Movement

class Box(Movement):
    def __init__(self, x, y):
        self.image = pygame.image.load("resources/images/box.png")
        self.width, self.height = self.image.get_width(), self.image.get_height()
        self.unoccupied_nodes = []
        self.x = x
        self.y = y

    @property
    def node(self):
        return (round(self.x/60), round(self.y/60))

    @property
    def hitbox(self):
        return pygame.Rect(self.x-5, self.y-5, self.width+10, self.height+10)

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))
        pygame.draw.rect(screen, (255, 0, 0), self.hitbox, 1)

    def is_stored(self, storage_places:list):
        for storage in storage_places:
            if self.hitbox.colliderect(storage.hitbox):
                return True
        return False

    def move(self, key):
        if key in self.controls:
            return self.controls.get(key)()