import pygame as pg
import pygame.sprite

import sprites
from settings import *
from sprites import Player, Layout

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

# Player ?
player = Player(run_rt_list)
player_group.add(player)
layout = Layout(LAYOUT, TILE_SIZE)


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

    layout.draw(screen)

    player_group.draw(screen)

    player_group.update()

    pg.display.flip()

pg.quit()
