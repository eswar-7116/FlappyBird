import pygame as pg
from random import *
import sys

# Initialisation, Window, BGI and Font
pg.init()
wn = pg.display.set_mode((600, 750))
bgi = pg.image.load('gd/background-day.png').convert()
score_font = pg.font.Font('gd/Pixeltype.ttf', 40)
game_over_font = pg.font.Font('gd/Pixeltype.ttf', 80)
title_font = pg.font.Font('gd/Adventure.ttf', 90)

# Bars
bar_up_surf = pg.image.load('gd/bar_up.png').convert()
bar_up = bar_up_surf.get_rect(topleft=(0, -150))
bar_down_surf = pg.image.load('gd/bar_down.png').convert()
bar_down = bar_down_surf.get_rect(topleft=(0, 650))

# Birds
bird_up_surf = pg.image.load('gd/redbird-upflap.png').convert_alpha()
bird_rect = bird_up_surf.get_rect(topleft=(100, 300))
bird_mid_surf = pg.image.load('gd/redbird-midflap.png').convert_alpha()
bird_down_surf = pg.image.load('gd/redbird-downflap.png').convert_alpha()
birds = [bird_up_surf, bird_mid_surf, bird_down_surf]
bird_index = 0

# Red Pipes
rpu1_surf = pg.image.load('gd/red_up.png').convert_alpha()
rpu1 = rpu1_surf.get_rect()
rpu1.top = randint(-40, 81)
rpu1.x = 300
rpd1_surf = pg.image.load('gd/red_down.png').convert_alpha()
rpd1 = rpd1_surf.get_rect()
rpd1.bottom = randint(650, 801)
rpd1.x = 300

rpu2_surf = pg.image.load('gd/red_up.png').convert_alpha()
rpu2 = rpu2_surf.get_rect()
rpu2.top = randint(-40, 81)
rpu2.x = 700
rpd2_surf = pg.image.load('gd/red_down.png').convert_alpha()
rpd2 = rpd2_surf.get_rect()
rpd2.x = 700
rpd2.bottom = randint(650, 801)

# Green Pipes
gpu1_surf = pg.image.load('gd/green_up.png').convert_alpha()
gpu1 = gpu1_surf.get_rect()
gpu1.top = randint(-40, 81)
gpu1.x = 500
gpd1_surf = pg.image.load('gd/green_down.png').convert_alpha()
gpd1 = gpd1_surf.get_rect()
gpd1.x = 500
gpd1.bottom = randint(650, 801)

gpu2_surf = pg.image.load('gd/green_up.png').convert_alpha()
gpu2 = gpu2_surf.get_rect()
gpu2.top = randint(-40, 81)
gpu2.x = 900
gpd2_surf = pg.image.load('gd/green_down.png').convert_alpha()
gpd2 = gpd2_surf.get_rect()
gpd2.x = 900
gpd2.bottom = randint(650, 801)

pipe_speed = 2


def pipe_out():
    rpu1.top = randint(-40, 81)
    rpu1.x = 300
    rpd1.bottom = randint(650, 801)
    rpd1.x = 300
    rpu2.top = randint(-40, 81)
    rpu2.x = 700
    rpd2.x = 700
    rpd2.bottom = randint(650, 801)
    gpu1.top = randint(-40, 81)
    gpu1.x = 500
    gpd1.x = 500
    gpd1.bottom = randint(650, 801)
    gpu2.top = randint(-40, 81)
    gpu2.x = 900
    gpd2.x = 900
    gpd2.bottom = randint(650, 801)


