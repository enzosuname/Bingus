import pygame as pg
import pygame.sprite

import sprites
from settings import *
from sprites import Player

pg.init()

# Set Base Screen
screen = pg.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pg.display.set_caption("Platformer Game")

# Groups

player_group = pygame.sprite.Group()

floor = sprites.SpriteSheet("images/sheet.png")
characters = sprites.SpriteSheet("images/characters.png")

x_margin = 112
y_margin = 0
x_pad = 0
y_pad = 0

width = 20
height = 27

player_x = 5
player_y = 69
player_x_pad = 12
player_y_pad = 0

#test = floor.image_at((x_margin + 16 * 1, y_margin, 16, 16), -1)

run_rt_list = characters.load_grid_images(1, 23, player_x, player_x_pad, player_y, player_y_pad, width, height, -1)
run_lft_list = [pg.transform.flip(characters, True, False) for characters in run_rt_list]

# Player ?
player = Player(run_rt_list)
player_group.add(player)


playing = True

clock = pg.time.Clock()

while playing:

    clock.tick(FPS)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            playing = False
        if event.type == pg.KEYDOWN:  # allow for q key to quit the game
            if event.key == pg.K_q:
                playing == False

    screen.fill(SKY)

    player_group.draw(screen)

    player_group.update()

    for val in range(0, 4):
        for layer in range(8, 11):
            screen.blit(
                pg.transform.scale(floor.image_at((x_margin, y_margin + 16*3, 16, 16), (255, 255, 255)),
                                [75, 75]), [75 * layer, 525 - 75 * val])

    for val in range(0, 4):
        screen.blit(
            pg.transform.scale(floor.image_at((x_margin + 16 * 3, y_margin + 16 * 3, 16, 16), (255, 255, 255)),
                               [75, 75]), [75 * 7, 525 - 75 * val])

    screen.blit(
        pg.transform.scale(floor.image_at((x_margin + 16, y_margin + 16 * 3, 16, 16), (255, 255, 255)),
                           [75, 75]), [75 * 7, 525 - 75 * 4])

    for val in range(0, 3):
        screen.blit(
            pg.transform.scale(floor.image_at((x_margin + 16, y_margin + 16 * 2, 16, 16), (255, 255, 255)),
                                [75, 75]), [75 * 8 + 75 * val, 525 - 75 * 4])


    for additive in range(0, 3):
        for val in range(1, 7):
            screen.blit(
                pg.transform.scale(floor.image_at((x_margin + 16 * additive, y_margin, 16, 16), (255, 255, 255)),
                                   [75, 75]), [75 * val, 525])

    screen.blit(
        pg.transform.scale(floor.image_at((x_margin + 16, y_margin + 16, 16, 16), (255, 255, 255)),
                           [75, 75]), [75 * 0, 525])
    screen.blit(
        pg.transform.scale(floor.image_at((x_margin + 16 * 2, y_margin + 16, 16, 16), (255, 255, 255)),
                           [75, 75]), [75 * 7, 525])

    # counter = -1
    # for player in run_rt_list:
    #         counter += 1
    #         screen.blit(
    #             pg.transform.scale(player, [37.5, 50.625]), [37.5 * counter, 475])




    pg.display.flip()

pg.quit()
