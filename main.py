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

ace_hearts = card.image_at((x_margin, y_margin, 43, 60))
#card_list = card.load_grid_images(4, 14, x_margin, x_pad, y_margin, y_pad)
print(ace_hearts)

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

   screen.blit(ace_hearts, (100, 100))

   pg.display.flip()

pg.quit()
