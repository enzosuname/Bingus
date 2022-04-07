import pygame as pg
import pygame.sprite

import sprites
from settings import *
from sprites import Player, Layout, Enemy

pg.init()

# Set Base Screen
screen = pg.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pg.display.set_caption("Platformer Game")

floor = sprites.SpriteSheet("images/sheet.png")

# Groups
global next

layout = Layout(LAYOUT, TILE_SIZE, next)

clock = pg.time.Clock()

next = 0
game_state = -1
max_level = 1

def start():
    screen = pg.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
    clock = pg.time.Clock()
    global game_state
    global next
    running = True
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                quit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_r:
                    SELECT_SOUND.play()
                    game_state = 0
                    running = False

        screen.fill(SKY)
        text = END.render(f"PRESS", True, BLACK)
        screen.blit(text, [295, 350])
        text = END.render(f"'R'", True, BLACK)
        screen.blit(text, [330, 425])
        text = END.render(f"TO START", True, BLACK)
        screen.blit(text, [240, 500])

        pg.display.flip()
        clock.tick(FPS)

def win():
    screen = pg.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
    clock = pg.time.Clock()
    global game_state
    global next
    running = True
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                quit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    SELECT_SOUND.play()
                    next = 0
                    game_state = -1
                    reset_game()
                    running = False

        screen.fill(SKY)
        text = END.render(f"YOU WIN!", True, GREEN)
        screen.blit(text, [240, 400])
        text = SCORE.render(f"If you wish to reset,", True, WHITE)
        screen.blit(text, [220, 600])
        text = SCORE.render(f"press the 'Escape' key", True, WHITE)
        screen.blit(text, [200, 650])

        pg.display.flip()
        clock.tick(FPS)

def gameover():
    screen = pg.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
    clock = pg.time.Clock()
    global game_state
    global next
    running = True
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                quit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_r:
                    SELECT_SOUND.play()
                    game_state = 0
                    running = False
                if event.key == pg.K_ESCAPE:
                    SELECT_SOUND.play()
                    next = 0
                    game_state = -1
                    reset_game()
                    running = False

        screen.fill(SKY)
        text = END.render(f"GAME OVER", True, RED)
        screen.blit(text, [240, 400])
        text = SCORE.render(f"If you wish to reset,", True, WHITE)
        screen.blit(text, [220, 600])
        text = SCORE.render(f"press the 'Escape' key", True, WHITE)
        screen.blit(text, [200, 650])
        text = SCORE.render(f"If you wish to contiune,", True, WHITE)
        screen.blit(text, [180, 495])
        text = SCORE.render(f"press the 'r' key", True, WHITE)
        screen.blit(text, [247, 535])

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
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_q:
                    next += 1
                    reset_game()

        screen.fill(SKY)

        layout.draw(screen)

        layout.update()

        if layout.Kill_Player() == False:
            game_state = 1
            playing = False
            reset_game()

        elif layout.Next_Level() == False:
            next += 1
            reset_game()

        if next == 3:
            layout.Cont()

        if game_state == 2:
            playing = False

        pg.display.flip()

def reset_game():
    global layout
    global next
    layout = Layout(LAYOUT, TILE_SIZE, next)
    if next == 1:
        layout = Layout(LAYOUT_2, TILE_SIZE, next)
    if next == 2:
        layout = Layout(LAYOUT_3, TILE_SIZE, next)
    if next == 3:
        layout = Layout(LAYOUT_4, TILE_SIZE, next)
    if next == 4:
        global game_state
        game_state = 2


robert = True
while robert:
    if game_state == -1:
        start()
    if game_state == 0:
        play()
    if game_state == 1:
        gameover()
    if game_state == 2:
        win()

pg.quit()
