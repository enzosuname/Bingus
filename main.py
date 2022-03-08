import pygame as pg
import pygame.sprite

import sprites
from settings import *
from sprites import Player, Layout, Background

pg.init()

# Set Base Screen
screen = pg.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pg.display.set_caption("Platformer Game")

floor = sprites.SpriteSheet("images/sheet.png")

# Groups

layout = Layout(LAYOUT, TILE_SIZE)
background = Background(BACKGROUND, TILE_SIZE)

# run_rt_list = characters.load_grid_images(1, 23, player_x, player_x_pad, player_y, player_y_pad, width, height, -1)
# player = Player(run_rt_list, layout.tile_list)
# player_group.add(player)



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

    background.draw(screen)

    layout.draw(screen)

    layout.update()

    pg.display.flip()

pg.quit()
