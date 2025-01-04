import pygame as pg
from screens.game import Game
from enums import Directions
from screens.start_screen import StartScreen
from utils.load_image import load_image
from utils.load_sound import load_sound

if __name__ == '__main__':
    pg.init()
    size = width, height = 1080, 620
    sc = pg.display.set_mode(size)
    pg.display.set_caption('Танчики')

    screen_number = 0
    screens = [
        StartScreen(width, height),
        Game(width, height),
    ]

    clock = pg.time.Clock()
    running = True
    while running:
        screen = screens[screen_number]
        sc.fill(screen.bg)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
            elif event.type == pg.MOUSEBUTTONDOWN:
                print(pg.mouse.get_pos())
                if hasattr(screen, 'btns'):
                    for btn in screen.btns:
                        if btn.rect.collidepoint(pg.mouse.get_pos()):
                            if btn.text == 'Играть':
                                screen_number = 1
                                load_sound('starting.mp3').play()
                            else:
                                pg.quit()

            elif event.type == pg.KEYDOWN:
                print(event.key)
                tank1 = screens[1].tank1
                tank2 = screens[1].tank2
                match event.key:
                    case 27:
                        screen = screens[screen_number]
                        screen.__init__(width, height)
                        screen_number = 0

                    case 1073742055:
                        tank1.shoot()
                    case 1073741906:
                        tank1.set_direction(Directions.TOP)
                    case 1073741904:
                        tank1.set_direction(Directions.LEFT)
                    case 1073741905:
                        tank1.set_direction(Directions.BOTTOM)
                    case 1073741903:
                        tank1.set_direction(Directions.RIGHT)

                    case 32:
                        tank2.shoot()
                    case 119:
                        tank2.set_direction(Directions.TOP)
                    case 97:
                        tank2.set_direction(Directions.LEFT)
                    case 115:
                        tank2.set_direction(Directions.BOTTOM)
                    case 100:
                        tank2.set_direction(Directions.RIGHT)

            elif event.type == pg.KEYUP:
                tank1 = screens[1].tank1
                tank2 = screens[1].tank2
                if event.key in [1073741906, 1073741904, 1073741905, 1073741903]:
                    tank1.set_direction(Directions.STOP)
                elif event.key in [119, 97, 115, 100]:
                    tank2.set_direction(Directions.STOP)

        screen.all.update()
        screen.all.draw(sc)
        pg.display.flip()
        clock.tick(50)
    
    pg.quit()