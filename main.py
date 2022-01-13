import pygame as pg
import sprites
from settings import *

pg.init()

# Set Base Screen
screen = pg.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pg.display.set_caption("Platformer Game")

floor = sprites.SpriteSheet("images/sheet.png")
x_margin = 112
y_margin = 0
x_pad = 0
y_pad = 0
width = 0
height = 0

# ace_hearts = card.image_at((x_margin, y_margin, 43, 60))
# card_list = card.load_grid_images(4, 14, x_margin, x_pad, y_margin, y_pad)
# print(ace_hearts)

test = floor.image_at((x_margin + 16 * 1, y_margin, 16, 16), -1)
# run_rt_list = floor.load_grid_images(7, 10, x_margin, x_pad, y_margin, y_pad, width, height)
# run_lft_list = [pg.transform.flip(player, True, False) for player in run_rt_list]
print(test)

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



    pg.display.flip()

pg.quit()
