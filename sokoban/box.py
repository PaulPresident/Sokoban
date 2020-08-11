import pygame

from sokoban.movement import Movement

class Box(Movement):
    def __init__(self):
        self.picture = pygame.image.load("resources/images/box.png")
        self.width, self.height = self.picture.get_width(), self.picture.get_height()
        self.x = 65
        self.y = 65

    @property
    def hitbox(self):
        return pygame.Rect(self.x-5, self.y-5, self.width+10, self.height+10)

    def draw(self, surface):
        pygame.draw.rect(surface, (255, 0, 0), self.hitbox, 1)
        surface.blit(self.picture, (self.x, self.y))

    def is_stored(self, storage_places:list):
        for storage in storage_places:
            if self.hitbox.colliderect(storage.hitbox):
                return True
        return False

    def move(self, key):
        if key in self.controls:
            return self.controls.get(key)()