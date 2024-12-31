import pygame as pg

from sprites.borders import Border
from sprites.tank import Tank
from enums import Directions
from sprites.map import Map

if __name__ == '__main__':
    pg.init()
    size = width, height = 1280, 920
    sc = pg.display.set_mode(size)
    pg.display.set_caption('Танчики')

    all = pg.sprite.Group()
    solids = pg.sprite.Group()

    tank1 = Tank(all, solids, 1, (10, 10))
    tank2 = Tank(all, solids, 2, (width - 150, height - 115  ))

    Border(all, solids, 0, 0, width, 0)
    Border(all, solids, 0, height - 0, width, height)
    Border(all, solids, 0, 0, 0, height)
    Border(all, solids, width, 0, width, height)

    map1 = Map(all, solids)

    clock = pg.time.Clock()
    running = True
    while running:
        sc.fill(pg.Color('black'))
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
            elif event.type == pg.KEYDOWN:
                print(event.key)
                match event.key:
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
                if event.key in [1073741906, 1073741904, 1073741905, 1073741903]:
                    tank1.set_direction(Directions.STOP)
                elif event.key in [119, 97, 115, 100]:
                    tank2.set_direction(Directions.STOP)

        all.update()
        all.draw(sc)
        pg.display.flip()
        clock.tick(50)
    
    pg.quit()