game_state = 'intro'
score = 0
gravity = 0
fps = pg.time.Clock()
while True:

    if game_state == 'over1':
        bird_index = 2
        pipe_speed = 0
        if bird_rect.bottom >= 650:
            gravity = 0
            bird_rect.bottom = 1000
            game_state = 'over2'

    # BGI
    wn.blit(bgi, (0, -170))

    # Event Loop
    for event in pg.event.get():
        # QUIT
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
        # KEYDOWN and K_i
        if event.type == pg.KEYDOWN and event.key == pg.K_i:
            print(f'pipe_speed = {pipe_speed}')
            print(f'game_state = {game_state}')
            print(f'score = {score}')
        # MOUSEBUTTONDOWN
        if event.type == pg.MOUSEBUTTONDOWN and not pg.mouse.get_pressed()[1]:
            if game_state == 'playing':
                gravity = -4
            elif game_state == 'over2' or game_state == 'intro':
                bird_rect.topleft = (100, 300)
                pipe_out()
                pipe_speed = 2
                gravity = 0
                game_state = 'playing'

    # Pipes
    if game_state == 'playing' or game_state == 'over1':
        rpu1.x -= pipe_speed
        rpu2.x -= pipe_speed
        gpu1.x -= pipe_speed
        gpu2.x -= pipe_speed
        rpd1.x -= pipe_speed
        gpd1.x -= pipe_speed
        gpd2.x -= pipe_speed
        rpd2.x -= pipe_speed
        wn.blit(rpu1_surf, rpu1)
        wn.blit(rpu2_surf, rpu2)
        wn.blit(gpu1_surf, gpu1)
        wn.blit(gpu2_surf, gpu2)
        wn.blit(rpd1_surf, rpd1)
        wn.blit(rpd2_surf, rpd2)
        wn.blit(gpd1_surf, gpd1)
        wn.blit(gpd2_surf, gpd2)
        if rpu1.right <= 0: rpu1.left = gpu2.left + 200
        if rpd1.right <= 0: rpd1.left = gpd2.left + 200
        if gpu1.right <= 0: gpu1.left = rpu1.left + 200
        if gpd1.right <= 0: gpd1.left = rpd1.left + 200
        if rpu2.right <= 0: rpu2.left = gpu1.left + 200
        if rpd2.right <= 0: rpd2.left = gpd1.left + 200
        if gpu2.right <= 0: gpu2.left = rpu2.left + 200
        if gpd2.right <= 0: gpd2.left = rpd2.left + 200

    # Bars
    if game_state == 'playing' or game_state == 'over1':
        wn.blit(bar_up_surf, bar_up)
        wn.blit(bar_down_surf, bar_down)

    # Bird
    if game_state != 'intro':
        bird_index += .1
        if bird_index > 3: bird_index = 0
        gravity += .1
        bird_rect.y += gravity
        wn.blit(birds[int(bird_index)], bird_rect)

    # Bird collisions
    if rpu1.colliderect(bird_rect) or rpd1.colliderect(bird_rect) or gpu1.colliderect(bird_rect) or gpd1.colliderect(
        bird_rect) or rpu2.colliderect(bird_rect) or rpd2.colliderect(bird_rect) or gpu2.colliderect(
        bird_rect) or gpd2.colliderect(bird_rect) or bar_up.colliderect(bird_rect) or bar_down.colliderect(
        bird_rect) and game_state == 'playing': game_state = 'over1'

    # Score
    if rpu1.right == bird_rect.left or rpd1.right == bird_rect.left or gpu1.right == bird_rect.left or gpd1.right == bird_rect.left or rpu2.right == bird_rect.left or rpd2.right == bird_rect.left or gpu2.right == bird_rect.left or gpd2.right == bird_rect.left and game_state == 'playing': score += 1
    score_text = score_font.render(f'Score {score}', True, '#00b300')
    wn.blit(score_text, (5, 5))

    if game_state == 'intro':
        title = title_font.render('Flappy Bird'.capitalize(), True, '#0086b3')
        wn.blit(title, (100, 120))
        play_text = score_font.render('Click to Play!', True, '#ffffff')
        wn.blit(play_text, (230, 290))

    if game_state == 'over2':
        game_over_text = game_over_font.render('GAME OVER', True, '#ffffff')
        wn.blit(game_over_text, (180, 150))
        play2_text = score_font.render('Click to Play Again!', True, '#ffffff')
        wn.blit(play2_text, (197, 250))

    fps.tick(60)
    pg.display.update()
