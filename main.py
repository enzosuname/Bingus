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

level = 0
game_state = -1
max_level = 1

def start():
    screen = pg.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
    clock = pg.time.Clock()
    global game_state
    running = True
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                quit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_r:
                    game_state = 0
                    running = False

        screen.fill(SKY)
        text = END.render(f"PRESS", True, GREEN)
        screen.blit(text, [295, 350])
        text = END.render(f"'R'", True, GREEN)
        screen.blit(text, [330, 425])
        text = END.render(f"TO START", True, GREEN)
        screen.blit(text, [240, 500])

        pg.display.flip()
        clock.tick(FPS)

def gameover():
    screen = pg.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
    clock = pg.time.Clock()
    global game_state
    running = True
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                quit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_r:
                    game_state = -1
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
        global game_state
        global next

        for event in pg.event.get():
            if event.type == pg.QUIT:
                quit()
            if event.type == pg.KEYDOWN:  # allow for q key to quit the game
                if event.key == pg.K_q:
                    next = 1
                    reset_game()

        screen.fill(SKY)

        layout.draw(screen)

        layout.update()

        if layout.Kill_Player() == False:
            game_state = 1
            playing = False
            reset_game()

        elif layout.Next_Level() == False:
            next = 1
            reset_game()

        pg.display.flip()

def reset_game():
    global layout
    layout = Layout(LAYOUT, TILE_SIZE)
    if next == 1:
        layout = Layout(LAYOUT_2, TILE_SIZE)


robert = True
while robert:
    if game_state == -1:
        start()
    if game_state == 0:
        play()
    if game_state == 1:
        gameover()

pg.quit()
