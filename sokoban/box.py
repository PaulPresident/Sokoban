import pygame

class Box():
    def __init__(self):
        self.surface = pygame.image.load('resources/images/box.png')
        self.x = 60
        self.y = 60

    @property
    def hitbox(self):
        return (self.x, self.y, self.x+60, self.y+60)

    def draw(self, surface):
        surface.blit(self.surface, (self.x, self.y))

    def is_hit(self, character):
        if self.hitbox[0] < character.x + 30 < self.hitbox[2] and self.hitbox[1] < character.y + 30 < self.hitbox[3]:
            return True
        return False

    def move(self, key):
        if key == pygame.K_w and self.y > 0:
            self.y -= 60
            return True
        if key == pygame.K_a and self.x > 0:
            self.x -= 60
            return True
        if key == pygame.K_s and self.y < 480 - 60:
            self.y += 60
            return True
        if key == pygame.K_d and self.x < 720 - 60:
            self.x += 60
            return True
        return False
