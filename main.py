import pygame


# TODO change names of vars, args, attrs in these classes
from sokoban.movement import width, height  # TODO find better place to store
from sokoban.button import Button
from sokoban.character import Character
from sokoban.storage import Storage
from sokoban.box import Box

pygame.init()
display = pygame.display
display.set_caption('Sokoban')

start = display.set_mode((width, height))
game = display.set_mode((width, height))
end = display.set_mode((width, height))

start_bool = True
game_bool = False
end_bool = False

movement = {
    pygame.K_w:pygame.K_s, pygame.K_s:pygame.K_w,
    pygame.K_a: pygame.K_d, pygame.K_d: pygame.K_a
} # TODO find better place to store under movement class maybe

start_button = Button("resources/images/start button.png", (200, 140))

storage_places = [Storage()]
boxes = [Box()]
character = Character()

# game attrs
boxes_stored = 0

# ! this will be an image
tile_w, tile_h = 60, 60
x1, y1 = 0, 0
all_rects = []

for row in range(0, 9):
    for col in range(0, 13):
        all_rects.append(pygame.Rect(x1 + (60 * col), y1 + (60 * row), tile_w, tile_h))


while start_bool:
    start.fill((255, 255, 255))

    start_button.draw(start) # TODO rename to play button
    pygame.draw.rect(start, (255, 0, 0), pygame.Rect(240, 160, 800, 200), 1) # ! for refrence only
    pygame.draw.rect(start, (255, 0, 0), pygame.Rect(480, 480, 320, 120), 1) # ! for refrence only

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            x, y = pygame.mouse.get_pos()
            mouse_rect = pygame.Rect(x, y, 0, 0)
            if mouse_rect.colliderect(start_button.hitbox):
                start_bool = False
                game_bool = True

while game_bool:
    game.fill((184, 180, 163))

    pygame.draw.rect(start, (255, 0, 0), pygame.draw.rect(game, (0, 0, 0), (120, 120, 60, 60), 1), 1)
    for rect in all_rects:
        pygame.draw.rect(game, (0, 0, 0), rect, 1)

    for storage in storage_places:
        storage.draw(surface=game)
    for box in boxes:
        box.draw(surface=game)
    character.draw(surface=game)

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)

        if event.type == pygame.KEYDOWN:
            character.move(key=event.key)

            for box in boxes:
                if box.hitbox.colliderect(character.hitbox):
                    if not box.move(key=event.key):
                        character.move(key=movement.get(event.key))

    for box in boxes:
        if box.is_stored(storage_places):
            boxes_stored += 1

    if boxes_stored == len(boxes):
        pygame.quit()
        exit(0)