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


playing = True

clock = pg.time.Clock()


def gameover():
    screen = g.display.set_mode(SIZE)
    clock = g.time.Clock()
    running = True
    while running:
        for event in g.event.get():
            if event.type == g.QUIT:
                quit()
            if event.type == g.KEYDOWN:
                if event.key == g.K_r:
                    running = False

        screen.fill(SKY)
        text = END.render(f"GAME OVER", True, RED)
        screen.blit(text, [240, 400])
        text = SCORE.render(f"If you wish to reset,", True, WHITE)
        screen.blit(text, [85, 600])
        text = SCORE.render(f"press the 'r' key", True, WHITE)
        screen.blit(text, [125, 650])

        g.display.flip()
        clock.tick(FPS)


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

    layout.Kill_Player()

    pg.display.flip()

pg.quit()
