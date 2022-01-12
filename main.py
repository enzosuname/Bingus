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

#ace_hearts = card.image_at((x_margin, y_margin, 43, 60))
#card_list = card.load_grid_images(4, 14, x_margin, x_pad, y_margin, y_pad)
#print(ace_hearts)

test = floor.image_at((x_margin + 16*1, y_margin, 16, 16), -1)
#run_rt_list = floor.load_grid_images(7, 10, x_margin, x_pad, y_margin, y_pad, width, height)
# run_lft_list = [pg.transform.flip(player, True, False) for player in run_rt_list]
print(test)

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

   screen.fill(SKY)

   for val in range(0,8):

       screen.blit(pg.transform.scale(floor.image_at((x_margin + 16 * val, y_margin, 16, 16)),\
                                      [100, 100]), [100*val, 500])

   pg.display.flip()

pg.quit()
