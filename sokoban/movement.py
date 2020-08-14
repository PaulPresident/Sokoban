import pygame

width, height = 1280, 720

class Movement():
    def __init__(self):
        self.width, self.height = 0, 0
        self.unoccupied_nodes = []
        self.x = 0
        self.y = 0

    @property
    def future_hitbox(self):
        return {
            'up': pygame.Rect(self.x, self.y-60, self.width, self.height),
            'down': pygame.Rect(self.x, self.y+60, self.width, self.height),
            'right': pygame.Rect(self.x+60, self.y, self.width, self.height),
            'left': pygame.Rect(self.x-60, self.y, self.width, self.height),
        }

    @property
    def controls(self):
        return {
            pygame.K_w: self.move_up,
            pygame.K_a: self.move_left,
            pygame.K_s: self.move_down,
            pygame.K_d: self.move_right
        }

    def move_up(self):
        for node in self.unoccupied_nodes:
            if self.y > 0 and self.future_hitbox.get('up').colliderect(node.hitbox):
                self.y -= 60
                return True
        return False

    def move_down(self):
        for node in self.unoccupied_nodes:
            if self.y < height - 60 and self.future_hitbox.get('down').colliderect(node.hitbox):
                self.y += 60
                return True
        return False

    def move_right(self):
        for node in self.unoccupied_nodes:
            if self.x < width - 60 and self.future_hitbox.get('right').colliderect(node.hitbox):
                self.x += 60
                return True
        return False

    def move_left(self):
        for node in self.unoccupied_nodes:
            if self.x > 0 and self.future_hitbox.get('left').colliderect(node.hitbox):
                self.x -= 60
                return True
        return False