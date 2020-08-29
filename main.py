import pygame
from pygame.locals import *


from sokoban.button import Button
from sokoban.game import Game
from sokoban.generator import Generator
from sokoban.character import Character
from sokoban.storage import Storage
from sokoban.box import Box
from sokoban.movement import Movement

pygame.init()
display = pygame.display
display.set_caption('Sokoban')
# print(display.list_modes())
# print(display.Info().current_w, display.Info().current_h)
width, height = 1600, 900

main_menu = display.set_mode((width, height))
options = display.set_mode((width, height))
game_screen = display.set_mode((width, height))

in_main_menu = True
in_options = False
in_game = False

game_title = Button("resources/images/Game Title.png", (width*(203/960), height*(71/540)))
play_button = Button("resources/images/Play Button.png", (width*(320/960), height*(220/540)))
options_button = Button("resources/images/Options Button.png", (width*(361/960), height*(345/540)))
exit_button = Button("resources/images/Exit Button.png", (width*(402/960), height*(443/540)))

def resize():
    game_title.resize(width, height)
    play_button.resize(width, height)
    options_button.resize(width, height)
    exit_button.resize(width, height)

resize()

while in_main_menu:
    main_menu.fill((255, 255, 255))

    game_title.draw(screen=main_menu)
    play_button.draw(screen=main_menu)
    options_button.draw(screen=main_menu)
    exit_button.draw(screen=main_menu)

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if play_button.is_clicked(mouse_pos=pygame.mouse.get_pos()):
                in_main_menu = False
                in_game = True
            if options_button.is_clicked(mouse_pos=pygame.mouse.get_pos()):
                in_main_menu = False
                in_options = True
            if exit_button.is_clicked(mouse_pos=pygame.mouse.get_pos()):
                pygame.quit()
                exit(0)

while in_options:
    options.fill((255, 255, 255))

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

# ! this will be an image
tile_w, tile_h = 60, 60
x1, y1 = 0, 0
all_rects = []

for row in range(0, 9):
    for col in range(0, 13):
        all_rects.append(pygame.Rect(x1 + (60 * col), y1 + (60 * row), tile_w, tile_h))


game = Game.generate()
game.check_nodes()
game.create_map()

while in_game:
    game_screen.fill((184, 180, 163))

    for rect in all_rects:
        pygame.draw.rect(game_screen, (0, 0, 0), rect, 1)
    game.check_nodes()
    game.draw(screen=game_screen)
    game.character.draw(screen=game_screen)

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
                        game.character.move(key=Movement.OPPOSITE_MOVEMENT.get(event.key))

    if game.win():
        pygame.quit()
        exit(0)