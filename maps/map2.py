from sprites.wall import Wall
import pygame as pg

def map2(all, solids, width, height):
    color = pg.Color('darkred')

    Wall(all, solids, (100, 100), (40, 300), color)
    Wall(all, solids, (100, 500), (40, 150), color)

    Wall(all, solids, (240, 0), (40, 150), color)
    Wall(all, solids, (240, 250), (40, 500), color)

    Wall(all, solids, (380, 0), (40, 250), color)
    Wall(all, solids, (380, 350), (40, 180), color)

    Wall(all, solids, (540, 100), (40, height - 200), color)

    Wall(all, solids, (680, 100), (40, (height - 300) // 3), color)
    Wall(all, solids, (680, (height - 300) // 3 + 200), (40, (height - 300) // 3), color)
    Wall(all, solids, (680, (height - 300) // 3 * 2 + 300), (40, (height - 300) // 3), color)

    Wall(all, solids, (840, 100), (40, 300), color)
    Wall(all, solids, (840, 500), (40, 150), color)

    return pg.Color('black')