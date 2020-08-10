import pygame

class Box():
    def __init__(self):
        self.surface = pygame.image.load('resources/images/box.png')
        self.x = 60
        self.y = 60
        self.hitbox = ((60, 60), (120, 60), (60, 120), (120, 120))

    def draw(self, surface):
        surface.blit(self.surface, (self.x, self.y))

    # TODO doesnt work
    def is_hit(self, hitbox):
        collisions = 0
        for coor in hitbox:
            for coor2 in self.hitbox:
                if coor == coor2:
                    collisions += 1
        if collisions == 2:
            return True
        return False