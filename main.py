import random

import pygame as pg
from screens.game import Game
from enums import Directions
from screens.start_screen import StartScreen
from sprites.lucky import Lucky
from utils.load_image import load_image
from utils.load_sound import load_sound
from screens.end import End
from utils.saves import save_game
import os

if __name__ == '__main__':
    pg.init()
    size = width, height = 1080, 620
    sc = pg.display.set_mode(size)
    pg.display.set_caption('Танчики')
    pg.display.set_icon(load_image('tank1.png'))



    screen_number = 0
    screens = [
        StartScreen(width, height),
        Game(width, height),
        End(width, height),
    ]



    clock = pg.time.Clock()
    running = True
    seconds = 0
    while running:
        screen = screens[screen_number]
        sc.blit(screen.bg, (0,0))

        if screen_number == 1:
            ticks = pg.time.get_ticks()
            if ticks // 1000 - seconds >= 1:
                seconds = ticks // 1000
                screen.timer.decrement()
                if not screen.timer.value:
                    print(1)
                    if screens[1].score1.value > screens[1].score2.value:
                        screens[2].setWinner(1)
                    elif screens[1].score1.value < screens[1].score2.value:
                        screens[2].setWinner(2)
                    else:
                        screens[2].setWinner(0)

                    screen_number = 2
                    screen.timer.running = False


        for event in pg.event.get():
            if event.type == pg.QUIT:
                if screen_number == 1: 
                    map = screen.map_number
                    tank1 = screen.tank1
                    tank2 = screen.tank2
                    save_game(map, screen.timer.value, tank1, tank2)
                pg.quit()
            elif event.type == pg.MOUSEBUTTONDOWN:
                if hasattr(screen, 'btns'):
                    for btn in screen.btns:
                        if btn.rect.collidepoint(pg.mouse.get_pos()):
                            if btn.text == 'Продолжить игру' or btn.text == 'Новая игра' or btn.text == 'Играть снова':
                                if not btn.text == 'Продолжить игру' and os.path.exists('save.json'):
                                    os.remove('save.json')
                                screens[1].__init__(width, height)
                                screen_number = 1
                                load_sound('starting.mp3').play()
                            elif btn.text == 'Выйти из игры':
                                pg.quit()

            elif event.type == pg.KEYDOWN:
                print(event.key)
                tank1 = screens[1].tank1
                tank2 = screens[1].tank2
                match event.key:
                    case pg.K_ESCAPE:
                        map = screen.map_number
                        tank1 = screen.tank1
                        tank2 = screen.tank2
                        save_game(map, screen.timer.value, tank1, tank2)
                        screen_number = 0

                    case pg.K_PERIOD:
                        tank1.shoot()
                    case pg.K_UP:
                        tank1.set_direction(Directions.TOP)
                    case pg.K_LEFT:
                        tank1.set_direction(Directions.LEFT)
                    case pg.K_DOWN:
                        tank1.set_direction(Directions.BOTTOM)
                    case pg.K_RIGHT:
                        tank1.set_direction(Directions.RIGHT)

                    case pg.K_SPACE:
                        tank2.shoot()
                    case pg.K_w:
                        tank2.set_direction(Directions.TOP)
                    case pg.K_a:
                        tank2.set_direction(Directions.LEFT)
                    case pg.K_s:
                        tank2.set_direction(Directions.BOTTOM)
                    case pg.K_d:
                        tank2.set_direction(Directions.RIGHT)

            elif event.type == pg.KEYUP:
                tank1 = screens[1].tank1
                tank2 = screens[1].tank2
                if event.key in [1073741906, 1073741904, 1073741905, 1073741903]:
                    tank1.set_direction(Directions.STOP)
                elif event.key in [119, 97, 115, 100]:
                    tank2.set_direction(Directions.STOP)


        if 1 == random.randrange(1000) and screen_number == 1:
            Lucky(screen.all, width, height)

        screen.all.update()
        screen.all.draw(sc)
        pg.display.flip()
        clock.tick(50)    
    
    pg.quit()