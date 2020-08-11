import pygame

width, height = 1280, 720

class Movement():
    def __init__(self):
        self.x = 0
        self.y = 0

    @property
    def controls(self):
        return {
            pygame.K_w: self.move_up,
            pygame.K_a: self.move_left,
            pygame.K_s: self.move_down,
            pygame.K_d: self.move_right
        }

    def move_up(self):
        if self.y > 0:
            self.y -= 60
            return True
        return False

    def move_down(self):
        if self.y < height - 60:
            self.y += 60
            return True
        return False

    def move_right(self):
        if self.x < width - 60:
            self.x += 60
            return True
        return False

    def move_left(self):
        if self.x > 0:
            self.x -= 60
            return True
        return False