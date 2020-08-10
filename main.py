import pygame

from sokoban.character import Character
from sokoban.box import Box

pygame.init()
width, height = 720, 480
display = pygame.display
display.set_caption('Sokoban')
surface = display.set_mode((width, height))

character = Character()
box = Box()

x1, x2, y1, y2 = 0, 60, 0, 60
all_rects = []

for row in range(1, 9):
    for col in range(1, 13):
        all_rects.append(pygame.Rect(x1 * col, y1 * row, x2 * col, y2 * row))


while True:
    surface.fill((184, 180, 163))

    for rect in all_rects:
        pygame.draw.rect(surface, (0, 0, 0), rect, 1)
    box.draw(surface=surface)
    character.draw(surface=surface)

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w and character.y > 0 and not box.is_hit(character.hitbox):
                character.y -= 60
            if event.key == pygame.K_a and character.x > 0 and not box.is_hit(character.hitbox):
                character.x -= 60
            if event.key == pygame.K_s and character.y < 480 - 60 and not box.is_hit(character.hitbox):
                character.y += 60
            if event.key == pygame.K_d and character.x < 720 - 60 and not box.is_hit(character.hitbox):
                character.x += 60