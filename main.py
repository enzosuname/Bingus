import pygame as pg
import sprites
from settings import *

pg.init()

# Set Base Screen
screen = pg.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pg.display.set_caption("Card Game")

card = sprites.SpriteSheet("images/deck_of_cards.png")
x_margin = 11
y_margin = 2
x_pad = 22
y_pad = 4

#ace_hearts = card.image_at((x_margin, y_margin, 43, 60))
#card_list = card.load_grid_images(4, 14, x_margin, x_pad, y_margin, y_pad)
#print(ace_hearts)

run_rt_list = thing.load_grid_images(1, 8, x_margin, x_pad, y_margin, y_pad, width, height, -1)
run_lft_list = [pg.transform.flip(player, True, False) for player in run_rt_list]
print(run_rt_list)

playing = True

clock = pg.time.Clock()

while playing:

   clock.tick(FPS)

   for event in pg.event.get():
       if event.type == pg.QUIT:
           playing = False
       if event.type == pg.KEYDOWN:    # allow for q key to quit the game
           if event.key == pg.K_q:
               playing == False

   screen.fill(BLACK)

   pg.display.flip()

pg.quit()
