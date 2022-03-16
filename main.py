import pygame as pg
import pygame.sprite

import sprites
from settings import *
from sprites import Player, Layout

pg.init()

# Set Base Screen
screen = pg.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pg.display.set_caption("Platformer Game")

floor = sprites.SpriteSheet("images/sheet.png")

# Groups

layout = Layout(LAYOUT, TILE_SIZE)

clock = pg.time.Clock()


def gameover():
    screen = pg.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
    clock = pg.time.Clock()
    running = True
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                quit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_r:
                    running = False

        screen.fill(SKY)
        text = END.render(f"GAME OVER", True, RED)
        screen.blit(text, [240, 400])
        text = SCORE.render(f"If you wish to reset,", True, WHITE)
        screen.blit(text, [85, 600])
        text = SCORE.render(f"press the 'r' key", True, WHITE)
        screen.blit(text, [125, 650])

        pg.display.flip()
        clock.tick(FPS)

def play():
    playing = True

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

        layout.update()

        if layout.Kill_Player() == False:
            gameover()

        pg.display.flip()

play()

pg.quit()
