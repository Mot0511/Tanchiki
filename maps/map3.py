import pygame as pg
from sprites.wall import Wall

def map3(all, solids, width, height):
    color = pg.Color('darkgreen')
    Wall(all, solids, (width // 2 - 230, height // 2 - 130), (30, 260), color)
    Wall(all, solids, (width // 2 - 100, height // 2 - 130), (width -  730, 30), color)
    Wall(all, solids, (width // 2 + 220, height // 2 - 100), (30, 230), color)
    Wall(all, solids, (width // 2 - 230, height // 2 + 100), (width -  730, 30), color)

    Wall(all, solids, (130, 100), (30, height - 200), color)
    Wall(all, solids, (130, 90), (width // 2 - 180, 10), color)
    Wall(all, solids, (width // 2 + 50, 90), (width // 2 - 180, 10), color)
    Wall(all, solids, (width - 160, 100), (30, height - 200), color)
    Wall(all, solids, (130, height - 100), (width // 2 - 180, 10), color)
    Wall(all, solids, (width // 2 + 50, height - 100), (width // 2 - 180, 10), color)

    return pg.Color('lightgrey')