import pygame
from pygame.locals import *


# from sokoban.movement import width, height  # TODO find better place to store
from sokoban.button import Button
from sokoban.game import Game
from sokoban.generator import Generator
from sokoban.character import Character
from sokoban.storage import Storage
from sokoban.box import Box

pygame.init()
display = pygame.display
display.set_caption('Sokoban')
# print(display.list_modes())
# print(display.Info().current_w, display.Info().current_h)
width, height = 1600, 900

main_menu = display.set_mode((width, height))
game_board = display.set_mode((width, height))
end = display.set_mode((width, height))
in_main_menu = True
in_game = False
in_end = False

movement = {
    pygame.K_w:pygame.K_s, pygame.K_s:pygame.K_w,
    pygame.K_a: pygame.K_d, pygame.K_d: pygame.K_a
} # TODO find better place to store under movement class maybe

play_button = Button("resources/images/start button.png", (200, 140))


while in_main_menu:
    main_menu.fill((255, 255, 255))

    play_button.draw(screen=main_menu)
    pygame.draw.rect(main_menu, (255, 0, 0), pygame.Rect(240, 160, 800, 200), 1) # ! for refrence only
    pygame.draw.rect(main_menu, (255, 0, 0), pygame.Rect(480, 480, 320, 120), 1) # ! for refrence only

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
# # TODO figure out resizing to specific sizes (1920, 1280|1600, 900|1280, 720)
        # if event.type == pygame.VIDEORESIZE:
#             main_menu = pygame.display.set_mode(event.size, HWSURFACE|DOUBLEBUF|RESIZABLE)
#             # main_menu.blit(pygame.transform.scale(play_button.image, event.size), (0, 0))
#             print(event.w-width)
#             print(event.h-height)
#             play_button.resize(screen=main_menu, w=event.w-width, h=event.h-height)
#             width = event.w
#             height = event.h
#             # pygame.transform.scale(main_menu, event.dict['size'], event.dict['size'])
#             # pygame.display.flip()

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            x, y = pygame.mouse.get_pos()
            mouse_rect = pygame.Rect(x, y, 0, 0)
            if mouse_rect.colliderect(play_button.hitbox):
                in_main_menu = False
                in_game = True



# ! this will be an image
tile_w, tile_h = 60, 60
x1, y1 = 0, 0
all_rects = []

for row in range(0, 9):
    for col in range(0, 13):
        all_rects.append(pygame.Rect(x1 + (60 * col), y1 + (60 * row), tile_w, tile_h))


game = Game.easy()
game.create_map()

while in_game:
    game_board.fill((184, 180, 163))

    for rect in all_rects:
        pygame.draw.rect(game_board, (0, 0, 0), rect, 1)
    # game.check_nodes()
    game.draw(screen=game_board)
    game.character.draw(screen=game_board)

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)

        if event.type == pygame.KEYDOWN:
            game.character.move(key=event.key)

            for box in game.boxes:
                if box.hitbox.colliderect(game.character.hitbox):
                    if not box.move(key=event.key):
                        game.character.move(key=movement.get(event.key))

    if game.win():
        pygame.quit()
        exit(0)