import pygame

from sokoban.character import Character
from sokoban.box import Box

pygame.init()
width, height = 720, 480
display = pygame.display
display.set_caption('Sokoban')
surface = display.set_mode((width, height))

movement = {
    pygame.K_w:pygame.K_s, pygame.K_s:pygame.K_w,
    pygame.K_a: pygame.K_d, pygame.K_d: pygame.K_a
}

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
            character.move(key=event.key, box=box)

            if box.is_hit(character):
                if not box.move(key=event.key):
                    character.move(key=movement.get(event.key), box=box)
